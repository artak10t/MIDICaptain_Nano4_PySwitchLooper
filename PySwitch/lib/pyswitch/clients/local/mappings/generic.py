from ....controller.client import ClientParameterMapping
from adafruit_midi.program_change import ProgramChange

# Send a simple PC message
def MAPPING_SEND_PROGRAM_CHANGE(): 
    return ClientParameterMapping.get(
        name = "ProgChg",
        set = ProgramChange(
            0    # Dummy value, will be overridden
        )
    )