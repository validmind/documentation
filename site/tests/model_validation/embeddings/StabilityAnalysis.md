# StabilityAnalysis

Base class for embeddings stability analysis tests

required_inputs = ["model", "dataset"]
default_params = {
mean_similarity_threshold": 0.7,
}
metadata = {
task_types": ["feature_extraction"],
tags": ["llm", "text_data", "text_embeddings", "visualization"],
}

@abstractmethod
def perturb_data(self, data: str) -> str:
Perturb a string of text (overriden by subclasses)