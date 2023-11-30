numbers = int(input("To how many terms do you wish to calculate the row of fibonacci? "))
term1: int = 0
term2: int = 1
maximum = int(numbers) - 2
x: int = 0
antwoord = f'0 1'
if numbers == 1:
    print(
        f'The row of Fibonacci calculated to {numbers} terms goes as follows: 0.')
elif numbers == 2:
    print(
        f'The row of Fibonacci calculated to {numbers} terms goes as follows: 0 1.')
elif numbers == 0:
    print(
        f'I am not gonna calculate that, as that is just an empty row. How about you try calculating it?.')
elif 0 < numbers:
    while x != maximum:
        term3 = term2 + term1
        term1 = term2
        term2 = term3
        antwoord2 = f'{antwoord} {str(term3)}'
        antwoord = antwoord2
        x += 1
    print(
                f'The row of Fibonacci calculated to {numbers} terms goes as follows: {antwoord}.')
elif numbers < 0:
            print(f'Nice try, but a row of fibonacci with negative terms does not exist.')
