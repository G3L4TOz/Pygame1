import pygame
from pygame.math import Vector2
import random

class Agent():

    def __init__(self) -> None:
        self.r = 50
        self.mass = 1
        self.force = Vector2(random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5))
        
        self.position = Vector2(random.randint(50, 1230), random.randint(50, 670))
        self.velocity = Vector2(0.0, 0.0)
        self.acc = Vector2(0, 0)

    def update(self):
        self.acc = self.force / self.mass
        self.velocity = self.velocity * 0.6
        self.velocity = self.velocity + self.acc
        self.position = self.position + self.velocity
        
        if self.position.x - self.r < 0:
            self.velocity.x = 0.5
            self.force.x = 0.5
        if self.position.x + self.r > 1280:
            self.velocity.x = -0.5
            self.force.x = -0.5
        if self.position.y - self.r < 0:
            self.velocity.y = 0.5
            self.force.y = 0.5
        if self.position.y + self.r > 720:
            self.velocity.y = -0.5
            self.force.y = -0.5

    def draw(self, screen):
        pygame.draw.circle(screen, (100, 100, 255), (int(self.position.x), int(self.position.y)), self.r)

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    agents = [Agent() for i in range(100)]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("green")

        # Update and draw each agent
        for agent in agents:
            agent.update()
            agent.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()