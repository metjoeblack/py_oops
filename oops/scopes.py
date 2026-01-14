
X = 1


def nester():
    print(X)                        # 1

    class C:
        print(X)                    # 1

        def method_1(self):
            print(X)                # 1

        def method_2(self):
            X = 3
            print(X)                # 3

    I = C()
    I.method_1()
    I.method_2()


def nester_2():
    X = 2
    print(X)                       # 2

    class C:
        print(X)                   # 2
        def method_1(self):
            print(X)               # 2

        def method_2(self):
            X = 3
            print(X)               # 3

    i = C()
    i.method_1()
    i.method_2()


def nester_3():
    X = 2
    print(X)                       # 2

    class C:
        X = 3
        print(X)                   # 3
        def method_1(self):
            print(X)               # 3 (wrong, actually 2)
            print(self.X)          # 3, inherited class local.

        def method_2(self):
            X = 4
            print(X)               # 4
            self.X = 5
            print(self.X)          # 5

    i = C()
    i.method_1()
    i.method_2()


if __name__ == '__main__':
    print(X)                        # 1
    # nester()
    # nester_2()
    nester_3()








