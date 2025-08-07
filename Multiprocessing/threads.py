import datetime
import random
import threading
import time

# Створіть два потоки. Один потік має вивести "Привіт!" 3 рази з інтервалом 0.5 секунди,
# інший - "Бувай!" 2 рази з інтервалом 0.8 секунди.
# def say_word(word, number_of_time, interval):
#     for _ in range(number_of_time):
#         print(word)
#         time.sleep(interval)
#
#
# thread_1 = threading.Thread(target=say_word, args=("Hello!", 4, 1.5))
# thread_2 = threading.Thread(target=say_word, args=("Bye!", 6, 0.7))
#
# thread_1.start()
# thread_2.start()
# thread_1.join()
# thread_2.join()

# def fetch_url(url):
#     print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Start downloading data from {url}")
#     time.sleep(random.uniform(0.5, 2.5))
#     data = f"Data from {url}"
#     print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] End downloading data from {url}")
#
#     return data
#
# urls = [
#     "http://example.com/page1",
#     "http://example.com/page2",
#     "http://example.com/page3",
#     "http://example.com/page4",
# ]
#
# start = time.perf_counter()
# threads_io = []
# for url in urls:
#     thread = threading.Thread(target=fetch_url, args=(url,))
#     thread.start()
#     threads_io.append(thread)
#
# for thread in threads_io:
#     thread.join()
#
# end = time.perf_counter()

# Імітуйте "завантаження" 5 файлів з різними випадковими затримками (від 0.1 до 1.0 секунди)
# за допомогою потоків.
# Виведіть повідомлення про початок та завершення завантаження кожного файлу.

files = [
    "screen_1",
    "screen_2",
    "screen_3",
    "screen_4",
    "screen_5"
]

semaphore = threading.Semaphore(2)

def fetch_f(file):
    with semaphore:
        print(f" Start downloading file {file}")
        time.sleep(random.uniform(0.1, 1.0))
        # data = f"Data from {url}"
        print(f" End downloading file {file}")

thread_io = []
for file in files:
    thread = threading.Thread(target=fetch_f, args=(file,))
    thread.start()
    thread_io.append(thread)

for thread in thread_io:
    thread.join()

# Уявіть, що у вас є спільний список `shared_list`, до якого кілька потоків додають елементи. Виправте стан гонки, щоб усі елементи були додані коректно.