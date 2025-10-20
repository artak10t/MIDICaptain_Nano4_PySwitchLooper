from micropython import const
from .. import KemperNRPNMessage, KemperMappings
from ....controller.client import ClientParameterMapping
from .. import NRPN_FUNCTION_SET_SINGLE_PARAMETER, NRPN_FUNCTION_REQUEST_STRING_PARAMETER, NRPN_FUNCTION_REQUEST_SINGLE_PARAMETER, NRPN_FUNCTION_RESPONSE_SINGLE_PARAMETER, NRPN_ADDRESS_PAGE_STRINGS, NRPN_FUNCTION_RESPONSE_STRING_PARAMETER

_NRPN_ADDRESS_PAGE_CABINET = const(0x0c)
_NRPN_CABINET_PARAMETER_STATE = const(0x02)
_NRPN_STRING_PARAMETER_ID_CABINET_NAME = const(0x20)

# Cab name (request only)
def MAPPING_CABINET_NAME(): 
    return ClientParameterMapping.get(
        depends = KemperMappings.RIG_DATE(),
        name = "Cab Name",
        request = KemperNRPNMessage(               
            NRPN_FUNCTION_REQUEST_STRING_PARAMETER, 
            NRPN_ADDRESS_PAGE_STRINGS,
            _NRPN_STRING_PARAMETER_ID_CABINET_NAME
        ),
        response = KemperNRPNMessage(
            NRPN_FUNCTION_RESPONSE_STRING_PARAMETER, 
            NRPN_ADDRESS_PAGE_STRINGS,
            _NRPN_STRING_PARAMETER_ID_CABINET_NAME
        ),
        type = ClientParameterMapping.PARAMETER_TYPE_STRING
    )

# Cab on/off
def MAPPING_CABINET_STATE(): 
    return ClientParameterMapping.get(
        name = "Cab State",
        set = KemperNRPNMessage(
            NRPN_FUNCTION_SET_SINGLE_PARAMETER, 
            _NRPN_ADDRESS_PAGE_CABINET,
            _NRPN_CABINET_PARAMETER_STATE
        ),
        request = KemperNRPNMessage(
            NRPN_FUNCTION_REQUEST_SINGLE_PARAMETER,
            _NRPN_ADDRESS_PAGE_CABINET,
            _NRPN_CABINET_PARAMETER_STATE
        ),
        response = KemperNRPNMessage(
            NRPN_FUNCTION_RESPONSE_SINGLE_PARAMETER,
            _NRPN_ADDRESS_PAGE_CABINET,
            _NRPN_CABINET_PARAMETER_STATE
        )
    )