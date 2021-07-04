"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

This module prepare the graphics elements for breakout game
including graphics, mouse listeners, and methods for ball movements.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    """
    Preparing all the graphics for breakout game.
    """
    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(window_width-ball_radius*2)/2, y=(window_height-ball_radius*2)/2)

        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        onmousemoved(self.paddle_tracker)
        self.__switch = False
        onmouseclicked(self.click)

        # Draw bricks
        for i in range(brick_cols):
            for j in range(brick_rows):
                brick = GRect(brick_width, brick_height)
                brick.filled = True
                if 0 <= j < 2:
                    brick.fill_color = 'red'
                    brick.color = 'red'
                elif 2 <= j < 4:
                    brick.fill_color = 'orange'
                    brick.color = 'orange'
                elif 4 <= j < 6:
                    brick.fill_color = 'yellow'
                    brick.color = 'yellow'
                elif 6 <= j < 8:
                    brick.fill_color = 'green'
                    brick.color = 'green'
                elif 8 <= j < 10:
                    brick.fill_color = 'blue'
                    brick.color = 'blue'
                else:
                    brick.fill_color = 'violet'
                    brick.color = 'violet'
                self.window.add(brick, x=(brick_width+brick_spacing)*i,
                                y=brick_offset+(brick_height+brick_spacing)*j)
        # Record number of bricks
        self.__num_bricks = brick_rows * brick_cols

    # Mouse listeners
    def paddle_tracker(self, event):
        """
        Moving the paddle following the x-axis movement of mouse.
        :param event: collect info from the mouse movement
        """
        if event.x <= self.paddle.width/2:
            self.paddle.x = 0
        elif event.x + self.paddle.width/2 >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = event.x - self.paddle.width/2

    def click(self, event):
        """
        Turn on the switch when user clicked mouse at the first time.
        :param event: store the position(x, y) of mouse-click
        """
        if not self.__switch:
            self.__switch = True

    # Getters
    def get_switch(self):
        return self.__switch

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def get_new_dx(self):
        """
        Create new x-speed so that every bounce of the ball will have different direction.
        :return: new dx range between 1 and MAX_X_SPEED
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        return self.__dx

    def get_num_bricks(self):
        """
        Users might need this info to decide when to stop the game.
        :return: the number of bricks
        """
        return self.__num_bricks

    # Reset the ball
    def reset_ball(self):
        """
        Reset position and velocity of ball when start a new round of game
        """
        self.set_ball_position()
        self.set_ball_velocity()
        self.__switch = False    # the ball should be still before first mouse click

    def set_ball_position(self):
        """
        Set the ball to the original position, middle of the window
        """
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)

    def set_ball_velocity(self):
        """
        Determine a new x-speed
        """
        self.__dy = INITIAL_Y_SPEED
        self.__dx = self.get_new_dx()

    def where_is_the_ball(self):
        """
        Check if the ball hit bricks or the paddle
        :return: If hit ball/bricks, return the hit object; if hit nothing, return None
        """
        corner1 = self.window.get_object_at(self.ball.x, self.ball.y)
        corner2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        corner3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        corner4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        if corner1 is not None:
            return corner1
        elif corner2 is not None:
            return corner2
        elif corner3 is not None:
            return corner3
        elif corner4 is not None:
            return corner4
        else:
            return None


