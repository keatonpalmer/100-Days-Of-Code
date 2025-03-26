friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
import random


# Option 1
roulette = random.choice(friends)
print(roulette)

# Can also be simplified to print(random.choice(friends))

#Option 2
random_index = random.randint(0, 4)
print(friends[random_index])