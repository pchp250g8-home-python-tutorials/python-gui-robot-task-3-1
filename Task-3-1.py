from robot import *

move_down()
move_right()

while(is_free_left() and is_free_right() and is_free_up() and is_free_down()):
    paint()
    move_right()
move_left()
while(is_free_left() and is_free_right() and is_free_up() and is_free_down()):
    paint()
    move_down()
move_right()