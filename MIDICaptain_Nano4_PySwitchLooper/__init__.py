import Live
from .MIDICaptain_Nano4_PySwitchLooper import MIDICaptain_Nano4_PySwitchLooper


def create_instance(c_instance):
    """ Creates and returns the APC20 script """
    return MIDICaptain_Nano4_PySwitchLooper(c_instance)

# local variables:
# tab-width: 4
