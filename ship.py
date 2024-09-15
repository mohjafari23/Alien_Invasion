import pygame
class ship:
    """A class to manage the ship."""
    def __init__(self,ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        # Load the ship image and get its rect.
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # Right movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        # Update the ship's position based on the movement flag.
        if self.moving_right:
            if self.rect.right >= self.screen_rect.right:
                self.moving_right = False
            else:
                 self.x += self.settings.ship_speed
        if self.moving_left:
            if self.rect.left <=0:
                self.moving_left = False
            else:
                self.x -=self.settings.ship_speed
        if self.moving_up:
            if self.rect.top <=0:
                self.moving_up = False
            else:
                self.y -=self.settings.ship_speed
        if self.moving_down:
            if self.rect.bottom >= self.screen_rect.height:
                self.moving_down = False    
            else:
                self.y +=self.settings.ship_speed  
        self.rect.x = self.x
        self.rect.y = self.y
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
