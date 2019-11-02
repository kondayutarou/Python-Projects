from selenium import webdriver
import logging


def assignee():
    print("""Input any key in the following to designate an assignee:
A: ABLIC Inc. (Seiko Instruments Inc.)
C: Canon Inc.
M: Mitsubishi Electric Corp
R: Rakuten, Inc.
N: No assignee
""")
    ui = input("> ")
    if ui.upper() == "A":
        return 'inassignee:"Seiko Instruments Inc."'
    elif ui.upper() == "C":
        return 'inassignee:"‎Canon Kabushiki Kaisha"'
    elif ui.upper() == "M":
        return 'inassignee:"Mitsubishi Electric Corp"'
    elif ui.upper() == "R":
        return 'inassignee:"Rakuten, Inc."'
    elif ui.upper() == "N":
        return ""


def term():
    print('Input a term to look up: ')
    ui = input("> ")
    return "\"" + ui + "\"" + " "


def patent_search(assign):
    browser.get("https://www.google.co.jp/?tbm=pts")
    # Find a search bar on Google Patents
    search_elem = browser.find_element_by_css_selector(".gLFyf")
    # Prompt a user to input search keys (term and assignee)
    search_elem.send_keys(term() + assign)
    search_elem.submit()
    # TODO: Display a hit number
    # TODO: Click each hit result


assignee = assignee()
browser = webdriver.Firefox(executable_path=r'C:\geckodriver\geckodriver.exe')
# First tab
patent_search(assignee)
# From second tab onwards
while True:
    browser.execute_script('window.open()')
    new_win = browser.window_handles[-1]
    browser.switch_to.window(new_win)
    patent_search(assignee)
