from audioplayer import AudioPlayer

# Playback stops when the object is destroyed (GC'ed), so save a reference to the object for non-blocking playback.
AudioPlayer("Other.mp3").play(block=True)

