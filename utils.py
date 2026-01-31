"""
Utility functions for colors and math
"""
import colorsys

def hsv_to_rgb(h, s, v):
    """Convert HSV to RGB (all values 0-1)"""
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return (r, g, b)

def cycle_color(time, speed=0.1):
    """Get a time-based cycling color"""
    hue = (time * speed) % 1.0
    return hsv_to_rgb(hue, 0.8, 1.0)