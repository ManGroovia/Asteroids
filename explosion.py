import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(self.containers)  # чтобы добавлялся в группы
        self.position = pygame.Vector2(x, y)
        self.radius = 1
        self.max_radius = 30
        self.growth_speed = 100  # пикселей в секунду

    def update(self, dt):
        self.radius += self.growth_speed * dt
        if self.radius >= self.max_radius:
            self.kill()

    def draw(self, screen):
        alpha = max(0, 255 * (1 - self.radius / self.max_radius))
        color = (255, 128, 0, int(alpha))  # оранжевый
        surface = pygame.Surface((self.radius*2, self.radius*2), pygame.SRCALPHA)
        pygame.draw.circle(surface, color, (self.radius, self.radius), self.radius)
        screen.blit(surface, self.position - pygame.Vector2(self.radius, self.radius))
