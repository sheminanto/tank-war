import pygame

FPS = 20
BLACK = (0,0,0)
fps_obj = pygame.time.Clock()

class Gameplay:
    def __init__(self,players,full_screen=False, mode = 'Single Player'):
        pygame.init()
        infoObject = pygame.display.Info()
        pygame.display.set_caption("Tank War")
        pygame.key.set_repeat(5)
        self.mode = mode
        self.players = players

        if full_screen == True:
            self.screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
        else:
            self.screen = pygame.display.set_mode((640, 480))

        # if mode == 'Multi Player':
        #     self.network = Network()
        # screen.fill(black)

    def update_screen(self):
        self.screen.fill(BLACK)
        for player in self.players:
            self.screen.blit(player.tank_image, player.tank_rect)
        pygame.display.flip()

    def show_menu(self):
        pass

    def add_player(self,player):
        self.players.append(player)

    def start(self):
        while True:
            for player in self.players:
                player.get_action()
                player.move()
            self.update_screen()
            fps_obj.tick(FPS)
