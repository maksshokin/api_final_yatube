# Проект yatube_api_final
Данный проект - это проработка навыков работы***DRF*** на примере проекта yatube от Яндекс Пкрактикума.


Проработанное API позволяет запрашивать данные о постах, группах, комментариях в социальной сети Yatube,
а также создавать новые.


Автор: Максим Шокин

# Запуск проекта

 Вам необходимо: 
>1
Клонировать репозиторий: 

git clone https://github.com/maksshokin/api_final_yatube
>2
Перейти в него в командной строке:

cd api_final_yatube
>3
Cоздать и активировать виртуальное окружение:

python -m venv venv

source venv/Scripts/activate
>4
Установить зависимости из файла requirements.txt:

python -m pip install --upgrade pip

pip install -r requirements.txt

>5
Выполнить миграции:

python yatube_api/manage.py migrate
>6
Запустить проект:

python yatube_api/manage.py runserver