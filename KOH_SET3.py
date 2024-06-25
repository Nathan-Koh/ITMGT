#!/usr/bin/env python
# coding: utf-8

# In[249]:


def relationship_status(from_member, to_member, social_graph):

    if to_member in social_graph[from_member]["following"] and from_member in social_graph[to_member]["following"]:
        return "friends"
    elif to_member in social_graph[from_member]["following"]:
        return "follower"
    elif from_member in social_graph[to_member]["following"]:
        return "followed by"
    else:
        return "no relationship"


# In[248]:


def tic_tac_toe(board):

    board_size = len(board)
    vert_counter = 0
    diag_counter_O = 0
    diag_counter_X = 0
    
    #horizontal
    for i in range(0, board_size):
        if board[i].count("O") == board_size:
            return "O"
        elif board[i].count("X") == board_size:
            return "X"
        else:
            continue

    #vertical O
    for j in range(0, board_size):
        for k in range(0, board_size):
            if board[k][j] == "O":
                vert_counter += 1
            else:
                continue
        if vert_counter == board_size:
            return "O"
        else:
            vert_counter = 0

    #vertical X
    for j in range(0, board_size):
        for k in range(0, board_size):
            if board[k][j] == "X":
                vert_counter += 1
            else:
                continue
        if vert_counter == board_size:
            return "X"
        else:
            vert_counter = 0

    #diagonals
    for n in range(0, board_size):
        if board[n][n] == "O":
            diag_counter_O += 1
        if board[n][n] == "X":
            diag_counter_X += 1
        
    if diag_counter_O == board_size:
        return "O"
    if diag_counter_X == board_size:
        return "X"
    else:
        diag_counter_O = 0
        diag_counter_X = 0
        
    for m in range(0, board_size):
        if board[m][board_size-m-1] == "O":
            diag_counter_O += 1
        if board[m][board_size-m-1] == "X":
            diag_counter_X += 1
        else:
            continue

    if diag_counter_O == board_size:
        return "O"
    if diag_counter_X == board_size:
        return "X"
    
    return "NO WINNER"


# In[246]:


def eta(first_stop, second_stop, route_map):

    eta = 0
    keys = []
    current_stop = first_stop
    
    for key in route_map.keys():
        keys.append(key)
    
    if first_stop == second_stop:
        return 0
    elif (first_stop, second_stop) in route_map.keys():
        eta = route_map[(first_stop,second_stop)]['travel_time_mins']
    else:
        while current_stop != second_stop:
            for x in range(0, len(keys)):
                if keys[x][0] == current_stop:
                    eta += route_map[keys[x]]['travel_time_mins']
                    current_stop = keys[x][1]
                    break
                else:
                    continue
 
    return eta


# In[ ]:




