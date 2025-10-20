from micropython import const

from . import BinaryParameterCallback

# Used for effect enable/disable. Abstract, must implement some methods (see end of class)
class EffectEnableCallback(BinaryParameterCallback):

    # The "None" Type is defined here, all others in derived classes
    CATEGORY_NONE = const(0)

    # Only used on init and reset
    CATEGORY_INITIAL = const(-1)
    
    def __init__(self, mapping_state, mapping_type):
        def color_callback(action, value):
            return self.get_effect_category_color(self.__effect_category, self.mapping_fxtype.value)

        super().__init__(
            mapping = mapping_state, 
            color_callback = color_callback
        )

        self.register_mapping(mapping_type)

        self.mapping_fxtype = mapping_type
        
        self.__effect_category = self.CATEGORY_NONE  
        self.__current_kpp_type = None
        
    def reset(self):
        super().reset()
        
        self.__current_kpp_type = None

    def update_displays(self):
        self.__effect_category = self.get_effect_category(self.mapping_fxtype.value) if self.mapping_fxtype.value != None else self.CATEGORY_NONE
        
        if self.__effect_category == self.CATEGORY_NONE:
            self.action.feedback_state(False)

        if self.__current_kpp_type == self.mapping_fxtype.value:
            super().update_displays()
            return

        self.__current_kpp_type = self.mapping_fxtype.value

        # Effect category text
        if self.action.label:
            self.action.label.text = self.get_effect_category_text(self.__effect_category, self.mapping_fxtype.value)

        super().update_displays()

    # Must return the effect category for a mapping value
    def get_effect_category(self, kpp_effect_type):
        pass                                           # pragma: no cover

    # Must return the color for a category    
    def get_effect_category_color(self, category, kpp_effect_type):
        pass                                           # pragma: no cover

    # Must return the text to show for a category    
    def get_effect_category_text(self, category, kpp_effect_type):
        pass                                           # pragma: no cover
