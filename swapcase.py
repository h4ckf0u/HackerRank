def swap_case(s):
    swap_string = ''
    for ch in s:
        if ch.isupper():
            swap_string += ch.lower()
        else:
            swap_string += ch.upper()
    return swap_string

if __name__ == '__main__':
    input_String = input()
    print(swap_case(input_String))
