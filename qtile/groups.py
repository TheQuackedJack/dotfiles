# ~/.config/qtile/groups.py

from libqtile.config import Group, Match, Rule, Key
from libqtile.lazy import lazy
from qtile import mod # constsnts

# Parse groups from validated group config
def create_groups(group_data):
    return [
        Group(
            name=group["name"],
            matches=[Match(**match) for match in group.get("matches", [])],
            exclusive=group.get("exclusive", False),
            spawn=group.get("spawn"),
            layout=group.get("layout"),
            layouts=group.get("layouts", []),
            persist=group.get("persist", True),
            init=group.get("init", True),
            layout_opts=group.get("layout_opts", {}),
            screen_affinity=group.get("screen_affinity"),
            position=group.get("position", 9223372036854775807),
            label=group.get("label")
        )
        for group in group_data["groups"]
    ]

# Parse keybindings for groups
def create_group_keys(group_data):
    return [
        Key([mod], group["key"], lazy.group[group["name"]].toscreen())
        for group in group_data["groups"]
        if "key" in group  # Add keys only if they are defined
    ]

# Parse rules for groups
def create_rules(group_data):
    return [
        Rule(
            match=[Match(**m) for m in rule["match"]],
            float=rule.get("float", False),
            intrusive=rule.get("intrusive", False),
            break_on_match=rule.get("break_on_match", True)
        )
        for group in group_data["groups"]
        for rule in group.get("rules", [])
    ]
