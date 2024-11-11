# TODO решите задачу
import json

INPUT_FILE = "input.json"


def task() -> float:
    with open(INPUT_FILE, 'r') as file:
        data = json.load(file)
        sum_ = sum(i['score'] * i["weight"] for i in data)
    return round(sum_, 3)


print(task())
