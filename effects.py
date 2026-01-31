"""
Visual effects: particles and lighting
"""
import random
import math
from OpenGL.GL import *
from utils import hsv_to_rgb

class ParticleSystem:
    """Colorful particle system"""
    
    def __init__(self, count=800):
        """Initialize particles"""
        self.count = count
        self.particles = []
        
        for i in range(count):
            # Random position in sphere
            theta = random.uniform(0, 2 * math.pi)
            phi = random.uniform(0, math.pi)
            r = random.uniform(4, 8)
            
            x = r * math.sin(phi) * math.cos(theta)
            y = r * math.sin(phi) * math.sin(theta)
            z = r * math.cos(phi)
            
            # Random velocity
            vx = random.uniform(-0.5, 0.5)
            vy = random.uniform(-0.5, 0.5)
            vz = random.uniform(-0.5, 0.5)
            
            # Random color offset
            color_offset = random.uniform(0, 1)
            
            self.particles.append({
                'pos': [x, y, z],
                'vel': [vx, vy, vz],
                'color_offset': color_offset,
                'size': random.uniform(2, 5)
            })
    
    def update(self, time, delta_time):
        """Update particle positions"""
        for p in self.particles:
            # Update position
            p['pos'][0] += p['vel'][0] * delta_time
            p['pos'][1] += p['vel'][1] * delta_time
            p['pos'][2] += p['vel'][2] * delta_time
            
            # Boundary check - reset if too far
            dist = math.sqrt(sum(x*x for x in p['pos']))
            if dist > 10:
                # Reset to inner sphere
                theta = random.uniform(0, 2 * math.pi)
                phi = random.uniform(0, math.pi)
                r = random.uniform(4, 6)
                
                p['pos'][0] = r * math.sin(phi) * math.cos(theta)
                p['pos'][1] = r * math.sin(phi) * math.sin(theta)
                p['pos'][2] = r * math.cos(phi)
    
    def render(self, time):
        """Render all particles"""
        glDisable(GL_LIGHTING)
        
        for p in self.particles:
            # Calculate color
            hue = (time * 0.1 + p['color_offset']) % 1.0
            color = hsv_to_rgb(hue, 0.9, 1.0)
            
            glColor4f(color[0], color[1], color[2], 0.8)
            glPointSize(p['size'])
            
            glBegin(GL_POINTS)
            glVertex3fv(p['pos'])
            glEnd()
        
        glEnable(GL_LIGHTING)

def setup_lighting(time):
    """Configure dynamic lighting"""
    # Ambient light
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.3, 1.0])
    
    # Diffuse light
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.8, 0.8, 1.0, 1.0])
    
    # Specular light
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    
    # Animated light position (orbiting)
    light_x = math.sin(time * 0.5) * 6
    light_y = 4.0
    light_z = math.cos(time * 0.5) * 6
    
    glLightfv(GL_LIGHT0, GL_POSITION, [light_x, light_y, light_z, 1.0])
