# Conversion function for the volume knobs which go from +12dB (100%) to 0 (50%) to -oo (0%), like the rig volume.
# Offset is the highest value. This is an approximation (see the Apple Grapher file in the /web/helpers folder. 
# Above -6dB it is pretty accurate, below the errors add up).
def convert_volume(value, offset = 0):
    if value >= 30:
        out = value * 0.24 - 24 + offset
    else:
        out = -166.6666666 / (value + 2) - 11.6 + offset

    return f"{ "+" if out > 0 else "" }{ round(out, 1) }dB"
