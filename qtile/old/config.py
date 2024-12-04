# ~/.config/qtile/config.py

from libqtile import qtile
from libqtile.config import Click, Drag
from libqtile.lazy import lazy

# Import configurations from modules
from config import (
    mod,
    terminal,
    follow_mouse_focus,
    bring_front_click,
    cursor_warp,
    auto_fullscreen,
    focus_on_window_activation,
    reconfigure_screens,
    auto_minimize,
    wl_xcursor_theme,
    wl_xcursor_size,
    widget_defaults,
    extension_defaults,
)
from config.keys import keys
from config.groups import groups
from config.layouts import layouts, floating_layout
from config.mouse import mouse
from config.screens import screens
from config.widgets import widgets

# Additional configurations
dgroups_key_binder = None
dgroups_app_rules = []

# Uncomment the following line if you use dgroups
# main = None

# Set focus behavior
# focus_on_window_activation = "smart"  # Already imported from config.__init__

# Auto-minimize behavior
# auto_minimize = True  # Already imported from config.__init__

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# Startup hooks (if any)
# from libqtile import hook
# @hook.subscribe.startup
# def autostart():
#     # Your startup applications here
