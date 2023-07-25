from threading import Thread
from typing import Iterable

import numpy as np
from matplotlib import pyplot as plt

from paam_python.utils import DEFAULT_SAMPLING_RATE

PeakType = tuple[float, float]
TimbreType = list[PeakType]
Wave = Iterable


_colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
_threads = []


def draw_spectre(*peaks: TimbreType | tuple[TimbreType, str], wait=False):
    def _inner():
        fig, ax = plt.subplots(1, 1, figsize=(14, 7))
        max_value = 0
        for i, p in enumerate(peaks):
            if isinstance(p, tuple):
                p, label = p
            else:
                label = f'#{i + 1}'
            freqs, amps = np.array(p).T
            max_value = max(max_value, amps.max())
            lower = np.zeros_like(freqs)
            color = _colors[i % len(_colors)]
            plt.plot([freqs, freqs], [lower, amps], color=color, label=label)
        ax.set_title('Спектр звуковой волны')
        ax.set_ylim(0, max_value * 1.1)
        ax.set_xlabel("Частота, Гц")
        ax.set_ylabel("Относительная амплитуда")
        ax.legend()
        fig.show()
        fig.waitforbuttonpress()
    # _inner()
    t = Thread(target=_inner)
    _threads.append(t)
    t.start()
    if wait:
        wait_graphics()


def draw_waves(*waves: Wave | tuple[Wave, str],
               sampling_rate: int = DEFAULT_SAMPLING_RATE, max_samples: int = 1500, wait=False):
    def _inner():
        n_samples = 0
        t_max = 0
        fig, ax = plt.subplots(1, 1, figsize=(14, 7))
        for i, wave in enumerate(waves):
            if isinstance(wave, tuple):
                wave, label = wave
            else:
                label = f'#{i + 1}'
            times = np.arange(wave.shape[0]) / sampling_rate
            color = _colors[i % len(_colors)]
            ax.plot(times, wave, label=label, color=color)
            n_samples = max(n_samples, wave.shape[0])
            t_max = times.max()
        if n_samples > max_samples:
            delta = max_samples / n_samples * t_max / 2
            center = t_max / 2
            ax.set_xlim(center - delta, center + delta)
        ax.set_xlabel('Время, с')
        ax.set_ylabel('Амплитуда')
        ax.set_title('Звуковая волна')
        ax.legend()
        fig.show()
        fig.waitforbuttonpress()
    # _inner()
    t = Thread(target=_inner)
    _threads.append(t)
    t.start()
    if wait:
        wait_graphics()


def wait_graphics():
    for t in _threads:
        t.join()
