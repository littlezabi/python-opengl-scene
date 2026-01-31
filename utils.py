"""Utility functions for color conversion and math helpers."""
import colorsys
import math

def hsv_to_rgb(h, s, v):
    """
    Convert HSV color to RGB.
    
    Args:
        h: Hue (0.0 to 1.0)
        s: Saturation (0.0 to 1.0)
        v: Value (0.0 to 1.0)
    
    Returns:
        tuple: (r, g, b) values from 0.0 to 1.0
    """
    return colorsys.hsv_to_rgb(h, s, v)

def cycle_color(time, speed=0.1, saturation=1.0, value=1.0):
    """
    Generate a cycling color based on time.
    
    Args:
        time: Current time value
        speed: Speed of color cycling
        saturation: Color saturation (0.0 to 1.0)
        value: Color brightness (0.0 to 1.0)
    
    Returns:
        tuple: (r, g, b) color values
    """
    hue = (time * speed) % 1.0
    return hsv_to_rgb(hue, saturation, value)

def lerp(a, b, t):
    """Linear interpolation between a and b."""
    return a + (b - a) * t

def clamp(value, min_val, max_val):
    """Clamp value between min and max."""
    return max(min_val, min(max_val, value))
