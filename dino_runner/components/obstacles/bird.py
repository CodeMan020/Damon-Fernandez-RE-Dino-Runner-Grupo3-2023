import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    def __init__(self,image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.randint(230, 330)
        self.flutters_index = 0


    def draw(self,screen):
        if self.flutters_index <= 5:
            self.image = BIRD [0]
        else:
            self.image = BIRD [1]

        if self.flutters_index >= 10:
            self.flutters_index = 0

        screen.blit(self.image, self.rect)
        self.flutters_index += 1