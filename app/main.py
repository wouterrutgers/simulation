from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
import multiprocessing
import math
import copy
import random

class Item(BaseModel):
    chance: float
    amount: int

class ItemList(BaseModel):
    items: List[Item]

app = FastAPI()

@app.post('/')
async def root(items: ItemList):
    averageTrials = 3000

    pool = multiprocessing.Pool()

    results = pool.map(simulate, [items] * averageTrials)
    kills = [result for result in results]

    return math.ceil(sum(kills) / averageTrials)

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
