import re

text = '''This is a test
This is another test
This "big test" is a test
This "big test" is a 'big test'
Almost "this entire" thing "is just a" quote
Suzie Smith-Hopper
Suzie Smith-Hopper is test
Suzie Smith-Hopper is--test
This----is--test
This-----is-test
Don't say anything
I can't think
This' is a 'test
don't tell Suzie Smith-Hopper that I broke Daniel's toy horse
I can't see Suzie Smith-Hopper anywhere; can you
Too long; didn't read
Suzie Smith-Hopper's car was stolen'''

text_1 = '''4 234 452,66 с НДС
4 234 452,66 без НДС
4 234 452.66 с НДС'''


def test_task(expression, example_text):
    regexp = re.compile(expression, re.VERBOSE | re.IGNORECASE)
    for test_string in example_text.split("\n"):
        print(f"Matching against \"{test_string}\"")
        match_objects = regexp.finditer(test_string)
        # print(regexp.findall(test_string))
        for match_obj in match_objects:
            print(match_obj.groupdict())


if __name__ == '__main__':
    with open("regex_test.txt", encoding="utf8") as regex_file:
        test_task(regex_file.read(), text_1)
