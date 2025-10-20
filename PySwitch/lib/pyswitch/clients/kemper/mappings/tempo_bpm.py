from micropython import const
from ....controller.client import ClientParameterMapping
from .. import KemperNRPNMessage
from .. import NRPN_FUNCTION_SET_SINGLE_PARAMETER, NRPN_FUNCTION_REQUEST_SINGLE_PARAMETER, NRPN_FUNCTION_RESPONSE_SINGLE_PARAMETER

_NRPN_ADDRESS_PAGE_RIG_PARAMETERS = const(0x04)
_NRPN_PARAMETER_ID_BPM = 0x00


# Tempo (BPM value)
def MAPPING_TEMPO_BPM():
    return ClientParameterMapping.get(
        name = "BPM",
        set = KemperNRPNMessage(
            NRPN_FUNCTION_SET_SINGLE_PARAMETER, 
            _NRPN_ADDRESS_PAGE_RIG_PARAMETERS,
            _NRPN_PARAMETER_ID_BPM
        ),
        request = KemperNRPNMessage(               
            NRPN_FUNCTION_REQUEST_SINGLE_PARAMETER, 
            _NRPN_ADDRESS_PAGE_RIG_PARAMETERS,
            _NRPN_PARAMETER_ID_BPM
        ),
        response = KemperNRPNMessage(               
            NRPN_FUNCTION_RESPONSE_SINGLE_PARAMETER, 
            _NRPN_ADDRESS_PAGE_RIG_PARAMETERS,
            _NRPN_PARAMETER_ID_BPM
        )
    )

# Output conversion for BPM
def convert_bpm(value):
    return str(round(value / 64))

