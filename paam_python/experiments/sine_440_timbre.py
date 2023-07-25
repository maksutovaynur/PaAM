"""
Тембры и эффект пропущенной фундаментальной (базовой) частоты.

Генерируем несколько волн кратных частот - базовую (220 Гц) и гармоники (440, 660 и 880 Гц).
Причём амплитуды гармоник ниже чем амплитуда базового тона (соотношение 6:4:3:2)
Слышим только один звук, но тембрально окрашенный.

Удаляем базовую частоту. Слышим по-другому тембрально окрашенный звук.
И, вероятно, нам слышится звук 220 Гц, хотя его здесь нет.
"""
from time import sleep

from paam_python.generator import generate_multiple_sines
from paam_python.graphics import draw_spectre, draw_waves
from paam_python.player import play_mono

sampling_rate = 44100
volume = 0.2

base_tone = (220, 6)
harmonics = [(440, 4), (660, 3), (880, 2)]

wave_timbre = generate_multiple_sines(
    [base_tone] + harmonics,
    duration=1.5, slope_at_start=0.1, slope_at_end=0.1, sampling_rate=sampling_rate)
wave_timbre_skipped_base = generate_multiple_sines(
    harmonics,
    duration=1.5, slope_at_start=0.1, slope_at_end=0.1, sampling_rate=sampling_rate)

play_mono(volume * wave_timbre)

sleep(1)

play_mono(volume * wave_timbre_skipped_base)

draw_spectre(([base_tone], 'Базовый тон'), (harmonics, 'Гармоники'), wait=False)
draw_waves((wave_timbre, 'База + гармоники'), (wave_timbre_skipped_base, 'Только гармоники'))
