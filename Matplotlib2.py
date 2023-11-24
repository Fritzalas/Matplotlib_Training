#!/usr/bin/env python
# coding: utf-8

# In[13]:


import matplotlib.pyplot as plt

#Data Insert:

Players = ['Lionel Messi', 'Cristiano Ronaldo', 'Robert Lewandowski', 'Kylian Mbappe', 'Erling Haaland']
Teams = ['PSG', 'Manchester United', 'Bayern Munich', 'PSG', 'Borussia Dortmund']
GoalsScored = [12, 15, 16, 13, 14]
Assists = [5, 6, 4, 7, 5]
GamesPlayed = [10, 10, 10, 10, 10]

plt.figure(figsize=(10, 6))
plt.plot(Players,GoalsScored,marker='o',label='Goals')
# Add a title to the plot
plt.title('Goals per Player')
# Show the legend
plt.legend()
# Add labels to the axes
plt.xlabel('Player')
plt.ylabel('Total_Goals')
# Add a grid
plt.grid(True, linestyle='--', alpha=0.7)

plt.show()


# In[19]:


markers = ['o', 'v', '^', '<', '>']
colors=['blue','red','green','purple','black']
plt.figure(figsize=(10,6))
for i in range(len(Players)):
    plt.scatter(GamesPlayed[i], GoalsScored[i], color=colors[i], marker=markers[i])
plt.title('Goals Scored vs Games Played')
plt.xlabel('Games Played')
plt.ylabel('Goals Scored')
# Add a grid
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()


# In[25]:


plt.figure(figsize=(15, 10))
plt.bar(Players, Assists, color='skyblue')
plt.title('Assists by Players in Champions League')
plt.xlabel('Players')
plt.ylabel('Assists')
plt.show()

