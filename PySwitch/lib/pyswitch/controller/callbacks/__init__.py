from micropython import const
from ...misc import Updateable, get_option
from ...colors import DEFAULT_SWITCH_COLOR, dim_color


class Callback(Updateable):
    def __init__(self, mappings = []):
        super().__init__()
        
        self.__initialized = False
        self.__mappings = []

        for m in mappings:
            self.register_mapping(m)

    # Must be used to register all mappings needed by the callback
    def register_mapping(self, mapping):
        if self.__initialized:
            raise Exception() # Mappings cannot be registered after the callback has been initialized
        
        self.__mappings.append(mapping)

    # Must be called before usage
    def init(self, appl, listener = None):
        if self.__initialized: 
            return
        
        self.__appl = appl
        self.__listener = listener

        for m in self.__mappings:
            self.__appl.client.register(m, self)

        self.__appl.add_updateable(self)

        self.__initialized = True

    # Reset state
    def reset(self):
        pass                   # pragma: no cover

    #@RuntimeStatistics.measure
    def update(self):
        for m in self.__mappings:
            self.__appl.client.request(m, self)

    def parameter_changed(self, mapping):
        if self.__listener:
            self.__listener.parameter_changed(mapping)

    def request_terminated(self, mapping):
        # Clear value before calling the listener
        for m in self.__mappings:
            if m != mapping:
                continue

            m.value = None

        if self.__listener:
            self.__listener.request_terminated(mapping)


###########################################################################################################


class BinaryParameterCallback(Callback):

    # Comparison modes (for the valueEnable value when requesting a value)
    EQUAL = const(0)                 # Enable when exactly the valueEnable value comes in
    
    GREATER = const(10)              # Enable when a value greater than valueEnable comes in
    GREATER_EQUAL = const(20)        # Enable when the valueEnable value comes in, or anything greater

    LESS = const(30)                 # Enable when a value less than valueEnable comes in
    LESS_EQUAL = const(40)           # Enable when the valueEnable value comes in, or anything less

    NO_STATE_CHANGE = const(999)     # Do not receive any values

    def __init__(self, 
                 
                 # A ClientParameterMapping instance. See mappings.py for some predeifined ones.
                 mapping, 

                 # Mapping to be used for disabling the functionality again (only used for sending)
                 mapping_disable = None,

                 # Color to be used
                 color = DEFAULT_SWITCH_COLOR,

                # Color callback (optional, called in update_displays, footprint: get_color())
                 color_callback = None,

                 # Text (optional)
                 text = None,

                 # Text for diabled state (optional)
                 text_disabled = None,

                 # Value to be sent as "enabled". Optional: Default is 1. If mapping.set is a list, this must
                 # also be a list of values for the set messages in the mapping.
                 value_enable = 1,                                       

                 # Value to be sent as "disabled". Optional: Default is 0. If mapping.set is a list, this must
                 # also be a list of values for the set messages in the mapping.
                 # SPECIAL: If you set this (or items of this) to "auto", the "disabled" value will be determined from the 
                 # client's current parameter value when the action state is False (the old value is restored).
                 value_disable = 0,                                      
                 
                 # Optional: The value of incoming messages will be compared against this to determine state
                 # (acc. to the comparison mode). If not set, "valueEnable" is used (first entry if valueEnabled is a list). 
                 reference_value = None,

                 # Mode of comparison when receiving a value. Default is GREATER_EQUAL. 
                 comparison_mode = 20,

                 # Dim factor in range [0..1] for on state (display label) Optional.
                 # If None, the global config value will be used
                 # If "off", the global off config value will be used.
                 display_dim_factor_on = None,

                 # Dim factor in range [0..1] for off state (display label) Optional.
                 # If None, the global config value will be used
                 # If "on", the global on config value will be used.
                 display_dim_factor_off = None,
                 
                 # LED brightness [0..1] for on state (Switch LEDs) Optional.
                 # If None, the global config value will be used
                 # If "off", the global off config value will be used.
                 led_brightness_on = None,

                 # LED brightness [0..1] for off state (Switch LEDs) Optional.
                 # If None, the global config value will be used
                 # If "on", the global on config value will be used.
                 led_brightness_off = None,

                 # If enabled, the callback will not wait until a MIDI value comes in, the state is displayed as-is any time.
                 use_internal_state = False
        ):
        super().__init__(mappings = [mapping])

        self.mapping = mapping
        self.mapping_disable = mapping_disable   # Can be changed from outside!

        self._value_enable = int(value_enable) if not isinstance(value_enable, list) else value_enable
        self._value_disable = int(value_disable) if value_disable != 'auto' and not isinstance(value_disable, list) else value_disable
        self.__reference_value = int(reference_value) if reference_value != None else ( self._value_enable if not isinstance(self._value_enable, list) else self._value_enable[0] )
        self._text = text
        self._text_disabled = text_disabled
        self.__comparison_mode = comparison_mode
        self.__display_dim_factor_on = display_dim_factor_on
        self.__display_dim_factor_off = display_dim_factor_off
        self._led_brightness_on = led_brightness_on
        self._led_brightness_off = led_brightness_off
        self._color = color
        self._color_callback = color_callback
        self.__use_internal_state = use_internal_state

        self.__current_value = self       # Just some value which will never occur as a mapping value ;)

        self.reset()

        # Auto mode for value_disable
        self.__update_value_disabled = False
        if not isinstance(self._value_disable, list):
            self.__update_value_disabled = (self._value_disable == "auto")
        else:
            self.__update_value_disabled = [v == "auto" for v in self._value_disable]            


    def init(self, appl, listener = None):
        super().init(appl, listener)

        self.__appl = appl

        # Initialize dim factors and brightness settings. 
        if self.__display_dim_factor_on == None:
            self.__display_dim_factor_on = get_option(appl.config, "displayDimFactorOn", 1)
        elif self.__display_dim_factor_on == "off":
            self.__display_dim_factor_on = get_option(appl.config, "displayDimFactorOff", 0.2)
        
        if self.__display_dim_factor_off == None:
            self.__display_dim_factor_off = get_option(appl.config, "displayDimFactorOff", 0.2)
        elif self.__display_dim_factor_off == "on":
            self.__display_dim_factor_off = get_option(appl.config, "displayDimFactorOn", 1)

        if self._led_brightness_on == None:
            self._led_brightness_on = get_option(appl.config, "ledBrightnessOn", 0.3)
        elif self._led_brightness_on == "off":
            self._led_brightness_on = get_option(appl.config, "ledBrightnessOff", 0.02)

        if self._led_brightness_off == None:
            self._led_brightness_off = get_option(appl.config, "ledBrightnessOff", 0.02)
        elif self._led_brightness_off == "on":
            self._led_brightness_off = get_option(appl.config, "ledBrightnessOn", 0.3)


    def state_changed_by_user(self):
        if self.action.state:
            set_mapping = self.mapping
            value = self._value_enable
        else:
            if self.mapping_disable:
                set_mapping = self.mapping_disable
            else:
                set_mapping = self.mapping

            value = self._value_disable

        if not isinstance(self._value_disable, list):
            if value != "auto":
                self.__appl.client.set(set_mapping, value)
        else:
            auto_contained = False
            for v in self._value_disable:
                if v == "auto":
                    auto_contained = True
                    break
            if not auto_contained:
                self.__appl.client.set(set_mapping, value)

        # Request value
        self.update()


    # Reset state
    def reset(self):
        self._current_display_state = -1
        self.__current_value = self       # Just some value which will never occur as a mapping value ;)
        self._current_color = -1


    def update_displays(self):
        value = self.mapping.value

        if value != self.__current_value:
            self.__current_value = value
            self.evaluate_value(value)

        color = self._color_callback(self.action, value) if self._color_callback else self._color

        # Set color, if new, or state have been changed
        if color != self._current_color or self._current_display_state != self.action.state:
            self._current_color = color
            self._current_display_state = self.action.state
        
            self.set_switch_color(color)
            self.set_label_color(color)
            self.__update_label_text()


    # Evaluate a new value
    def evaluate_value(self, value):
        state = False

        if value != None:
            mode = self.__comparison_mode

            if mode == self.EQUAL:
                if value == self.__reference_value:
                    state = True

            elif mode == self.GREATER_EQUAL:
                if value >= self.__reference_value:
                    state = True

            elif mode == self.GREATER:
                if value > self.__reference_value: 
                    state = True

            elif mode == self.LESS_EQUAL:
                if value <= self.__reference_value:
                    state = True

            elif mode == self.LESS:
                if value < self.__reference_value: 
                    state = True        

            elif mode == self.NO_STATE_CHANGE:
                state = self.action.state

            else:
                raise Exception() #"Invalid comparison mode: " + repr(self.__comparison_mode))        

        self.action.feedback_state(state)        

        # If enabled, remember the value for later when disabled
        if state == True or not self.__update_value_disabled or value == None:
            return
        
        if not isinstance(self._value_disable, list):
            self._value_disable = value
        else:
            for i in range(len(self._value_disable)):
                if self.__update_value_disabled[i]:
                    self._value_disable[i] = value


    # Update switch brightness
    def set_switch_color(self, color):
        # Update switch LED color 
        self.action.switch_color = color

        if self.action.state == True and (self.mapping.response or self.__use_internal_state):
            # Switched on
            self.action.switch_brightness = self._led_brightness_on
        else:
            # Switched off
            self.action.switch_brightness = self._led_brightness_off


   # Update label color, if any
    def set_label_color(self, color):
        if not self.action.label:
            return
            
        if self.action.state == True and (self.mapping.response or self.__use_internal_state):
            self.action.label.back_color = dim_color(color, self.__display_dim_factor_on)
        else:
            self.action.label.back_color = dim_color(color, self.__display_dim_factor_off)


    # Update text if set
    def __update_label_text(self):
        if not self.action.label:
            return
            
        if not self._text:
            return
        
        if self.action.state == True or not (self.mapping.response or self.__use_internal_state):
            self.action.label.text = self._text
        else:
            if self._text_disabled:
                self.action.label.text = self._text_disabled
            else:
                self.action.label.text = self._text


