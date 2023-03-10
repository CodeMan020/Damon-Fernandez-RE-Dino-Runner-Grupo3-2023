import pygame
import random
from dino_runner.components.obstacles.smallcactus import SmallCactus
from dino_runner.components.obstacles.largecactus import LargeCactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, DINO_DEAD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.hammer:
                    self.reset_obstacles()
                if not (game.player.shield or game.player.hammer):
                    game.player.image = DINO_DEAD    
                    pygame.time.delay(1000) 
                    game.death_count += 1    
                    game.playing = False 
                    break  

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []