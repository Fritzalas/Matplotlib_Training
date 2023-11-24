#!/usr/bin/env python
# coding: utf-8

# In[11]:


import matplotlib.pyplot as plt

#Data:
Players = ['Lionel Messi', 'Cristiano Ronaldo', 'Robert Lewandowski', 'Kylian Mbappe', 'Erling Haaland']
GoalsScored = [45, 52, 48, 42, 50]
Assists = [20, 15, 18, 23, 22]
MinutesPlayed = [2800, 2900, 2750, 2700, 2850]

# Set a wider x-axis
plt.figure(figsize=(10, 6))

# Create a histogram
plt.hist(GoalsScored,color='blue', edgecolor='black',bins=5,density=False)

# Add title and labels
plt.title('Histogram of Goals Scored')
plt.xlabel('Goals Scored')
plt.ylabel('Frequency')

# Show the plot
plt.show()


# In[13]:


# Create a box plot
plt.boxplot(Assists, vert=False)

# Add title and labels
plt.title('Box Plot of Assists')
plt.xlabel('Number of Assists')

# Show the plot
plt.show()


# In[15]:


import seaborn as sns
import pandas as pd

data = pd.DataFrame({'Goals Scored': GoalsScored, 'Assists': Assists, 'Minutes Played': MinutesPlayed})

# Calculate the correlation matrix
correlation_matrix = data.corr()

# Create a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)

# Add title
plt.title('Correlation Matrix Heatmap')

# Show the plot
plt.show()


# In[17]:


# Create a 3D scatterplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
ax.scatter(GoalsScored, Assists, MinutesPlayed, c='red', marker='o')

# Add labels
ax.set_xlabel('Goals Scored')
ax.set_ylabel('Assists')
ax.set_zlabel('Minutes Played')

# Add title
ax.set_title('3D Scatterplot of Goals Scored, Assists, and Minutes Played')

# Show the plot
plt.show()


# In[27]:


import numpy as np
import matplotlib.pyplot as plt

# Set a wider x-axis
plt.figure(figsize=(10, 6))
players = ['Lionel Messi', 'Cristiano Ronaldo', 'Robert Lewandowski', 'Kylian Mbappe', 'Erling Haaland']
player_indices = np.arange(len(players))  # the x locations for the players
goals = np.array([45, 52, 48, 42, 50])
assists = np.array([20, 15, 18, 23, 22])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i, player in enumerate(player_indices):
    ax.bar3d(i, goals[i], 0, 0.4, 0.8, assists[i], color='b')

ax.set_title('3D Bar Plot of Player Performance')
ax.set_xticks(player_indices)
ax.set_xticklabels(players, rotation=45, horizontalalignment='right')
ax.set_xlabel('Players')
ax.set_ylabel('Goals')
ax.set_zlabel('Assists')
plt.show()


# In[ ]:




