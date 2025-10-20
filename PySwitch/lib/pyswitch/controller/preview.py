from ..misc import PeriodCounter

# Handler which controle the DisplayLabel override_text mechanisms for usage 
# as value preview or similar things. It handles the blinking and timeouts etc.
class ValuePreview:

    # There is only one ValuePreview handler for each label
    @staticmethod
    def get(label):
        if not hasattr(label, "value_preview"):
            label.value_preview = ValuePreview(
                create_key = ValuePreview,
                label = label
            )

        return label.value_preview

    ###################################################################################################

    def __init__(self,
                 create_key,
                 label
        ):
        if create_key != ValuePreview:
            raise Exception()   # Pseudo private constructor
        
        self.label = label

        self.__period = None
        self.__blink_period = None
        self.__stay = False

        self.__blink_state = False
        self.__orig_color = label.text_color

        self.__clients = None # List of clients to be canceled when another client enters. Each one must have a cancel() method.

    # Sets a preview (override) text on the label.
    def preview(self, 
                text,
                client = None,                 # If a client is given, it must have a cancel() method which will be called when someone else enters preview.
                stay = False,                  # If True, the value will not disappear until reset is called.
                timeout_millis = 1500,         # Set to a value to let the preview disappear after that amount of time. Set to None or 0 for no timeout.
                blink_interval_millis = None,  # Set to a value for blinking. Set to None or 0 for no blinking.
                blink_color = (200, 200, 200)  # Blinking color.
        ):

        if self.__clients:
            for c in self.__clients:
                if c == client:
                    continue

                c.cancel()

        self.__stay = stay

        self.label.override_text = text
        self.label.update_label()

        if timeout_millis:
            if not self.__period:
                self.__period = PeriodCounter(timeout_millis)
            else:
                self.__period.interval = timeout_millis                

            self.__period.reset()
        else:
            self.__period = None

        if blink_interval_millis:
            if not self.__blink_period:
                self.__blink_period = PeriodCounter(blink_interval_millis)
            else:
                self.__blink_period.interval = blink_interval_millis
        else:
            self.__blink_period = None

        self.__blink_color = blink_color

        if client:
            if not self.__clients:
                self.__clients = []

            if not client in self.__clients:
                self.__clients.append(client)
        
    # Preview a mapping value (percentage)
    def preview_mapping(self, 
                        value,                         # Value to show
                        mapping,                       # Mapping (for deriving the name)
                        max_value,                     # Max. value (for calculating percentage)
                        client = None,                 # If a client is given, it must have a cancel() method which will be called when someone else enters preview.
                        stay = False,                  # If True, the value will not disappear until reset is called.
                        timeout_millis = 1500,         # Set to a value to let the preview disappear after that amount of time. Set to None or 0 for no timeout.
                        blink_interval_millis = None,  # Set to a value for blinking. Set to None or 0 for no blinking.
                        blink_color = (200, 200, 200), # Blinking color
                        text_callback = None           # Text callback (optional, signature: (value:int) => text:string with value is in the mapping range)
        ):
        val = round(value * 100 / max_value)

        if text_callback:
            text = text_callback(val)
        else:
            prefix = f"{ mapping.name }: " if mapping.name else ""
            text = f"{ prefix }{ str(val) }%"
        
        self.preview(
            text = text,
            client = client,
            stay = stay,
            timeout_millis = timeout_millis,
            blink_interval_millis = blink_interval_millis,
            blink_color = blink_color
        )        

    # Reset the display label to its default behaviour, either immediately or after the timeout period.
    def reset(self, immediately = False):
        self.__blink_period = None
        self.__stay = False

        self.label.text_color = self.__orig_color

        if not self.__period:
            immediately = True

        if immediately:
            self.label.override_text = None
            self.label.update_label()
            self.__period = None
        else:
            self.__period.reset()
        
    # Must be called regularly
    def update(self):
        if self.label.override_text:
            # Free preview display after a period
            if not self.__stay and self.__period and self.__period.exceeded:
                self.label.override_text = None
                self.label.update_label()

            # Blink
            if self.__blink_period and self.__blink_period.exceeded:
                self.__blink_state = not self.__blink_state

                if self.__blink_state:
                    self.label.text_color = self.__blink_color
                else:
                    self.label.text_color = self.__orig_color

