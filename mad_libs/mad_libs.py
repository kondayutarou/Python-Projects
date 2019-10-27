import os
import logging
import re

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable()


def user_input(type_of_word):
    if type_of_word.endswith("."):
        print(f"Input a word for {type_of_word[0:-1].lower()}")
        while True:
            ui = input("> ")
            if ui.isalpha():
                return ui + "."
            else:
                print("Invalid")
    else:
        print(f"Input a word for {type_of_word.lower()}")
        while True:
            ui = input("> ")
            if ui.isalpha():
                return ui
            else:
                print("Invalid")


def text_handler(script):
    split_result = script.split()
    logging.debug(split_result)
    mad_regex = re.compile(r"(VERB|NOUN|ADJECTIVE|ADVERB)"  # Either one of VERB, NOUN, ADJECTIVE, or ADVERB
                           r"(.)?", re.VERBOSE)  # The word may end with a period or comma
    for index, word in enumerate(split_result):
        if mad_regex.search(word):
            logging.debug(word)
            split_result[index] = user_input(word)
        else:
            continue
    return " ".join(split_result)


if not os.path.exists(r".\base_script\base_script.txt"):
    os.makedirs(r".\base_script")
    open(r".\base_script\script.txt", 'w')
    print("""Mad libs is initialised.
Write into the created script.txt inside base_script folder.""")
else:
    path = os.path.abspath(r".\base_script")
    logging.debug(path)
    os.chdir(path)
    base_file = open('base_script.txt', 'r')
    base_content = base_file.read()
    base_file.close()
    mad_file = open("mad.txt", "w")
    mad_product = text_handler(base_content)
    print(mad_product)
    mad_file.write(mad_product)
    mad_file.close()
