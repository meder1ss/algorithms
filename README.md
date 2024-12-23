# Алгоритмы
# 1. Гистограмма
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Вовочка ломает систему безопасности Пентагона. Для этого ему понадобилось узнать, какие символы в секретных зашифрованных посланиях употребляются чаще других. Для удобства изучения Вовочка хочет получить графическое представление встречаемости символов. Поэтому он хочет построить гистограмму количества символов в сообщении. Гистограмма — это график, в котором каждому символу, встречающемуся в сообщении хотя бы один раз, соответствует столбик, высота которого пропорциональна количеству этих символов в сообщении.

Формат ввода
Входной файл содержит зашифрованный текст сообщения. Он содержит строчные и прописные латинские буквы, цифры, знаки препинания («.», «!», «?», «:», «-», «,», «;», «(», «)»), пробелы и переводы строк. Размер входного файла не превышает 10000 байт. Текст содержит хотя бы один непробельный символ. Все строки входного файла не длиннее 200 символов.Для каждого символа c кроме пробелов и переводов строк выведите столбик из символов «#», количество которых должно быть равно количеству символов c в данном тексте. Под каждым столбиком напишите символ, соответствующий ему. Отформатируйте гистограмму так, чтобы нижние концы столбиков были на одной строке, первая строка и первый столбец были непустыми. Не отделяйте столбики друг от друга. Отсортируйте столбики в порядке увеличения кодов символов.

