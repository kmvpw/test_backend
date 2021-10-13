Тестовое задание Яндекс.Практикум

Задача 1. Даны два списка, нужно вернуть элементы, которые есть в 1-ом списке, но нет во 2-ом. Оценить эффективность своего решения. 
Решение: Использование структуры данных set, найти разницу множеств.
Преобразовать list в set - O(len(list)). 
Опреция вычитания (разница множеств) - O(len(left)) - зависит от длины множества, из которого вычитаем. 
По условиям задачи не указано, в каком виде нужно вернуть результат. Поэтому от дальнеших преобразований отказываемся.
Эффективность решения линейная  - O(max(left, right)).

Задача 2. Дан массив целых чисел. Нужно удалить из него нули. Можно использовать только О(1) дополнительной памяти.
Эффективность O(n). Нули смещаем в конец, при достижении конца списка - делаем срез до индекса, куда перемещали нули.