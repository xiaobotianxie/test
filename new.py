from io import StringIO
import json
from multiprocessing import pool
import os, time, random

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(std):
        print('%s %s' % (std.__name, std.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

    def set_name(self, name):
        self.__name = name


bart = Student('Bart Simple', 59)

class Animal(object):
    def run(self):
        print('Animal is run')

class Dog(Animal):
    pass
    # def run(self):
    #     print('Dog is run')

class Cat(Animal):
    def run(self):
        print('Cat is run')


# with open('/Users/sibofeng/PycharmProjects/test/file.txt') as f:
    # print(f.read())

# print('Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac:
# pid = os.fork()
# print(pid)
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(5)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')