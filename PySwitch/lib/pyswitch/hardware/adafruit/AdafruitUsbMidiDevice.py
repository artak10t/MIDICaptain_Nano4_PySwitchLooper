from adafruit_midi import MIDI as _MIDI
from adafruit_midi.midi_message import MIDIUnknownEvent as _MIDIUnknownEvent

# USB MIDI Device
class AdafruitUsbMidiDevice:
    def __init__(self, 
                 port_in,
                 port_out,
                 in_buf_size,
                 in_channel = None,  # All
                 out_channel = 0,                 
        ):

        self.__midi = _MIDI(
            midi_out = port_out,
            out_channel = out_channel,
            midi_in = port_in,
            in_channel = in_channel,
            in_buf_size = in_buf_size
        )

    # def __repr__(self):
    #     return "USB"

    def send(self, midi_message):
        if isinstance(midi_message, _MIDIUnknownEvent):
            return
        
        self.__midi.send(midi_message)

    def receive(self):
        return self.__midi.receive()