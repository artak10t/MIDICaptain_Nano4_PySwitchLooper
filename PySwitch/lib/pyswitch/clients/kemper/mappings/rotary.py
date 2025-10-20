from micropython import const
from .. import KemperNRPNMessage, KemperEffectSlot
from ....controller.client import ClientParameterMapping
from .. import NRPN_FUNCTION_SET_SINGLE_PARAMETER, NRPN_FUNCTION_REQUEST_SINGLE_PARAMETER, NRPN_FUNCTION_RESPONSE_SINGLE_PARAMETER

# _CC_ROTARY_SPEED = const(33)     # 1 = Fast, 0 = Slow
# _CC_ROTARY_SPEED_GLOBAL = const(33)

_NRPN_EFFECT_PARAMETER_ADDRESS_ROTARY_SPEED = const(0x1e)  # 30

# Rotary speed (fast/slow)
def MAPPING_ROTARY_SPEED(slot_id):
    return ClientParameterMapping.get(
        name = f"Rot. Speed { KemperEffectSlot.EFFECT_SLOT_NAME[slot_id] }",
        set = KemperNRPNMessage(
            NRPN_FUNCTION_SET_SINGLE_PARAMETER, 
            KemperEffectSlot.NRPN_SLOT_ADDRESS_PAGE[slot_id],
            _NRPN_EFFECT_PARAMETER_ADDRESS_ROTARY_SPEED
        ),
        request = KemperNRPNMessage(               
            NRPN_FUNCTION_REQUEST_SINGLE_PARAMETER, 
            KemperEffectSlot.NRPN_SLOT_ADDRESS_PAGE[slot_id],
            _NRPN_EFFECT_PARAMETER_ADDRESS_ROTARY_SPEED
        ),
        response = KemperNRPNMessage(
            NRPN_FUNCTION_RESPONSE_SINGLE_PARAMETER,
            KemperEffectSlot.NRPN_SLOT_ADDRESS_PAGE[slot_id],
            _NRPN_EFFECT_PARAMETER_ADDRESS_ROTARY_SPEED
        )
    )

