"""
Генерируем две волны разных частот в один аудиоканал (моно):
- 440 Гц (Ля первой октавы)
- 660 Гц (Примерно Ми второй октавы)
с одинаковой амплитудой

Слышим чистую квинту
"""
from paam_python.generator import generate_multiple_sines
from paam_python.graphics import draw_waves
from paam_python.player import play_mono

sampling_rate = 44100
volume = 0.5

wave = generate_multiple_sines([(440, 1), (660, 1)],
                               duration=1.5, slope_at_start=0.1, slope_at_end=0.1, sampling_rate=sampling_rate)

draw_waves((wave, '440 Гц + 660 Гц'))

play_mono(volume * wave)
