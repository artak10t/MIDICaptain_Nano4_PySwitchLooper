from micropython import const

from ....controller.client import ClientTwoPartParameterMapping

from adafruit_midi.control_change import ControlChange
from adafruit_midi.program_change import ProgramChange

_CC_RIG_SELECT = const(50)       # This selects slot 1 of the current bank. The slots 2-5 can be addressed by adding (n-1) to the value.
_CC_BANK_PRESELECT = const(47)
_CC_RIG_INDEX_PART_1 = const(32) # The second part will be sent as program change.

# Selects a rig of the current bank. Rig index must be in range [0..4]
def MAPPING_RIG_SELECT(rig):
    return ClientTwoPartParameterMapping.get(
        f"Select Rig { str(rig + 1) }",
        set = ControlChange(
            _CC_RIG_SELECT + rig,
            1    # Dummy value, will be overridden
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

# Pre-selects a bank.
def MAPPING_BANK_SELECT():
    return ClientTwoPartParameterMapping.get(
        name = "Select Bank",
        set = ControlChange(
            _CC_BANK_PRESELECT,
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

# # Selects a rig of a specific bank. Rig index must be in range [0..4]
# def APPING_BANK_AND_RIG_SELECT(rig):
#     return ClientTwoPartParameterMapping.get(
#         name = f"Select Rig { str(rig + 1) } + Bank",
#         set = [
#             ControlChange(
#                 _CC_BANK_PRESELECT,
#                 0    # Dummy value, will be overridden
#             ),
#             ControlChange(
#                 _CC_RIG_SELECT + rig,
#                 1    # Dummy value, will be overridden
#             ),
#             ControlChange(
#                 _CC_RIG_SELECT + rig,
#                 0    # Dummy value, will be overridden
#             )
#         ],

#         response = [
#             ControlChange(
#                 _CC_RIG_INDEX_PART_1,
#                 0    # Dummy value, will be ignored
#             ),
#             ProgramChange(
#                 0    # Dummy value, will be ignored
#             )
#         ]
#     )
