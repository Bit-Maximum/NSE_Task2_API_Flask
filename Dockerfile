FROM python:3.12-slim
LABEL authors="Bit Maximum"

WORKDIR /app

# Установим PoEtry :)
RUN pip install poetry

# Копируем файлы poetry
COPY pyproject.toml poetry.lock ./

# Оключим создание дополнительного виртуального окружения
RUN poetry config virtualenvs.create false

# Установим зависимости
RUN poetry install --no-interaction --no-root

# Скопируем остальное приожение
COPY . .

# Установим зависимости в режиме разработчика
RUN poetry install --no-interaction