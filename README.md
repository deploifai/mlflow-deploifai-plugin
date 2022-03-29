# MLFLow plugin for Deploifai

## What is Deploifai?
Deploifai is a modern developer platform for Machine Learning. We build 
tools to automate cloud infrastructure, and make the best tools for data 
science and ML simple and straightforward for the community.

## What does this plugin do?
This plugin helps the MLFlow client to connect and work with the Deploifai 
MLFlow community server. Without this plugin, Deploifai MLFlow server cannot be 
used.

## How to install

```shell
pip install mlflow-deploifai
```

Once the plugin is installed, use MLFlow just as you would normally.

#### Note: Use experiment_id to set_experiment
```python
import mlflow

mlflow.set_experiment(experiment_id="experiment id")
```

## Contributing
We are working on a contribution page. We welcome you raising any issues, 
and even having your PR submissions. Thanks!
