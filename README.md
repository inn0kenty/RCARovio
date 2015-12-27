# Информация

Данная программа позволяет автоматизировать работу Rovio, описыв его
действия с помощью простого языка. Интерпретируя который, Rovio будет играть свою роль в спектакле.

# Установка

```bash
$ pip install git+http://git.robotscityamsterdam.com/git/inn0kenty/rovio.git
```

# Операторам

После установки в системе появится программа - rovio, работающая из командной
строки.

Программе при запуске необходимо подсунуть файл с командами, которые
должен выполнить Rovio.

Запустить программу можно следующим образом:

```bash
$ rovio <file_name>
```

где `<file_name>` путь к файлу с командами

## Структура файла с командами

 - Каждая команда в файле должна быть на новой строке 
 - В файле не может быть пустых строк 
 - Самая первая команда в файле имеет вид:

   ```
   address xxx.xxx.xxx.xxx
   ```

   где `xxx.xxx.xxx.xxx` - ip адрес Rovio. После этой команды могут быть любые
   команды, из раздела [Доступные команды](#Доступные команды), в любой последовательности.
 - У некоторых команд может быть параметр - время или скорость. Этот параметр отделяется от команды пробелом

## Доступные команды

|Команда|Параметр|Описание|
|:-----:|:------:|:------:|
|forward|время в секундах|движение вперед|
|backward|время в секундах|движение назад|
|straight_left|время в секундах|движение|
|straight_right|время в секундах|движение|
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

Если программа выдаст сообщение 'Syntax test OK', значит с файлом все впорядке и
его можно использовать, иначе программа выдаст сообщене об ошибке и укажет на
какой строке файла она находится.

## Проверка доступности Rovio

Иногда может понадобиться удаленно проверить включен ли Rovio. Для этого можно
воспользоваться командой:

```bash
$ rovio -p <file_name>
```

Если Rovio включен, то вы увидете сообщение об успешном пинге и уровень
батареи, иначе вы увидите сообщение об ошибке.
NB: В данном случае, в файле с командами может быть только первая строка с
адресом, т.к. остальные команды не выполняются.

## Настройки программы
Файл с настройками программы иеет путь `/etc/rovio/rovio.cfg`. Файл содержит
следующие параметры:
 - open - имя программы через которую будут открываться полученные от Rovio
     изображения (по умолчанию - open)
 - resolution - размер получаемых от Rovio изображений, указывается с помощью
     цифры:
     - 0 - {176, 144}
     - 1 - {352, 288}
     - 2 - {320, 240}
     - 3 - {640, 480} (По умолчанию)


# Разработчикам
