"""Liquid and fluid animation calculations."""
import math

def calculate_liquid_deformation(vertex, normal, time, amplitude=0.15):
    """
    Calculate liquid deformation for a vertex.
    
    Args:
        vertex: Tuple (x, y, z) vertex position
        normal: Tuple (nx, ny, nz) vertex normal
        time: Current time value
        amplitude: Deformation amplitude
    
    Returns:
        tuple: New (x, y, z) position
    """
    x, y, z = vertex
    nx, ny, nz = normal
    
    wave1 = math.sin(time * 2.0 + x * 3.0) * math.cos(time * 2.0 + y * 3.0)
    wave2 = math.sin(time * 1.5 + z * 2.5) * math.cos(time * 1.8 + x * 2.0)
    wave3 = math.sin(time * 2.5 + y * 2.8) * 0.5
    
    offset = (wave1 + wave2 + wave3) * amplitude * 0.3
    new_x = x + nx * offset
    new_y = y + ny * offset
    new_z = z + nz * offset
    return (new_x, new_y, new_z)

def calculate_wave(x, y, z, time, frequency=2.0, amplitude=0.3):
    """
    Calculate wave amplitude at a position.
    
    Args:
        x, y, z: Position coordinates
        time: Current time
        frequency: Wave frequency
        amplitude: Wave amplitude
    
    Returns:
        float: Wave displacement value
    """
    wave = math.sin(x * frequency + time * 2.0) * math.cos(z * frequency + time * 2.0)
    return wave * amplitude

def calculate_ripple(x, z, time, center_x=0, center_z=0, speed=2.0):
    """
    Calculate ripple effect from a center point.
    
    Args:
        x, z: Position coordinates
        time: Current time
        center_x, center_z: Ripple center
        speed: Ripple speed
    
    Returns:
        float: Ripple displacement
    """
    dist = math.sqrt((x - center_x)**2 + (z - center_z)**2)
    ripple = math.sin(dist * 2.0 - time * speed) * math.exp(-dist * 0.2)
    return ripple * 0.2
