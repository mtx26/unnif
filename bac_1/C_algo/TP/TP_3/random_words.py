import random
import string


def random_words():
    chars = string.ascii_letters + string.digits

    while True:
        length = random.randint(1, 20)
        word = ""

        for _ in range(length):
            word += random.choice(chars)

        yield word


def write_random_words(file, generator, amount):
    for _ in range(amount):
        file.write(next(generator) + "\n")


def write_hidden_answer(path, position, value):
    generator = random_words()

    before_count = random.randint(1_000_000, 5_000_000)
    after_count = random.randint(1_000_000, 5_000_000)

    with open(path, "w") as file:
        write_random_words(file, generator, before_count)

        file.write(f"Le trésor est en {position} et vaut {value}.\n")

        write_random_words(file, generator, after_count)


write_hidden_answer("hidden_answer.txt", (3, 7), 678)