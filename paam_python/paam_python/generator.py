import numpy as np

from paam_python.utils import DEFAULT_SAMPLING_RATE, normalize_wave, duration_to_samples, add_slope_at_end, \
    add_slope_at_start


def generate_sine(frequency: float,
                  duration: float, slope_at_start: float = 0, slope_at_end: float = 0,
                  sampling_rate: int = DEFAULT_SAMPLING_RATE, normalize=True):
    n_samples = duration_to_samples(duration, sampling_rate=sampling_rate)
    time_points = np.arange(n_samples) / sampling_rate
    wave = np.sin(2 * np.pi * frequency * time_points).astype(np.float32)
    if normalize:
        wave = normalize_wave(wave)
    if slope_at_start:
        add_slope_at_start(wave, slope_at_start, sampling_rate=sampling_rate)
    if slope_at_end:
        add_slope_at_end(wave, slope_at_end, sampling_rate=sampling_rate)
    return wave


def generate_multiple_sines(sines: list[tuple[float, float]],
                            duration: float, slope_at_start: float = 0, slope_at_end: float = 0,
                            sampling_rate: int = DEFAULT_SAMPLING_RATE, normalize=True):
    waves = [
        amplitude * generate_sine(frequency, duration, sampling_rate=sampling_rate, normalize=False)
        for frequency, amplitude in sines
    ]
    wave = np.sum(waves, axis=0)
    if normalize:
        wave = normalize_wave(wave)
    if slope_at_start:
        add_slope_at_start(wave, slope_at_start, sampling_rate=sampling_rate)
    if slope_at_end:
        add_slope_at_end(wave, slope_at_end, sampling_rate=sampling_rate)
    return wave
