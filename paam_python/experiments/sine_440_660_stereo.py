"""
Генерируем две волны разных частот в два разных аудиоканала:
- 440 Гц (Ля первой октавы) в левое ухо
- 660 Гц (Примерно Ми второй октавы) в правое ухо
с одинаковой амплитудой

Слышим чистую квинту

Послушайте в наушниках, попеременно вынимая правый или левый, убедитесь, что в каждое ухо идёт своя волна
"""
from paam_python.generator import generate_sine
from paam_python.player import play_stereo

sampling_rate = 44100
volume = 0.5

left = generate_sine(440, duration=1.5, slope_at_start=0.1, slope_at_end=0.1, sampling_rate=sampling_rate)
right = generate_sine(660, duration=1.5, slope_at_start=0.1, slope_at_end=0.1, sampling_rate=sampling_rate)

play_stereo(volume * left, volume * right)
