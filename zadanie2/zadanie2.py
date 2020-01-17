#!/usr/bin/python3
#zadanie na 4
from typing import List

TABLE_OF_STATES = {
    0: {'0': {0, 1}, '1': {0, 2}, '2': {0, 3}, '3': {0, 4}, '4': {0, 5}, 'a': {0, 7}, 'b': {0, 8}, 'c': {0, 9}, 'd': {0, 10}, 'e': {0, 11}},
    1: {'0': 6},
    2: {'1': 6},
    3: {'2': 6},
    4: {'3': 6},
    5: {'4': 6},
    6: {'0': 6, '1': 6, '2': 6, '3': 6, '4': 6},
    7: {'a': 12},
    8: {'b': 12},
    9: {'c': 12},
    10: {'d': 12},
    11: {'e': 12},
    12: {'a': 12, 'b': 12, 'c': 12, 'd': 12, 'e': 12}
}
ALPHABET = ['0', '1', '2', '3', '4', 'a', 'b', 'c', 'd', 'e']
ACCEPTING_STATE = [6, 12]
history: List[int] = []

def transaction(input: str, current_state: int): #dziala na podstawie rekurencji
    global history
    print("Aktualny stan: ", 'q' + str(current_state)) #dlatego wypisywane stringi są od tyłu
    if current_state in ACCEPTING_STATE:
        if current_state is ACCEPTING_STATE[0]:
            print("Powtorzenie wystapilo posrod cyfr:", list(TABLE_OF_STATES[history[-2]])[0])
        else:
            print("Powtorzenie wystapilo posrod liter:", list(TABLE_OF_STATES[history[-2]])[0])
        return
    if input == "":
        return

    single_sign = input[0]
    if single_sign in TABLE_OF_STATES[current_state].keys():
        possible_states = TABLE_OF_STATES[current_state][single_sign]
        if isinstance(possible_states, int):
            possible_states = [possible_states]    

        for state in possible_states:
            history.append(state)
            rest_of_string = input[1:]
            transaction(rest_of_string, state)

            
def main():
    global history
    fileName: str = 'dane.txt'
    inputed_strings: List[str] = [line.rstrip('\n').split('#') for line in open(fileName)] #dane można wprowadzac w nowych linijka oraz po znaku '#' - jak kto woli
    print("Wprowadzone przyklady: ", inputed_strings)
    for i in inputed_strings:
        for j in i:
            print("\nSprawdzam ciag", j)
            history = [0]
            current_state = 0
            transaction(j, current_state)
            print("Koncowy stan", history[-1])
            print("Lista stanow:", history)

if __name__ == "__main__":
    main()