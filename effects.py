"""Visual effects including particles and lighting."""
import random
import math
from OpenGL.GL import *
from utils import cycle_color, hsv_to_rgb


class Particle:
    """Single particle in the particle system."""
    
    def __init__(self):
        """Initialize particle with random properties."""
        theta = random.uniform(0, 2 * math.pi)
        phi = random.uniform(0, math.pi)
        r = random.uniform(4.0, 8.0)
        
        self.x = r * math.sin(phi) * math.cos(theta)
        self.y = r * math.sin(phi) * math.sin(theta)
        self.z = r * math.cos(phi)
        
        self.vx = random.uniform(-0.5, 0.5)
        self.vy = random.uniform(-0.5, 0.5)
        self.vz = random.uniform(-0.5, 0.5)
        
        self.color_offset = random.uniform(0, 1.0)
        self.size = random.uniform(2.0, 5.0)
        
    def update(self, delta_time, time):
        """Update particle position."""
        speed = 0.3
        self.x += self.vx * delta_time * speed
        self.y += self.vy * delta_time * speed
        self.z += self.vz * delta_time * speed
        
        max_dist = 10.0
        dist = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        if dist > max_dist:
            self.x *= -0.8
            self.y *= -0.8
            self.z *= -0.8


class ParticleSystem:
    """Particle system for visual effects."""
    
    def __init__(self, count=800):
        """Initialize particle system."""
        self.particles = [Particle() for _ in range(count)]
        
    def update(self, delta_time, time):
        """Update all particles."""
        for particle in self.particles:
            particle.update(delta_time, time)
            
    def render(self, time):
        """Render all particles."""
        glDisable(GL_LIGHTING)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE)
        
        glBegin(GL_POINTS)
        for particle in self.particles:
            hue = (time * 0.1 + particle.color_offset) % 1.0
            r, g, b = hsv_to_rgb(hue, 0.8, 1.0)
            glColor4f(r, g, b, 0.6)
            glVertex3f(particle.x, particle.y, particle.z)
        glEnd()
        
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_LIGHTING)

def setup_lighting(time):
    """Set up and animate scene lighting."""
    
    Args:
        time: Current time for animation
    """
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    
    ambient = [0.2, 0.2, 0.3, 1.0]
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient)
    
    diffuse = [0.8, 0.8, 1.0, 1.0]
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse)
    
    specular = [1.0, 1.0, 1.0, 1.0]
    glLightfv(GL_LIGHT0, GL_SPECULAR, specular)
    
    light_x = math.sin(time * 0.5) * 5.0
    light_y = 3.0
    light_z = math.cos(time * 0.5) * 5.0
    position = [light_x, light_y, light_z, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, position)
    
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 50.0)