#!/usr/bin/python3
#zadanie na 4
from typing import Tuple

TABLE_OF_STATES = {
    0: {'1': 1, '2': 2, '5': 5, 'A': 0},
    1: {'1': 2, '2': 3, '5': 6, 'A': 1},
    2: {'1': 3, '2': 4, '5': 7, 'A': 2},
    3: {'1': 4, '2': 5, '5': 8, 'A': 3},
    4: {'1': 5, '2': 6, '5': 9, 'A': 4},
    5: {'1': 6, '2': 7, '5': 10, 'A': 5},
    6: {'1': 7, '2': 8, '5': 11, 'A': 6},
    7: {'1': 8, '2': 9, '5': 12, 'A': 7},
    8: {'1': 9, '2': 10, '5': 12, 'A': 8},
    9: {'1': 10, '2': 11, '5': 12, 'A': 13},
    10: {'1': 11, '2': 12, '5': 12, 'A': 13},
    11: {'1': 12, '2': 12, '5': 12, 'A': 13},
    12: {'1': 12, '2': 12, '5': 12, 'A': 13},
    13: {'1': 13, '2': 13, '5': 13, 'A': 13},
}
ALPHABET = ['1', '2', '5', 'A']
ACCEPTING_STATE = 13

def transaction(input: str, actual_state: int, total_amount: int) -> Tuple[int, bool, int]:

    if input not in ALPHABET:
        print("Wprowadzone monety nie rozpoznane...")
        return actual_state, False, total_amount
    
    if input is not 'A':
        total_amount += int(input)
    state = TABLE_OF_STATES[actual_state][input]
    print("Aktualny stan automatu: ", 'q' + str(state))
    print("Aktualna wartosc wrzuconych pieniedzy:", total_amount)
    is_accepting: bool = False
    if state is ACCEPTING_STATE:
        is_accepting = True
    
    return state, is_accepting, total_amount

def main():
    print('''\tAutomat przyjmuje monety o nominalach 1, 2, 5. Prosze wkladac monety osobno...
        Cennik: bilet na basen - 9zl; bilet na basen z saunami - 12zl
        Gdy wartosc wyrzuconych pieniedzy bedzie wieksza niz 9 prosze wcisnac przycisk A w celu wydania biletu''')
    actual_status: int = 0
    is_accepting = False
    total_amount: int = 0
    history = [0]
    print("Aktualny stan:  q0")
    while is_accepting is False:
        input1 = str(input("Włóż monetę: "))
        actual_status, is_accepting, total_amount = transaction(input1, actual_status, total_amount)
        history.append(actual_status)
    if total_amount >= 12:
        print('Wydawanie biletu na basen z sauna...')
        print("Zwracanie reszty:", total_amount - 12)
    else:
        print('Wydawanie biletu na basen...')
        print("Zwracanie reszty:", total_amount - 9)
    print("Koncowy stan", history[-1])
    print("Lista stanow:", history)


if __name__ == "__main__":
    main()