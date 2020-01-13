#ABC
#BCD
#CDC
#DCD
#CDC
#0:3
#1:4
#2:5

def count_substring(string, sub_string):
     length = len(sub_string)
     count = 0
     for i in range(0,len(string)):
        if string[i:length] == len(sub_string):
            break
        if string[i:length] == sub_string:
            count += 1
        length += 1

     return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
