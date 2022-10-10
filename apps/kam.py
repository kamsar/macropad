# MACROPAD Hotkeys example: Function keys

from utils.apps.key import Key, KeyApp
from utils.commands import (
    ConsumerControlCode,
    Keycode,
    Media,
    Press,
    Release,
    Sequence,
    Text
)
from utils.constants import COLOR_FUNC


class KamApp(KeyApp):
    name = "Freyja's Blessings"

    # First row
    key_0 = Key("Split", COLOR_FUNC, Press(Keycode.COMMAND, Keycode.BACKSLASH))
    key_1 = Key("Windows", COLOR_FUNC, Press(Keycode.CONTROL, Keycode.W))
    key_2 = Key("Log", COLOR_FUNC, Text("console.log('log', "),
                double_tap_command=Text('JSON.stringify(x, null, 2)'))

    # Second row
    key_3 = Key("Focus", COLOR_FUNC,
                Press(Keycode.COMMAND, Keycode.OPTION, Keycode.T),
                double_tap_command=Sequence(Press(Keycode.COMMAND, Keycode.K), Release(Keycode.K), Press(Keycode.W), Release(Keycode.W, Keycode.COMMAND)))
    key_4 = Key("Reveal", COLOR_FUNC,
                Sequence(Press(Keycode.F1), Text(
                    "reveal in explorer"), Press(Keycode.ENTER)),
                double_tap_command=Sequence(Press(Keycode.F1), Text("reveal in finder"), Press(Keycode.ENTER)))
    key_5 = Key("Jump", COLOR_FUNC, Press(
        Keycode.COMMAND, Keycode.SHIFT, Keycode.O))

    # Third row
    key_6 = Key("Wrap", COLOR_FUNC, Sequence(
        Press(Keycode.F1), Text("wrap with"), Press(Keycode.ENTER)))
    key_7 = Key("Refactor", COLOR_FUNC, Press(
        Keycode.CONTROL, Keycode.SHIFT, Keycode.R))
    key_8 = Key("Fmt", COLOR_FUNC, Press(
        Keycode.OPTION, Keycode.SHIFT, Keycode.F))

    # Fourth row
    key_9 = Key("<<", COLOR_FUNC, Media(
        ConsumerControlCode.SCAN_PREVIOUS_TRACK))
    key_10 = Key("> ||", COLOR_FUNC, Media(ConsumerControlCode.PLAY_PAUSE))
    key_11 = Key(">>", COLOR_FUNC, Media(ConsumerControlCode.SCAN_NEXT_TRACK))

    # go to last edited location (note: cmd-k, q seems to not be happy with macros so using ye olde search)
    encoder_button = Sequence(Press(Keycode.COMMAND, Keycode.K), Release(Keycode.K), Press(Keycode.Q), Release(Keycode.Q, Keycode.COMMAND))

    # next/prev locations
    encoder_increase = Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.MINUS)
    encoder_decrease = Press(Keycode.CONTROL, Keycode.MINUS)
