#21 narrator guy
#8 news woman
#17 ara ara
#13 deep voice man

import sys
import asyncio
import io
from voicevox import Client
from pydub import AudioSegment
from pydub.playback import play

if len(sys.argv) < 2:
    print("Usage: python anime.py [voice-id] <text>")
    sys.exit(1)

if len(sys.argv) == 2:
  voice = 13
  text_to_speak = sys.argv[1]
else:
  voice = sys.argv[1]
  text_to_speak = sys.argv[2]

async def main():
    async with Client() as client:
        audio_query = await client.create_audio_query(text_to_speak, speaker=voice)
        audio_data = await audio_query.synthesis(speaker=voice)

        audio = AudioSegment.from_file(io.BytesIO(audio_data), format="wav")
        play(audio)

asyncio.run(main())

