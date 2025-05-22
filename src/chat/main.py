import pygame
import math

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Isometric 3D Robotic Arm with Shadows and Side Colors")
clock = pygame.time.Clock()

# Arm parameters: (base, shoulder, elbow)
arm_lengths = (0, 150, 120)  # Base doesn't have length, just the arm lengths

# Robot angles (base, shoulder, elbow)
angles = [0, 45, 30]  # Base, shoulder, elbow (degrees)
L1, L2 = arm_lengths[1], arm_lengths[2]  # Shoulder to elbow, elbow to wrist

# Isometric Projection Function
def isometric_projection(x, y, z):
    """Convert a 3D point into an isometric 2D projection."""
    iso_x = (x - y) * math.sqrt(2)
    iso_y = (x + 2 * y) * math.sqrt(2) / math.sqrt(6) - z
    return (int(iso_x + 400), int(-iso_y + 300))  # Offset to center on the screen

# Function to calculate the joint positions (forward kinematics)
def forward_kinematics():
    """Calculate forward kinematics to get joint positions."""
    # Calculate 2D positions for each joint (based on arm lengths and angles)
    shoulder_x = L1 * math.cos(math.radians(angles[1]))
    shoulder_y = L1 * math.sin(math.radians(angles[1]))
    
    elbow_x = shoulder_x + L2 * math.cos(math.radians(angles[1] + angles[2]))
    elbow_y = shoulder_y + L2 * math.sin(math.radians(angles[1] + angles[2]))

    wrist_x, wrist_y = elbow_x, elbow_y

    return (0, 0, 0), (shoulder_x, shoulder_y, 0), (elbow_x, elbow_y, 0), (wrist_x, wrist_y, 0)

# Function to draw shadow for a joint
def draw_shadow(position, size):
    """Draw an elliptical shadow at the given position."""
    shadow_color = (50, 50, 50)  # Dark gray shadow color
    shadow_position = (position[0], position[1] + 10)  # Offset downward for the shadow
    shadow_size = (size[0] * 1.2, size[1] * 0.5)  # Slightly larger and flatter ellipse

    pygame.draw.ellipse(screen, shadow_color, pygame.Rect(shadow_position[0] - shadow_size[0] // 2,
                                                          shadow_position[1] - shadow_size[1] // 2,
                                                          shadow_size[0], shadow_size[1]))

# Function to determine whether the segment is facing the camera
def is_facing_away(angle):
    """Determine if the segment is facing away from the camera."""
    # Simple logic: If the angle is between -90 and 90 degrees, the segment is facing the camera.
    # Otherwise, it's facing away.
    if -90 <= angle <= 90:
        return False  # Facing the camera
    else:
        return True  # Facing away

# Function to draw the floor
def draw_floor():
    """Draw a simple floor at the bottom of the screen."""
    floor_color = (150, 150, 150)  # Light gray floor color
    pygame.draw.rect(screen, floor_color, pygame.Rect(0, 500, 800, 100))  # Floor covering bottom 100px

# Main loop
running = True
while running:
    screen.fill((255, 255, 255))  # White background

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Control the angles using the arrow keys or any other input method
    keys = pygame.key.get_pressed()

    # Increment or decrement base, shoulder, elbow angles with arrow keys
    if keys[pygame.K_LEFT]:     # Rotate base counterclockwise
        angles[0] -= 1
    if keys[pygame.K_RIGHT]:    # Rotate base clockwise
        angles[0] += 1
    if keys[pygame.K_UP]:       # Raise shoulder angle
        angles[1] += 1
    if keys[pygame.K_DOWN]:     # Lower shoulder angle
        angles[1] -= 1

    # For elbow, you can also use the arrow keys or add custom controls
    if keys[pygame.K_w]:        # Elbow move up
        angles[2] += 1
    if keys[pygame.K_s]:        # Elbow move down
        angles[2] -= 1

    # Update arm joint angles and calculate forward kinematics
    base_pos, shoulder_pos, elbow_pos, wrist_pos = forward_kinematics()

    # Project all joint positions to 2D using isometric projection
    base_2d = isometric_projection(base_pos[0], base_pos[1], base_pos[2])
    shoulder_2d = isometric_projection(shoulder_pos[0], shoulder_pos[1], shoulder_pos[2])
    elbow_2d = isometric_projection(elbow_pos[0], elbow_pos[1], elbow_pos[2])
    wrist_2d = isometric_projection(wrist_pos[0], wrist_pos[1], wrist_pos[2])

    # Draw the shadow beneath each joint
    draw_shadow(base_2d, (20, 10))  # Shadow size under the base
    draw_shadow(shoulder_2d, (20, 10))  # Shadow size under the shoulder
    draw_shadow(elbow_2d, (20, 10))  # Shadow size under the elbow
    draw_shadow(wrist_2d, (20, 10))  # Shadow size under the wrist

    # Draw the arm using lines, with shading based on which side is facing away
    pygame.draw.line(screen, (255, 0, 0) if not is_facing_away(angles[0]) else (0, 0, 255), base_2d, shoulder_2d, 5)  # Base to shoulder
    pygame.draw.line(screen, (255, 0, 0) if not is_facing_away(angles[1]) else (0, 0, 255), shoulder_2d, elbow_2d, 5)  # Shoulder to elbow
    pygame.draw.line(screen, (255, 0, 0) if not is_facing_away(angles[2]) else (0, 0, 255), elbow_2d, wrist_2d, 5)  # Elbow to wrist

    # Draw the joints as circles
    pygame.draw.circle(screen, (255, 0, 0), base_2d, 8)
    pygame.draw.circle(screen, (0, 255, 0), shoulder_2d, 8)
    pygame.draw.circle(screen, (0, 0, 255), elbow_2d, 8)
    pygame.draw.circle(screen, (255, 255, 0), wrist_2d, 8)

    # Draw the floor at the bottom of the screen
    draw_floor()

    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
