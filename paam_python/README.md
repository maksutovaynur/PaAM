# Эксперименты в Python


## Описание экспериментов
В каждом эксперименте генерируется звук определённых характеристик, а также рисуются спектры и волны на графиках.
- Простая синусоида в 440 Гц [sine_440_mono.py](experiments/sine_440_mono.py)
- Две синусоиды, моно [sine_440_660_mono.py](experiments/sine_440_660_mono.py)
- Две синусоиды, стерео [sine_440_660_stereo.py](experiments/sine_440_660_stereo.py)
- Тембрально окрашенный звук и эффект пропущенного основного тона [sine_440_timbre.py](experiments/sine_440_timbre.py)

## Подготовка к работе
- Установите Python версии `3.10` любым удобным способом. 
Например, можно установить пакет [miniconda3](https://conda.io/en/latest/miniconda.html)
- Если вы работаете на Linux, то дополнительно нужно установить PortAudio. Например, на ubuntu:
```bash
sudo apt-get install libasound-dev portaudio19-dev
```
- Установите [Poetry](https://python-poetry.org/docs/). 
После чего установите необходимые python-зависимости проекта 
следующей командой (нужно находиться в папке `PaAM/paam_python`):
```bash
poetry install
```
- Альтернативно предыдущему пункту можно установить зависимости через pip:
```bash
pip install -r requirements.txt
```

## Запуск экспериментов
### Через Poetry
```bash
poetry run python experiments/my_script_name.py
```
Например, 
```bash
poetry run python experiments/sine_440_mono.py
```

### Напрямую с помощью Python (при установке пакетов через Pip)
```bash
python experiments/sine_440_mono.py
```
