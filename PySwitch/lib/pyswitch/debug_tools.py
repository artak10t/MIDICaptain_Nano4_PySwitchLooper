from .controller.midi import SystemExclusive, ControlChange, ProgramChange, MIDIUnknownEvent

# Stringifies a MIDI message.
def stringify_midi_message(midi_message):
    if not midi_message:
        return repr(midi_message)
    
    ret = ""
    if isinstance(midi_message, SystemExclusive):
        # SysEx
        ret = f"{ _stringify_midi_message_part(midi_message.manufacturer_id) }{ _stringify_midi_message_part(midi_message.data) } String: { ''.join(chr(int(c)) for c in list(midi_message.data)) }"

    elif isinstance(midi_message, ControlChange):    
        # CC
        ret = repr(midi_message.control) + ", " + repr(midi_message.value)

    elif isinstance(midi_message, ProgramChange):    
        # PC
        ret = repr(midi_message.patch)

    elif isinstance(midi_message, MIDIUnknownEvent):    
        # Unknown
        ret = repr(midi_message.status)
    
    else:
        # All others
        ret = repr(midi_message)

    # Add class name
    return f"{ ret } ({ midi_message.__class__.__name__ })"

# Internal helper for stringify_midi_message(): Creates a readable hex 
# value list from the passed data.
def _stringify_midi_message_part(part):
    intlist = list(part)
    hexlist = ""
    for i in range(len(intlist)):
        end = ", "
        if i == len(intlist) - 1:
            end = ""
        hexlist = hexlist + hex(intlist[i])[2:] + end

    return f"[{ hexlist }]"
