class ContentGenerator:
    def __init__(self, model_name: str = "gpt2"):
        # Initialize without loading model immediately
        self.model_name = model_name
        self.generator = None

    def _lazy_load(self):
        if self.generator is None:
            from transformers import pipeline
            self.generator = pipeline("text-generation", model=self.model_name)

    def generate(self, prompt: str, max_length: int = 100) -> str:
        self._lazy_load()
        return self.generator(prompt, max_length=max_length)[0]["generated_text"]