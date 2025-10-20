from micropython import const
from .. import KemperNRPNMessage
from ....controller.client import ClientParameterMapping
from .. import NRPN_FUNCTION_SET_SINGLE_PARAMETER, NRPN_FUNCTION_RESPONSE_SINGLE_PARAMETER, NRPN_FUNCTION_REQUEST_SINGLE_PARAMETER

_NRPN_ADDRESS_PAGE_SYSTEM = const(0x7f)

_NRPN_SYS_PARAMETER_MAIN_VOL = const(0)
_NRPN_SYS_PARAMETER_MON_VOL = const(2)
_NRPN_SYS_PARAMETER_LOOPER_VOL = const(52)
_NRPN_SYS_PARAMETER_SPACE_INTENSITY = const(36)

# Main volume
def MAPPING_MAIN_VOLUME(): 
    return ClientParameterMapping.get(
        name = "MainVol",
        set = KemperNRPNMessage(
            NRPN_FUNCTION_SET_SINGLE_PARAMETER, 
            _NRPN_ADDRESS_PAGE_SYSTEM,
            _NRPN_SYS_PARAMETER_MAIN_VOL
        ),
        request = KemperNRPNMessage(
            NRPN_FUNCTION_REQUEST_SINGLE_PARAMETER,
            _NRPN_ADDRESS_PAGE_SYSTEM,
            _NRPN_SYS_PARAMETER_MAIN_VOL
        ),
        response = KemperNRPNMessage(
            NRPN_FUNCTION_RESPONSE_SINGLE_PARAMETER,
            _NRPN_ADDRESS_PAGE_SYSTEM,
            _NRPN_SYS_PARAMETER_MAIN_VOL
        )
    )

# Monitor volume
def MAPPING_MONITOR_VOLUME(): 
    return ClientParameterMapping.get(
        name = "MonVol",
        set = KemperNRPNMessage(
            NRPN_FUNCTION_SET_SINGLE_PARAMETER, 
            _NRPN_ADDRESS_PAGE_SYSTEM,
            _NRPN_SYS_PARAMETER_MON_VOL
        ),
        request = KemperNRPNMessage(
            NRPN_FUNCTION_REQUEST_SINGLE_PARAMETER,
            _NRPN_ADDRESS_PAGE_SYSTEM,
            _NRPN_SYS_PARAMETER_MON_VOL
        ),
        response = KemperNRPNMessage(
            NRPN_FUNCTION_RESPONSE_SINGLE_PARAMETER,
            _NRPN_ADDRESS_PAGE_SYSTEM,
            _NRPN_SYS_PARAMETER_MON_VOL
        )
    )

# Looper volume
def MAPPING_LOOPER_VOLUME(): 
    return ClientParameterMapping.get(
        name = "LoopVol",
        set = KemperNRPNMessage(
            NRPN_FUNCTION_SET_SINGLE_PARAMETER, 
            _NRPN_ADDRESS_PAGE_SYSTEM,
            _NRPN_SYS_PARAMETER_LOOPER_VOL
        ),
        request = KemperNRPNMessage(
            NRPN_FUNCTION_REQUEST_SINGLE_PARAMETER,
            _NRPN_ADDRESS_PAGE_SYSTEM,
            _NRPN_SYS_PARAMETER_LOOPER_VOL
        ),
        response = KemperNRPNMessage(
            NRPN_FUNCTION_RESPONSE_SINGLE_PARAMETER,
            _NRPN_ADDRESS_PAGE_SYSTEM,
            _NRPN_SYS_PARAMETER_LOOPER_VOL
        )
    )

# Space Intensity
def MAPPING_SPACE_INTENSITY():
    return ClientParameterMapping.get(
        name = "SpaceInt",
        set = KemperNRPNMessage(
            NRPN_FUNCTION_SET_SINGLE_PARAMETER,
            _NRPN_ADDRESS_PAGE_SYSTEM,
            _NRPN_SYS_PARAMETER_SPACE_INTENSITY
        ),
        request = KemperNRPNMessage(
            NRPN_FUNCTION_REQUEST_SINGLE_PARAMETER,
            _NRPN_ADDRESS_PAGE_SYSTEM,
            _NRPN_SYS_PARAMETER_SPACE_INTENSITY
        ),
        response = KemperNRPNMessage(
            NRPN_FUNCTION_RESPONSE_SINGLE_PARAMETER,
            _NRPN_ADDRESS_PAGE_SYSTEM,
            _NRPN_SYS_PARAMETER_SPACE_INTENSITY
        )
    )