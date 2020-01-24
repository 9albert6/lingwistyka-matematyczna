# S :: = W;Z
# Z :: = W;Z|ε
# W :: = PW'
# W':: = OW|ε
# P :: = L|(W)
# L :: = CL'
# L':: = L|ε
# C :: = 0|1|2|3|4|5|6|7|8|9
# O :: = *|:|+|-|^

def parse_string(test_str:str, actual_position: int) -> int:
    if test_str is '':
        return 0

    if test_str[actual_position] in '0123456789':
        actual_position += 1
        if actual_position == len(test_str):
            return actual_position        
        while test_str[actual_position] in '0123456789':
            actual_position += 1
        if test_str[actual_position] in '*:+-^':
            actual_position += 1
            actual_position += parse_string(test_str[actual_position:], 0)
        elif test_str[actual_position] in ')':
            actual_position += 1
            if test_str[actual_position] in '*:+-^':
                actual_position += 1
                actual_position += parse_string(test_str[actual_position:], 0)
        elif test_str[actual_position] in ';':
            actual_position += 1
            actual_position += parse_string(test_str[actual_position:], 0)
        elif test_str[actual_position] in '.':
            actual_position += 1
            actual_position += parse_string(test_str[actual_position:], 0)

    elif test_str[actual_position] in '(':
        actual_position += 1
        actual_position += parse_string(test_str[actual_position:], 0)

    elif test_str[actual_position] in ')': 
        actual_position += 1
        if test_str[actual_position] in '*:+-^':
            actual_position += 1
            actual_position += parse_string(test_str[actual_position:], 0)
        elif test_str[actual_position] in ';':
            actual_position += 1
            actual_position += parse_string(test_str[actual_position:], 0)

    if actual_position == len(test_str):
            return actual_position   
    else:
        raise Exception("Not parsed!")

def main():
    # (1.2*3)+5-(23.4+3)^3; 8:13;
    tested_string = "(1.2*3)+5-(23.4+3)^3; 8:13;"
    try:
        returned = parse_string(tested_string.replace(' ',''), 0)
        
    except Exception as identifier:
        print(identifier)
        return

    if returned != -1 and returned != None:
        print (returned)
        print("gut")
    else:
        print (returned)
        print("bad")


if __name__ == "__main__":
    main()