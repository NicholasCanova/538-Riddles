import random
import numpy as np

player_1_num = np.random.uniform(0, 1, 100000000)
player_2_num = np.random.uniform(0, 1, 100000000)


for i in range(0, len(player_1_num)):
	if player_1_num[i] < .60:
		player_1_num[i] = random.random()
	else:
		pass

for j in range(0, len(player_2_num)):
	if player_2_num[j] < 0.625:
		player_2_num[j] = random.random()
	else:
		pass


counter = 0
for k in range(0, len(player_1_num)):
	if player_1_num[k] > player_2_num[k]:
		counter += 1
	else:
		pass

ratio = float(counter) / len(player_1_num)
print "player 1's winning percentage"
print ratio