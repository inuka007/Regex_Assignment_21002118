def pi_function(String, Pattern, start, pi_array):
    if start > len(String) - len(Pattern):
        return False

    q = 0
    for i in range(len(Pattern)):
        if String[i + start] != Pattern[i]:
            break
        q += 1

    if q == len(Pattern):
        return True

    if q == 0:
        return pi_function(String, Pattern, start + 1, pi_array)

    return pi_function(String, Pattern, start + (q - pi_array[q - 1][1]), pi_array)


def KMP_algorithm(String, Pattern):
    pi = []
    for i in range(len(Pattern) + 1):
        postfix = []
        prefix = []

        sub_string = "".join(Pattern[: i])

        for j in range(1, i):
            prefix.append(sub_string[: j])
            postfix.append(sub_string[i - j:])

        len_max = 0 #longest pre-fix

        for j in range(len(prefix)):
            if prefix[j] in postfix:
                if len(prefix[j]) > len_max:
                    len_max = len(prefix[j])

        if i != 0:
            pi.append([Pattern[i - 1], len_max])

    return pi_function(String, Pattern, 0, pi)


def patternFind(String, Pattern):
    # Regular Expression (RegEx) is a sequence of characters that defines a search pattern.
    #        > - ends with. ex:- inuka> - given string ends with 'inuka'
    #        < - starts with. ex:- <inuka - given string starts with 'inuka'
    #        | - or. ex:- abc|def - given string contains 'abc' or 'def'

    # When it is an "or" relation
    if any(i == '|' for i in Pattern):
        return patternFind(String, Pattern.split('|')[0]) or patternFind(String, Pattern.split('|')[1])

    #When String starts with Pattern and ends with Pattern
    elif Pattern[0] == "<" and Pattern[-1] == ">":
        if KMP_algorithm(String, "".join(Pattern[1: len(Pattern) - 1])) and len(String) == (len(Pattern) - 2):
            return True
        else:
            return False

    # When the String starts with Pattern
    elif Pattern[0] == "<":
        if KMP_algorithm(String[: len(Pattern) - 1], "".join(Pattern[1:])):
            return True
        else:
            return False

    #When String ends with Pattern
    elif Pattern[-1] == ">":
        if KMP_algorithm(String[len(String) - len(Pattern) + 1:], "".join(Pattern[0: len(Pattern) - 1])):
            return True and patternFind(String, "".join(Pattern[:len(Pattern) - 1]))
        else:
            return False

    return KMP_algorithm(String, Pattern)