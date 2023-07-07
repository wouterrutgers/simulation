from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from simulate import simulate
import multiprocessing
import math

class Item(BaseModel):
    chance: float
    amount: int

class ItemList(BaseModel):
    items: List[Item]

app = FastAPI()

@app.post('/')
async def root(items: ItemList):
    averageTrials = 5000

    pool = multiprocessing.Pool(multiprocessing.cpu_count())

    results = pool.map(simulate, [items] * averageTrials)
    kills = [result for result in results]

    return math.ceil(sum(kills) / averageTrials)
