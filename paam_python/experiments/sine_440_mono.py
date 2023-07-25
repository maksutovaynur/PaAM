"""
Генерируем чистый синусоидальный звук частотой 440 Гц (Ля первой октавы)
"""
from paam_python.generator import generate_sine
from paam_python.graphics import draw_waves
from paam_python.player import play_mono

sampling_rate = 44100
volume = 0.5

sine = generate_sine(frequency=440, duration=1.5, slope_at_start=0.1, slope_at_end=0.1, sampling_rate=sampling_rate)

play_mono(volume * sine)

draw_waves((sine, 'Синусоида 440 Гц'))
