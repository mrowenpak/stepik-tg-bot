def say_test(number: int, word : str) -> str:
    word = word.capitalize()
    return word*number

print(say_test(2, 'hello '))