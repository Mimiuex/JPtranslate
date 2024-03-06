from voicevox import Client
import asyncio 

from pydub import AudioSegment
from pydub.playback import play

async def main(text, audio_filename):
    async with Client() as client:

        audio_query = await client.create_audio_query(
            text, speaker = 20 #synthesize the audio
        )
        with open(audio_filename, "wb") as f: #open the file "voice.wav"
            f.write(await audio_query.synthesis(speaker = 20)) #write the synthesized audio to the file
            
            song = AudioSegment.from_wav(audio_filename)
            play(song)

if __name__ == "__main__":
    asyncio.run(main())
    