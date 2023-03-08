import pygame 
from dino_runner.components.dino import Dino
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DINO_START
from dino_runner.components.obstacles.obstaclemanager import ObstacleManager
from dino_runner.components import text_utils

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dino()
        self.obstacle_manager = ObstacleManager()
        self.points = 0
        self.running = True
        self.death_count = 0
        self.menu = True


    def run(self):
        if self.menu:
            self.show_menu()
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()

    def show_menu(self):
        self.running = True

        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        self.print_menu_elements()
        pygame.display.update()
        self.handle_key_events_on_menu()

    def print_menu_elements(self):
        if self.death_count == 0:
            text, text_rect = text_utils.get_centered_message('Press any key to start')
            self.screen.blit(text, text_rect)
        #TAREA POSIBLE: puntaje con el que terminaste y contador de muertes poner en texto
        else:
            self.stats_game()


        self.screen.blit(DINO_START, (50, 300))


    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.points = 0
                self.playing = True
                self.run()
                pygame.time.delay(1000)
                self.reset()
            
    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        text, text_rect = text_utils.get_score_element(self.points)
        self.screen.blit(text, text_rect)

    def reset(self):
        self.obstacle_manager.reset_obstacles()
        self.game_speed = 20
        self.points = self.points
        self.death_count += 1
        

    def stats_game(self):
        text, text_rect = text_utils.get_centered_message('Press any key to start')
        self.screen.blit(text, text_rect)
        text, text_rect = text_utils.get_score_element(self.points)
        self.screen.blit(text, text_rect)
        text, text_rect = text_utils.get_death_count(self.death_count)
        self.screen.blit(text, text_rect) 



 #Tarea resetear la velocidad y el puntaje
