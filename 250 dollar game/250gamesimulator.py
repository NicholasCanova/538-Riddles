import random

counter2 = 0
for i in range(0, 1000000):
	total = random.uniform(0, 1)
	counter1 = 1
	while (total < 1.0):
		counter1 += 1
		next = random.uniform(0, 1)
		total += next

	counter2 += counter1

print counter2 / 1000000.0