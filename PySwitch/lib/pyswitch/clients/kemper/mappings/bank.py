from micropython import const
from ....controller.client import ClientTwoPartParameterMapping

from adafruit_midi.control_change import ControlChange
from adafruit_midi.program_change import ProgramChange

_CC_BANK_INCREASE = const(48)
_CC_BANK_DECREASE = const(49)
_CC_RIG_INDEX_PART_1 = const(32) # The second part will be sent as program change.


def MAPPING_NEXT_BANK(): 
    return ClientTwoPartParameterMapping.get(
        name = "Next Bank",
        set = ControlChange(
            _CC_BANK_INCREASE,
            0    # Dummy value, will be overridden
        ),
        response = [
            ControlChange(
                _CC_RIG_INDEX_PART_1,
                0    # Dummy value, will be ignored
            ),
            ProgramChange(
                0    # Dummy value, will be ignored
            )
        ]
    )

def MAPPING_PREVIOUS_BANK():
    return ClientTwoPartParameterMapping.get(
        name = "Prev Bank",
        set = ControlChange(
            _CC_BANK_DECREASE,
            0    # Dummy value, will be overridden
        ),
        response = [
            ControlChange(
                _CC_RIG_INDEX_PART_1,
                0    # Dummy value, will be ignored
            ),
            ProgramChange(
                0    # Dummy value, will be ignored
            )
        ]
    )