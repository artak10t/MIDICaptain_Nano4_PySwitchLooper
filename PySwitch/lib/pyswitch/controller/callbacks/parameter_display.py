from . import Callback

# Callback for DisplayLabel to show a parameter value
class ParameterDisplayCallback(Callback):
    def __init__(self, 
                 mapping, 
                 convert_value = None,   # Conversion routine: (value) => string/None (None for default behaviour)
                 default_text = ""
        ):
        Callback.__init__(self, mappings = [mapping])
        
        self.__mapping = mapping
        self.__convert_value = convert_value
        self.__default_text = default_text

    def update_label(self, label):
        if self.__convert_value:
            conv = self.__convert_value(self.__mapping.value)
            if (conv != None):
                label.text = str(conv)
                return

        if self.__mapping.value != None:
            label.text = str(self.__mapping.value)
        else:
            label.text = self.__default_text
