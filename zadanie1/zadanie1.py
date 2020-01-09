#!/usr/bin/python3
from typing import Tuple

TABLE_OF_STATES = {
    0: {'1': 1, '2': 2, '5': 5},
    1: {'1': 2, '2': 3, '5': 6},
    2: {'1': 3, '2': 4, '5': 7},
    3: {'1': 4, '2': 5, '5': 8},
    4: {'1': 5, '2': 6, '5': 9},
    5: {'1': 6, '2': 7, '5': 9},
    6: {'1': 7, '2': 8, '5': 9},
    7: {'1': 8, '2': 9, '5': 9},
    8: {'1': 9, '2': 9, '5': 9},
    9: {'1': 9, '2': 9, '5': 9}
}
ALPHABET = ['1', '2', '5']
ACCEPTING_STATE = 9

def transaction(input: str, actual_state: int, total_amount: int) -> Tuple[int, bool, int]:

    if input not in ALPHABET:
        print("Wprowadzone monety nie rozpoznane...")
        return actual_state, False, total_amount
    
    total_amount += int(input)
    state = TABLE_OF_STATES[actual_state][input]
    print("Aktualny stan: ", 'q' + str(state))
    is_accepting: bool = False
    if state is ACCEPTING_STATE:
        is_accepting = True
    
    return state, is_accepting, total_amount

def main():
    print("Automat przyjmuje monety o nominalach 1, 2, 5. Prosze wkladac monety osobno...")
    actual_status: int = 0
    is_accepting = False
    total_amount: int = 0
    history = [0]
    print("Aktualny stan:  q0")
    while is_accepting is False:
        input1 = str(input("Włóż monetę: "))
        actual_status, is_accepting, total_amount = transaction(input1, actual_status, total_amount)
        history.append(actual_status)
    print('Wydawanie biletu...')
    print("Zwracanie reszty:", total_amount - 9)
    print(sorted(set(history)))


if __name__ == "__main__":
    main()