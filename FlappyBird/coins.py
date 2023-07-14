import pygame, random, os

script_dir = os.path.dirname(os.path.abspath(__file__))
coin_dir = os.path.join(script_dir, "assets", "coin.png")

class Coins:
    def __init__(self, coin_size, pipe_list, coins):
        self.coin_surface = pygame.image.load(coin_dir).convert_alpha()
        self.coin_surface = pygame.transform.scale(self.coin_surface, (coin_size, coin_size))
        self.coin_rect = self.coin_surface.get_rect()
        self.coin_rect.midtop = self.get_valid_position(pipe_list, coins)
        self.is_collected = False

    def get_valid_position(self, pipe_list, coins):
        valid_position = False
        while not valid_position:
            random_x = random.randint(700, 900)
            random_y = random.randint(200, 600)
            self.coin_rect.center = (random_x, random_y)

            for pipe in pipe_list:
                if self.coin_rect.colliderect(pipe):
                    break
            else:
                for coin in coins:
                    if coin != self and self.coin_rect.colliderect(coin.coin_rect):
                        break
                else:
                    valid_position = True

        return self.coin_rect.midtop

    def move(self):
        self.coin_rect.centerx -= 5

    def draw(self, screen):
        screen.blit(self.coin_surface, self.coin_rect)

    def check_collision(self, bird_rect):
        if self.coin_rect.colliderect(bird_rect) and not self.is_collected:
            self.is_collected = True
            return True
        return False
