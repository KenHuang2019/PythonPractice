def is_isogram(string):
    lower_string = string.lower()
    nonspace_string = lower_string.replace(' ', '')
    index = []
    for char in nonspace_string:
        new_index = nonspace_string.find(char)
        if (new_index in index) == True:
            return False
        index.append(new_index)
    return True


def is_isogram_best(string):
    return len(string) == len(set(string.lower()))

if __name__ == 'is_isogram':
    is_isogram()
if __name__ == 'is_isogram_best':
    is_isogram_best()
