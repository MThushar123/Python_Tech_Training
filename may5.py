import threading

class Foo:
    def __init__(self):
        self.first_done = threading.Event()
        self.second_done = threading.Event()
        self.lock = threading.Lock()
    
    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.first_done.set()
    
    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.first_done.wait()
        with self.lock:
            printSecond()
            self.second_done.set()
    
    def third(self, printThird: 'Callable[[], None]') -> None:
        self.second_done.wait()
        with self.lock:
            printThird()

def main():
    def print_first(): print("first", end=" ")
    def print_second(): print("second", end=" ")
    def print_third(): print("third")
    
    foo = Foo()
    
    t1 = threading.Thread(target=foo.first, args=(print_first,))
    t2 = threading.Thread(target=foo.second, args=(print_second,))
    t3 = threading.Thread(target=foo.third, args=(print_third,))
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()
    
    print()  # New line

if __name__ == "__main__":
    main()