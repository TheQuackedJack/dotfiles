# ~/.config/qtile/config/screens.py

from libqtile.config import Screen
from libqtile import bar
from .widgets import widgets  # Import the widgets
from config import widget_defaults

# Screens and bars
screens = [
    Screen(
        bottom=bar.Bar(
            widgets,
            24,
            # Border settings (optional)
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"],  # Borders are magenta
        ),
    ),
    # Add more screens if you have multiple monitors
]
