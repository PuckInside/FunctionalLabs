def CheckingForPattern(string: str, pattern: str):
    if pattern == '':
        return True
    if string == '':
        return True
    
    if '.' == pattern[0]:
        if 1 >= len(pattern):
            return True
        if '.' == pattern[1]:
            return CheckingForPattern(string, pattern[1:])
        if '*' == pattern[1]:
            return False
        if pattern[1] in string:
            index = string.find(pattern[1]) + 1
            return CheckingForPattern(string[index:], pattern[2:])
    elif '*' == pattern[0]:
        return CheckingForPattern(string[1:], pattern[1:])
    elif pattern[0] == string[0]:
        return CheckingForPattern(string[1:], pattern[1:])
    else:
        return False

if CheckingForPattern("Apple", "**ple"):
    print("True")
else:
    print("False")