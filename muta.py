def mutate_string(string, position, character):
    temp_string = list(string)
    temp_string[position] = character
    return ''.join(temp_string)

if __name__ == '__main__':
    input_str = input()
    pos,char = input().split()
    s_new = mutate_string(input_str, int(pos), char)
    print(s_new)
