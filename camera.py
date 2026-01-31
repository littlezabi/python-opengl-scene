"""Camera controls and transformations."""
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import math


class Camera:
    """Camera class for handling view transformations."""
    
    def __init__(self):
        """Initialize camera with default values."""
        self.distance = 10.0
        self.rotation_x = 20.0
        self.rotation_y = 0.0
        self.auto_rotate = True
        self.auto_rotate_speed = 10.0
        
    def update(self, keys, delta_time):
        """Update camera based on input."""
        rotate_speed = 50.0 * delta_time
        zoom_speed = 5.0 * delta_time
        
        if keys[pygame.K_LEFT]:
            self.rotation_y -= rotate_speed
            self.auto_rotate = False
        if keys[pygame.K_RIGHT]:
            self.rotation_y += rotate_speed
            self.auto_rotate = False
        if keys[pygame.K_UP]:
            self.rotation_x -= rotate_speed
            self.auto_rotate = False
        if keys[pygame.K_DOWN]:
            self.rotation_x += rotate_speed
            self.auto_rotate = False
            
        if keys[pygame.K_PLUS] or keys[pygame.K_EQUALS] or keys[pygame.K_w]:
            self.distance = max(3.0, self.distance - zoom_speed)
        if keys[pygame.K_MINUS] or keys[pygame.K_s]:
            self.distance = min(20.0, self.distance + zoom_speed)
            
        if keys[pygame.K_SPACE]:
            pygame.time.wait(200)  # Debounce
            self.auto_rotate = not self.auto_rotate
            
        if self.auto_rotate:
            self.rotation_y += self.auto_rotate_speed * delta_time
            
        # Clamp vertical rotation
        self.rotation_x = max(-80.0, min(80.0, self.rotation_x))
        
    def apply(self):
        """Apply camera transformations."""
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -self.distance)
        glRotatef(self.rotation_x, 1, 0, 0)
        glRotatef(self.rotation_y, 0, 1, 0)
