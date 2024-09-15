import sys
import pygame
from settings import settings
from ship import ship
from bullet import Bullet
class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        pygame.init()
        self.settings = settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption(self.settings.set_caption)
        self.ship = ship(self)
        self.bullets = pygame.sprite.Group()
    def run_game(self):
        """"Start the main loops of the game"""
        while True:
            self._check_event()
            self.ship.update()
            self._update_bullets()
            self._update_screen()   
    def _update_bullets(self):
     """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
     self.bullets.update()
     # Get rid of bullets that have disappeared.
     for bullet in self.bullets.copy():
                if bullet.rect.bottom <=0:
                    self.bullets.remove(bullet)
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
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
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
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
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) <= self.settings.bullets_allowed: 
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)               
if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
