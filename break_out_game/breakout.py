"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This module build a breakout game with element from breakoutgraphics.py.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120     # 120 frames per second
NUM_LIVES = 3			    # Number of attempts


def main():
    graphics = BreakoutGraphics()

    dx = graphics.get_dx()
    dy = graphics.get_dy()
    num_lives = NUM_LIVES                   # record the number of lives remained
    num_bricks = graphics.get_num_bricks()  # record the number of bricks remained

    while True:
        # Pause
        pause(FRAME_RATE)
        # Check
        switch = graphics.get_switch()      # check if the game is began
        # Wall bounce
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            dx = -dx
        if graphics.ball.y <= 0:
            dy = -dy
        # The ball falls over the bottom of window
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            num_lives -= 1
            graphics.reset_ball()

        # Hit paddle/bricks
        maybe_object = graphics.where_is_the_ball()
        if maybe_object == graphics.paddle:
            dy = -dy
            dx = graphics.get_new_dx()

        elif maybe_object is not None and maybe_object is not graphics.paddle:  # the object is a brick
            graphics.window.remove(maybe_object)
            dy = -dy
            dx = graphics.get_new_dx()
            num_bricks -= 1

        # Update
        if switch and num_lives > 0 and num_bricks > 0:
            graphics.ball.move(dx, dy)
            while (graphics.paddle.y <= graphics.ball.y + graphics.ball.height
                   <= graphics.paddle.y + graphics.paddle.height) and dy < 0:     # Avoid the ball to stocked in paddle
                graphics.ball.move(dx, dy)
        elif num_lives == 0 or num_bricks == 0:
            break


if __name__ == '__main__':
    main()
