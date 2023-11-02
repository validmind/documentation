# StabilityAnalysis

Base class for embeddings stability analysis tests

category = "model_diagnosis
required_inputs = ["model", "dataset"]
default_params = {
text_column": None,
mean_similarity_threshold": 0.7,
}
metadata = {
task_types": ["feature_extraction"],
tags": ["llm", "text_data", "text_embeddings", "visualization"],
}

@abstractmethod
def perturb_data(self, data: str) -> str:
Perturb a string of text (overriden by subclasses)