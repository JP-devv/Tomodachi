#6 strong woman
#10 small girl
#11 nasal guy
#14 book girl
#15-18 eroi onna
#19 whispering girl
#28 obachan
#35 old lady 2
#27 light whisper girl
#39-40 npc guy
#42 sakeji
#49 super shy girl
#50 whisper shy girl
#51 butler 
#53 npc guy 3
#54 betty
#55 boy

#21 narrator guy
#8 news woman
#17 ara ara
#13 deep voice man

# paste this
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

