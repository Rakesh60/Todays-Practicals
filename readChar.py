def count_characters(file_name):
    char_count = {}
    with open(file_name, 'r') as file:
        for line in file:
            for char in line:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
    return char_count

print(count_characters('file.txt'))
