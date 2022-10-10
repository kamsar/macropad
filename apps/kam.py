# MACROPAD Hotkeys example: Function keys

from utils.apps.key import Key, KeyApp
from utils.commands import (
    ConsumerControlCode,
    Keycode,
    Media,
    Press,
    Sequence,
    Text
)
from utils.constants import COLOR_FUNC


class KamApp(KeyApp):
    name = "Freyja's Blessings"

    # First row
    key_0 = Key("Split", COLOR_FUNC, Press(Keycode.COMMAND, Keycode.BACKSLASH))
    key_1 = Key("WindSw", COLOR_FUNC, Press(Keycode.CONTROL, Keycode.W))
    key_2 = Key("Log/Dmp", COLOR_FUNC, Text("console.log('log', "), double_tap_command=Text('JSON.stringify(x, null, 2)'))

    # Second row
    key_3 = Key("Focus", COLOR_FUNC, Press(Keycode.COMMAND, Keycode.OPTION, Keycode.T))
    key_4 = Key("Reveal", COLOR_FUNC, Sequence(Press(Keycode.F1), Text("reveal in explorer"), Press(Keycode.ENTER)), double_tap_command=Sequence())
    key_5 = Key("JmpFn", COLOR_FUNC, Press(Keycode.COMMAND, Keycode.SHIFT, Keycode.O))

    # Third row
    key_6 = Key("Wrap", COLOR_FUNC, Sequence(Press(Keycode.F1), Text("wrap with"), Press(Keycode.ENTER)))
    key_7 = Key("Refac", COLOR_FUNC, Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.R))
    key_8 = Key("Fmt", COLOR_FUNC, Press(Keycode.OPTION, Keycode.SHIFT, Keycode.F))

    # Fourth row
    key_9 = Key("<<", COLOR_FUNC, Media(ConsumerControlCode.SCAN_PREVIOUS_TRACK))
    key_10 = Key("> ||", COLOR_FUNC, Media(ConsumerControlCode.PLAY_PAUSE))
    key_11 = Key(">>", COLOR_FUNC, Media(ConsumerControlCode.SCAN_NEXT_TRACK))

    encoder_button = Media(ConsumerControlCode.MUTE)

    encoder_increase = Media(ConsumerControlCode.VOLUME_INCREMENT)
    encoder_decrease = Media(ConsumerControlCode.VOLUME_DECREMENT)
