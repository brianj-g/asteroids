import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        split_speed_multiplier = 1.2
        split_angle = random.uniform(20, 50)
        rotate_a = self.velocity.rotate(split_angle)
        rotate_b = self.velocity.rotate(-1 * split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        sub_a = Asteroid(self.position.x, self.position.y, new_radius)
        sub_b = Asteroid(self.position.x, self.position.y, new_radius)
        sub_a.velocity = rotate_a * split_speed_multiplier
        sub_b.velocity = rotate_b * split_speed_multiplier

   
