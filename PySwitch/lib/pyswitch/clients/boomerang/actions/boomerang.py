from ....colors import Colors, dim_color
from ...local.actions.rotate import ROTATING_MESSAGES

# Play/Stop all for the Boomerang III Phrase Sampler
def BOOMERANG_PLAY_STOP_ALL(display = None,
                            id = False,
                            use_leds = True,
                            enable_callback = None,
                            text = "PlayStp",
                            color = Colors.GREEN,
                            led_brightness_1 = 0.3,
                            led_brightness_2 = 0.02,
                            num_leds = 1
):
    return _BOOMERANG_ACTION(
        pc_1 = 17,
        pc_2 = 25,
        display = display,
        id = id,
        use_leds = use_leds,
        enable_callback = enable_callback,
        text = text,
        color = color,
        led_brightness_1 = led_brightness_1,
        led_brightness_2 = led_brightness_2,
        num_leds = num_leds
    )

# Sync Serial for the Boomerang III Phrase Sampler
def BOOMERANG_SYNC_SERIAL(display = None,
                          id = False,
                          use_leds = True,
                          enable_callback = None,
                          text = "SyncSerial",
                          color = Colors.YELLOW,
                          led_brightness_1 = 0.3,
                          led_brightness_2 = 0.02,
                          num_leds = 1
):
    return _BOOMERANG_ACTION(
        pc_1 = 43,
        pc_2 = 65,
        display = display,
        id = id,
        use_leds = use_leds,
        enable_callback = enable_callback,
        text = text,
        color = color,
        led_brightness_1 = led_brightness_1,
        led_brightness_2 = led_brightness_2,
        num_leds = num_leds
    )

# Mute/Thru for the Boomerang III Phrase Sampler
def BOOMERANG_MUTE_THRU(display = None,
                          id = False,
                          use_leds = True,
                          enable_callback = None,
                          text = "MuteThru",
                          color = Colors.PURPLE,
                          led_brightness_1 = 0.3,
                          led_brightness_2 = 0.02,
                          num_leds = 1
):
    return _BOOMERANG_ACTION(
        pc_1 = 3,
        pc_2 = 8,
        display = display,
        id = id,
        use_leds = use_leds,
        enable_callback = enable_callback,
        text = text,
        color = color,
        led_brightness_1 = led_brightness_1,
        led_brightness_2 = led_brightness_2,
        num_leds = num_leds
    )

# Panic for the Boomerang III Phrase Sampler
def BOOMERANG_PANIC(display = None,
                    id = False,
                    use_leds = True,
                    enable_callback = None,
                    text = "PANIC",
                    color = Colors.RED,
                    led_brightness_1 = 0.3,
                    led_brightness_2 = 0.02,
                    num_leds = 1
):
    return _BOOMERANG_ACTION(
        pc_1 = 11,
        pc_2 = 40,
        display = display,
        id = id,
        use_leds = use_leds,
        enable_callback = enable_callback,
        text = text,
        color = color,
        led_brightness_1 = led_brightness_1,
        led_brightness_2 = led_brightness_2,
        num_leds = num_leds
    )

# Erase for the Boomerang III Phrase Sampler
def BOOMERANG_ERASE(display = None,
                    id = False,
                    use_leds = True,
                    enable_callback = None,
                    text = "ERASE",
                    color = Colors.RED,
                    led_brightness_1 = 0.3,
                    led_brightness_2 = 0.02,
                    num_leds = 1
):
    return _BOOMERANG_ACTION(
        pc_1 = 16,
        pc_2 = 61,
        display = display,
        id = id,
        use_leds = use_leds,
        enable_callback = enable_callback,
        text = text,
        color = color,
        led_brightness_1 = led_brightness_1,
        led_brightness_2 = led_brightness_2,
        num_leds = num_leds
    )

# Erase all for the Boomerang III Phrase Sampler
def BOOMERANG_ERASE_ALL(display = None,
                        id = False,
                        use_leds = True,
                        enable_callback = None,
                        text = "ERASEALL",
                        color = Colors.RED,
                        led_brightness_1 = 0.3,
                        led_brightness_2 = 0.02,
                        num_leds = 1
):
    return _BOOMERANG_ACTION(
        pc_1 = 28,
        pc_2 = 35,
        display = display,
        id = id,
        use_leds = use_leds,
        enable_callback = enable_callback,
        text = text,
        color = color,
        led_brightness_1 = led_brightness_1,
        led_brightness_2 = led_brightness_2,
        num_leds = num_leds
    )

# Stack for the Boomerang III Phrase Sampler
def BOOMERANG_STACK(display = None,
                    id = False,
                    use_leds = True,
                    enable_callback = None,
                    text = "Stack",
                    color = Colors.YELLOW,
                    led_brightness_1 = 0.3,
                    led_brightness_2 = 0.02,
                    num_leds = 1
):
    return _BOOMERANG_ACTION(
        pc_1 = 15,
        pc_2 = 23,
        display = display,
        id = id,
        use_leds = use_leds,
        enable_callback = enable_callback,
        text = text,
        color = color,
        led_brightness_1 = led_brightness_1,
        led_brightness_2 = led_brightness_2,
        num_leds = num_leds
    )

