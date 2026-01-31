"""
Beautiful 3D Scene with Pygame and OpenGL
Main entry point and game loop
"""
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys

from scene import Scene
from camera import Camera

# Window settings
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FPS = 60

def main():
    """Main application entry point"""
    # Initialize Pygame
    pygame.init()
    
    # Set up display with OpenGL
    display = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT), 
        DOUBLEBUF | OPENGL
    )
    pygame.display.set_caption("Beautiful 3D OpenGL Scene")
    
    # Initialize scene and camera
    scene = Scene()
    camera = Camera()
    
    # Set up clock for FPS control
    clock = pygame.time.Clock()
    
    # Main loop variables
    running = True
    time = 0.0
    auto_rotate = True
    
    print("=== Beautiful 3D Scene ===")
    print("Controls:")
    print("  Arrow Keys: Rotate camera")
    print("  +/- or W/S: Zoom in/out")
    print("  Space: Toggle auto-rotation")
    print("  ESC: Exit")
    print("\nStarting scene...\n")
    
    # Main game loop
    while running:
        # Calculate delta time
        delta_time = clock.tick(FPS) / 1000.0
        time += delta_time
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    auto_rotate = not auto_rotate
                    print(f"Auto-rotation: {'ON' if auto_rotate else 'OFF'}")
        
        # Get keyboard state for continuous input
        keys = pygame.key.get_pressed()
        
        # Update camera
        camera.update(keys, auto_rotate, delta_time)
        
        # Update scene
        scene.update(time, delta_time)
        
        # Render scene
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        camera.apply()
        scene.render(time)
        
        # Swap buffers
        pygame.display.flip()
        
        # Optional: Print FPS every 2 seconds
        if int(time * 10) % 20 == 0:
            fps = clock.get_fps()
            if fps > 0:
                print(f"FPS: {fps:.1f}", end='\r')
    
    # Clean up
    print("\n\nShutting down...")
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()