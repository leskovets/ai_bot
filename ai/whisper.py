import os

import whisper


def voice_to_text(file_name: str) -> str:

    model = whisper.load_model("base")
    result = model.transcribe(file_name, fp16=False)

    os.remove(file_name)
    return result["text"]
