import numpy as np


# Simulation times
times = 100000
# Number of doors, only one door has car, the others are goats
doors_nb = 3

# If change door, the times to get the car
change_win_times = 0
# If don't change door, the times to get the car
not_change_win_times = 0

# Simulation 
for time in range(times):
	# Initialize the doors, True represents car, False represents goat
	doors = [False, False, False]
	doors[np.random.choice(doors_nb)] = True
	# You firstly choose a door randomly
	first_door_choose =  np.random.choice(doors_nb)
	# You don't change the door choice, if it has car, you will win
	if doors[first_door_choose]:
		not_change_win_times += 1
	# Host choose a door which has a goat
	host_door_choose = np.random.choice([i for i in range(doors_nb) 
			    	   if not doors[i] and i != first_door_choose]) 
	# You choose to change the door
	second_door_choose = np.random.choice([i for i in range(doors_nb)
				  if i not in [first_door_choose, host_door_choose]])
	# If your second door choice has a car, you will win
	if doors[second_door_choose]:
		change_win_times += 1

# Possibilities to win with change and not change the first door choice
print("If not change, win possibility is", not_change_win_times / times)
print("If change, win possibility is:", change_win_times / times)
