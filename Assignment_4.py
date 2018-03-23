import abc


class Singleton(type):
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class Subject(metaclass=Singleton):

    def __init__(self):
        self._observers = set()
        self._bid_price = None
        self._current_bidder = None

    def attach(self, observer):
        observer._subject = self
        self._observers.add(observer)

    def detach(self, observer):
        observer._subject = None
        self._observers.discard(observer)

    def _notify(self):
        for observer in self._observers:
            observer.update(self._bid_price,self._current_bidder)
        print(self._bid_price,self._current_bidder)

    @property
    def bidd_price(self):
        return self._bid_price


    @bidd_price.setter
    def bidd_price(self, arg):
        self._bid_price = arg
        self._notify()

    @property
    def current_bidder(self):
        return self._current_bidder

    @current_bidder.setter
    def current_bidder(self, arg):
        self._current_bidder = arg
        self._notify()


class Observer(metaclass= abc.ABCMeta):

    def __init__(self):
        self._subject = None
        self.cur_bid_price = None
        self._current_bidder = None

    @abc.abstractmethod
    def update(self, arg):
        pass


class ConcreteObserver(Observer):
    """
    Implement the Observer updating interface to keep its state
    consistent with the subject's.
    Store state that should stay consistent with the subject's.
    """

    def update(self, arg1, arg2):
        self.cur_bid_price = arg1
        self._current_bidder = arg2

        # ...


def main():
    subject1 = Subject()
    subject2 = Subject()
    concrete_observer1 = ConcreteObserver()
    concrete_observer2 = ConcreteObserver()
    subject1.attach(concrete_observer1)
    subject2.attach(concrete_observer2)
    subject1.bidd_price = 123
    subject1.current_bidder = "Bidder 1"
    subject2.bidd_price = 223
    subject2.current_bidder = "Bidder 2"


if __name__ == "__main__":
    main()