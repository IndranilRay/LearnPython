"""
Defining and using clock
ver: 1.0
"""
import time
import os


class Clock( object ):
    """
        Use keyword arguments to allow constructors to pass in as
        many arguments as possible to implement constructor overloading in other languages
    """
    def __init__(self, **kw):
        if 'hour' in kw and 'minute' in kw and 'seconds' in kw:
            self._hour = kw['hour']
            self._minute = kw['minute']
            self._seconds = kw['seconds']

        else:
            tm = time.localtime(time.time())
            self._hour = tm.tm_hour
            self._minute = tm.tm_min
            self._seconds = tm.tm_sec

    def run(self):
        self._seconds += 1
        if self._seconds == 60:
            self._seconds = 0
            self._minute += 1
            if self._minute == 60:
                self._minute == 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return "%02d:%02d:%02d" % (self._hour, self._minute,self._seconds)


if __name__ == '__main__':
    clock = Clock()
    while True:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print(clock.show())
        time.sleep(1)
        clock.run()






