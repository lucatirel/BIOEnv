class Test():
    def __init__(self, name) -> None:
        self.name = name

if __name__ == "__main__":
    a = Test("aaa")
    b = Test("bbb")
    l = [a,b]
    l.remove(b)
    print(l)
    print(l[0].name)