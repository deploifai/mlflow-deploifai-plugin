from setuptools import setup, find_packages


setup(
    name="mlflow-deploifai",
    version="0.0.1",
    description="Deploifai plugin for MLflow",
    packages=find_packages(),
    # Require MLflow as a dependency of the plugin, so that plugin users can simply install
    # the plugin & then immediately use it with MLflow
    install_requires=["mlflow"],
    entry_points={
        "mlflow.request_header_provider":
            "unused=mlflow_deploifai.request_header_provider:DeploifaiRequestHeaderProvider"
    },
)