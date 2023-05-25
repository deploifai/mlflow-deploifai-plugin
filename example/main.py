import os
import mlflow
from time import sleep

# only if running an experiment outside deploifai (this must come before setting mlflow tracking uri and experiment)
os.environ["MLFLOW_TRACKING_USERNAME"] = "<workspace>/<project>/<experiment>"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "drat"

# setup mlflow for this experiment
mlflow.set_tracking_uri("http://localhost:8180")
mlflow.set_experiment("<workspace>/<project>/<experiment>")


def main(limit):
    with mlflow.start_run():
        for i in range(1, limit):
            mlflow.log_metric("key", i)
            print(i)
            sleep(1)


if __name__ == "__main__":
    main(10)
