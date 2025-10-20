from micropython import const
from .. import KemperNRPNMessage
from ....controller.client import ClientParameterMapping
from .. import NRPN_FUNCTION_SET_SINGLE_PARAMETER

_NRPN_ADDRESS_PAGE_FREEZE = const(0x7d)

_NRPN_LOOPER_PARAMETER_REC_PLAY_OVERDUB = const(88)
_NRPN_LOOPER_PARAMETER_STOP = const(89)
_NRPN_LOOPER_PARAMETER_TRIGGER = const(90)
_NRPN_LOOPER_PARAMETER_REVERSE = const(91)
_NRPN_LOOPER_PARAMETER_HALF_SPEED = const(92)
_NRPN_LOOPER_PARAMETER_CANCEL = const(93)
_NRPN_LOOPER_PARAMETER_ERASE = const(94)


def MAPPING_LOOPER_REC_PLAY_OVERDUB():
    return ClientParameterMapping.get(
        name = "LoopRec",
        set = KemperNRPNMessage(
            NRPN_FUNCTION_SET_SINGLE_PARAMETER, 
            _NRPN_ADDRESS_PAGE_FREEZE,
            _NRPN_LOOPER_PARAMETER_REC_PLAY_OVERDUB
        )
    )

def MAPPING_LOOPER_STOP():
    return ClientParameterMapping.get(
        name = "LoopStop",
        set = KemperNRPNMessage(
            NRPN_FUNCTION_SET_SINGLE_PARAMETER, 
            _NRPN_ADDRESS_PAGE_FREEZE,
            _NRPN_LOOPER_PARAMETER_STOP
        )
    )

def MAPPING_LOOPER_TRIGGER():
    return ClientParameterMapping.get(
        name = "LoopTrig",
        set = KemperNRPNMessage(
            NRPN_FUNCTION_SET_SINGLE_PARAMETER, 
            _NRPN_ADDRESS_PAGE_FREEZE,
            _NRPN_LOOPER_PARAMETER_TRIGGER
        )
    )

def MAPPING_LOOPER_REVERSE():
    return ClientParameterMapping.get(
        name = "LoopRev",
        set = KemperNRPNMessage(
            NRPN_FUNCTION_SET_SINGLE_PARAMETER, 
            _NRPN_ADDRESS_PAGE_FREEZE,
            _NRPN_LOOPER_PARAMETER_REVERSE
        )
    )

def MAPPING_LOOPER_HALF_SPEED():
    return ClientParameterMapping.get(
        name = "Loop1/2",
        set = KemperNRPNMessage(
            NRPN_FUNCTION_SET_SINGLE_PARAMETER, 
            _NRPN_ADDRESS_PAGE_FREEZE,
            _NRPN_LOOPER_PARAMETER_HALF_SPEED
        )
    )

def MAPPING_LOOPER_CANCEL():
    return ClientParameterMapping.get(
        name = "LoopCanc",
        set = KemperNRPNMessage(
            NRPN_FUNCTION_SET_SINGLE_PARAMETER, 
            _NRPN_ADDRESS_PAGE_FREEZE,
            _NRPN_LOOPER_PARAMETER_CANCEL
        )
    )

def MAPPING_LOOPER_ERASE():
    return ClientParameterMapping.get(
        name = "LoopErase",
        set = KemperNRPNMessage(
            NRPN_FUNCTION_SET_SINGLE_PARAMETER, 
            _NRPN_ADDRESS_PAGE_FREEZE,
            _NRPN_LOOPER_PARAMETER_ERASE
        )
    )