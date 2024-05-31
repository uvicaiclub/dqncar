# Misc imports
import numpy as np
import random as rnd

# These are your other files.
from buffer import ReplayBuffer
from model import Model

# Tensorflow if you're using tensorflow
import tensorflow as tf

# pytorch if you're using pytorch
import torch

class DQNAgent():
    def __init__(self, input_dims, output_dims):
            self.output_dims = output_dims
            self.input_dims = input_dims
            #self.observation_space = observation_space

            #self.model = 
            #self.target_model = 

            #self.replay_memory =             

            #self.optimizer =

            # this is only important if you're using pytorch. it speeds things up. alot. 
            #self.device = 

    # Method for predicting an action 
    def get_action(self, state) -> int:
        ''' 
        Get action function call.
        Ideally your state is processed by your target network. 

        Your state can be inputted into this function as an array/tuple, in which case
        needs to be turned into a tensor before being inputted into your network.

        or it can be inputted into this function as a tensor already. 
        mostly fashion. do what you please.
        '''
        action = 0
        return action
    
    def learn(self) -> float:
        ''' 
        This function will be the source of 90% of your problems at the
        start. this is where the magic happens. it's also where the tears happen.

        ask questions. please.

        I'll leave a lot more things up here to make it less painful.

        it returns a tuple in case you want to keep track of your losses (you do)
        '''
        loss = 0
        # We just pass through the learn function if the batch size has not been reached. 
        #if self.replay_memory.__len__() < BUFFER_BATCH_SIZE:
        #    return

        state = []
        action = []
        reward = []
        next_state = []
        #for _ in range(BATCH_SIZE):
        #    s, a, r, n = self.replay_memory.collect_memory()
            # append to lists above probably

        # Convert list of tensors to tensor.

        # One hot encoding our actions. 

        # Find our predictions
        
        # Get the training model assessed Q value of the current turn. 

        # get max value

        # Calculate our target

        # Calculate MSE Loss

        # backward pass

        # self.update_target_counter += 1

        #if self.update_target_counter % TARGET_UPDATE == 0:
            # update

        return loss 

    def save(self, save_to_path: str) -> None:
        # if pytorch
        #torch.save(self.target_model.state_dict(), save_to_path)
        pass

    def load(self, load_path: str) -> None:

        # if tensorflow
        #loaded_target = tf.keras.models.load_model(load_path)
        #loaded_model = tf.keras.models.load_model(load_path)

        # if pytorch
        #self.target_model.load_state_dict(torch.load(load_path))
        #self.model.load_state_dict(torch.load(load_path))

        pass




if __name__ == "__main__":
    '''
    For those unfamiliar with this format, this is so that if you want to run this file
    instead of the main.py file to test this file specifically, everything in this block will be run.
    So, if you had a print statement outside of this block and called functions or classes,
    they will be ignored. 
    '''
    input_dims = 4
    output_dims = 2
    buffer = DQNAgent(input_dims, output_dims)
    print('dqn agent')

