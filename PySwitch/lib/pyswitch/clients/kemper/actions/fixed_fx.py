from ....controller.actions import PushButtonAction
from ....controller.callbacks import BinaryParameterCallback
from ....colors import Colors

from ..mappings.fixed_fx import MAPPING_FIXED_TRANSPOSE
from ..mappings.fixed_fx import MAPPING_FIXED_GATE
from ..mappings.fixed_fx import MAPPING_FIXED_COMP
from ..mappings.fixed_fx import MAPPING_FIXED_BOOST
from ..mappings.fixed_fx import MAPPING_FIXED_WAH
from ..mappings.fixed_fx import MAPPING_FIXED_CHORUS

from ..mappings.fixed_fx import MAPPING_FIXED_AIR
from ..mappings.fixed_fx import MAPPING_FIXED_DBL_TRACKER

FIXED_SLOT_ID_TRANSPOSE = 0
FIXED_SLOT_ID_GATE = 1
FIXED_SLOT_ID_COMP = 2
FIXED_SLOT_ID_BOOST = 3
FIXED_SLOT_ID_WAH = 4
FIXED_SLOT_ID_CHORUS = 5

FIXED_SLOT_ID_AIR = 6
FIXED_SLOT_ID_DBL_TRACKER = 7

# Action to control the on/off state of all fixed FX slots.
def FIXED_EFFECT_STATE(slot,                                      # Fixed Effect Slot ID
                       text = None,                               # Text (set to None for auto)
                       display = None,
                       color = None,                              # Color (set to None for auto)
                       id = False,
                       use_leds = True, 
                       enable_callback = None,
                       mode = PushButtonAction.HOLD_MOMENTARY
):
    if slot == FIXED_SLOT_ID_TRANSPOSE:
        _color = color if color else Colors.WHITE
        _text = text if text else "Transpose"
        _mapping = MAPPING_FIXED_TRANSPOSE()

    elif slot == FIXED_SLOT_ID_GATE:
        _color = color if color else Colors.LIGHT_BLUE
        _text = text if text else "Gate"
        _mapping = MAPPING_FIXED_GATE()

    elif slot == FIXED_SLOT_ID_COMP:
        _color = color if color else Colors.BLUE
        _text = text if text else "Comp"
        _mapping = MAPPING_FIXED_COMP()

    elif slot == FIXED_SLOT_ID_BOOST:
        _color = color if color else Colors.RED
        _text = text if text else "Boost"
        _mapping = MAPPING_FIXED_BOOST()

    elif slot == FIXED_SLOT_ID_WAH:
        _color = color if color else Colors.ORANGE
        _text = text if text else "Wah"
        _mapping = MAPPING_FIXED_WAH()

    elif slot == FIXED_SLOT_ID_CHORUS:
        _color = color if color else Colors.BLUE
        _text = text if text else "Chorus"
        _mapping = MAPPING_FIXED_CHORUS()

    elif slot == FIXED_SLOT_ID_AIR:
        _color = color if color else Colors.BLUE
        _text = text if text else "Air"
        _mapping = MAPPING_FIXED_AIR()

    elif slot == FIXED_SLOT_ID_DBL_TRACKER:
        _color = color if color else Colors.BLUE
        _text = text if text else "Doubler"
        _mapping = MAPPING_FIXED_DBL_TRACKER()

    return PushButtonAction({
        "callback": BinaryParameterCallback(
            mapping = _mapping,
            text = _text,
            color = _color
        ),
        "mode": mode,
        "display": display,
        "id": id,
        "useSwitchLeds": use_leds,
        "enableCallback": enable_callback
    })
