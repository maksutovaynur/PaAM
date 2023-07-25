import numpy as np

DEFAULT_SAMPLING_RATE = 44100


def duration_to_samples(duration, sampling_rate: int = DEFAULT_SAMPLING_RATE):
    """

    :param sampling_rate: Частота дискретизации в герцах
    :param duration: Длительность в секундах
    :return: Число точек (семплов) в звуковой волне
    """
    return int(duration * sampling_rate)


def samples_to_duration(n_samples, sampling_rate: int = DEFAULT_SAMPLING_RATE):
    """

    :param n_samples: Число точек (семплов) в звуковой волне
    :param sampling_rate: Частота дискретизации в герцах
    :return: Длительность звука в секундах
    """
    return n_samples / sampling_rate


def normalize_wave(wave: np.array):
    mean_power = calc_mean_power(wave)
    return wave / mean_power


def calc_mean_power(wave: np.array) -> float:
    return ((wave * wave).sum(axis=0) / wave.shape[0]) ** .5


def add_slope_at_start(wave: np.array, duration: float, sampling_rate: int = DEFAULT_SAMPLING_RATE) -> None:
    slope_n_samples = min(wave.shape[0], duration_to_samples(duration, sampling_rate=sampling_rate))
    for i in range(slope_n_samples):
        wave[i] *= i / slope_n_samples


def add_slope_at_end(wave: np.array, duration: float, sampling_rate: int = DEFAULT_SAMPLING_RATE) -> None:
    slope_n_samples = min(wave.shape[0], duration_to_samples(duration, sampling_rate=sampling_rate))
    for i in range(slope_n_samples):
        wave[wave.shape[0] - i - 1] *= i / slope_n_samples
