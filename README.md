Тестовое задание по автоматизации тестирования UI и API веб-приложения, расположенного по URL https://reqres.in

Задача:
Необходимо на Python + PyTest написать проект, где реализовать следующие пункты:
1) Написать позитивные и негативные API тесты, которые представлены на главной странице как образец;
2) Написать UI тесты с главной страницы, которые будут проверять, что при нажатии на кнопку отображения образца запроса, получаемый результат (тело ответа и статус код) такой же как и через вызов API;
3) Все тесты параметризировать и добавить фикстуры;
4) Добавить возможность масштабировать проект (К примеру: если в WEB - добавится новая страница, а в API добавится новая версия API. То в таком случае добавляется новый класс и не нарушается текущая реализация);
5) Подключить отчетность Allure Framework;

Технологический стек проекта: Python, Pytest, Selenium, requests, allure.

Решение:
1) Были написаны позитивные и негативные API-автотесты для всех методов с главной страницы. В тестах проверяется статус-код ответа от сервера, валидируется тело ответа в соответствии со схемой
2) Написаны UI-автотесты. Реализованы с помощью Selenium WebDriver.
3) Реализована возможность масштабирования проекта с помощью паттерна PageObject. Для написания автоматизированных тестов для новой страницы нужно создать новые файлы с классами для тестов и методов. В случае добавления новой версии API добавляются новые эндпоинты в будущие методы для тестов, старые продолжают работать.
4) К API и WEB автотестам подключен Allure Framework с созданием скриншотов в процессе прохождения автотеста.

Запуск проекта:
1) Перейти в папку проекта и вызвать команду в терминале: pip install -r requirements.txt
2) Для запуска WEB-автотестов через браузер Google Chrome необходимо вызвать команду pytest --browser=chrome --alluredir=./chrome/allure-results ./tests/. Для запуска WEB-автотестов через браузер Mozilla Firefox необходимо вызвать команду pytest --browser=firefox --alluredir=./firefox/allure-results ./tests/
3) Для генерации отчета установить Allure (подробности можно узнать [тут](https://docs.qameta.io/allure/#_installing_a_commandline))
4) Сгенерировать отчет по автотестам, запущенным в браузере Google Chrome можно командой allure generate -c ./chrome/allure-results -o ./chrome/allure-report. Сгенерировать отчет по автотестам, запущенным в браузере Mozilla Firefox можно командой allure generate -c ./firefox/allure-results -o ./firefox/allure-report.
5) Для просмотра allure-отчета об автотестах, выполненных в браузере Google Chrome вызовите команду allure open ./chrome/allure-report. Для просмотра allure-отчета об автотестах, выполненных в браузере Mozilla Firefox вызовите команду allure open ./firefox/allure-report.