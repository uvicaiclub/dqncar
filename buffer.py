import numpy as np
import random as rnd
from collections import deque

class ReplayBuffer():
    '''
    This is the replay buffer method for the DQN model. 

    No code is in it other than the functions because I'm curious to see various implementations
    one thing to note, memories almost always come in the SARS' format. That is 
    Experience = (state, action, reward, new_state)


    '''
    def __init__(self):
        return

    def store_memory(self, experience: tuple):
        return

    def collect_memory(self):
        return 
        
    def erase_memory(self):
        return
    
    def __len__(self):
        return


if __name__ == "__main__":
    '''
    For those unfamiliar with this format, this is so that if you want to run this file
    instead of the main.py file to test this file specifically, everything in this block will be run.
    So, if you had a print statement outside of this block and called functions or classes,
    they will be ignored. 
    '''
    buffer = ReplayBuffer()
    print('cool new buffer!')