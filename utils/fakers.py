from faker import Faker
from string import ascii_letters, digits

fake = Faker()


def random_number(start: int = 100, end: int = 1000) -> int:
    return fake.random.randint(start, end)


def random_string(start: int = 9, end: int = 15) -> str:
    return ''.join(fake.random.choice(ascii_letters + digits) for _ in range(fake.random.randint(start, end)))


def random_list_of_strings(start: int = 9, end: int = 15) -> list[str]:
    return [random_string() for _ in range(fake.random.randint(start, end))]


def random_email() -> str:
    return fake.email()
