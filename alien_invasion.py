import sys
import pygame
from settings import settings
from ship import ship
class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        pygame.init()
        self.settings = settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption(self.settings.set_caption)
        self.ship = ship(self)
        
    def run_game(self):
        """"Start the main loops of the game"""
        while True:
            self._check_event()
            self.ship.update()
            self._update_screen()
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
    def _check_event(self):
        """respond to the mouse and keyboard"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)  
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)     
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
         # move the ship to the right continues
             self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
                   # move the ship to the left continues
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
                   # move the ship to the up continues
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
                   # move the ship to the down continues
            self.ship.moving_down = True
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
                   # STOP move the ship to the right continues
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
                   # STOP move the ship to the left continues
            self.ship.moving_left = False       
        elif event.key == pygame.K_UP:
                   # STOP move the ship to the up continues
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
                   # move the ship to the down continues
            self.ship.moving_down = False


               
if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()