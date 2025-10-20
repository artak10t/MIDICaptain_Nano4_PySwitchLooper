from pyswitch.clients.local.actions.rotate import ROTATING_MESSAGES
from pyswitch.clients.local.actions.custom import CUSTOM_MESSAGE
from pyswitch.colors import Colors
from display import DISPLAY_HEADER_1
from display import DISPLAY_HEADER_2
from display import DISPLAY_FOOTER_1
from display import DISPLAY_FOOTER_2
from pyswitch.hardware.devices.pa_midicaptain_nano_4 import *
from pyswitch.controller.callbacks import BinaryParameterCallback
from pyswitch.controller.actions import PushButtonAction
from pyswitch.controller.client import ClientParameterMapping
from adafruit_midi.system_exclusive import SystemExclusive
from adafruit_midi.control_change import ControlChange

Inputs = [
    {
        "assignment": PA_MIDICAPTAIN_NANO_SWITCH_1,
        "actions": [
            CUSTOM_MESSAGE(
                message = [176, 20, 127],
                message_release = [176, 20, 0],
                use_leds = False
            ),
            PushButtonAction(
                {
                    "callback": BinaryParameterCallback(
                        mapping = ClientParameterMapping.get(
                            name = "Guitar",
                            set = SystemExclusive(
                                manufacturer_id = [0x00, 0x20, 0x33], 
                                data = [0x02, 0x7f, 0x01, 0x00, 0x04, 0x01]
                            ), 
                            request = SystemExclusive(
                                manufacturer_id = [0x00, 0x20, 0x33], 
                                data = [0x02, 0x7f, 0x41, 0x00, 0x04, 0x01]
                            ), 
                            response = SystemExclusive(
                                manufacturer_id = [0x00, 0x20, 0x33], 
                                data = [0x02, 0x7f, 0x01, 0x00, 0x04, 0x01]
                            )
                        ), 
                        color = Colors.RED, 
                        text = "Guitar", 
                        value_enable = 12000,
                        value_disable = "auto",
                        reference_value = 12000,
                        comparison_mode = BinaryParameterCallback.GREATER_EQUAL
                    ),
                    "display": DISPLAY_HEADER_1,
                    "useSwitchLeds": True,
                    "mode": PushButtonAction.LATCH,
                }
            )
        ],
    },
    {
        "assignment": PA_MIDICAPTAIN_NANO_SWITCH_2,
        "actions": [
            CUSTOM_MESSAGE(
                message = [176, 21, 127],
                message_release = [176, 21, 0],
                use_leds = False
            ),
            PushButtonAction(
                {
                    "callback": BinaryParameterCallback(
                        mapping = ClientParameterMapping.get(
                            name = "Vocal",
                            set = SystemExclusive(
                                manufacturer_id = [0x00, 0x20, 0x33], 
                                data = [0x02, 0x7f, 0x01, 0x00, 0x04, 0x01]
                            ), 
                            request = SystemExclusive(
                                manufacturer_id = [0x00, 0x20, 0x33], 
                                data = [0x02, 0x7f, 0x41, 0x00, 0x04, 0x01]
                            ), 
                            response = SystemExclusive(
                                manufacturer_id = [0x00, 0x20, 0x33], 
                                data = [0x02, 0x7f, 0x01, 0x00, 0x04, 0x01]
                            )
                        ), 
                        color = Colors.RED, 
                        text = "Vocal", 
                        value_enable = 12000,
                        value_disable = "auto",
                        reference_value = 12000,
                        comparison_mode = BinaryParameterCallback.GREATER_EQUAL
                    ),
                    "display": DISPLAY_HEADER_2,
                    "useSwitchLeds": True,
                    "mode": PushButtonAction.LATCH,
                }
            )
        ],
    },
    {
        "assignment": PA_MIDICAPTAIN_NANO_SWITCH_A,
 	    "actions": [
            PushButtonAction(
                {
                    "callback": BinaryParameterCallback(
                        mapping = ClientParameterMapping.get(
                            name = "Session",
                            set = ControlChange(22, 0),
                            response = ControlChange(22, 0)
                        ), 
                        color = Colors.GREEN,
                        text = "Session", 
                        value_enable = 127,
                        value_disable = 127
                    ),
                    "display": DISPLAY_FOOTER_1,
                    "useSwitchLeds": True,
                    "mode": PushButtonAction.LATCH                 
                }
            )            
        ]   
    },
    {
        "assignment": PA_MIDICAPTAIN_NANO_SWITCH_B,
        "actions": [
            CUSTOM_MESSAGE(
                message = [176, 23, 127],
                use_leds = False
            ),
            PushButtonAction(
                {
                    "callback": BinaryParameterCallback(
                        mapping = ClientParameterMapping.get(
                            name = "Undo",
                            set = SystemExclusive(
                                manufacturer_id = [0x00, 0x20, 0x33], 
                                data = [0x02, 0x7f, 0x01, 0x00, 0x04, 0x01]
                            ), 
                            request = SystemExclusive(
                                manufacturer_id = [0x00, 0x20, 0x33], 
                                data = [0x02, 0x7f, 0x41, 0x00, 0x04, 0x01]
                            ), 
                            response = SystemExclusive(
                                manufacturer_id = [0x00, 0x20, 0x33], 
                                data = [0x02, 0x7f, 0x01, 0x00, 0x04, 0x01]
                            )
                        ), 
                        color = Colors.DARK_GRAY, 
                        text = "Undo", 
                        value_enable = 12000,
                        value_disable = "auto",
                        reference_value = 12000,
                        comparison_mode = BinaryParameterCallback.GREATER_EQUAL
                    ),
                    "display": DISPLAY_FOOTER_2,
                    "useSwitchLeds": True,
                    "mode": PushButtonAction.MOMENTARY,
                }
            )
        ],
    },
    
]
