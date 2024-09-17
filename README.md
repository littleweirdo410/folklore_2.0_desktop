# Фольклор 2.0
![Static Badge](https://img.shields.io/badge/OS-Windows_10%2B-purple) ![GitHub Release](https://img.shields.io/github/v/release/littleweirdo410/folklore_2.0_desktop)
 ![Static Badge](https://img.shields.io/badge/main_language-Python?logo=python&logoSize=auto&labelColor=yellow&color=gray) ![GitHub language count](https://img.shields.io/github/languages/count/littleweirdo410/folklore_2.0_desktop) ![GitHub License](https://img.shields.io/github/license/littleweirdo410/folklore_2.0_desktop) ![Website](https://img.shields.io/website?url=https%3A%2F%2Fmoscowfolklore.ru%2F) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/littleweirdo410/folklore_2.0_desktop)
 
## Назначение приложения

«Фольклор 2.0» -- десктопное приложение для ОС Windows, созданное мной в 2021 году на 3-м курсе бакалавриата в ходе написания курсовой работы на тему [«Русская фольклорная музыкальная традиция в культурном пространстве современной Москвы: формы актуализации (на материалах сетевых источников и СМИ)»](https://disk.yandex.ru/i/fPK9egMKqViYZw). Данная работа была продолжена и расширена в 2022 году, на 4 курсе и послужила источником глав I и II моей бакалаврской выпускной квалификационной работы [«Русская и татарская музыкальная фольклорная традиция в современной Москве: актуализация и репрезентация»](https://disk.yandex.ru/i/x4irhSLIWO_I8Q).

Предназначение приложения -- визуализировать данные о музыкальных фольклорных мероприятиях, проводившихся в рамках городского фестиваля "Московская Масленица" с 2018 по 2020 гг. За 2021 год «Фольклор 2.0» неоднократно демонстрировался как онлайн, так и оффлайн вместо мультимедийной презентации на научных конференциях, где я делилась своими наработками по теме. Статья, обобщающая результаты этого этапа исследования, [вышла в ELibrary](https://www.elibrary.ru/item.asp?id=47213713):

> Гусева, М. А. Репрезентация и восприятие русской фольклорной музыкальной традиции в современной Москве на примере фестиваля «Московская Масленица» / М. А. Гусева // ТЕОРИЯ и ПРАКТИКА СОВРЕМЕННОЙ науки : сборник статей VI Международной научно-практической конференции. В 2 частях, Пенза, 20 ноября 2021 года. Том 1. – Пенза: Наука и Просвещение, 2021. – С. 196-212. – EDN OMQRTT.

Довольно-таки странное название «Фольклор 2.0» пришло мне в голову в готовом виде как-то само собой ещё на этапе возникновения концепта приложения и с тех пор не менялось, став своего рода факультетским брендом.

## Характер собранных данных

Какого характера были данные, собранные при написании курсовой работы, и что конкретно надо было визуализировать?

В первую очередь следует прояснить следующее: **целью** курсовой работы было выявление форм и методов актуализации русской народной музыки в культурном пространстве современной Москвы на примере популярного городского фестиваля «Московская Масленица», который является частью цикла уличных мероприятий «Московские сезоны». Фестиваль проходит в столице с 2017 года и считается действительно массовым по посещаемости среди жителей и гостей Москвы. В силу глубоких исторических корней праздника в ходе мероприятий «Масленицы» активно используется фольклорная составляющая русской культуры, на площадках звучит народная музыка, поэтому лучше образца для изучения в рамках вышеозначенной темы просто не сыскать.

Возможно, наличие авторских терминов слегка затрудняет попытки осмысления содержания предыдущего абзаца, поэтому разберёмся с <ins>терминологией</ins> не отходя от кассы:

**Форма актуализации** -- это образ действия, направленного на повышение известности, узнаваемости и актуальности (отсюда и "актуализация") в обществе нынешнего века традиционной музыки, дошедшей до нас прямиком из седой старины. Таковых может быть бесконечное множество (музыкальный спектакль, фестиваль, концерт, городской праздник, мастер-класс и т.д.), но, как показало исследование, большинство из них, кроме концертов и музыкальных спектаклей, исчезающе редки. Ваша покорная слуга сама в составе фольклорно-этнографического театра МГУ "Братыня" за жизнь принимала участие почти исключительно в этих двух типах мероприятий (а также в трёх мастер-классах по русским народным танцам и гаданиям и в одном масштабном комплексном проекте, включавшем в себя издание [книги-альбома](https://culture.gov.karelia.ru/news/06-09-2023-proekt-russkaya-svadba-zaonezhya/) и [съёмку фильма](https://www.youtube.com/watch?v=5XBe6ZQfoek&t=1s) -- короче, наберёте в поисковике "Денис Князев, Русская свадьба Заонежья", и будет вам счастье. И мой мордент там увидите).

**Методы актуализации**, в свою очередь, -- это не что иное, как совокупность жанровых, культурных, исполнительских и иных особенностей, из которых складывается общее впечатление от мероприятия и которые составляют его непосредственную сущность. Все эти разнообразные оттенки индивидуальной стилистики, присущей каждому исполнителю в частности или приветствуемой организатором площадки в целом, можно условно разделить на три больших зонтичных группы: синтез фольклора с культурными традициями других стран и народов (далее «синтез культурных традиций» или «синтез культур»), синтез фольклора с разными жанрами (далее «синтез жанров») и стремление к аутентичной подаче фольклорного материала, не отходящей далеко от подлинных этнографических записей сельских бабушек и дедушек, последних из могикан, сохранивших в своей памяти истинную традицию (далее «аутентичность»). В итоговой дипломной работе 4 курса "метод актуализации" по научно-методологическим причинам был переименован в "содержание мероприятия, актуализирующего народную культуру", окончательное состояние терминологии вкратце обрисовано [здесь](https://moscowfolklore.ru/site.wsgi/about/) и <a href="#moscow">ниже</a>.

Таким образом, ключевая практическая задача напрямую следовала из цели исследования и применяемой терминологии. Чтобы выявить формы и методы актуализации русской народной музыки на примере "Московской Масленицы", требовалось:

* Собрать информацию обо всех площадках проведения фестиваля за рассматриваемый период (2018-2020 гг.)
* Выяснить, какие из них и когда становились домом для музыкальных фольклорных мероприятий
* Для каждого события на всех задействованных в разные годы площадках посредством изучения состава выступающих и характера мероприятий выписать формы (концерт или музыкальный спектакль -- других, к сожалению, не нашлось) и методы (аутентичность, синтез жанров или синтез культур) актуализации
* Свести всё собранное по крупицам в единую таблицу и проанализировать с количественно-статистической точки зрения, дабы иметь возможность сделать предварительные выводы

Львиная доля информации о количестве **мест проведения** фестиваля «Московская Масленица» была получена благодаря Порталу открытых данных г. Москвы, где был обнаружен набор данных (датасет) с географическими координатами и адресами всех площадок фестиваля за всё время его проведения. В датасете содержится 60 позиций. Основная часть сведений о **формах актуализации** русского музыкального фольклора была почерпнута с официального сайта Департамента культуры г. Москвы, сайта проекта «Московские сезоны» и из местных онлайн-СМИ. Представление же о **методах актуализации** составлялось на основе просмотра видеозаписей выступлений участников фестиваля и их социальных сетей. 

## Выбор фреймворка

Если начинающего Python-разработчика вдруг посещает смелая мысль о создании своего собственного десктопного приложения, как правило, он выбирает из двух доступных опций: **Tkinter** и **PyQt** (вообще-то существует ещё и **Customtkinter**, названый сынок старого доброго Tkinter, в базовых случаях мало чем уступающий PyQt в плане красоты получающегося интерфейса, но в период создания "Фольклора 2.0" я о нём ничего не слышала и своими ручками пока не пробовала). Эти две библиотеки для создания графических пользовательских интерфейсов (GUI, Graphic User Interface) в чём-то сходны по назначению и функционалу, но различий между ними куда больше, поэтому выбирать из них наиболее подходящий необходимо сугубо индивидуально, исходя из потребностей конкретного проекта. **Рассмотрим основные особенности двух братьев-~~акробатьев~~ в деталях:**

<table border="1">
    <thead>
        <tr>
            <th><center>Tkinter</center></th>
            <th><center>PyQT</center></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center" aria-label="Tkinter"> Объектно-ориентированная обёртка поверх инструментария кроссплатформенной библиотеки базовых элементов графического интерфейса Tk (Tk + <i>inter</i>face = Tkinter)</td>
            <td align="center" aria-label="PyQT">Обёртка поверх фреймворка Qt, предназначенного для разработки кроссплатформенного программного обеспечения и изначально написанного на C++</td>
        </tr>
      <tr>
            <td align="center" aria-label="Tkinter">Встроенный компонент большинства дистрибутивов Python</td>
            <td align="center" aria-label="PyQT">Отдельно устанавливаемая библиотека</td>
        </tr>
       <tr>
            <td align="center" aria-label="Tkinter">Прост в освоении</td>
            <td align="center" aria-label="PyQT">Многие знания — многие печали, шире функционал — больше сложностей в освоении</td>
        </tr>
       <tr>
            <td align="center" aria-label="Tkinter">Высокая скорость разработки — голый прототип можно наклепать буквально за вечер</td>
            <td align="center" aria-label="PyQT">Если в деталях работы фреймворка так с кондачка не разобраться, то и времени в разработку придётся вложить побольше</td>
        </tr>
       <tr>
            <td align="center" aria-label="Tkinter">Предоставляет только набор базовых элементов интерфейса</td>
            <td align="center" aria-label="PyQT">Комплексное решение, поддерживающее расширенные возможности для кастомизации виджетов, многопоточность, работу приложения с сетью, интеграцию с устаревшим движком для двухмерной/трёхмерной графики OpenGL (то есть при желании реально наваять целую 3D-игру) — в общем, с помощью PyQt можно сделать действительно всё что угодно, кроме разве что ААА-игр</td>
        </tr>
       <tr>
            <td align="center" aria-label="Tkinter">Дизайн приложения выглядит несколько устаревшим, "любительским"</td>
            <td align="center" aria-label="PyQT">Приложения выглядят более современными, более визуально привлекательными, я бы даже сказала, "профессиональными", что ли; дизайн можно настроить до мельчайших параметров</td>
        </tr>
       <tr>
            <td align="center" aria-label="Tkinter">Предназначен исключительно для десктопных приложений</td>
            <td align="center" aria-label="PyQT">Помимо приложений для персональных компьютеров, подходит также для разработки мобильных приложений</td>
        </tr>
       <tr>
            <td align="center" aria-label="Tkinter">Чем выше размер приложения, тем сильнее проседает производительность</td>
            <td align="center" aria-label="PyQT">Отлично подходит для более громоздких проектов, где требуется высокая производительность</td>
        </tr>
    </tbody>
</table>

Казалось бы, выбор очевиден, ведь PyQt обскакал Tkinter почти по всем параметрам. Однако если подходить к делу с холодной головой, то довольно скоро окажется, что все финтифлюшки PyQt в наших обстоятельствах вовсе ни к чему и ведут лишь к потере времени, переусложнению проекта и чрезмерной плодячке новых сущностей.

Так, среди немногих пунктов в таблице, по которым PyQt с треском проигрывает Tkinter, значится скорость разработки. В условиях, когда приложение является ~~Частью Чего-то Большего~~ побочным продуктом более серьёзной деятельности -- научной, в которую, как бы ни хотелось покодить в своё удовольствие, прямо здесь и прямо сейчас требуется вложить как можно больше времени, высокая скорость разработки становится ключевым преимуществом. Проще говоря, кому интересен блистающий великолепием дизайн, если данные, которые ты хочешь с его помощью визуализировать, обработаны из рук вон плохо? Зачем тратить на что-то глубоко второстепенное те усилия, которые можно было бы перенаправить на доработку основного содержания? Да и вообще -- для чего городить огород, если для моих нужд с лихвой хватит базового решения, простого, как буханка хлеба?

Убедительно? То-то же.

Вот и я подумала, что использование PyQt в качестве фреймворка для разработки GUI не даст мне ничего положительного, кроме чувства морального удовлетворения от того, что я пошла более сложным путём. <ins>Так что мой выбор в итоге вполне закономерно пал на Tkinter.</ins>

#### Функционал приложения

Интерфейс приложения включает в себя:

* интерактивную карту мест проведения музыкальных фольклорных мероприятий в рамках фестиваля «Московская Масленица»;
* легенду карты;
* многоуровневое меню с более подробной информацией о местах проведения, исполнителях и характере мероприятий;
* справку с информацией о создателе;
* возможность обратной связи, предусмотренной в разделе "Опции".

<ins>Интерактивная карта</ins>

Открывается по нажатии кнопки "Открыть карту" в отдельном окне установленного в системе браузера. Для удобства просмотра маркеры на карте кластеризованы автоматическим образом. При наведении курсора на маркер можно прочитать адрес площадки, которую он обозначает. В отдельности от приложения карту можно посмотреть [здесь](https://moscowfolklore.ru/site.wsgi/interactive_map/).

<ins>Легенда карты</ins>

Открывается в отдельном окошке приложения при нажатии одноимённой кнопки. Элементов легенды карты всего 2: **зелёными маркерами** обозначены места, где в рамках фестиваля проводились мероприятия, посвящённые актуализации русского музыкального фольклора, а **оранжевыми маркерами** отмечены точки на карте, где подобные мероприятия не проводились. При нажатии кнопки "Элемент 1 из 2" или "Элемент 2 из 2" в зависимости от текущего состояния окна легенда карты переключается на отображение следующего элемента. Каждый элемент снабжён иллюстрирующим его содержание значком и кратким текстом, раскрывающим его содержание.

<ins>Многоуровневое меню</ins>

Многоуровневое меню даёт возможность познакомиться с обработанными данными поближе и представляет собой своеобразную вертикальную таблицу из 3-х полей со скроллбарами (полосами прокрутки). В первом поле перечислены все адреса мест проведения музыкальных фольклорных мероприятий "Московской Масленицы". Двойной клик левой кнопкой мыши на нужный адрес активирует второе поле, в котором расписано, какие исполнители и коллективы в разные годы выступали на данной площадке. Если напротив какого-либо года стоит прочерк, значит, в этом году фольклорных событий по этому адресу не проходило. Если же напротив года указан тег "Неизвестно", то имеются сведения о том, что мероприятие проводилось, но точной информации о его содержании не сохранилось. Двойной клик на строчку с конкретным годом и исполнителем делает доступным третье поле, где через запятую перечислены форма и метод актуализации сответственно.

<ins>Справка</ins>

Справка открывается в отдельном окошке приложения при нажатии кнопки, расположенной в правом верхнем углу главного окна и изображающей жёлтый кубик со знаками вопроса, нарисованными на его гранях. Содержит краткую сводку информации о проекте, актуальную на момент его создания.

#### Состав проекта и стек технологий

* **Приложение "Фольклор 2.0"**
   * *Текущая версия*: [1.0.1](https://github.com/littleweirdo410/folklore_2.0_desktop/releases/tag/latest)
   * *Операционная система:* Windows 10 (64 bit) и выше
   * *Язык программирования:* Python 3.9
   * *Использованные библиотеки:*
      * <ins>Tkinter 8.6</ins> -- для создания графического интерфейса приложения и связи всех его элементов между собой
      * <ins>Pandas 2.2.2</ins> -- для анализа собранных в ходе исследования неструктурированных данных
      * <ins>Folium 0.12.1</ins> -- для конструирования интерактивной карты
      * <ins>Selenium 4.20.0</ins> -- обычно применяется для автоматизированного тестирования веб-приложений и требует наличия соответствующего веб-драйвера в папке с проектом исполняемого файла. В нашем случае эта библиотека нужна для просмотра интерактивной карты в браузере через интерфейс приложения. Текущая версия "Фольклора 2.0" работает с любыми распространёнными браузерами, основанными на движке Chrome (кроме Яндекс Браузера), установленными в системе. Планируется добавление возможности использовать веб-драйверы для других популярных браузеров (Firefox, Microsoft Edge, Yandex)
      * <ins>Pyinstaller 6.6.0</ins> -- для компиляции Python-проекта в исполняемый файл, пригодный для распространения и запуска на других компьютерах, где в системе не установлен Python
   * *Комплект поставки*: архив, содержащий исполняемый файл ```.exe``` и папку с сопутствующими файлами, необходимыми для его функционирования

#### Расширенная документация и дополнительные материалы

Готовый к использованию дистрибутив приложения, снабжённый кратким руководством пользователя и небольшой видеоинструкцией по применению, прикреплён к репозиторию на Github в разделе [Releases](https://github.com/littleweirdo410/folklore_2.0_desktop/releases/tag/latest).

Также стоит отметить, что значительная часть данного приложения при работе над итоговой выпускной квалификационной работой впоследствии была переупакована в [сайт](https://moscowfolklore.ru/) и вошла в состав его первой части ["Московская Масленица"](https://moscowfolklore.ru/site.wsgi/moscow_maslenitsa/).

Если хочется больше наукообразия, то ещё раз советую заглянуть в саму [курсовую работу](https://disk.yandex.ru/i/fPK9egMKqViYZw). А можно забежать вперёд и ознакомиться с бакалаврской ВКР, в которой примерное представление о сути приложения даёт [глава I](https://disk.yandex.ru/i/x4irhSLIWO_I8Q).
