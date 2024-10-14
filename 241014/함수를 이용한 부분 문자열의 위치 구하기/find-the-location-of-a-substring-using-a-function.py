str1 = input()
str2 = input()

def get_index(string, target):
    th = False
    index = -1
    for i in range(len(string)-len(target)+1):
        for j in range(len(target)):
            if string[i + j] != target[j]:
                th = False
                index = -1
                break
            else:
                th = True
                if index == -1:
                    index = i
        if th and index != -1:
            return index
    return index

print(get_index(str1, str2))