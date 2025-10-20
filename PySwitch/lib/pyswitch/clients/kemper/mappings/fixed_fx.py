from .. import KemperNRPNMessage
from ....controller.client import ClientParameterMapping
from .. import NRPN_FUNCTION_SET_SINGLE_PARAMETER, NRPN_FUNCTION_REQUEST_SINGLE_PARAMETER, NRPN_FUNCTION_RESPONSE_SINGLE_PARAMETER

_NRPN_ADDRESS_PAGE_FIXED = 5

# Fixed FX: Transpose on/off
def MAPPING_FIXED_TRANSPOSE():
    return _MAPPING_FIXED("TranspSt", 1)

# Fixed FX: Gate on/off
def MAPPING_FIXED_GATE():
    return _MAPPING_FIXED("FixGateSt", 6)

# Fixed FX: Compressor on/off
def MAPPING_FIXED_COMP():
    return _MAPPING_FIXED("FixCompSt", 11)

# Fixed FX: Boost on/off
def MAPPING_FIXED_BOOST():
    return _MAPPING_FIXED("FixBoost", 16)

# Fixed FX: Wah on/off
def MAPPING_FIXED_WAH():
    return _MAPPING_FIXED("FixWah", 21)

# Fixed FX: Vintage Chorus on/off
def MAPPING_FIXED_CHORUS():
    return _MAPPING_FIXED("FixChor", 26)

# Fixed FX: Air Chorus on/off
def MAPPING_FIXED_AIR():
    return _MAPPING_FIXED("FixAir", 36)

# Fixed FX: Double Tracker on/off
def MAPPING_FIXED_DBL_TRACKER():
    return _MAPPING_FIXED("FixTracker", 41)


################################################################

# Common definition shared by all fixed fx mappings
def _MAPPING_FIXED(name, param):
    return ClientParameterMapping.get(
        name = name,
        set = KemperNRPNMessage(
            NRPN_FUNCTION_SET_SINGLE_PARAMETER, 
            _NRPN_ADDRESS_PAGE_FIXED,
            param
        ),
        request = KemperNRPNMessage(               
            NRPN_FUNCTION_REQUEST_SINGLE_PARAMETER, 
            _NRPN_ADDRESS_PAGE_FIXED,
            param
        ),
        response = KemperNRPNMessage(               
            NRPN_FUNCTION_RESPONSE_SINGLE_PARAMETER, 
            _NRPN_ADDRESS_PAGE_FIXED,
            param
        )
    )
