## Меркурьев М. А.

### Практическая работа №2 "API, Flask" по дисциплине "Инженерия интернет-систем"

# Датасет

За основу был взят датасет "Grocery Sales Database":\
[https://www.kaggle.com/datasets/andrexibiza/grocery-sales-dataset/](https://www.kaggle.com/datasets/andrexibiza/grocery-sales-dataset/)

# Установка

Перед началом работы убедитесь, что у вас установлен Python (рекомендуемая версия: 3.8+).

Установите зависимости с помощью `pip`:

```bash
pip install -r requirements.txt
```

или используя `poetry`:

```bash
poetry install
```

# Запуск проекта

Для запуска сервера выполните команду:

```bash
python app.py
```

После запуска сервер будет доступен по адресу: `http://127.0.0.1:5000/`

# API Эндпоинты

## 1. Эндпоинты городов (`/api/v1/cities`)

| Метод  | URL                        | Описание                            |
| ------ | -------------------------- | ----------------------------------- |
| GET    | `/api/v1/cities/`          | Получить список всех городов        |
| GET    | `/api/v1/cities/<city_id>` | Получить данные о конкретном городе |
| POST   | `/api/v1/cities/`          | Добавить новый город                |
| PUT    | `/api/v1/cities/<city_id>` | Обновить данные города              |
| DELETE | `/api/v1/cities/<city_id>` | Удалить город                       |

### Примеры запросов

#### Получить список городов

```bash
curl -L -X GET http://127.0.0.1:5000/api/v1/cities/
```

#### Добавить новый город

```bash
curl -L -X POST http://127.0.0.1:5000/api/v1/cities/ \  
    -H "Content-Type: application/json" \  
    -d '{"name": "New City", "zipcode": 12345}'
```

## 2. Эндпоинты товаров (`/api/v1/products`)

| Метод | URL                    | Описание                   |
| ----- | ---------------------- | -------------------------- |
| GET   | `/api/v1/products/max` | Самый дорогой товар        |
| GET   | `/api/v1/products/min` | Самый дешевый товар        |
| GET   | `/api/v1/products/avg` | Средняя цена по категориям |

### Примеры запросов

#### Получить самый дорогой товар

```bash
curl -L -X GET http://127.0.0.1:5000/api/v1/products/max
```

#### Получить среднюю цену по категориям

```bash
curl -L -X GET http://127.0.0.1:5000/api/v1/products/avg
```

# Автор

**Меркурьев М. А.**\
*Группа: М9124-09.04.04рпис*\
*Дальневосточный федеральный университет, 2025*

