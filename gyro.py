import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re

def plot_gyro(path: str, filename: str):
    label = ['accel_x', 'accel_y', 'accel_z', 'temperature', 'anglvel_x', 'anglvel_y', 'anglvel_z', 'timestamp']
    df_x = pd.read_csv(path + '/' + filename + '.x', header=None, index_col=False, sep=' ', names=label)
    df_y = pd.read_csv(path + '/' + filename + '.y', header=None, index_col=False, sep=' ', names=label)
    df_z = pd.read_csv(path + '/' + filename + '.z', header=None, index_col=False, sep=' ', names=label)

    df = pd.concat([df_x['accel_x'], df_y['accel_y'], df_z['accel_z']], axis=1)
    df.reindex(df_x.index)

    #print(df.head())
    #print(df.describe())

    fig, axs = plt.subplots(2, 3, figsize=(12, 9))
    sns.distplot(df['accel_x'], bins=10, rug=True, label='accel_x', ax=axs[0, 0])
    sns.distplot(df['accel_y'], bins=10, rug=True, label='accel_y', ax=axs[0, 1])
    sns.distplot(df['accel_z'], bins=10, rug=True, label='accel_z', ax=axs[0, 2])
    sns.violinplot(y=df['accel_x'], ax=axs[1, 0])
    sns.violinplot(y=df['accel_y'], ax=axs[1, 1])
    sns.violinplot(y=df['accel_z'], ax=axs[1, 2])

    #plt.legend()
    #plt.savefig('5000-300dpi.pdf', dpi=300)
    plt.savefig(path + '_' + filename + '.png', dpi=300)
    fig.canvas.set_window_title(path)
    plt.show()

if __name__ == '__main__':
    for unit in [x for x in os.listdir() if re.match(r'^\w{4}$', x)]:
        print(unit)
        plot_gyro(unit, '5000')
