class StepperIndex:
    def __getitem__(self, i):
        return self.data[i]


if __name__ == '__main__':
    X = StepperIndex()
    X.data = 'Spam'
    print(X[0])

    # Any class that support for loops automatically support all iteration contexts
    for item in X:
        print(item, end='')
    print([item*2 for item in X])
    print(list(map(str.upper, X)))
    (a, b, c, d) = X

