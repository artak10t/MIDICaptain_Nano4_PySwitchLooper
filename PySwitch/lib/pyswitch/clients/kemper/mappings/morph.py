from micropython import const
from .. import KemperNRPNMessage
from ....controller.client import ClientParameterMapping
from .. import NRPN_FUNCTION_REQUEST_SINGLE_PARAMETER, NRPN_FUNCTION_RESPONSE_SINGLE_PARAMETER

from adafruit_midi.control_change import ControlChange

_CC_MORPH_PEDAL = const(11)
_CC_MORPH_BUTTON = const(80)                     # Also includes ride/fall times

_NRPN_ADDRESS_PAGE_ZERO = const(0x00)            # As of the notes of sumsar

def MAPPING_MORPH_BUTTON(): 
    return ClientParameterMapping.get(
        name = "Morph Button",
        set = ControlChange(
            _CC_MORPH_BUTTON, 
            0
        ),
        request = KemperNRPNMessage(
            NRPN_FUNCTION_REQUEST_SINGLE_PARAMETER,
            _NRPN_ADDRESS_PAGE_ZERO,
            0x0b
        ),
        response = KemperNRPNMessage(
            NRPN_FUNCTION_RESPONSE_SINGLE_PARAMETER,
            _NRPN_ADDRESS_PAGE_ZERO,
            0x0b
        )
    )

def MAPPING_MORPH_PEDAL(): 
    return ClientParameterMapping.get(
        name = "Morph",
        set = ControlChange(
            _CC_MORPH_PEDAL, 
            0
        ),
        request = KemperNRPNMessage(
            NRPN_FUNCTION_REQUEST_SINGLE_PARAMETER,
            _NRPN_ADDRESS_PAGE_ZERO,
            0x0b
        ),
        response = KemperNRPNMessage(
            NRPN_FUNCTION_RESPONSE_SINGLE_PARAMETER,
            _NRPN_ADDRESS_PAGE_ZERO,
            0x0b
        )
    )