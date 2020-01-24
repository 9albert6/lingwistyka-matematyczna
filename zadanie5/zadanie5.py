
# S::=B;{B;}
# B::=W{OW}
# W::=A[.L]
# A::=[-]L
# L::=C{C}
# C::=1|2|3|4|5|6|7|8|9|0
# O::=*/+-^

# S ->  ^-?\d+(\.\d+)?([\*\/\+\-\^]-?\d+(\.\d+)?)*;(-?\d+(\.\d+)?([\*\/\+\-\^]-?\d+(\.\d+)?)*;)*$
# B -> -?\d+(\.\d+)?([\*\/\+\-\^]-?\d+(\.\d+)?)*
# W -> -?\d+(\.\d+)?
# A -> -?\d+
# L -> \d+
# C -> \d 
# O -> [\*\/\+\-\^]

import re

if __name__ == "__main__":
    pattern = re.compile("^-?\d+(\.\d+)?([\*\/\+\-\^]-?\d+(\.\d+)?)*;(-?\d+(\.\d+)?([\*\/\+\-\^]-?\d+(\.\d+)?)*;)*$")
    tested_string = "12+2*9;3*8.7^1.2-2/3"

    print("Sprawdzany ciag:", tested_string)
    if pattern.match(tested_string):
        print("Badany ciąg pozwala na poprawne operacje artmetyczne!")
    else:
        print("Badany ciąg NIE pozwala na poprawne operacje artmetyczne!")