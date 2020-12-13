# a = 0
#
# if a == 0:
#
#     print("我是零食中超")
# elif a == 1:
#
#     print("我是哈哈哈")
#
# else:
#     print("我是超")



# import os,sys
#
# print(os.listdir("./"))
#
# print(os.getcwd())
#
import _thread
import logging

from time import sleep,ctime


logging.basicConfig(level=logging.INFO)
#from _thread import

def loop0():

        logging.info("start loop0 at "+ctime())
        sleep(4)
        logging.info("end loop10at"+ctime())




def loop1():

        logging.info("start loop1 at "+ctime())
        sleep(2)
        logging.info("end loop1 at"+ctime())


def main():

        logging.info("start all at "+ctime())

        _thread.start_new_thread(loop0,())
        _thread.start_new_thread(loop1,())

        sleep(6)

        logging.info("end all at"+ctime())




if __name__ == '__main__':
    main()








