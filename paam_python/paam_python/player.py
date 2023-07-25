import numpy as np
import pyaudio

from paam_python.utils import DEFAULT_SAMPLING_RATE


def play_mono(wave: np.array, sampling_rate: int = DEFAULT_SAMPLING_RATE):
    wave_bytes = wave.astype(np.float32).tobytes()
    _device = pyaudio.PyAudio()
    # if not _device.is_format_supported(sampling_rate, output_format=pyaudio.paFloat32, output_channels=2):
    #     print(f"WARNING: possibly mono for {sampling_rate}Hz is not supported")
    stream = _device.open(format=pyaudio.paFloat32, channels=1, rate=sampling_rate, output=True)
    stream.write(wave_bytes)
    stream.stop_stream()
    stream.close()
    _device.terminate()


def play_stereo(left: np.array, right: np.array, sampling_rate: int = DEFAULT_SAMPLING_RATE):
    wave_bytes = np.array([left, right]).astype(np.float32).T.tobytes()
    _device = pyaudio.PyAudio()
    # if not _device.is_format_supported(sampling_rate, output_format=pyaudio.paFloat32, output_channels=2):
    #     print(f"WARNING: possibly mono for {sampling_rate}Hz is not supported")
    stream = _device.open(format=pyaudio.paFloat32, channels=2, rate=sampling_rate, output=True)
    stream.write(wave_bytes)
    stream.stop_stream()
    stream.close()
    _device.terminate()

