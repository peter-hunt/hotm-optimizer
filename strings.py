"""
A utility module for advanced string manipulation, styling, and formatting for CLI applications.

This module provides functions for:
- 24-bit and 8-bit ANSI color and style formatting for modern terminals.
  Colors can be specified by name, hex code, RGB tuple, or 8-bit code.
- Text layout utilities like table formatting, line wrapping, and truncation.
- String case conversion (PascalCase <-> snake_case).

Example of Advanced Coloring:
    from strings import color, format_table

    # Style text with a hex code and multiple styles
    title = color("INVENTORY", fg="#00ff9c", style=("bold", "underline"))
    print(title)

    # Use RGB tuples for specific colors
    headers = [color("Item", fg=(255, 255, 100)), color("Qty", fg=(100, 200, 255))]
    rows = [
        [color("Health Potion", fg="#ff6b6b"), 5],
        [color("Mana Potion", fg="#4d94ff"), 3]
    ]
    print(format_table(headers, rows, header_style=())) # Disable default header style
"""

import re
import textwrap
from functools import partial
from typing import Any, Iterable

__all__ = [
    "color", "style_text",
    "red", "green", "yellow", "blue", "magenta", "cyan", "white",
    "bold", "underline",
    "format_table", "wrap_text", "truncate", "pluralize",
    "is_pascal", "is_snake", "is_title",
    "pascal_to_snake", "snake_to_pascal",
    "title_to_snake", "snake_to_title",
]


# --- Core Coloring Engine ---
NAMED_STYLES = {
    # 8 standard colors
    "black": "\033[30m", "red": "\033[31m", "green": "\033[32m", "yellow": "\033[33m",
    "blue": "\033[34m", "magenta": "\033[35m", "cyan": "\033[36m", "white": "\033[37m",
    # Styles
    "bold": "\033[1m", "underline": "\033[4m", "italic": "\033[3m",
    # Reset
    "reset": "\033[0m"
}


def _hex_to_rgb(hex_str: str) -> tuple[int, int, int]:
    """Converts a hex color string to an (R, G, B) tuple."""
    hex_str = hex_str.lstrip('#')
    if len(hex_str) == 3:
        return tuple(int(c * 2, 16) for c in hex_str)
    if len(hex_str) == 6:
        return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))
    raise ValueError("Invalid hex color format. Use '#rgb' or '#rrggbb'.")


def _to_ansi_code(c: Any, background: bool = False) -> str:
    """Converts a flexible color input to an ANSI escape code string."""
    prefix = "\033[48" if background else "\033[38"

    if isinstance(c, str):
        if c.startswith('#'):
            r, g, b = _hex_to_rgb(c)
            return f"{prefix};2;{r};{g};{b}m"
        if c.lower() in NAMED_STYLES:
            # For named colors, we use the simpler 30-37 codes
            if background:
                return NAMED_STYLES[c.lower()].replace("[3", "[4")
            return NAMED_STYLES[c.lower()]
        raise ValueError(f"Unknown color name: '{c}'")

    if isinstance(c, int):  # 8-bit color
        if 0 <= c <= 255:
            return f"{prefix};5;{c}m"
        raise ValueError("8-bit color code must be between 0 and 255.")

    if isinstance(c, (tuple, list)) and len(c) == 3:  # RGB color
        r, g, b = c
        return f"{prefix};2;{r};{g};{b}m"

    raise TypeError(
        f"Unsupported color type: '{type(c).__name__}'. Use str, int, or tuple(r,g,b).")


def color(
    text: Any,
    fg: Any = None,
    bg: Any = None,
    style: str | Iterable[str] | None = None
) -> str:
    """
    Applies foreground, background, and text styles using 24-bit/8-bit ANSI codes.

    Args:
        text: The text to be styled.
        fg (Any, optional): Foreground color. Can be a name ('red'), hex ('#ff0000'),
                            RGB tuple ((255,0,0)), or 8-bit int (0-255).
        bg (Any, optional): Background color. Accepts the same formats as `fg`.
        style (str | Iterable[str], optional): A style name ('bold') or list of names.

    Returns:
        The styled string with ANSI escape codes.
    """
    codes = []
    if fg:
        codes.append(_to_ansi_code(fg, background=False))
    if bg:
        codes.append(_to_ansi_code(bg, background=True))
    if style:
        if isinstance(style, str):
            style = [style]
        for s in style:
            if s.lower() in NAMED_STYLES:
                codes.append(NAMED_STYLES[s.lower()])

    if not codes:
        return str(text)

    return "".join(codes) + str(text) + NAMED_STYLES["reset"]


