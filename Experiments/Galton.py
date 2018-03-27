
import random

slotNUM = 10
ballNUM = 10000

slots = [ballNUM]
print(slots)

layerNUM = 20

for iters in range(layerNUM):
    new_slots = [0] * (iters+2)
    for s in range(len(slots)):
        for ball in range(slots[s]):
            if random.random() > 0.5:
                new_slots[s] += 1
            else:
                new_slots[s+1] += 1
    slots = new_slots
print(slots)

prob = [balls/ballNUM for balls in slots]
print(prob)