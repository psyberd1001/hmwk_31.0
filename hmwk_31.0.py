import threading
import time
from time import sleep


def func_1():
    for i in range(10):
        time.sleep(1)
        print(i, threading.current_thread())


def func_2():
    for i in range(10):
        time.sleep(1)
        print(i, threading.current_thread())


def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as fl_1:
        started_at = time.time()
        for i in range(word_count):
            fl_1.write(f'Какое-то слово №{i}\n')
            sleep(0.1)

        ending_at = time.time()
        result = ending_at - started_at
        print(f'Завершилась запись в файл - {file_name}. Затраченное время - {round(result, 4)}')


thread = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread.start()
thread.join()
thread_1 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread_1.start()

thread_2 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread_2.start()

thread_3 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread_3.start()
print(thread.is_alive())

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
