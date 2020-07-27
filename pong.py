## Robert Giglio III
## 11/10/2016
## Robert Giglio III
## Pong game

from livewires import games, color
import random

#create game window
games.init(screen_width = 640, screen_height = 480, fps = 50)

class Paddle(games.Sprite):
    """ A paddle to hit a pong ball. """
    image = games.load_image("paddle.png")

    def __init__(self):
        """Initialize a paddle object. """
        super(Paddle,self).__init__(image = Paddle.image,
                                    x = games.screen.width / 10,
                                    y = games.screen.height / 2)
        self.score = games.Text(value = 0, size = 30, color = color.black,
                                top = 15, right = games.screen.width - 10)
        games.screen.add(self.score)

    def update(self):
        """ Move paddle with arrow keys or 'w', 's'; Traps paddle on screen """
        if self.top < 0:
            self.top = 0;
        if self.bottom > games.screen.height:
            self.bottom = games.screen.height
            
        if games.keyboard.is_pressed(games.K_w) or games.keyboard.is_pressed(games.K_UP):
            self.y -= 3
        if games.keyboard.is_pressed(games.K_s) or games.keyboard.is_pressed(games.K_DOWN):
            self.y += 3

        self.check_hit()

    def check_hit(self):
        """Check if ball hit. """
        for ball in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10
            ball.handle_hit()
                                    
class Ball(games.Sprite):
    """ A pong ball. """
    image = games.load_image("ball.png")
    speed = random.randrange(1,2)

    def __init__(self, dir_change = 100):
        """Initializes a pong ball object. """
        self.dir_change = dir_change
        if random.randrange(self.dir_change) <= 30:
            self.speed = -self.speed
        super(Ball, self).__init__(image = Ball.image,
                                   x = games.screen.width /2,
                                   y = games.screen.height /2,
                                   dy = (Ball.speed * .3) + Ball.speed, dx = (Ball.speed * .3) + Ball.speed)

    def update(self):
        """ Ball bounces off of 3 walls and ends game when enter goal. """
        if self.right > games.screen.width:
            self.dx = -self.dx
        if self.top < 0 or self.bottom > games.screen.height:
            self.dy = -self.dy

        if self.left < 0:
            self.end_game()
            self.destroy()

    def handle_hit(self):
        """ Bounces ball off of paddle. """
        self.dx = -self.dx
        self.dy = -self.dy
        
    def end_game(self):
        """ Ends game. """
        end_message = games.Message(value = "Game over", size = 90,
                                    color = color.red,
                                    x = games.screen.width / 2,
                                    y = games.screen.height / 2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)
        

def main():
    """Play the game. """
    
    #set background
    game_board = games.load_image("background.png", transparent = False)
    games.screen.background = game_board

    #add sprites
    the_paddle = Paddle()
    games.screen.add(the_paddle)
    
    the_ball = Ball()
    games.screen.add(the_ball)

 #   games.mouse.is_visible = False

 #  games.screen.event_grab = True
    games.screen.mainloop()


#start game
main()