# Copy for the Boomerang III Phrase Sampler
def BOOMERANG_COPY(display = None,
                   id = False,
                   use_leds = True,
                   enable_callback = None,
                   text = "Copy",
                   color = Colors.BLUE,
                   led_brightness_1 = 0.3,
                   led_brightness_2 = 0.02,
                   num_leds = 1
):
    return _BOOMERANG_ACTION(
        pc_1 = 1,
        pc_2 = 4,
        display = display,
        id = id,
        use_leds = use_leds,
        enable_callback = enable_callback,
        text = text,
        color = color,
        led_brightness_1 = led_brightness_1,
        led_brightness_2 = led_brightness_2,
        num_leds = num_leds
    )

# Fade for the Boomerang III Phrase Sampler
def BOOMERANG_FADE(display = None,
                   id = False,
                   use_leds = True,
                   enable_callback = None,
                   text = "Fade",
                   color = Colors.LIGHT_BLUE,
                   led_brightness_1 = 0.3,
                   led_brightness_2 = 0.02,
                   num_leds = 1
):
    return _BOOMERANG_ACTION(
        pc_1 = 21,
        pc_2 = 32,
        display = display,
        id = id,
        use_leds = use_leds,
        enable_callback = enable_callback,
        text = text,
        color = color,
        led_brightness_1 = led_brightness_1,
        led_brightness_2 = led_brightness_2,
        num_leds = num_leds
    )

# Octave for the Boomerang III Phrase Sampler
def BOOMERANG_OCTAVE(display = None,
                     id = False,
                     use_leds = True,
                     enable_callback = None,
                     text = "Octave",
                     color = Colors.WHITE,
                     led_brightness_1 = 0.3,
                     led_brightness_2 = 0.02,
                     num_leds = 1
):
    return _BOOMERANG_ACTION(
        pc_1 = 2,
        pc_2 = 49,
        display = display,
        id = id,
        use_leds = use_leds,
        enable_callback = enable_callback,
        text = text,
        color = color,
        led_brightness_1 = led_brightness_1,
        led_brightness_2 = led_brightness_2,
        num_leds = num_leds
    )

# Once for the Boomerang III Phrase Sampler
def BOOMERANG_ONCE(display = None,
                   id = False,
                   use_leds = True,
                   enable_callback = None,
                   text = "Once",
                   color = Colors.LIGHT_GREEN,
                   led_brightness_1 = 0.3,
                   led_brightness_2 = 0.02,
                   num_leds = 1
):
    return _BOOMERANG_ACTION(
        pc_1 = 10,
        pc_2 = 18,
        display = display,
        id = id,
        use_leds = use_leds,
        enable_callback = enable_callback,
        text = text,
        color = color,
        led_brightness_1 = led_brightness_1,
        led_brightness_2 = led_brightness_2,
        num_leds = num_leds
    )

# Reverse for the Boomerang III Phrase Sampler
def BOOMERANG_REVERSE(display = None,
                      id = False,
                      use_leds = True,
                      enable_callback = None,
                      text = "Reverse",
                      color = Colors.TURQUOISE,
                      led_brightness_1 = 0.3,
                      led_brightness_2 = 0.02,
                      num_leds = 1
):
    return _BOOMERANG_ACTION(
        pc_1 = 47,
        pc_2 = 56,
        display = display,
        id = id,
        use_leds = use_leds,
        enable_callback = enable_callback,
        text = text,
        color = color,
        led_brightness_1 = led_brightness_1,
        led_brightness_2 = led_brightness_2,
        num_leds = num_leds
    )

##########################################################################

# Generic base for boomerang actions. Sends alternating program changes according to this documentation:
# https://docs.google.com/spreadsheets/d/e/2PACX-1vRKr8ttZLSIDv1lK7TfUtOViNB0szfXfeRY5ljkcO00BuiLVeKsJLb_H3SE1rU4grACfDoBipLCnu6Q/pubhtml?fbclid=IwAR07NmuCNAbIilwMjv3MT7FDmX1zn89htp21m24x-Rn0f7V-Zu8hS6Sa8N4
def _BOOMERANG_ACTION(pc_1,
                      pc_2,
                      display,
                      id,
                      use_leds,
                      enable_callback,
                      text,
                      color,
                      led_brightness_1,
                      led_brightness_2,
                      num_leds = 1
):
    return ROTATING_MESSAGES(
        messages = (
            (207, pc_1),
            (207, pc_2)
        ),
        display = display,
        id = id,
        use_leds = use_leds,
        enable_callback = enable_callback,
        texts = [text],
        led_colors = [
            [
                dim_color(color, led_brightness_1 if i == (num_leds - j - 1) else led_brightness_2)
                for j in range(num_leds)
            ]
            for i in range(num_leds)
        ] if num_leds > 1 else [
            dim_color(color, led_brightness_1),
            dim_color(color, led_brightness_2)
        ],
        display_colors = [
            color
        ],
        led_brightness = 1,
        num_leds = num_leds
    )