Формат вывода
Для каждого символа c кроме пробелов и переводов строк выведите столбик из символов «#», количество которых должно быть равно количеству символов c в данном тексте. Под каждым столбиком напишите символ, соответствующий ему. Отформатируйте гистограмму так, чтобы нижние концы столбиков были на одной строке, первая строка и первый столбец были непустыми. Не отделяйте столбики друг от друга. Отсортируйте столбики в порядке увеличения кодов символов.
![image](https://user-images.githubusercontent.com/94699444/224814868-c5aeb9ea-6652-4cee-bec1-ca9d2a94aa61.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/1.py)

# 4. Контрольная работа
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Петя и Вася — одноклассники и лучшие друзья, поэтому они во всём помогают друг другу. Завтра у них контрольная по математике, и учитель подготовил целых K вариантов заданий.

В классе стоит один ряд парт, за каждой из них (кроме, возможно, последней) на контрольной будут сидеть ровно два ученика. Ученики знают, что варианты будут раздаваться строго по порядку: правый относительно учителя ученик первой парты получит вариант 1, левый — вариант 2, правый ученик второй парты получит вариант 3 (если число вариантов больше двух) и т.д. Так как K может быть меньше чем число учеников N, то после варианта K снова выдаётся вариант 1. На последней парте в случае нечётного числа учеников используется только место 1.

Петя самым первым вошёл в класс и сел на своё любимое место. Вася вошёл следом и хочет получить такой же вариант, что и Петя, при этом сидя к нему как можно ближе. То есть между ними должно оказаться как можно меньше парт, а при наличии двух таких мест с равным расстоянием от Пети Вася сядет позади Пети, а не перед ним. Напишите программу, которая подскажет Васе, какой ряд и какое место (справа или слева от учителя) ему следует выбрать. Если же один и тот же вариант Вася с Петей писать не смогут, то выдайте одно число  - 1.

Формат ввода
В первой строке входных данных находится количество учеников в классе 2 ≤ N ≤ 109. Во второй строке — количество подготовленных для контрольной вариантов заданий 2 ≤ K ≤ N. В третьей строке — номер ряда, на который уже сел Петя, в четвёртой — цифра 1, если он сел на правое место, и 2, если на левое.

Формат вывода
Если Вася никак не сможет писать тот же вариант, что и Петя, то выведите  - 1. Если решение существует, то выведите два числа — номер ряда, на который следует сесть Васе, и 1, если ему надо сесть на правое место, или 2, если на левое. Разрешается использовать только первые N мест в порядке раздачи вариантов.
![image](https://user-images.githubusercontent.com/94699444/224815128-f3822324-46b9-493f-8ebd-14c2a6d559fb.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/4.py)

# 5. Хорошая строка
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
На день рождения маленький Ипполит получил долгожданный подарок — набор дощечек с написанными на них буквами латинского алфавита. Теперь-то ему будет чем заняться долгими вечерами, тем более что мама обещала подарить ему в следующем году последовательность целых неотрицательных чисел, если он хорошо освоит этот набор. Ради такого богатства Ипполит готов на многое.

Прямо сейчас юный исследователь полностью поглощён изучением хорошести строк. Хорошестью строки называется количество позиций от 1 до L - 1 (где L — длина строки), таких, что следующая буква в строке является следующей по алфавиту. Например, хорошесть строки "abcdefghijklmnopqrstuvwxyz" равна 25, а строки "abdc" — только 1.

Ипполит размышляет над решением закономерно возникающей задачи: чему равна максимально возможная хорошесть строки, которую можно собрать, используя дощечки из данного набора? Вы-то и поможете ему с ней справиться.

Формат ввода
Первая строка ввода содержит единственное целое число N — количество различных букв в наборе (1 ≤ N ≤ 26). Обратите внимание: в наборе всегда используются N первых букв латинского алфавита.

Следующие N строк содержат целые положительные числа ci — количество букв соответствующего типа (1 ≤ ci ≤ 109). Таким образом, первое число означает количество букв "a", второе число задаёт количество букв "b" и так далее.

Формат вывода
Выведите единственное целое число — максимально возможную хорошесть строки, которую можно собрать из имеющихся дощечек.
![image](https://user-images.githubusercontent.com/94699444/224815265-ccf2c693-91b6-4420-bb95-64b3bfe02036.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/5.py)

# 7. SNTP
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Для того чтобы компьютеры поддерживали актуальное время, они могут обращаться к серверам точного времени SNTP (Simple Network Time Protocol). К сожалению, компьютер не может просто получить время у сервера, потому что информация по сети передаётся не мгновенно: пока сообщение с текущим временем дойдёт до компьютера, оно потеряет свою актуальность. Протокол взаимодействия клиента (компьютера, запрашивающего точное время) и сервера (компьютера, выдающего точное время) выглядит следующим образом:

1. Клиент отправляет запрос на сервер и запоминает время отправления A (по клиентскому времени).

2. Сервер получает запрос в момент времени B (по точному серверному времени) и отправляет клиенту сообщение, содержащее время B.

3. Клиент получает ответ на свой запрос в момент времени C (по клиентскому времени) и запоминает его. Теперь клиент, из предположения, что сетевые задержки при передаче сообщений от клиента серверу и от сервера клиенту одинаковы, может определить и установить себе точное время, используя известные значения A, B, C.

Вам предстоит реализовать алгоритм, с точностью до секунды определяющий точное время для установки на клиенте по известным A, B и C. При необходимости округлите результат до целого числа секунд по правилам арифметики (в меньшую сторону, если дробная часть числа меньше 1/2, иначе в большую сторону).

Возможно, что, пока клиент ожидал ответа, по клиентскому времени успели наступить новые сутки, однако известно, что между отправкой клиентом запроса и получением ответа от сервера прошло менее 24 часов.

Формат ввода
Программа получает на вход три временные метки A, B, C, по одной в каждой строке. Все временные метки представлены в формате «hh:mm:ss», где «hh» – это часы, «mm» – минуты, «ss» – секунды. Часы, минуты и секунды записываются ровно двумя цифрами каждое (возможно, с дополнительными нулями в начале числа).

Формат вывода
Программа должна вывести одну временную метку в формате, описанном во входных данных, – вычисленное точное время для установки на клиенте. В выводе не должно быть пробелов, пустых строк в начале вывода.
![image](https://user-images.githubusercontent.com/94699444/224815390-893b0403-7a77-407c-9f28-eec085480b8c.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/7.py)

# 8. Минимальный прямоугольник
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
На клетчатой плоскости закрашено K клеток. Требуется найти минимальный по площади прямоугольник, со сторонами, параллельными линиям сетки, покрывающий все закрашенные клетки.

Формат ввода
Во входном файле, на первой строке, находится число K (1 ≤ K ≤ 100). На следующих K строках находятся пары чисел Xi и Yi – координаты закрашенных клеток (|Xi|, |Yi| ≤ 109).

Формат вывода
Выведите в выходной файл координаты левого нижнего и правого верхнего углов прямоугольника.
![image](https://user-images.githubusercontent.com/94699444/224815534-3b819d1d-ae68-4ed1-9ced-d29e39368e3c.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/8.py)

# 10. Скучная лекция
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Лёша сидел на лекции. Ему было невероятно скучно. Голос лектора казался таким далеким и незаметным...

Чтобы окончательно не уснуть, он взял листок и написал на нём свое любимое слово. Чуть ниже он повторил своё любимое слово, без первой буквы. Ещё ниже он снова написал своё любимое слово, но в этот раз без двух первых и последней буквы.

Тут ему пришла в голову мысль — времени до конца лекции все равно ещё очень много, почему бы не продолжить выписывать всеми возможными способами это слово без какой-то части с начала и какой-то части с конца?

После лекции Лёша рассказал Максу, как замечательно он скоротал время. Максу стало интересно посчитать, сколько букв каждого вида встречается у Лёши в листочке. Но к сожалению, сам листочек куда-то запропастился.

Макс хорошо знает любимое слово Лёши, а ещё у него не так много свободного времени, как у его друга, так что помогите ему быстро восстановить, сколько раз Лёше пришлось выписать каждую букву.

Формат ввода
На вход подаётся строка, состоящая из строчных латинских букв — любимое слово Лёши.

Длина строки лежит в пределах от 5 до 100 000 символов.

Формат вывода
Для каждой буквы на листочке Лёши, выведите её, а затем через двоеточие и пробел сколько раз она встретилась в выписанных Лёшей словах (см. формат вывода в примерах). Буквы должны следовать в алфавитном порядке. Буквы, не встречающиеся на листочке, выводить не нужно.
![image](https://user-images.githubusercontent.com/94699444/224815662-c92f5aea-7d60-43f0-86bd-4dac8ad0dbdd.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/10.py)

# 11. Стек с защитой от ошибок
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Научитесь пользоваться стандартной структурой данных stack для целых чисел. Напишите программу, содержащую описание стека и моделирующую работу стека, реализовав все указанные здесь методы. Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию. После выполнения каждой команды программа должна вывести одну строчку. Возможные команды для программы:

push n
Добавить в стек число n (значение n задается после команды). Программа должна вывести ok.

pop
Удалить из стека последний элемент. Программа должна вывести его значение.

back
Программа должна вывести значение последнего элемента, не удаляя его из стека.

size
Программа должна вывести количество элементов в стеке.

clear
Программа должна очистить стек и вывести ok.

exit
Программа должна вывести bye и завершить работу.

Перед исполнением операций back и pop программа должна проверять, содержится ли в стеке хотя бы один элемент. Если во входных данных встречается операция back или pop, и при этом стек пуст, то программа должна вместо числового значения вывести строку error.

Формат ввода
Вводятся команды управления стеком, по одной на строке

Формат вывода
Программа должна вывести протокол работы стека, по одному сообщению на строке
![image](https://user-images.githubusercontent.com/94699444/224815819-1eed8244-374d-402c-bd53-32b67d6ca91b.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/11.py)

# 12. Правильная скобочная последовательность
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Рассмотрим последовательность, состоящую из круглых, квадратных и фигурных скобок. Программа дожна определить, является ли данная скобочная последовательность правильной. Пустая последовательность явлется правильной. Если A – правильная, то последовательности (A), [A], {A} – правильные. Если A и B – правильные последовательности, то последовательность AB – правильная.

Формат ввода
В единственной строке записана скобочная последовательность, содержащая не более 100000 скобок.

Формат вывода
Если данная последовательность правильная, то программа должна вывести строку yes, иначе строку no.
![image](https://user-images.githubusercontent.com/94699444/224815941-902d56ce-9711-4141-8635-3667f90bcaf1.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/12.py)

# 13. Постфиксная запись
Ограничение времени	1 секунда
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
В постфиксной записи (или обратной польской записи) операция записывается после двух операндов. Например, сумма двух чисел A и B записывается как A B +. Запись B C + D * обозначает привычное нам (B + C) * D, а запись A B C + D * + означает A + (B + C) * D. Достоинство постфиксной записи в том, что она не требует скобок и дополнительных соглашений о приоритете операторов для своего чтения.
Формат ввода
В единственной строке записано выражение в постфиксной записи, содержащее цифры и операции +, -, *. Цифры и операции разделяются пробелами. В конце строки может быть произвольное количество пробелов.
Формат вывода
Необходимо вывести значение записанного выражения.
![image](https://user-images.githubusercontent.com/94699444/224816032-77bdf343-4eeb-40c4-aa4f-0784458104af.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/13.py)

# 14. Сортировка вагонов lite
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
К тупику со стороны пути 1 (см. рисунок) подъехал поезд. Разрешается отцепить от поезда один или сразу несколько первых вагонов и завезти их в тупик (при желании, можно даже завезти в тупик сразу весь поезд). После этого часть из этих вагонов вывезти в сторону пути 2. После этого можно завезти в тупик еще несколько вагонов и снова часть оказавшихся вагонов вывезти в сторону пути 2. И так далее (так, что каждый вагон может лишь один раз заехать с пути 1 в тупик, а затем один раз выехать из тупика на путь 2). Заезжать в тупик с пути 2 или выезжать из тупика на путь 1 запрещается. Нельзя с пути 1 попасть на путь 2, не заезжая в тупик.
![image](https://user-images.githubusercontent.com/94699444/224816484-2a460507-8049-4a2d-b4ec-61773b01117d.png)
Известно, в каком порядке изначально идут вагоны поезда. Требуется с помощью указанных операций сделать так, чтобы вагоны поезда шли по порядку (сначала первый, потом второй и т.д., считая от головы поезда, едущего по пути 2 в сторону от тупика). Напишите программу, определяющую, можно ли это сделать.

Формат ввода
Вводится число N — количество вагонов в поезде (1 ≤ N ≤ 100). Дальше идут номера вагонов в порядке от головы поезда, едущего по пути 1 в сторону тупика. Вагоны пронумерованы натуральными числами от 1 до N, каждое из которых встречается ровно один раз.

Формат вывода
Если сделать так, чтобы вагоны шли в порядке от 1 до N, считая от головы поезда, когда поезд поедет по пути 2 из тупика, можно, выведите сообщение YES, если это сделать нельзя, выведите NO.
![image](https://user-images.githubusercontent.com/94699444/224816575-fb4277fa-6a38-46be-bd64-d9afc87e5e9b.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/14.py)

# 15. Великое Лайнландское переселение
Ограничение времени	1 секунда
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Лайнландия представляет из себя одномерный мир, являющийся прямой, на котором располагаются N городов, последовательно пронумерованных от 0 до N - 1 . Направление в сторону от первого города к нулевому названо западным, а в обратную — восточным.
Когда в Лайнландии неожиданно начался кризис, все были жители мира стали испытывать глубокое смятение. По всей Лайнландии стали ходить слухи, что на востоке живётся лучше, чем на западе.
Так и началось Великое Лайнландское переселение. Обитатели мира целыми городами отправились на восток, покинув родные улицы, и двигались до тех пор, пока не приходили в город, в котором средняя цена проживания была меньше, чем в родном.

Формат ввода
В первой строке дано одно число N (2≤N≤10^5) — количество городов в Лайнландии. Во второй строке дано N чисел ai (0≤ai≤10^9) — средняя цена проживания в городах с нулевого по (N - 1)-ый соответственно.
Формат вывода
Для каждого города в порядке с нулевого по (N - 1)-ый выведите номер города, в который переселятся его изначальные жители. Если жители города не остановятся в каком-либо другом городе, отправившись в Восточное Бесконечное Ничто, выведите -1 .
![image](https://user-images.githubusercontent.com/94699444/224816918-05a89d8d-44ec-4ae5-8a57-77fe0e303459.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/15.py)

# 16. Очередь с защитой от ошибок
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Научитесь пользоваться стандартной структурой данных queue для целых чисел. Напишите программу, содержащую описание очереди и моделирующую работу очереди, реализовав все указанные здесь методы. 

Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию. После выполнения каждой команды программа должна вывести одну строчку.

Возможные команды для программы:

push n
Добавить в очередь число n (значение n задается после команды). Программа должна вывести ok.

pop
Удалить из очереди первый элемент. Программа должна вывести его значение.

front
Программа должна вывести значение первого элемента, не удаляя его из очереди.

size
Программа должна вывести количество элементов в очереди.

clear
Программа должна очистить очередь и вывести ok.

exit
Программа должна вывести bye и завершить работу.

Перед исполнением операций front и pop программа должна проверять, содержится ли в очереди хотя бы один элемент. Если во входных данных встречается операция front или pop, и при этом очередь пуста, то программа должна вместо числового значения вывести строку error.

Формат ввода
Вводятся команды управления очередью, по одной на строке

Формат вывода
Требуется вывести протокол работы очереди, по одному сообщению на строке
![image](https://user-images.githubusercontent.com/94699444/224817071-6f1abd58-85eb-4b4a-b697-877cb3d3b056.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/16.py)

# 17. Игра в пьяницу
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
В игре в пьяницу карточная колода раздается поровну двум игрокам. Далее они вскрывают по одной верхней карте, и тот, чья карта старше, забирает себе обе вскрытые карты, которые кладутся под низ его колоды. Тот, кто остается без карт – проигрывает. Для простоты будем считать, что все карты различны по номиналу, а также, что самая младшая карта побеждает самую старшую карту ("шестерка берет туза"). Игрок, который забирает себе карты, сначала кладет под низ своей колоды карту первого игрока, затем карту второго игрока (то есть карта второго игрока оказывается внизу колоды). Напишите программу, которая моделирует игру в пьяницу и определяет, кто выигрывает. В игре участвует 10 карт, имеющих значения от 0 до 9, большая карта побеждает меньшую, карта со значением 0 побеждает карту 9.

Формат ввода
Программа получает на вход две строки: первая строка содержит 5 чисел, разделенных пробелами — номера карт первого игрока, вторая – аналогично 5 карт второго игрока. Карты перечислены сверху вниз, то есть каждая строка начинается с той карты, которая будет открыта первой.

Формат вывода
Программа должна определить, кто выигрывает при данной раздаче, и вывести слово first или second, после чего вывести количество ходов, сделанных до выигрыша. Если на протяжении 10^6 ходов игра не заканчивается, программа должна вывести слово botva.
![image](https://user-images.githubusercontent.com/94699444/224817177-1efa25ff-94bd-451d-9f40-2f5257050cd1.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/17.py)

# 18. Дек с защитой от ошибок
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Научитесь пользоваться стандартной структурой данных deque для целых чисел.  Напишите программу, содержащую описание дека и моделирующую работу дека, реализовав все указанные здесь методы. Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию. После выполнения каждой команды программа должна вывести одну строчку.

Возможные команды для программы:

push_front n
Добавить (положить) в начало дека новый элемент. Программа должна вывести ok.

push_back n
Добавить (положить) в конец дека новый элемент. Программа должна вывести ok.

pop_front
Извлечь из дека первый элемент. Программа должна вывести его значение.

pop_back
Извлечь из дека последний элемент. Программа должна вывести его значение.

front
Узнать значение первого элемента (не удаляя его). Программа должна вывести его значение.

back
Узнать значение последнего элемента (не удаляя его). Программа должна вывести его значение.

size
Вывести количество элементов в деке.

clear
Очистить дек (удалить из него все элементы) и вывести ok.

exit
Программа должна вывести bye и завершить работу.

Гарантируется, что количество элементов в деке в любой момент не превосходит 100. Перед исполнением операций pop_front, pop_back, front, back программа должна проверять, содержится ли в деке хотя бы один элемент. Если во входных данных встречается операция pop_front, pop_back, front, back, и при этом дек пуст, то программа должна вместо числового значения вывести строку error.

Формат ввода
Вводятся команды управления деком, по одной на строке.

Формат вывода
Требуется вывести протокол работы дека, по одному сообщению на строке
![image](https://user-images.githubusercontent.com/94699444/224817301-ecb47916-aea6-4a4c-81b1-acc190acdab8.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/18.py)

# 19. Хипуй
Ограничение времени	2 секунды
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
В этой задаче вам необходимо самостоятельно (не используя соответствующие классы и функции стандартной библиотеки) организовать структуру данных Heap для хранения целых чисел, над которой определены следующие операции: a) Insert(k) – добавить в Heap число k ; b) Extract достать из Heap наибольшее число (удалив его при этом).

Формат ввода
В первой строке содержится количество команд N (1 ≤ N ≤ 100000), далее следуют N команд, каждая в своей строке. Команда может иметь формат: “0 <число>” или “1”, обозначающий, соответственно, операции Insert(<число>) и Extract. Гарантируется, что при выполнении команды Extract в структуре находится по крайней мере один элемент.

Формат вывода
Для каждой команды извлечения необходимо отдельной строкой вывести число, полученное при выполнении команды Extract.
![image](https://user-images.githubusercontent.com/94699444/224817395-e973aaf6-876f-4ac6-b8c7-7e1c1e9a9075.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/19.py)

# 20. Пирамидальная сортировка
Ограничение времени	2 секунды
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Отсортируйте данный массив. Используйте пирамидальную сортировку.

Формат ввода
Первая строка входных данных содержит количество элементов в массиве N, N ≤ 105. Далее задаются N целых чисел, не превосходящих по абсолютной величине 109.

Формат вывода
Выведите эти числа в порядке неубывания.
![image](https://user-images.githubusercontent.com/94699444/224817509-0e6a99d9-e3a7-4d4f-98f4-7400803ca793.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/20.py)

# 21. Три единицы подряд
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
По данному числу N определите количество последовательностей из нулей и единиц длины N, в которых никакие три единицы не стоят рядом.

Формат ввода
Во входном файле написано натуральное число N, не превосходящее 35.

Формат вывода
Выведите количество искомых последовательностей. Гарантируется, что ответ не превосходит 231-1.
![image](https://user-images.githubusercontent.com/94699444/224817595-3a72753c-c9a5-4d23-ae5b-446a328ceb9c.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/21.py)

# 22. Кузнечик
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
У одного из студентов в комнате живёт кузнечик, который очень любит прыгать по клетчатой одномерной доске. Длина доски — N клеток. К его сожалению, он умеет прыгать только на 1, 2, …, k клеток вперёд.

Однажды студентам стало интересно, сколькими способами кузнечик может допрыгать из первой клетки до последней. Помогите им ответить на этот вопрос.

Формат ввода
В первой и единственной строке входного файла записано два целых числа — N и k .

Формат вывода
Выведите одно число — количество способов, которыми кузнечик может допрыгать из первой клетки до последней.
![image](https://user-images.githubusercontent.com/94699444/224817738-e295c3c8-118e-4cd1-89d9-01d473adc177.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/22.py)

# 23. Калькулятор
Ограничение времени	2 секунды
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Имеется калькулятор, который выполняет следующие операции:

умножить число X на 2;
умножить число X на 3;
прибавить к числу X единицу.
Определите, какое наименьшее количество операций требуется, чтобы получить из числа 1 число N.

Формат ввода
Во входном файле написано натуральное число N, не превосходящее 106.

Формат вывода
В первой строке выходного файла выведите минимальное количество операций. Во второй строке выведите числа, последовательно получающиеся при выполнении операций. Первое из них должно быть равно 1, а последнее N. Если решений несколько, выведите любое.
![image](https://user-images.githubusercontent.com/94699444/224817818-518909d5-c516-457b-a5cd-621363eb0434.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/23.py)

# 24. Покупка билетов
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
За билетами на премьеру нового мюзикла выстроилась очередь из N человек, каждый из которых хочет купить 1 билет. На всю очередь работала только одна касса, поэтому продажа билетов шла очень медленно, приводя «постояльцев» очереди в отчаяние. Самые сообразительные быстро заметили, что, как правило, несколько билетов в одни руки кассир продаёт быстрее, чем когда эти же билеты продаются по одному. Поэтому они предложили нескольким подряд стоящим людям отдавать деньги первому из них, чтобы он купил билеты на всех.

Однако для борьбы со спекулянтами кассир продавала не более 3-х билетов в одни руки, поэтому договориться таким образом между собой могли лишь 2 или 3 подряд стоящих человека.

Известно, что на продажу i-му человеку из очереди одного билета кассир тратит Ai секунд, на продажу двух билетов — Bi секунд, трех билетов — Ci секунд. Напишите программу, которая подсчитает минимальное время, за которое могли быть обслужены все покупатели.

Обратите внимание, что билеты на группу объединившихся людей всегда покупает первый из них. Также никто в целях ускорения не покупает лишних билетов (то есть билетов, которые никому не нужны).

Формат ввода
На вход программы поступает сначала число N — количество покупателей в очереди (1 ≤ N ≤ 5000). Далее идет N троек натуральных чисел Ai, Bi, Ci. Каждое из этих чисел не превышает 3600. Люди в очереди нумеруются, начиная от кассы.

Формат вывода
Требуется вывести одно число — минимальное время в секундах, за которое могли быть обслужены все покупатели.
![image](https://user-images.githubusercontent.com/94699444/224817915-31afea4c-9abf-4284-afd0-da984d140995.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/24.py)

# 25. Гвоздики
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
В дощечке в один ряд вбиты гвоздики. Любые два гвоздика можно соединить ниточкой. Требуется соединить некоторые пары гвоздиков ниточками так, чтобы к каждому гвоздику была привязана хотя бы одна ниточка, а суммарная длина всех ниточек была минимальна.

Формат ввода
В первой строке входных данных записано число N — количество гвоздиков (2 ≤ N ≤ 100). В следующей строке заданы N чисел — координаты всех гвоздиков (неотрицательные целые числа, не превосходящие 10000).

Формат вывода
Выведите единственное число — минимальную суммарную длину всех ниточек.
![image](https://user-images.githubusercontent.com/94699444/224817997-6b450c8a-d734-45cd-8504-4f3b02f69a6f.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/25.py)

# 26. Самый дешевый путь
Ограничение времени	1 секунда
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
В каждой клетке прямоугольной таблицы N×M записано некоторое число. Изначально игрок находится в левой верхней клетке. За один ход ему разрешается перемещаться в соседнюю клетку либо вправо, либо вниз (влево и вверх перемещаться запрещено). При проходе через клетку с игрока берут столько килограммов еды, какое число записано в этой клетке (еду берут также за первую и последнюю клетки его пути).
Требуется найти минимальный вес еды в килограммах, отдав которую игрок может попасть в правый нижний угол.

Формат ввода
Вводятся два числа N и M — размеры таблицы (1≤N≤20, 1≤M≤20). Затем идет N строк по M чисел в каждой — размеры штрафов в килограммах за прохождение через соответствующие клетки (числа от 0 до 100).
Формат вывода
Выведите минимальный вес еды в килограммах, отдав которую можно попасть в правый нижний угол.
![image](https://user-images.githubusercontent.com/94699444/224818230-6a461464-d9c9-4190-a802-368c9994f456.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/26.py)

# 27. Вывести маршрут максимальной стоимости
Ограничение времени	1 секунда
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
В левом верхнем углу прямоугольной таблицы размером N×M находится черепашка. В каждой клетке таблицы записано некоторое число. Черепашка может перемещаться вправо или вниз, при этом маршрут черепашки заканчивается в правом нижнем углу таблицы.
Подсчитаем сумму чисел, записанных в клетках, через которую проползла черепашка (включая начальную и конечную клетку). Найдите наибольшее возможное значение этой суммы и маршрут, на котором достигается эта сумма.

Формат ввода
В первой строке входных данных записаны два натуральных числа N и M, не превосходящих 100 — размеры таблицы. Далее идет N строк, каждая из которых содержит M чисел, разделенных пробелами — описание таблицы. Все числа в клетках таблицы целые и могут принимать значения от 0 до 100.
Формат вывода
Первая строка выходных данных содержит максимальную возможную сумму, вторая — маршрут, на котором достигается эта сумма. Маршрут выводится в виде последовательности, которая должна содержать N-1 букву D, означающую передвижение вниз и M-1 букву R, означающую передвижение направо. Если таких последовательностей несколько, необходимо вывести ровно одну (любую) из них.
![image](https://user-images.githubusercontent.com/94699444/224818358-8fb1ed0a-4595-4d87-8e9d-ffda5fc88927.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/27.py)

# 28. Ход конём
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Дана прямоугольная доска N × M (N строк и M столбцов). В левом верхнем углу находится шахматный конь, которого необходимо переместить в правый нижний угол доски. В данной задаче конь может перемещаться на две клетки вниз и одну клетку вправо или на одну клетку вниз и две клетки вправо.

Необходимо определить, сколько существует различных маршрутов, ведущих из левого верхнего в правый нижний угол.

Формат ввода
Входной файл содержит два натуральных числа N и M , .

Формат вывода
В выходной файл выведите единственное число — количество способов добраться конём до правого нижнего угла доски.
![image](https://user-images.githubusercontent.com/94699444/224818439-8809a0e9-e783-44d5-b378-e8e42d6392b5.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/28.py)

# 29. Кафе
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Около Петиного университета недавно открылось новое кафе, в котором действует следующая система скидок: при каждой покупке более чем на 100 рублей покупатель получает купон, дающий право на один бесплатный обед (при покупке на сумму 100 рублей и меньше такой купон покупатель не получает).

Однажды Пете на глаза попался прейскурант на ближайшие N дней. Внимательно его изучив, он решил, что будет обедать в этом кафе все N дней, причем каждый день он будет покупать в кафе ровно один обед. Однако стипендия у Пети небольшая, и поэтому он хочет по максимуму использовать предоставляемую систему скидок так, чтобы его суммарные затраты были минимальны. Требуется найти минимально возможную суммарную стоимость обедов и номера дней, в которые Пете следует воспользоваться купонами.

Формат ввода
В первой строке входного файла записано целое число N (0 ≤ N ≤ 100). В каждой из последующих N строк записано одно целое число, обозначающее стоимость обеда в рублях на соответствующий день. Стоимость — неотрицательное целое число, не превосходящее 300.

Формат вывода
В первой строке выдайте минимальную возможную суммарную стоимость обедов. Во второй строке выдайте два числа K1 и K2 — количество купонов, которые останутся неиспользованными у Пети после этих N дней и количество использованных им купонов соответственно.

В последующих K2 строках выдайте в возрастающем порядке номера дней, когда Пете следует воспользоваться купонами. Если существует несколько решений с минимальной суммарной стоимостью, то выдайте то из них, в котором значение K1 максимально (на случай, если Петя когда-нибудь ещё решит заглянуть в это кафе). Если таких решений несколько, выведите любое из них.
![image](https://user-images.githubusercontent.com/94699444/224818517-1144d32d-0016-47f1-a49e-3c700733710b.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/29.py)

# 30. НОП с восстановлением ответа
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Даны две последовательности, требуется найти и вывести их наибольшую общую подпоследовательность.

Формат ввода
В первой строке входных данных содержится число N – длина первой последовательности (1 ≤ N ≤ 1000). Во второй строке заданы члены первой последовательности (через пробел) – целые числа, не превосходящие 10000 по модулю.

В третьей строке записано число M – длина второй последовательности (1 ≤ M ≤ 1000). В четвертой строке задаются члены второй последовательности (через пробел) – целые числа, не превосходящие 10000 по модулю.

Формат вывода
Требуется вывести наибольшую общую подпоследовательность данных последовательностей, через пробел.
![image](https://user-images.githubusercontent.com/94699444/224818614-84c3abdf-2dc1-486f-a541-5bbe8f7eaade.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/30.py)

# 36. Длина кратчайшего пути
Все языки	Python 3.6
Ограничение времени	1 секунда	5 секунд
Ограничение памяти	64Mb	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
В неориентированном графе требуется найти длину минимального пути между двумя вершинами.

Формат ввода
Первым на вход поступает число N – количество вершин в графе (1 ≤ N ≤ 100). Затем записана матрица смежности (0 обозначает отсутствие ребра, 1 – наличие ребра). Далее задаются номера двух вершин – начальной и конечной.

Формат вывода
Выведите L – длину кратчайшего пути (количество ребер, которые нужно пройти).

Если пути нет, нужно вывести -1.
![image](https://user-images.githubusercontent.com/94699444/224818745-20948846-ba28-415f-9e0e-56c507f30bf2.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/36.py)

# 37. Путь в графе
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
В неориентированном графе требуется найти минимальный путь между двумя вершинами.

Формат ввода
Первым на вход поступает число N – количество вершин в графе (1 ≤ N ≤ 100). Затем записана матрица смежности (0 обозначает отсутствие ребра, 1 – наличие ребра). Далее задаются номера двух вершин – начальной и конечной.

Формат вывода
Выведите сначала L – длину кратчайшего пути (количество ребер, которые нужно пройти), а потом сам путь. Если путь имеет длину 0, то его выводить не нужно, достаточно вывести длину.

Необходимо вывести путь (номера всех вершин в правильном порядке). Если пути нет, нужно вывести -1.
![image](https://user-images.githubusercontent.com/94699444/224818822-5ae3d1e5-1b06-4b16-b862-4890f4d9a412.png)
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/37.py)

# 38. Аквариумы
Ограничение времени	1 секунда
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
В аквазоне требуется заселить n последовательно пронумерованных аквариумов. «Расстояние» между аквариумами определяется как разность их номеров.
Продаются k видов рыб, привлекательность для посетителей рыбки i-го вида — ci.
Рыбы одного вида конфликтуют настолько, что они должны находится в аквариумах на расстоянии как минимум k друг от друга. Требуется заселить все аквариумы так, чтобы избежать конфликтов между рыбками, при этом суммарная привлекательность аквазоны должны быть наибольшей.

Формат ввода
В первой строке находятся два числа k(1≤k≤5) и n(1≤n≤10^5).
В следующей строке следуют k чисел ci(1≤ci≤10^5).

Формат вывода
В единственной строке выведите ответ на задачу.
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/38.py)

# 39. Настольная игра
# ![Решение](https://github.com/meder1ss/algorithms/blob/main/39.py)
