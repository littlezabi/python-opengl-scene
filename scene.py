"""
3D Scene setup and rendering coordination
"""
from OpenGL.GL import *
from OpenGL.GLU import *
from objects import LiquidSphere, Torus, WaterPlane
from effects import ParticleSystem, setup_lighting

class Scene:
    """Main 3D scene manager"""
    
    def __init__(self):
        """Initialize the 3D scene"""
        # Set up OpenGL state
        self.init_opengl()
        
        # Create scene objects
        self.liquid_sphere = LiquidSphere(radius=1.5, resolution=40)
        self.torus = Torus(major_radius=1.5, minor_radius=0.5, resolution=30)
        self.water_plane = WaterPlane(size=20.0, resolution=50)
        self.particles = ParticleSystem(count=800)
        
        print("Scene initialized successfully!")
    
    def init_opengl(self):
        """Initialize OpenGL settings"""
        # Set background color (dark blue/space-like)
        glClearColor(0.05, 0.05, 0.1, 1.0)
        
        # Enable depth testing
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
        
        # Enable lighting
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        
        # Enable blending for transparency
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        
        # Smooth shading
        glShadeModel(GL_SMOOTH)
        
        # Enable point smoothing for particles
        glEnable(GL_POINT_SMOOTH)
        glHint(GL_POINT_SMOOTH_HINT, GL_NICEST)
        
        # Set up perspective projection
        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, 1280/720, 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)
    
    def update(self, time, delta_time):
        """Update scene objects"""
        self.particles.update(time, delta_time)
    
    def render(self, time):
        """Render all scene objects"""
        # Set up lighting
        setup_lighting(time)
        
        # Render liquid sphere at center
        glPushMatrix()
        self.liquid_sphere.render(time)
        glPopMatrix()
        
        # Render torus (offset and rotating)
        glPushMatrix()
        glTranslatef(3.5, 0.5, 0.0)
        glRotatef(time * 20, 0.3, 1.0, 0.2)
        self.torus.render(time)
        glPopMatrix()
        
        # Render water plane below
        glPushMatrix()
        glTranslatef(0.0, -2.5, 0.0)
        self.water_plane.render(time)
        glPopMatrix()
        
        # Render particles
        self.particles.render(time)