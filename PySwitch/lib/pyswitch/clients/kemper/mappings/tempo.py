from micropython import const
from .. import KemperNRPNExtendedMessage
from ....controller.client import ClientParameterMapping

from adafruit_midi.control_change import ControlChange

_CC_TAP_TEMPO = const(30)

# Switch tuner mode on/off (no receive possible!)
def MAPPING_TAP_TEMPO(): 
    return ClientParameterMapping.get(
        name = "Tap Tempo",
        set = ControlChange(
            _CC_TAP_TEMPO, 
            0    # Dummy value, will be overridden
        )
    )

def MAPPING_TEMPO_DISPLAY():
    return ClientParameterMapping.get(
        name = "Tempo Pulse",
        response = KemperNRPNExtendedMessage(
            0x01,
            [
                0x7c,
                0x00,
                0x00
            ]
        )
    )

# MIDI Clock message, sent 24x every beat
#MAPPING_MIDI_CLOCK = ClientParameterMapping.get(
#    name = "Clock",
#    response = MidiClockMessage()
#)

#MAPPING_MIDI_CLOCK_START = ClientParameterMapping.get(
#    name = "Start",
#    response = Start()
#)