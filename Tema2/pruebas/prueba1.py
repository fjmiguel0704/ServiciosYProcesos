from multiprocessing import *

def hello (name):
    print("hello world", name)

if __name__ == "__main__":
    p = Process(target=hello, args=("Fernando",))
    p.start()
    p.join()
    print ("Fin main")