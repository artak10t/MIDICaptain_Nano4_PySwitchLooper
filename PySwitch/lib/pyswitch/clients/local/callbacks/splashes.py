from ....controller.callbacks import Callback

# Simple callback just showing the passed Display Element
class SplashesCallback(Callback):
    def __init__(self, 
                 splashes   # Display element to show
        ):
        Callback.__init__(self)

        self.__splashes = splashes
        
    def get_root(self):
        return self.__splashes