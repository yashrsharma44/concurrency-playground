from threading import Thread
import random
import time

# Global Variable which is shared among the 2 threads
rand_int = 0


def update():
    global rand_int
