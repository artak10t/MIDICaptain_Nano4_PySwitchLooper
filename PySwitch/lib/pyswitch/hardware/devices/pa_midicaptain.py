import board as _board
from usb_midi import ports as _ports

# USB Midi in/out for PA MIDICaptain devices. No UART, so ports have to be adafruit MIDI ports from 
# the usb_midi module.
def PA_MIDICAPTAIN_USB_MIDI(in_channel = None, out_channel = 0, in_buf_size = 100):
    from ..adafruit.AdafruitUsbMidiDevice import AdafruitUsbMidiDevice
    return AdafruitUsbMidiDevice(
        port_in = _ports[0],
        port_out = _ports[1],
        in_channel = in_channel,
        out_channel = out_channel,
        in_buf_size = in_buf_size
    )

# DIN Midi in/out for PA MIDICaptain devices. Uses UART mode so the ports must be board GPIO pins.
def PA_MIDICAPTAIN_DIN_MIDI(in_channel = None, out_channel = 0, in_buf_size = 100):
    from ..adafruit.AdafruitDinMidiDevice import AdafruitDinMidiDevice
    return AdafruitDinMidiDevice(
        gpio_in = _board.GP16,
        gpio_out = _board.GP17,
        in_channel = in_channel,
        out_channel = out_channel,
        baudrate = 31250,
        timeout = 0.001,
        in_buf_size = in_buf_size
    )

