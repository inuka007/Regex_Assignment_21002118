#created file for regular expression
import regex

if __name__ == '__main__':
    #accessing files
    text = open("input/test_text.txt", 'r')
    pattern = open("input/test_pattern.txt", 'r')
    result = open("output/result.output", 'w')

    String = text.readline().strip()
    Pattern = pattern.readline().strip()

    #using the regex.py for the string and pattern to write the output file
    result.writelines(str(regex.patternFind(String, Pattern)))

    #closing files
    text.close()
    pattern.close()
    result.close()