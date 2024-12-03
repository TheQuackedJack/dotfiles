# ~/.config/qtile/config/__init__.py

# Define global settings and variables

mod = "mod4"           # Sets the mod key to SUPER/WINDOWS
terminal = "alacritty" # Your preferred terminal emulator

# Qtile settings
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

# Widget defaults
widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()