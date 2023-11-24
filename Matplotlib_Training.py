#!/usr/bin/env python
# coding: utf-8

# In[18]:


import matplotlib.pyplot as plt

# Data
players = ['Harry Kane', 'Mo Salah', 'Bruno Fernandes', 'Jamie Vardy', 'Son Heung-min']
goals_scored = [23, 25, 21, 22, 19]
assists = [8, 7, 11, 6, 10]
GamesPlayed = [34, 33, 34, 35, 33]
TeamPoints = [65, 74, 70, 64, 65]
Teams = ['Tottenham Hotspur', 'Liverpool', 'Manchester United', 'Leicester City', 'Tottenham Hotspur']

#Create line plot
plt.plot(players,goals_scored,marker='o')
plt.grid(True, linestyle='--', alpha=0.7)
plt.title('Total_Goals_Scored_For_Players')
plt.ylabel('Goals Scored')
plt.xlabel('Players')
plt.show()


# In[19]:


plt.scatter(GamesPlayed,goals_scored,marker='^')
plt.grid(True, linestyle='--', alpha=0.7)
plt.title('Total_Goals_Scored_VS_Games_Played')
plt.ylabel('Goals Scored')
plt.xlabel('Games Played')
for i, player in enumerate(players):
    plt.annotate(player, (GamesPlayed[i], goals_scored[i]), textcoords="offset points", xytext=(0, 5), ha='center')
plt.show()


# In[22]:


# Sort data to identify the top two players
sorted_indices = sorted(range(len(TeamPoints)), key=lambda k: TeamPoints[k], reverse=True)
top_two_indices = sorted_indices[:2]

plt.bar(Teams,TeamPoints,color=['red' if i in top_two_indices else 'blue' for i in range(len(Teams))])
plt.grid(True, linestyle='--', alpha=0.7)
plt.title('Teams_VS_TeamPoints_In_League')
plt.ylabel('Team Points')
plt.xlabel('Teams')
plt.show()


# In[24]:


# Find the index of the player with the maximum assists
max_assists_index = assists.index(max(assists))

# Create an explode list
explode = [0.1 if i == max_assists_index else 0 for i in range(len(players))]

# Create a pie chart
plt.pie(assists, labels=players, autopct='%1.1f%%', startangle=90, colors=['red', 'blue', 'green', 'purple', 'orange'], explode=explode)

# Add title
plt.title('Distribution of Assists Among Premier League Players')

# Show the plot
plt.show()


# In[ ]:




