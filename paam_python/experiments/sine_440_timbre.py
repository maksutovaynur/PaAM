"""
Генерируем две волны разных частот в один аудиоканал (моно):
- 440 Гц (Ля первой октавы)
- 660 Гц (Примерно Ми второй октавы)
с одинаковой амплитудой

Слышим чистую квинту
"""
from time import sleep

from paam_python.generator import generate_multiple_sines
from paam_python.graphics import draw_spectre, draw_waves
from paam_python.player import play_mono

sampling_rate = 44100
volume = 0.5

base_tone = (220, 12)
harmonics = [(440, 8), (660, 6), (880, 4), (1100, 2), (1320, 1)]

wave_timbre = generate_multiple_sines(
    [base_tone] + harmonics,
    duration=1.5, slope_at_start=0.1, slope_at_end=0.1, sampling_rate=sampling_rate)
wave_timbre_skipped_base = generate_multiple_sines(
    harmonics,
    duration=1.5, slope_at_start=0.1, slope_at_end=0.1, sampling_rate=sampling_rate)

draw_spectre(([base_tone], 'Базовый тон'), (harmonics, 'Гармоники'))
draw_waves((wave_timbre, 'База + гармоники'), (wave_timbre_skipped_base, 'Только гармоники'))

play_mono(volume * wave_timbre)

sleep(1)

play_mono(volume * wave_timbre_skipped_base)
