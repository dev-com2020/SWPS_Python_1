# with open("plik.txt") as f:
#     data = f.read()
from contextlib import contextmanager


class OpenMessage:
    def __enter__(self):
        print("Start")
        return "Hello from context"

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"Błąd {exc_val}")
        return True


with OpenMessage() as msg:
    print(msg)


@contextmanager
def open_mes():
    print("1")
    yield "Hello!"
    print("2")


with open_mes() as msg:
    print(msg)