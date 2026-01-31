"""
Camera controls and transformations
"""
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

class Camera:
    """Camera controller with rotation and zoom"""
    
    def __init__(self):
        """Initialize camera"""
        self.distance = 10.0
        self.rotation_x = 20.0
        self.rotation_y = 0.0
        self.auto_rotation_speed = 15.0
        self.manual_rotation_speed = 50.0
        self.zoom_speed = 5.0
        
        self.min_distance = 5.0
        self.max_distance = 20.0
    
    def update(self, keys, auto_rotate, delta_time):
        """Update camera based on input"""
        # Auto rotation
        if auto_rotate:
            self.rotation_y += self.auto_rotation_speed * delta_time
        
        # Manual rotation with arrow keys
        if keys[K_LEFT]:
            self.rotation_y -= self.manual_rotation_speed * delta_time
        if keys[K_RIGHT]:
            self.rotation_y += self.manual_rotation_speed * delta_time
        if keys[K_UP]:
            self.rotation_x += self.manual_rotation_speed * delta_time
        if keys[K_DOWN]:
            self.rotation_x -= self.manual_rotation_speed * delta_time
        
        # Zoom with +/- or W/S
        if keys[K_PLUS] or keys[K_EQUALS] or keys[K_w]:
            self.distance -= self.zoom_speed * delta_time
        if keys[K_MINUS] or keys[K_s]:
            self.distance += self.zoom_speed * delta_time
        
        # Clamp distance
        self.distance = max(self.min_distance, min(self.max_distance, self.distance))
        
        # Clamp rotation_x
        self.rotation_x = max(-89, min(89, self.rotation_x))
    
    def apply(self):
        """Apply camera transformations"""
        glLoadIdentity()
        
        # Move camera back
        glTranslatef(0, 0, -self.distance)
        
        # Apply rotations
        glRotatef(self.rotation_x, 1, 0, 0)
        glRotatef(self.rotation_y, 0, 1, 0)
