# Optimised for mail address
import os
import re
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable()


def user_regex():
    print("Input a RegEx that you want to find.")
    print("Suggested regex for mail address search: ^(.* )?(.*)(@.*.)(com|net)$")
    regex = input("> ")
    # Set condition for a regex string input by a user.
    if len(regex) > 0:
        regex = re.compile(regex)
        return regex
    else:
        print("Invalid")


def regex_search():
    txt_regex = re.compile(r"^(.*)(.txt)$")
    ur = user_regex()
    # Make a list of the current working folder.
    for item in os.listdir(os.getcwd()):
        # Select only a file that ends with .txt extension.
        if os.path.isfile(os.path.join(os.getcwd(), item)) and txt_regex.search(item):
            # Initialise result of user-input regex search result from a text file.
            rs_hits = []
            logging.debug(txt_regex.search(item).group(0))
            # Display a file from which user-input regex is searched.
            print(f"From {os.path.join(os.getcwd(), item)}:")
            text_file = open(os.path.join(os.getcwd(), item), "r")
            contents = text_file.readlines()
            logging.debug(contents)
            for content in contents:
                if ur.search(content):
                    reconstructed_search_result = "".join((ur.search(content).group(2, 3, 4)))
                    rs_hits.append(reconstructed_search_result)
            for hit in rs_hits:
                print(hit)


regex_search()
