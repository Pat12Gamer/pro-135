import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('star_with_gravity.csv')

radius = df['Radius'].to_list()
mass = df['Mass'].to_list()
distance = df['Distance'].to_list()
name = df['Star_name'].to_list()
gravity = df['Gravity'].to_list()

plt.figure(figsize= (10, 5))
plt.title("Star name vs Mass")
plt.bar(name, mass)
plt.figure(figsize= (10, 5))
plt.title("Star name vs Radius")
plt.bar(name, mass)
plt.figure(figsize= (10, 5))
plt.title("Star name vs Distance")
plt.bar(name, mass)
plt.figure(figsize= (10, 5))
plt.title("Star name vs Gravity")
plt.bar(name, mass)