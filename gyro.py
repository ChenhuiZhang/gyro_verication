import pandas as pd
import matplotlib.pyplot as plt

label = ['accel_x', 'accel_y', 'accel_z', 'temperature', 'anglvel_x', 'anglvel_y', 'anglvel_z', 'timestamp']
df = pd.read_csv('example', header=None, sep=' ', names=label)
print(df.describe())
