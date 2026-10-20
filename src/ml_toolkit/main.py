from config import ExperimentConfig
from pipeline import generate_fake_csv, read_csv

exp1 = ExperimentConfig("exp1", tags=("tag1", "tag2"))

exp1.to_json("exp1.json")

gen = read_csv("data.csv", ",")

print(next(gen))