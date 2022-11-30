import multiprocessing
from multiprocessing import Process
from datetime import datetime

def calculating(queue):
    while True:
        if queue.empty():
            continue
        number, pow = queue.get()
        result_pow = number ** pow
        nowtime = datetime.now()
        sumnumbers = sum(range(result_pow + 1))
        with open("file.txt", "a", encoding='utf8') as file:
            file.write(str(nowtime) + " >> " + str(number) + " ^ " + str(pow) + " = " + str(result_pow) + ": Сумма числа от нуля до полученного результата возведения в степени = " + str(sumnumbers) + "\n")

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process = Process(target=calculating, args=(queue,))
    process.start()
    while True:
        try:
            input_str = input("Введите число и стпенень через пробел: ")
            if input_str == 'bye':
                break
            print(6)
            num_input, pow_input = (input_str.split(' '))
            print(76)
            num: int = int(num_input)
            pow: int = int(pow_input)
            print(90)
            numtuple : tuple = (num, pow)
            queue.put(numtuple)
        except:
            print("Неправильно введены данные")