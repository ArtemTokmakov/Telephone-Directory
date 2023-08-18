# Телефонный справочник 
 
Программа для управления телефонным справочником. Позволяет выводить записи на экран, добавлять новые записи, редактировать существующие записи и выполнять поиск по характеристикам. Записи сохраняются в файл 'contacts.csv'. 
 
## Установка 
 
1. Склонируйте репозиторий или скачайте файлы в ZIP-архиве. 
2. Убедитесь, что у вас установлен Python версии 3.x.  
 
## Использование 
 
1. Запустите программу, выполнив команду  python main.py . 
2. Следуйте инструкциям в меню для выполнения нужных действий. 
 
## Формат записей 
 
Каждая запись в справочнике содержит следующие поля: 
 
- Фамилия 
- Имя 
- Отчество 
- Название организации 
- Рабочий телефон 
- Личный телефон 

## Функционал программы

1. Вывод записей на экран: 
   - Пользователь может выбрать номер страницы и количество записей на странице. 
   - Программа выводит указанное количество записей на выбранной странице. 
 
2. Добавление новой записи: 
   - Пользователь вводит данные для каждого поля новой записи (фамилия, имя, отчество, название организации, рабочий телефон, личный телефон). 
   - Новая запись добавляется в справочник и сохраняется в файл 'contacts.csv'. 
 
3. Редактирование записи: 
   - Пользователь выбирает номер записи, которую хочет отредактировать. 
   - Программа отображает текущую запись и запрашивает новые значения для каждого поля. 
   - Измененная запись сохраняется в справочнике и в файле 'contacts.csv'. 
 
4. Поиск записей: 
   - Пользователь может ввести фамилию, имя и/или название организации для поиска. 
   - Программа выводит все записи, которые соответствуют введенным характеристикам. 
 
5. Завершение программы: 
   - Пользователь может выбрать опцию "Выход" в главном меню, чтобы завершить программу. 
 
Программа также предоставляет возможность загрузки записей из файла 'contacts.csv' при запуске и автоматическое сохранение изменений в справочнике в этот файл. 
 
Весь функционал программы реализован с помощью функций, которые обеспечивают удобное взаимодействие с пользователем и обработку данных. 

## Лицензия 
 
Этот проект лицензирован в соответствии с условиями лицензии [MIT](https://opensource.org/licenses/MIT). 
 
Вы можете свободно использовать, изменять и распространять данный код. 
 
## Автор 
 
Автор этого кода - Токмаков Артём.