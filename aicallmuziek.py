import os
import openai

openai.api_key = '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'

audio_file= open("sample-0.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript)