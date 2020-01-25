# S :: = W;Z
# Z :: = W;Z|ε
# W :: = PW'
# W':: = OW|ε
# P :: = R|(W)
# R :: = LR'
# R'::= .L|ε
# L :: = CL'
# L':: = L|ε
# C :: = 0|1|2|3|4|5|6|7|8|9
# O :: = *|:|+|-|^

def O(test_str:str) -> int:
    actual_position = 0
    if test_str[actual_position] in '*:+-^':
        actual_position += 1
    else:
        raise Exception("Not parsed! Expected sign is an operator!")
    return actual_position

def C(test_str:str) -> int:
    actual_position = 0
    if test_str[actual_position] in '0123456789':
        actual_position += 1
    else:
        raise Exception("Not parsed! Expected sign is a figure!")
    return actual_position

def L_prim(test_str:str) -> int:
    actual_position = 0
    if test_str[actual_position] in '0123456789':
        actual_position += L(test_str[actual_position:])
    return actual_position

def L(test_str:str) -> int:
    actual_position = 0
    if test_str[actual_position] in '0123456789':
        actual_position += C(test_str[actual_position:])
        actual_position += L_prim(test_str[actual_position:])
    else:
        raise Exception("Not parsed! Expected sign is a figure!")
    return actual_position

def R_prim(test_str:str) -> int:
    actual_position = 0
    if test_str[actual_position] is '.':
        actual_position += 1
        actual_position += L(test_str[actual_position:])
    return actual_position

def R(test_str:str) -> int:
    actual_position = 0
    if test_str[actual_position] in '0123456789':
        actual_position += L(test_str[actual_position:])
        actual_position += R_prim(test_str[actual_position:])
    else:
        raise Exception("Not parsed! Expected sign is a figure!")
    return actual_position

def P(test_str:str) -> int:
    actual_position = 0
    if test_str[actual_position] in '0123456789':
        actual_position += R(test_str[actual_position:])
    elif test_str[actual_position] is '(':
        actual_position += 1
        actual_position += W(test_str[actual_position:])
        if test_str[actual_position] is ')':
            actual_position += 1
        else:
            raise Exception("Not parsed! Expected sign is )!")
    else:
        raise Exception("Not parsed! Expected sign is a figure or (!")
    return actual_position

def W_prim(test_str:str) -> int:
    actual_position = 0
    if test_str[actual_position] in '*:+-^':
        actual_position += 1
        actual_position += W(test_str[actual_position:])
    return actual_position
        
def W(test_str:str) -> int:
    actual_position = 0
    if test_str[actual_position] in '0123456789' or test_str[actual_position] is '(':
        actual_position += P(test_str[actual_position:])
        actual_position += W_prim(test_str[actual_position:])
    else:
        raise Exception("Not parsed! Expected sign is a figure or (!")
    return actual_position

def Z(test_str:str) -> int:
    actual_position = 0
    if test_str[actual_position] in '0123456789' or test_str[actual_position] is '(':
        actual_position += W(test_str[actual_position:])
        if test_str[actual_position] is ';':
            actual_position += 1
            actual_position += Z(test_str[actual_position:])
        else:
            raise Exception("Not parsed! Expected sign is ;")
    return actual_position

def S(test_str:str) -> int:
    actual_position = 0
    if test_str[actual_position] in '0123456789' or test_str[actual_position] is '(':
        actual_position += W(test_str[actual_position:])
        if test_str[actual_position] is ';':
            actual_position += 1
            actual_position += Z(test_str[actual_position:])
        else:
            raise Exception("Not parsed! Expected sign is ;")
    else:
        raise Exception("Not parsed! Expected sign is a figure or (!")
    return actual_position
        

def parse_string(test_str:str, actual_position: int) -> int:
   actual_position += S(test_str)
   return actual_position

def main():
    # (1.2*3)+5-(23.4+3)^3; 8:13;
    tested_string = "(1.2*3)+5-(23.4+3)^3; 8:1.3;"
    try:
        returned = parse_string(tested_string.replace(' ','') + '#', 0)
        
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