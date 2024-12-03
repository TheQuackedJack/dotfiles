# ~/.config/qtile/config/widgets.py

from libqtile import widget
from config import widget_defaults, extension_defaults

# Widget list
widgets = [
    widget.CurrentLayout(),
    widget.GroupBox(),
    widget.Prompt(),
    widget.WindowName(),
    widget.Chord(
        chords_colors={
            "launch": ("#ff0000", "#ffffff"),
        },
        name_transform=lambda name: name.upper(),
    ),
    widget.TextBox("default config", name="default"),
    widget.TextBox(
        "Press <M-r> to spawn",
        foreground="#d75f5f",
    ),
    # Systray (note: incompatible with Wayland)
    # widget.StatusNotifier(),
    widget.Systray(),
    widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
    widget.QuickExit(),
]
