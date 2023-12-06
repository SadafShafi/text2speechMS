import torch
from TTS.api import TTS
from unittest.mock import patch

class Text2Speech:
    def __init__(self, prompt = "Hi, how are you ?", language="en",speaker = "female-en-5"):
        """
          SPEAKERS:
            'female-en-5',
            'female-en-5\n',
            'female-pt-4\n',
            'male-en-2',
            'male-en-2\n',
            'male-pt-3\n'
          Languages :
            'en', 
            'fr-fr', 
            'pt-br'
        """

        self.prompt = prompt
        self.language = language
        self.speaker = speaker

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"The Device is {self.device}")
        self.tts = TTS('tts_models/multilingual/multi-dataset/your_tts').to("cuda")
        print(self.tts.speakers,self.tts.languages)

    def t2s(self):
        try:
            print("TTS started")
            wav_path = self.tts.tts_to_file(
                text=self.prompt,
                speaker=self.speaker,
                language=self.language,
                file_path="output.wav"
            )
            print("audio generated")
            return wav_path
        except Exception as e:
            print(f"Error generating audio: {str(e)}")
            return "None"
