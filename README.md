# Regex_Assignment_21002118
DSA -III Assignment related to RegEx using KMP algorithm - Weerasekera I.N(21002118)
<br /><br />

## Instructions
1)First, clone this repository to your local desktop and intsall `Python3` compiler.<br/>
2)Go to the file `test_text.txt` inside the folder [input](https://github.com//inuka007/Regex_Assignment_21002118/tree/main/input) and put a String or Text that you desire.<br/>
3)In the file `test_pattern.txt` inside the folder [input](https://github.com//inuka007/Regex_Assignment_21002118/tree/main/input), write the pattern you want to find in the initial text entered.<br/>
4)Go to `main.py` in the main directory and run the file using your local python 3.10 compiler<br/>
5)Go to the `result.output` in the [output](https://github.com//inuka007/Regex_Assignment_21002118/tree/main/output) folder<br/><br/>
Regular Expression (RegEx) is a sequence of characters that defines a search pattern. The symbols are used as follows where each functionality is explained,<br/>
  •	>   -  ends with<br/>
  •	<   -  starts with<br/>
  •	|    -   or<br/>


You can change this text file name to any name but has to chnage the following code snippet in order to do that in `main.py`.
```python
text = open("input/test_text.txt", 'r')
pattern = open("input/test_pattern.txt", 'r')
result = open("output/result.output", 'w')
```
#
`regex.py` contains the main functions like KMP algorithm and the Pattern finding function. You have to run the `main.py` for the code to execute
<br/><br/>
For the main.py we have to import `regex.py` 
```python
import regex
```
<br /><br />

## Methodology
`Knuth-Morris-Pratt(KMP)` algorithm is used in the program to find regex using straightforward if statements, an algorithm can accomplish this and filter the pattern. Additionally, the appropriate function is called with the matching condition, and a Boolean value of 'true' or 'false' is returned.<br />
Here I am implementing a KMP algorithm using pi function and using that algorithm with the selected patterns the program finds whether they are available or not in the original text.

```python
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
```

In this program, the program recognizes `<` `|` `>` as the regex characters of a vast number of regular expressions.

<br><br>
