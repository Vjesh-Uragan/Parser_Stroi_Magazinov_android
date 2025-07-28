```python
from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def parse_obi(query):
    url = f"https://www.obi.ru/search/{query.replace(' ', '%20')}/"
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(r.text, "html.parser")
    items = soup.find_all("div", class_="b-product-tile")
    results = []
    for item in items:
        title_tag = item.find("a", class_="b-product-tile__title")
        price_tag = item.find("span", class_="b-product-tile__price-current__number")
        if title_tag and price_tag:
            title = title_tag.text.strip()
            price = price_tag.text.strip()
            link = "https://www.obi.ru" + title_tag["href"]
            results.append({
                "site": "obi.ru",
                "title": title,
                "price": price,
                "url": link
            })
    return results

def parse_lemanapro(query):
    url = f"https://lemanapro.ru/search/?q={query.replace(' ', '+')}"
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(r.text, "html.parser")
    items = soup.find_all("div", class_="product-item")
    results = []
    for item in items:
        title_tag = item.find("a", class_="product-title")
        price_tag = item.find("span", class_="price")
        if title_tag and price_tag:
            title = title_tag.text.strip()
            price = price_tag.text.strip()
            link = "https://lemanapro.ru" + title_tag["href"]
            results.append({
                "site": "lemanapro.ru",
                "title": title,
                "price": price,
                "url": link
            })
    return results

@app.route("/api/search", methods=["POST"])
def search():
    data = request.json
    query = data.get("query", "")
    results = []
    results += parse_obi(query)
    results += parse_lemanapro(query)
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

```

Готово!
Ваш файл `app.py` теперь возвращает все подходящие товары по ключевому слову с обоих магазинов (obi.ru и lemanapro.ru), включая название, цену и ссылку.

---

**Что делать дальше:**
1. Перезапустите сервер:
   Остановите старый процесс (если был запущен) и снова выполните:
   ```
   python app.py
   ```
2. Проверьте работу поиска с Android-приложения — теперь должны отображаться все найденные товары по вашему запросу.

---




```plaintext
   python app.py
```

---


куда добавить файл app.py

---



Файл `app.py` — это основной файл вашего серверного (бэкенд) приложения на Python (Flask).
Вот куда и как его правильно разместить:

---

## Куда добавить файл `app.py`

1. **Создайте папку для бэкенда**
   Обычно её называют `backend` или `server` в корне вашего проекта.

2. **Положите файл `app.py` в эту папку**
   Пример структуры:
   ```
   ваш_проект/
   ├── backend/
   │   ├── app.py
   │   └── requirements.txt
   ├── app/
   └── ...
   ```

3. **В этой же папке (`backend`) создайте файл `requirements.txt`**
   В него добавьте:
   ```
   Flask
   requests
   beautifulsoup4
   ```

---

## Как запустить сервер

1. Откройте терминал/командную строку.
2. Перейдите в папку `backend`:
   ```
   cd путь_к_вашему_проекту/backend
   ```
3. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```
4. Запустите сервер:
   ```
   python app.py
   ```

---

## Как проверить

- После запуска сервер будет доступен по адресу:
  `http://localhost:5000/api/search`
- Можно проверить работу через Postman, curl или ваше Android-приложение.

---

**Если структура вашего проекта другая — напишите, я подскажу, куда лучше положить файл!**
Если возникнут ошибки при запуске — пришлите их сюда, я помогу!

```plaintext
   ваш_проект/
   ├── backend/
   │   ├── app.py
   │   └── requirements.txt
   ├── app/
   └── ...
```

```plaintext
   Flask
   requests
   beautifulsoup4
```

```plaintext
   cd путь_к_вашему_проекту/backend
```

```plaintext
   pip install -r requirements.txt
```

```plaintext
   python app.py
```

---



Файл `app.py` **НЕ добавляется** в Android-приложение.

---

### Пометка

- `app.py` — это серверная часть (бэкенд), написанная на Python (Flask).
- Android-приложение — это клиент, который работает на телефоне и отправляет запросы на сервер.
- Сервер (файл `app.py`) должен работать на компьютере, сервере или облаке, а не на телефоне.

---

## Как правильно:

1. **Файл `app.py` размещается и запускается на компьютере или сервере**
   (например, на вашем ПК, ноутбуке, VPS или в облаке).

2. **Android-приложение**
   - Устанавливается на телефон.
   - В коде приложения указывается адрес сервера, где запущен `app.py` (например, `http://192.168.1.10:5000/api/search`).

---

## Как это работает

1. Вы запускаете сервер (`app.py`) на компьютере.
2. Сервер ждёт запросы на поиск товаров.
3. Приложение на телефоне отправляет запросы на этот сервер.
4. Сервер парсит сайты и возвращает результаты в приложение.

---

**Если вы хотите всё протестировать на одном компьютере:**
- Запустите сервер (`app.py`) на ПК.
- В Android-приложении укажите IP-адрес вашего ПК (например, `http://192.168.1.10:5000/api/search`).
- Телефон и ПК должны быть в одной Wi-Fi сети.