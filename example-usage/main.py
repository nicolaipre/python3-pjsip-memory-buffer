

from Audio import BufferIO()
from Softphone import Softphone()

# Set up and connect pjsua as normal
# ...


# Ex 1. Listen to audio from phone and write captured audio to audio_buffer
audio_buffer = BufferIO(sample_rate=48000.0)
softphone = Softphone(sample_rate=48000.0)
softphone.listen(audio_buffer)


# Ex 2. Play audio from audio_buffer to phone
audio_buffer = BufferIO(sample_rate=48000.0)
softphone = Softphone(sample_rate=48000.0)
softphone.play(audio_buffer)


# Ex 3. Stream between two audio sources (for instance Discord and a mobile phone)

## Create two audio IO buffers
call_audio    = BufferIO(sample_rate=48000.0)
discord_audio = BufferIO(sample_rate=48000.0)

## Create the audio connections
softphone  =  Softphone(sample_rate=48000.0)
disc_vc    = DiscordVoice(sample_rate=48000.0)

## Cross-stream
softphone.listen(call_audio)  # Capture phone audio to buffer
disc_vc.play(call_audio)      # Play phone audio to discord voice connector

disc_vc.listen(discord_audio) # Capture discord audio to buffer
softphone.play(discord_audio) # Play discord audio to phone
