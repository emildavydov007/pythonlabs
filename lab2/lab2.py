from itertools import product

def count_code_words() -> int:
    
    first_letters = ('X', 'Y', 'Z')
    other_letters = ('A', 'B', 'C', 'D')

    count = 0
    for first in first_letters:
        for rest in product(other_letters, repeat=3):
            count += 1
    return count

def count_twos_base3():
    n = 9**8 + 3**5 - 9
    
    # перевод в 3-ичную систему
    base3 = ''
    while n > 0:
        base3 = str(n % 3) + base3
        n //= 3
    
    return base3.count('2')


def find_numbers():
    result = []
    
    for n in range(40000, 50001):
        m = n
        
        # убираем все двойки
        while m % 2 == 0:
            m //= 2
        
        # считаем делители m
        count = 0
        for i in range(1, int(m**0.5) + 1):
            if m % i == 0:
                count += 1
                if i != m // i:
                    count += 1
        
        if count == 5:
            result.append(n)
    
    return result

print(count_code_words())
print(count_twos_base3())
print(find_numbers())