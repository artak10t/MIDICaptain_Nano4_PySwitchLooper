from adafruit_midi import MIDI as _MIDI
from adafruit_midi.midi_message import MIDIUnknownEvent as _MIDIUnknownEvent
from busio import UART as _UART

# DIN MIDI Device
class AdafruitDinMidiDevice:
    def __init__(self, 
                 gpio_in, 
                 gpio_out,
                 in_buf_size, 
                 baudrate, 
                 timeout,
                 in_channel = None,   # All
                 out_channel = 0, 
        ):

        midi_uart = _UART(
            gpio_in, 
            gpio_out, 
            baudrate = baudrate, 
            timeout = timeout
        ) 

        self.__midi = _MIDI(
            midi_out = midi_uart, 
            out_channel = out_channel,
            midi_in = midi_uart, 
            in_channel = in_channel,
            in_buf_size = in_buf_size
        )

    # def __repr__(self):
    #     return "DIN"

    def send(self, midi_message):
        if isinstance(midi_message, _MIDIUnknownEvent):
            return
        
        self.__midi.send(midi_message)

    def receive(self):
        return self.__midi.receive()