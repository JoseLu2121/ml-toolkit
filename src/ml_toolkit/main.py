from config import ExperimentConfig
from pipeline import generate_fake_csv

exp1 = ExperimentConfig("exp1", tags=("tag1", "tag2"))

exp1.to_json("exp1.json")


generate_fake_csv(100, "data.csv", 5, None, True)