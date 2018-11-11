"""
 Class SkipObject defines an iterable object that skips every other item
 on iteration. Its iterator object is creating a new form of iterable object to multiple
 active loops
"""


class SkipObjects:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        return SkipIterator(self.wrapped)


class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item


if __name__ == '__main__':
    alpha ='abcdefg'
    skipper = SkipObjects(alpha)
    I = iter(skipper)
    print(next(I), next(I), next(I))

    # for x in skipper:
    #     for y in skipper:
    #         print(x+y, end=' ')



