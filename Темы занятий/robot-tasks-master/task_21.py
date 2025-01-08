#!/usr/bin/python3

from pyrob.api import *



@task(delay=0.05)
def task_4_11():
    pass
    # a = 1
    # move_down()1
    # if not wall_is_beneath():
    #     for i in range(a):
    #         move_right()
    #         fill_cell()
    #     move_left(a)
    #     a+=1
    
        
        


if __name__ == '__main__':
    run_tasks()
