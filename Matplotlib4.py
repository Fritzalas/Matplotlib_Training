#!/usr/bin/env python
# coding: utf-8

# In[10]:


import matplotlib.pyplot as plt
import numpy as np

# Sample data for illustration
players = ['Lionel Messi', 'Cristiano Ronaldo', 'Neymar Jr.', 'Kylian Mbappe', 'Robert Lewandowski']
goals = [36, 34, 21, 33, 41]
assists = [12, 7, 10, 7, 5]
dribbles = [174, 89, 142, 90, 41]

# Set up the figure with three subplots
fig, axes = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

# Plot goals scored
axes[0].bar(players, goals, color='blue', alpha=0.7)
axes[0].set_ylabel('Goals Scored')
axes[0].set_title('Player Performance Metrics')
axes[0].grid(True, linestyle='--', alpha=0.7)  # Add grid
# Annotate max value with a pointer
max_goal_player = players[np.argmax(goals)]
max_goal_value = max(goals)
axes[0].annotate(f'Max: {max_goal_player}\n({max_goal_value} goals)',
                 xy=(players[np.argmax(goals)], max(goals)),
                 xytext=(15, 15),
                 textcoords='offset points',
                 arrowprops=dict(arrowstyle='->', color='red'))


# Plot assists
axes[1].bar(players, assists, color='green', alpha=0.7)
axes[1].set_ylabel('Assists')
axes[1].grid(True, linestyle='--', alpha=0.7)  # Add grid
# Annotate max value with a larger pointer
max_assist_player = players[np.argmax(assists)]
max_assist_value = max(assists)
axes[1].annotate(f'Max: {max_assist_player}\n({max_assist_value} assists)',
                 xy=(players[np.argmax(assists)], max(assists)),
                 xytext=(15, 15),
                 textcoords='offset points',
                 arrowprops=dict(arrowstyle='->', color='red', lw=2, shrinkA=0, shrinkB=0))


# Plot dribbles
axes[2].bar(players, dribbles, color='orange', alpha=0.7)
axes[2].set_ylabel('Dribbles')
axes[2].set_xlabel('Players')
axes[2].grid(True, linestyle='--', alpha=0.7)  # Add grid
# Annotate max value with a larger pointer
max_dribble_player = players[np.argmax(dribbles)]
max_dribble_value = max(dribbles)
axes[2].annotate(f'Max: {max_dribble_player}\n({max_dribble_value} dribbles)',
                 xy=(players[np.argmax(dribbles)], max(dribbles)),
                 xytext=(15, 15),
                 textcoords='offset points',
                 arrowprops=dict(arrowstyle='->', color='red', lw=2, shrinkA=0, shrinkB=0))

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()


# In[ ]:




