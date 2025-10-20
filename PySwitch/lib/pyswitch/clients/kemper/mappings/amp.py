from micropython import const
from .. import KemperNRPNMessage, KemperMappings
from ....controller.client import ClientParameterMapping
from .. import NRPN_FUNCTION_SET_SINGLE_PARAMETER, NRPN_FUNCTION_REQUEST_STRING_PARAMETER, NRPN_FUNCTION_REQUEST_SINGLE_PARAMETER, NRPN_FUNCTION_RESPONSE_SINGLE_PARAMETER, NRPN_ADDRESS_PAGE_STRINGS, NRPN_FUNCTION_RESPONSE_STRING_PARAMETER

_NRPN_ADDRESS_PAGE_AMP = const(0x0a)

_NRPN_AMP_PARAMETER_STATE = const(0x02)
_NRPN_AMP_PARAMETER_GAIN = const(0x04)

_NRPN_STRING_PARAMETER_ID_AMP_NAME = const(0x10)

# Amp name (request only)
def MAPPING_AMP_NAME(): 
    return ClientParameterMapping.get(
        depends = KemperMappings.RIG_DATE(),
        name = "Amp Name",
        request = KemperNRPNMessage(               
            NRPN_FUNCTION_REQUEST_STRING_PARAMETER, 
            NRPN_ADDRESS_PAGE_STRINGS,
            _NRPN_STRING_PARAMETER_ID_AMP_NAME
        ),
        response = KemperNRPNMessage(
            NRPN_FUNCTION_RESPONSE_STRING_PARAMETER, 
            NRPN_ADDRESS_PAGE_STRINGS,
            _NRPN_STRING_PARAMETER_ID_AMP_NAME
        ),
        type = ClientParameterMapping.PARAMETER_TYPE_STRING
    )

# Amp on/off
def MAPPING_AMP_STATE(): 
    return ClientParameterMapping.get(
        name = "Amp State",
        set = KemperNRPNMessage(
            NRPN_FUNCTION_SET_SINGLE_PARAMETER, 
            _NRPN_ADDRESS_PAGE_AMP,
            _NRPN_AMP_PARAMETER_STATE
        ),
        request = KemperNRPNMessage(
            NRPN_FUNCTION_REQUEST_SINGLE_PARAMETER,
            _NRPN_ADDRESS_PAGE_AMP,
            _NRPN_AMP_PARAMETER_STATE
        ),
        response = KemperNRPNMessage(
            NRPN_FUNCTION_RESPONSE_SINGLE_PARAMETER,
            _NRPN_ADDRESS_PAGE_AMP,
            _NRPN_AMP_PARAMETER_STATE
        )
    )

# Amp gain
def MAPPING_AMP_GAIN(): 
    return ClientParameterMapping.get(
        name = "Gain",
        set = KemperNRPNMessage(
            NRPN_FUNCTION_SET_SINGLE_PARAMETER, 
            _NRPN_ADDRESS_PAGE_AMP,
            _NRPN_AMP_PARAMETER_GAIN
        ),
        request = KemperNRPNMessage(
            NRPN_FUNCTION_REQUEST_SINGLE_PARAMETER,
            _NRPN_ADDRESS_PAGE_AMP,
            _NRPN_AMP_PARAMETER_GAIN
        ),
        response = KemperNRPNMessage(
            NRPN_FUNCTION_RESPONSE_SINGLE_PARAMETER,
            _NRPN_ADDRESS_PAGE_AMP,
            _NRPN_AMP_PARAMETER_GAIN
        )
    )
