# ~/.config/qtile/config/groups.py

from libqtile.config import Group, Key
from libqtile.lazy import lazy
from config import mod
from .keys import keys  # Import keys to extend them with group keys

# Define groups
groups = [Group(i) for i in "123456789"]

# Add key bindings for switching to groups and moving windows to groups
for i in groups:
    keys.extend(
        [
            # Switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # Move window to group and switch to that group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Move focused window to group {i.name} and switch to it",
            ),
        ]
    )
