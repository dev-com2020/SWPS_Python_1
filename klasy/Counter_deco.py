class Counter_deko:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"wywołano {self.count} raz/y")
        return self.func(*args, **kwargs)

@Counter_deko
def powitanie():
    print("Siemka!")

powitanie()
powitanie()
