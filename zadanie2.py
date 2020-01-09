#!/usr/bin/python3
from typing import List

TABLE_OF_STATES = {
    0: {'0': {0, 1}, '1': {0, 2}, '2': {0, 3}, '3': {0, 4}, '4': {0, 4}},
    1: {'0': 6},
    2: {'1': 6},
    3: {'2': 6},
    4: {'3': 6},
    5: {'4': 6},
    6: {'0': 6, '1': 6, '2': 6, '3': 6, '4': 6}
}
ALPHABET = ['0', '1', '2', '3', '4']
ACCEPTING_STATE = 6

def transaction(input: str, current_state: int) -> bool: #dziala na podstawie rekurencji
    print("Aktualny stan: ", 'q' + str(current_state)) #dlatego wypisywane stringi są od tyłu
    if input is "": 
        return current_state is ACCEPTING_STATE

    single_sign = input[0]
    if single_sign in TABLE_OF_STATES[current_state].keys():
        possible_states = TABLE_OF_STATES[current_state][single_sign]
        if isinstance(possible_states, int):
            possible_states = [possible_states]
    else:
        return False

    for state in possible_states:
        rest_of_string = input[1:]
        if transaction(rest_of_string, state):
            return True

    return False


def main():
    fileName: str = 'dane.txt'
    inputed_strings: List[str] = [line.rstrip('\n').split('#') for line in open(fileName)]
    print("Wprowadzone przyklady: ", inputed_strings)
    for i in inputed_strings:
        for j in i:
            print("Sprawdzam ciag", j)
            current_state = 0
            is_repeted: bool = transaction(j, current_state)
            if is_repeted:
                print("Dla ciągu", j, "występuje powtorzenie!")
            else:
                print("Dla ciągu", j, "nie występuje powtorzenie!")

if __name__ == "__main__":
    main()