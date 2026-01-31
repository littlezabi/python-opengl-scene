"""
Liquid animation calculations
"""
import math

def calculate_liquid_deformation(vertex, normal, time):
    """Calculate liquid wave deformation for a vertex"""
    x, y, z = vertex
    nx, ny, nz = normal
    
    # Multiple wave layers for complex liquid effect
    wave1 = math.sin(time * 2.0 + x * 3.0) * math.cos(time * 2.0 + y * 3.0)
    wave2 = math.sin(time * 1.5 + z * 2.5) * math.cos(time * 1.3 + x * 2.0)
    wave3 = math.sin(time * 2.5 + y * 2.0) * 0.5
    
    # Combine waves
    amplitude = 0.15
    offset = (wave1 + wave2 + wave3) * amplitude
    
    # Displace along normal
    new_x = x + nx * offset
    new_y = y + ny * offset
    new_z = z + nz * offset
    
    return [new_x, new_y, new_z]

def calculate_wave(x, y, z, time):
    """Calculate wave amplitude at a position"""
    wave = math.sin(x * 0.5 + time * 2.0) * math.cos(z * 0.5 + time * 1.5)
    wave += math.sin(x * 0.8 - time * 1.2) * math.cos(z * 0.6 + time * 1.8) * 0.5
    
    return wave * 0.3
