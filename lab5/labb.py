def line_generator(file_path, max_len):
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            for i in range(0, len(line), max_len):
                yield line[i:i + max_len]

def reverse_words(s):
    words = s.split()
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    return ' '.join(reversed_words)

def process_file(file_path, max_len):
    gen = line_generator(file_path, max_len)
    result = map(reverse_words, gen)
    return result

# Создание файла
with open('laba5.txt', 'w', encoding='utf-8') as f:
    f.write("Hello world\n")
    f.write("This is a test file\n")

# запуск
result = process_file('laba5.txt', 10)
for line in result:
    print(line)
