import os
import mlflow
from time import sleep

os.environ["MLFLOW_TRACKING_USERNAME"] = "user"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "password"

# mlflow.create_experiment("test")
mlflow.set_tracking_uri("http://localhost")
mlflow.set_experiment(experiment_id="1")


def main():
  with mlflow.start_run():
    for i in range(1, 100):
      mlflow.log_metric("key", i)
      print(i)
      sleep(1)


if __name__ == "__main__":
  main()
