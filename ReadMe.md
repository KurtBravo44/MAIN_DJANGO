Проект "django_main"

Для локального развёртывания проекта необходимо произвести следующие настройки:

- Для того, чтобы работало кэширование, необходимо установить коннект с redis.
     Пример в оболочке PowerShell: wsl; redis-cli
     Дожна появиться строка: 127.0.0.1:6379
  (Из закешированных данных: количество уникальные клиентов "Подписчики рассылки")


- В проекте находится файл .env.example
    Создайте файл .env и пропишите все недостающие доступы, которые указаны в файле "примере"

    ВАЖНО!!!!!
    (В качестве инструментра отправки почтовых писем используется пакет SMTPLib. Хост:Mail.ru)

ЛОГИКА ПРОЕКТА:

Проект подразумевает наличие 4 доступов:
-Админские права
-Права Модератора
-Права контент Менеджера
-Клиентские права

Для того, чтобы получить доступ к админке, пропишите: python manage.py csu или python3 manage.py csu

При регистрации пользователя, ему необходимо активировать почту. Письмо с подтверждением отправляется на контактный email.

-Модератор регистрируется и автоматически получает права, если в его почте есть стока "manager", также получает сразу активацию аккаунта
-Контент Менеджер регистрируется и автоматически получает права, если в его почте есть строка "sky.pro", также получает сразу активацию аккаунта
-Клиент регистрируется и ему необходимо активировать аккаунт с помощью высланного письма.





