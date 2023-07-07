import copy
import random
import logging

logger = logging.getLogger("api")

def simulate(items):
    localItems = copy.deepcopy(items.items)
    kills = 0

    while sum(item.amount for item in localItems):
        kills += 1

        for i in range(len(localItems)):
            chance = localItems[i].chance
            count = localItems[i].amount

            if count > 0:
                if random.random() < 1 / chance:
                    localItems[i].amount -= 1
                    continue

    return kills
