import torch
from TTS.api import TTS
from unittest.mock import patch

class Text2Speech:
    def __init__(self, referenceAudiopth, language="en"):
        self.referenceAudiopth = referenceAudiopth
        self.language = language
        device = "cuda" if torch.cuda.is_available() else "cpu"
        # with patch('builtins.input', return_value='y'):
        #     self.tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)
        self.tts = TTS('tts_models/multilingual/multi-dataset/your_tts', gpu=True)
        print(f"The Device is {device}")
        # self.tts = TTS(model_path="tts/tts_models--multilingual--multi-dataset--xtts_v2/",
        #               config_path="tts/tts_models--multilingual--multi-dataset--xtts_v2/config.json",).to(device)


    def t2s(self, text):
        try:
            print(text)
            wav_path = self.tts.tts_to_file(
                text=text,
                speaker_wav=self.referenceAudiopth,
                language=self.language,
                file_path="output.wav"
            )

            print("audio generated")
            return wav_path
        except Exception as e:
           print(f"Error generating audio: {str(e)}")
           return None
