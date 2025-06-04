
import re

def generator_numbers(text: str):
    pattern = r'[-+]?\d+(?:[.,]\d+)?'
    words = filter(lambda x: re.fullmatch(pattern, x), text.split())
    for word in words:
        yield float(word)

def sum_profit(text: str, func: callable):
    # print(func(text))
    return sum(func(text))
    # for i in func(text):
    #     print(i)


def print_generator_numbers():
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers) 
    # print(total_income)
    print(f"Загальний дохід: {total_income}")

if __name__ == '__main__':
    print_generator_numbers()