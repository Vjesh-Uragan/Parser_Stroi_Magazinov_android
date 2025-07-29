В папке App
app.py Описание backend (серверной части)



файл requirements.txt с содержимым:
  flask
  requests
  beautifulsoup4


  Установите зависимости
    pip install -r requirements.txt

Для продакшена используйте Gunicorn
  pip install gunicorn
  gunicorn -w 4 -b 0.0.0.0:5000 your_flask_file:app

  (где your_flask_file — имя файла без .py, а app — имя Flask-приложения)

  
