# Информация

Данная программа позволяет автоматизировать работу Rovio, описав его
действия с помощью простого языка, интерпретируя который, Rovio будет играть 
свою роль в спектакле.

# Установка

В терминале необходимо выполнить команду:

```bash
$ sudo pip2 install git+http://git.robotscityamsterdam.com/git/inn0kenty/rovio.git
```

Система может попросить логин и пароль. Тогда необходимо ввести логин `rca`, 
пароль `SxyVcIZfbklBi5jiUtZO`

# Операторам

После установки, в системе появится программа - rovio, работающая из командной
строки.

Программе при запуске необходимо подсунуть файл с командами, которые
должен выполнить Rovio.

Запустить программу можно следующим образом:

```bash
$ rovio <file_name>
```

где `<file_name>` путь к файлу с командами

## Структура файла с командами

- Каждая команда в файле должна быть на отдельной строке 
- В файле не может быть пустых строк 
- Самая первая команда в файле имеет вид:

    ```
    address xxx.xxx.xxx.xxx
    ```

    где `xxx.xxx.xxx.xxx` - ip адрес Rovio. После этой команды могут быть любые 
    команды, из раздела [Доступные команды](#Доступные команды), 
    в любой последовательности.
- У некоторых команд может быть параметр - время или скорость. Этот параметр 
    отделяется от команды пробелом

## Доступные команды

|Команда|Параметр|Описание|
|:-----:|:------:|:------:|
|forward|время в секундах|движение вперед|
|backward|время в секундах|движение назад|
|straight_left|время в секундах|движение налево|
|straight_right|время в секундах|движение направо|
|rotate_left_by_speed|скорость (от 1 до 10), где 1 - самая быстрая|поворот налево с заданной скоростью|
|rotate_right_by_speed|скорость (от 1 до 10), где 1 - самая быстрая|поворот направо с заданной скоростью|
|diagonal_forward_left|время в секундах|движение по диагонале вперед и налево|
|diagonal_forward_right|время в секундах|движение по диагонале вперед и направо|
|diagonal_backward_left|время в секундах|движение по диагонале назад и налево|
|diagonal_backward_right|время в секундах|движение по диагонале назад и направо|
|head_up|-|поднять голову на максимум|
|head_down|-|опустить голову|
|head_middle|-|переместить голову на центр|
|rotate_left_by_20_degree|-|поворот налево на 20 градусов|
|rotate_right_by_20_degree|-|поворот направо на 20 градусов|
|capture_image|-|снять и показать изображение с камеры|
|wait|время в секундах|подождать заданное колличество секунд|

## Проверка синтаксиса файла с командами

После создания файла с командами, необхдимо его проверить на наличие ошибок. Это
важно, иначе, при работе, Rovio не получит сломанную команду и начнет вести себя
не так, как от него ожидается.

Проверка делается следующим образом:

```bash
$ rovio -t <file_name>
```

Если программа выдаст сообщение `Syntax test OK`, значит с файлом все впорядке и
его можно использовать, иначе программа выдаст сообщене об ошибке и укажет на
какой строке файла она находится.

## Проверка доступности Rovio

Иногда может понадобиться удаленно проверить включен ли Rovio. Для этого можно
воспользоваться командой:

```bash
$ rovio -p <file_name>
```

Если Rovio включен, то вы увидете сообщение `Ping test OK`, а также уровень 
заряда батареи, иначе вы увидите сообщение об ошибке.

NB: В данном случае, в файле с командами может быть только первая строка с
адресом, т.к. остальные команды не выполняются.

## Настройки программы

Файл с настройками программы иеет путь `/etc/rovio/rovio.cfg`. 

Файл содержит следующие параметры:

- open - имя программы через которую будут открываться полученные от Rovio
    изображения (если параметр не указан, то изображения будут открываться 
    через программу open, если она стоит в системе, иначе изображения вообще
    не будут открываться)
- resolution - размер получаемых от Rovio изображений, указывается с помощью
    цифры:
    
    - 0 - размер 176 на 144
    - 1 - размер 352 на 288
    - 2 - размер 320 на 240
    - 3 - размер 640 на 480 (Используется по умолчанию)

## Пример файла с командами

```
address 192.168.1.25 
forward 5
straight_right 5
rotate_right_by_speed 1
capture_image
```

# Проблемы?

Обо всех ошибках и неадекватном поведении, просьба сообщать мне на почту 
`innlebedev@gmail.com`. В теме письма укажите `RCA Rovio`, опишите проблему и
прекрепите файл с командами.
