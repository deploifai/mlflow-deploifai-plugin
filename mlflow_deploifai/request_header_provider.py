from mlflow.tracking.request_header.abstract_request_header_provider import RequestHeaderProvider
from mlflow.tracking.fluent import active_run, _get_experiment_id, get_experiment


class DeploifaiRequestHeaderProvider(RequestHeaderProvider):
  def in_context(self):
    return True

  def request_headers(self):
    exp_id = _get_experiment_id()
    return {
      "experiment": str(exp_id),
      "client": "deploifai"
    }
