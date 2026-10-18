from config import ExperimentConfig


exp1 = ExperimentConfig("exp1", tags=("hola", "adios"))

exp1.to_json("exp1.json")

