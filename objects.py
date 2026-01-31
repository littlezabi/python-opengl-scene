"""
3D object definitions and rendering
"""
import math
import numpy as np
from OpenGL.GL import *
from liquid import calculate_liquid_deformation
from utils import hsv_to_rgb, cycle_color

class LiquidSphere:
    """Animated liquid sphere with wave deformations"""
    
    def __init__(self, radius=1.0, resolution=40):
        """Initialize sphere geometry"""
        self.radius = radius
        self.resolution = resolution
        self.vertices, self.normals = self.generate_sphere()
    
    def generate_sphere(self):
        """Generate sphere vertices and normals"""
        vertices = []
        normals = []
        
        for i in range(self.resolution + 1):
            lat = math.pi * i / self.resolution - math.pi / 2
            
            for j in range(self.resolution + 1):
                lon = 2 * math.pi * j / self.resolution
                
                # Calculate position
                x = self.radius * math.cos(lat) * math.cos(lon)
                y = self.radius * math.sin(lat)
                z = self.radius * math.cos(lat) * math.sin(lon)
                
                # Normal is normalized position for sphere
                nx = math.cos(lat) * math.cos(lon)
                ny = math.sin(lat)
                nz = math.cos(lat) * math.sin(lon)
                
                vertices.append([x, y, z])
                normals.append([nx, ny, nz])
        
        return vertices, normals
    
    def render(self, time):
        """Render animated liquid sphere"""
        glPushMatrix()
        glRotatef(time * 15, 0, 1, 0)
        
        # Draw sphere with liquid animation
        for i in range(self.resolution):
            glBegin(GL_QUAD_STRIP)
            
            for j in range(self.resolution + 1):
                for k in range(2):
                    idx = (i + k) * (self.resolution + 1) + j
                    
                    # Get original vertex and normal
                    vertex = self.vertices[idx]
                    normal = self.normals[idx]
                    
                    # Apply liquid deformation
                    deformed = calculate_liquid_deformation(vertex, normal, time)
                    
                    # Calculate color based on position and time
                    hue = (vertex[1] * 0.2 + time * 0.1) % 1.0
                    color = hsv_to_rgb(hue * 0.3 + 0.5, 0.8, 1.0)
                    
                    glColor4f(color[0], color[1], color[2], 0.85)
                    glNormal3fv(normal)
                    glVertex3fv(deformed)
            
            glEnd()
        
        glPopMatrix()

class Torus:
    """Rotating torus with color gradients"""
    
    def __init__(self, major_radius=1.5, minor_radius=0.5, resolution=30):
        """Initialize torus geometry"""
        self.major_r = major_radius
        self.minor_r = minor_radius
        self.resolution = resolution
        self.vertices, self.normals = self.generate_torus()
    
    def generate_torus(self):
        """Generate torus vertices and normals"""
        vertices = []
        normals = []
        
        for i in range(self.resolution):
            theta = 2 * math.pi * i / self.resolution
            
            for j in range(self.resolution):
                phi = 2 * math.pi * j / self.resolution
                
                # Torus equations
                x = (self.major_r + self.minor_r * math.cos(phi)) * math.cos(theta)
                y = self.minor_r * math.sin(phi)
                z = (self.major_r + self.minor_r * math.cos(phi)) * math.sin(theta)
                
                # Normal calculation
                cx = self.major_r * math.cos(theta)
                cy = 0
                cz = self.major_r * math.sin(theta)
                
                nx = x - cx
                ny = y - cy
                nz = z - cz
                
                # Normalize
                length = math.sqrt(nx*nx + ny*ny + nz*nz)
                nx /= length
                ny /= length
                nz /= length
                
                vertices.append([x, y, z])
                normals.append([nx, ny, nz])
        
        return vertices, normals
    
    def render(self, time):
        """Render torus with flowing colors"""
        for i in range(self.resolution):
            glBegin(GL_QUAD_STRIP)
            
            for j in range(self.resolution + 1):
                for k in range(2):
                    ii = (i + k) % self.resolution
                    jj = j % self.resolution
                    idx = ii * self.resolution + jj
                    
                    vertex = self.vertices[idx]
                    normal = self.normals[idx]
                    
                    # Color based on angle and time
                    hue = (ii / self.resolution + time * 0.15) % 1.0
                    color = hsv_to_rgb(hue * 0.2 + 0.05, 1.0, 1.0)
                    
                    glColor4f(color[0], color[1], color[2], 0.9)
                    glNormal3fv(normal)
                    glVertex3fv(vertex)
            
            glEnd()

class WaterPlane:
    """Undulating water plane with wave effects"""
    
    def __init__(self, size=20.0, resolution=50):
        """Initialize water plane"""
        self.size = size
        self.resolution = resolution
        self.generate_plane()
    
    def generate_plane(self):
        """Generate plane grid"""
        self.step = self.size / self.resolution
    
    def render(self, time):
        """Render animated water plane"""
        glPushMatrix()
        
        half_size = self.size / 2
        
        for i in range(self.resolution):
            glBegin(GL_QUAD_STRIP)
            
            for j in range(self.resolution + 1):
                for k in range(2):
                    x = -half_size + (i + k) * self.step
                    z = -half_size + j * self.step
                    
                    # Wave calculation
                    wave = math.sin(x * 0.5 + time * 2) * math.cos(z * 0.5 + time * 2) * 0.3
                    wave += math.sin(x * 0.3 - time * 1.5) * 0.2
                    y = wave
                    
                    # Color based on wave height
                    hue = 0.5 + wave * 0.2
                    color = hsv_to_rgb(hue, 0.7, 0.6)
                    
                    glColor4f(color[0], color[1], color[2], 0.6)
                    glNormal3f(0, 1, 0)
                    glVertex3f(x, y, z)
            
            glEnd()
        
        glPopMatrix()