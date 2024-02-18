from django.apps import AppConfig
from ctransformers import AutoModelForCausalLM



class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self) -> None:
        self.llm = AutoModelForCausalLM.from_pretrained("TheBloke/StableBeluga-13B-GGML", model_type="llama")
        # self.llm = AutoModelForCausalLM.from_pretrained("C:/Users/megaf/Downloads/app/DoubleCheck/main/stablebeluga-13b.ggmlv3.q6_k.bin", model_type="llama")