# --- Convenience and Backward Compatibility ---
def style_text(text: str, *styles: str) -> str:
    """
    (Compatibility) Apply one or more simple ANSI styles to a string.
    Note: `color()` is more powerful.
    """
    return "".join(styles) + str(text) + NAMED_STYLES["reset"]


# Refactored convenience functions to use the new `color` engine
red = partial(color, fg="red")
green = partial(color, fg="green")
yellow = partial(color, fg="yellow")
blue = partial(color, fg="blue")
magenta = partial(color, fg="magenta")
cyan = partial(color, fg="cyan")
white = partial(color, fg="white")
bold = partial(color, style="bold")
underline = partial(color, style="underline")


# --- Text Layout Engine ---
def format_table(headers: list[str], rows: list[list[Any]], header_style: tuple = ("bold", "underline")) -> str:
    """
    Formats data into a clean, aligned text-based table.
    Can handle pre-colored strings.
    """
    # Helper to get the visible length of a string, ignoring ANSI codes
    def visible_len(s):
        return len(re.sub(r'\033\[[0-9;]*m', '', str(s)))

    if not rows and not headers:
        return ""

    all_data = [[str(item) for item in headers]] + [[str(item)
                                                     for item in row] for row in rows]
    col_widths = [max(visible_len(item) for item in col)
                  for col in zip(*all_data)]

    # Format header
    styled_headers = [color(h, style=header_style)
                      for h in headers] if header_style else headers
    header_line = "  ".join(h + " " * (w - visible_len(h))
                            for h, w in zip(styled_headers, col_widths))
    separator = "-" * visible_len(header_line)

    row_lines = []
    for row in rows:
        row_lines.append("  ".join(item + " " * (w - visible_len(item))
                         for item, w in zip(row, col_widths)))

    return "\n".join([header_line, separator] + row_lines)


def wrap_text(text: str, width: int = 70) -> str:
    """Wraps a long string to a specified width."""
    return textwrap.fill(text, width=width)


def truncate(text: str, length: int, suffix: str = "...") -> str:
    """Truncates a string to a max length."""
    if len(text) <= length:
        return text
    return text[:length - len(suffix)] + suffix


def pluralize(count: int, singular: str, plural: str | None = None) -> str:
    """Returns a formatted string with the correct singular/plural form."""
    if count == 1:
        return f"{count} {singular}"
    if plural:
        return f"{count} {plural}"
    return f"{count} {singular}s"


# --- Case Conversion ---
def is_pascal(s: str) -> bool:
    """Check if a string is in PascalCase."""
    return re.fullmatch(r"([A-Z][a-z0-9]*)+", s) is not None


def is_snake(s: str) -> bool:
    """Check if a string is in snake_case."""
    return re.fullmatch(r"[a-z0-9]+(_[a-z0-9]+)*", s) is not None


def is_title(s: str) -> bool:
    """Check if a string is in Title Case."""
    return re.fullmatch(r"[A-Z][a-z0-9]*( [A-Z][a-z0-9])*", s) is not None


def pascal_to_snake(s: str) -> str:
    """Convert a PascalCase string to snake_case."""
    return "".join(f"_{c.lower()}" if c.isupper() else c for c in s).lstrip("_")


def snake_to_pascal(s: str) -> str:
    """Convert a snake_case string to PascalCase."""
    return "".join(c.capitalize() for c in s.split("_"))


def title_to_snake(s: str) -> str:
    """Convert a Title Case string to snake_case."""
    return '_'.join(word.lower() for word in s.split(' '))


def snake_to_title(s: str) -> str:
    """Convert a snake_case string to Title Case."""
    return ' '.join(word.capitalize() for word in s.split('_'))
