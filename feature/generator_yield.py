def count_up_to(n: int):
    i = 1
    while i <= n:
        yield i
        i += 1


def read_lines(filename: str):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()


def fetch_all_pages(fetch_page):
    page = 1
    while True:
        data = fetch_page(page)
        if not data:
            break
        yield from data
        page += 1


# for number in count_up_to(5):
#     print(number)


gen = count_up_to(3)
print(next(gen))
print("robię cokolwiek...")
print(next(gen))
