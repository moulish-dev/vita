class BaseTTS:
    def generate_audio(self, text: str, output_path: str):
        raise NotImplementedError