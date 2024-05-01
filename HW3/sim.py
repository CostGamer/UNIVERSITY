import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class MoveSimul:
    g = 9.8

    def __init__(self, vx0, vy0, t_sim, interval=1.0):
        """
        :param vx0: Initial velocity on the x-axis
        :param vy0: Initial velocity on the y-axis
        :param t_sim: Duration of the simulation
        :param interval: Simulation interval (default: 1.0)
        """
        self.t = np.arange(0, t_sim + interval, interval)
        self.vx = vx0 - self.g * self.t
        self.vy = vy0
        self.x = vx0 * self.t - 0.5 * self.g * self.t ** 2
        self.y = vy0 * self.t
        self.result = pd.DataFrame({'t': self.t,
                                    'x': self.x,
                                    'y': self.y,
                                    'vx': self.vx,
                                    'vy': self.vy})

    def print_result(self):
        print(self.result)

    def save_result(self, filepath='./result'):
        self.result.to_csv('{}.csv'.format(filepath), index=False)

    def plot_result(self, figure_path=None):
        plt.style.use('default')
        fig, ax1 = plt.subplots(1, 1, figsize=(12, 7), dpi=100)
        ax1.plot(self.result["y"], self.result["x"],
                 color='tab:red', label='Simulation_data')
        ax1.set_title('Trajectory', fontsize=20, family='Arial')
        ax1.tick_params(labelsize=20)
        ax1.set_xlabel('y', fontsize=20, fontname='Arial')
        ax1.set_ylabel('x', fontsize=20, fontname='Arial')
        plt.show()

        if figure_path:
            fig.savefig('{}.png'.format(figure_path), dpi=300, format='png')


if __name__ == '__main__':
    # Initializing the parameters
    move1 = MoveSimul(vx0=100, vy0=15, t_sim=15)

    move1.print_result()  # Output of results
    move1.save_result(filepath='./result')  # Saving the results
    move1.plot_result(figure_path='./result')  # Plotting
