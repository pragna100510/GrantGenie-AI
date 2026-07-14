from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

from config import (
    IBM_API_KEY,
    IBM_PROJECT_ID,
    IBM_URL,
)

credentials = Credentials(
    url=IBM_URL,
    api_key=IBM_API_KEY
)

model = ModelInference(
    model_id="meta-llama/llama-3-3-70b-instruct",
    credentials=credentials,
    project_id=IBM_PROJECT_ID,
    params={
        "max_new_tokens": 400,
        "temperature": 0.3,
    }
)