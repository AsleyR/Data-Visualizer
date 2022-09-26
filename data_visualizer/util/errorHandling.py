import pathlib
from pydub import AudioSegment
from pydub.playback import play

def playErrorSound():
    ERROR_SOUND = pathlib.Path(__file__).parent.parent.resolve() / "media/audio/computer-error.wav"
    print(ERROR_SOUND)
    error = AudioSegment.from_wav(ERROR_SOUND)
    play(error)
    