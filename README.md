# Тестирование Web-приложения с использованием стиля PageObject

Использованные технологии:
* Python
* PyTest
* Selenium

Проект выполнен в рамках курса "Автоматизация тестирования с помощью Selenium и Python" https://stepik.org/course/575

Перед запуском тестов необходимо установить зависимости из файла requirements.txt с помощью команды
```
pip install -r requirements.txt
```
Тесты с маркировкой need_review запускаются командой
```
pytest -v --tb=line --language=en -m need_review
```

Полный прогон тестов из файлов test_main_page.py и test_product_page.py можно запустить с помощью команд
```
pytest -s test_main_page.py
```
```
pytest -s test_product_page.py
```