import numpy
import tensorflow
import keras
from keras import layers

class DQNAgent:
    def __init__(self, state_size, action_size=4): 
        #four actions: down, left, right, rotate
        self.state_size = state_size
        self.action_size = action_size
        self.model = self.build_model()

    def build_model(self):
        model = keras.Sequential([
            layers.Dense(64, activation="relu"),
            layers.Dense(64, activation="relu"),
            layers.Dense(self.action_size, activation="linear")
            ])
        model.compile(optimizer="adam", loss="mse")
        return model

    def choose_action(self, state, exploration_prob):
        if numpy.random.rand() < exploration_prob:
            action = int(numpy.random.choice(self.action_size))
            return action
        else:
            q_values = self.model.predict(numpy.reshape(state, (1, self.state_size)))
            #print("q_values: ")
            return numpy.argmax(q_values)
    def get_max_column_height(occupied_coords):
        column_counts = collections.defaultdict(lambda: 0)
        for row, col in occupied_coords:
            column_counts[col] += 1
        return max(column_counts.keys()) if column_counts else 0


    def update_q_values(self, state, action, reward, next_state, done):
        target = reward
        if not done:
            target += 0.9 * numpy.max(self.model.predict(numpy.reshape(next_state, (1, self.state_size))))

        target_f = self.model.predict(numpy.reshape(state, (1, self.action_size)))
        target_f[0][action] = target
        self.model.fit(numpy.reshape(state, (1, self.state_size)), target_f, epochs=1, ) #can set verbose to 0 later

def train_dqn_solver(env, agent, num_episodes):
    for episode in range(num_episodes):
        state = env.reset() # in other words, reset the tetris game; start from the beginning
        total_reward = 0
        exploration_prob = max(0.1, 0.9 - 0.01*episode)

        while True:
            action = agent.choose_action(state, exploration_prob)
            next_state, reward, done = env.step(action) # in other words, execute the action in the game
                                                        # and get the next set of data
            state = next_state
            total_reward += reward

        print(f"Episode {episode + 1}/{num_episodes}, Total Reward: {total_reward}")
        


    
