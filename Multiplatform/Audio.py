## Credit to Haider Imtiaz

# Audio Editor
# pip install pydub
from pydub import AudioSegment
from pydub.utils import mediainfo
from pydub.playback import play
# Extract Sound from Video
sound = AudioSegment.from_file("video.mp4", format="mp4")
sound.export("music.mp3", format="mp3")
# Get Media Info
info = mediainfo("musci.wav")
print(info)
# Play Sound
play("music.mp3")
# Combine Sounds
sound1 = AudioSegment.from_file("music.mp3")
sound2 = AudioSegment.from_file("music.mp3")
combined = sound1 + sound2
combined.export("music_combined.mp3", format="mp3")
# Split Audio
sound = AudioSegment.from_file("music.mp3", format="mp3")
sound_1 = sound[:10000]
sound_2 = sound[10000:]
sound_1.export("music_1.mp3", format="mp3")
sound_2.export("music_2.mp3", format="mp3")
# Increase or Reduce Volumn
sound = AudioSegment.from_file("music.mp3", format="mp3")
sound_volumn = sound + 10
sound_volumn.export("music_volumn.mp3", format="mp3")
# Adding Silence to Audio
sound = AudioSegment.from_file("music.mp3", format="mp3")
sound_silence = sound + AudioSegment.silent(duration=1000)
sound_silence.export("music_silence.mp3", format="mp3")