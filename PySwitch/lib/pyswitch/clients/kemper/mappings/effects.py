from micropython import const
from .. import KemperNRPNMessage, KemperEffectSlot
from ....controller.client import ClientParameterMapping
from .. import NRPN_FUNCTION_SET_SINGLE_PARAMETER, NRPN_FUNCTION_REQUEST_SINGLE_PARAMETER, NRPN_FUNCTION_RESPONSE_SINGLE_PARAMETER

from adafruit_midi.control_change import ControlChange

_CC_EFFECT_BUTTON_I = const(75)  # II to IV are consecutive from this: 76, 77, 78

# _NRPN_EFFECT_PARAMETER_ADDRESS_MIX = const(0x04)
# _NRPN_EFFECT_PARAMETER_ADDRESS_MIX2 = const(0x36)  # 54
_NRPN_EFFECT_PARAMETER_ADDRESS_MIX_DLY_REV = const(0x45)  # 69

# Effect Button I-IIII (set only). num must be a number (1 to 4).
def MAPPING_EFFECT_BUTTON(num): 
    return ClientParameterMapping.get(
        name = f"Effect Button { repr(num) }",
        set = ControlChange(
            _CC_EFFECT_BUTTON_I + (num - 1),
            0
        )
    )


def MAPPING_DLY_REV_MIX(slot_id):
    return ClientParameterMapping.get(
        name = f"Mix { KemperEffectSlot.EFFECT_SLOT_NAME[slot_id] }",
        set = KemperNRPNMessage(
            NRPN_FUNCTION_SET_SINGLE_PARAMETER, 
            KemperEffectSlot.NRPN_SLOT_ADDRESS_PAGE[slot_id],
            _NRPN_EFFECT_PARAMETER_ADDRESS_MIX_DLY_REV
        ),
        request = KemperNRPNMessage(               
            NRPN_FUNCTION_REQUEST_SINGLE_PARAMETER, 
            KemperEffectSlot.NRPN_SLOT_ADDRESS_PAGE[slot_id],
            _NRPN_EFFECT_PARAMETER_ADDRESS_MIX_DLY_REV
        ),
        response = KemperNRPNMessage(               
            NRPN_FUNCTION_RESPONSE_SINGLE_PARAMETER, 
            KemperEffectSlot.NRPN_SLOT_ADDRESS_PAGE[slot_id],
            _NRPN_EFFECT_PARAMETER_ADDRESS_MIX_DLY_REV
        )
    )

