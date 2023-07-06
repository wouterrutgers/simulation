from multiprocessing import Pool
from flask import Flask, request, jsonify
import random
import copy
import math

app = Flask(__name__)

def simulate(chances):
    items = copy.deepcopy(chances)
    kills = 0

    while sum(item["amount"] for item in items):
        kills += 1

        for i in range(len(items)):
            chance = items[i]["chance"]
            count = items[i]["amount"]

            if count > 0:
                if random.random() < 1 / chance:
                    items[i]["amount"] -= 1
                    continue

    return kills

def simulate_process(chances):
    return simulate(chances)

def completed_in(chances):
    averageTrials = 5000
    totalTrials = 0

    with Pool() as pool:
        results = pool.map(simulate_process, [chances] * averageTrials)

    totalTrials = sum(results)
    return math.ceil(totalTrials / averageTrials)

@app.route('/', methods=['POST'])
def receive_post():
    data = request.get_json()
    return jsonify(completed_in(data))

if __name__ == '__main__':
    app.run()
