#!/usr/bin/python3
#zadanie na 4
from typing import Tuple
import tkinter as tk

TABLE_OF_STATES = {
    0: {'a': ['-', 1, 'R'], 'b': ['a', '-', 'R'], '0': ['-', 2, '-']},
    1: {'a': ['b', 0, 'R'], 'b': ['a', '-', 'R'], '0': ['-', 2, '-']},
    2: {'a': ['-', '-', '-'], 'b': ['-', '-', '-'], '0': ['-', '-', '-']}
}
ALPHABET = ['a', 'b', '0'] 
ACCEPTING_STATE = [2]
tasma = []
glowica = 0
input_string = ''
current_state: int = 0
is_accepting: bool = False
i = 0
history = []

def transaction(input: str, current_state: int) -> Tuple[int, bool]: 
    
    global tasma
    global glowica
    global history
    state = TABLE_OF_STATES[current_state][input]
    if state[1] == '-':
        state[1] = current_state
    print("Aktualny stan automatu: ", 'q' + str(state[1]))
    label4['text'] =  'q' + str(state[1])
    is_accepting: bool = False

    if state[0] == '-':
        tasma.append(input)
    else:
        tasma.append(state[0])
    print("Taśma:", tasma)
    label6['text'] =  tasma


    if state[2] == 'R':
        glowica += 1
    elif state[2] == 'L':
        glowica -= 1
    print("Glowica znajduje sie na", glowica, "pozycji.")
    label8['text'] =  glowica
    if state[1] in ACCEPTING_STATE:
        is_accepting = True
    
    history.append(state[1])
    return state[1], is_accepting

def allow_moving():
    global input_string
    global current_state
    global is_accepting
    global i
    global tasma
    print("Badam ciag:", input_string)
    # print("Aktualny stan automatu: q0")
    # while is_accepting is False:    
    current_state, is_accepting = transaction(input_string[i], current_state)
    i += 1
    if is_accepting:
        button['state'] = tk.DISABLED
        button['text'] = "Koniec ciagu"
        label9['text'] = history


def main(inp):
    global input_string
    global current_state
    global is_accepting
    global i
    global tasma
    global glowica
    current_state = 0
    is_accepting = False
    i = 0
    tasma = []
    glowica = 0
    input_string = inp.widget.get()
    label2['text'] = "Badany ciag: " + input_string
    button['state'] = tk.NORMAL
    button['text'] = "Krok dalej"
    input_string += '0'

if __name__ == "__main__":

    top = tk.Tk()
    var = tk.IntVar()
    canvas = tk.Canvas(top, height=400, width=400)
    canvas.pack()
    frame = tk.Frame(top)
    frame.place(relx=0.5, rely=0.05, relwidth=0.75, relheight=0.1, anchor='n')
    label = tk.Label(frame, text="Wprowadz ciag: ")
    label.place(relwidth=0.5, relheight=1)
    inp = tk.Entry(frame)
    inp.place(relx=0.5, relheight=1, relwidth=0.5)
    inp.bind("<Return>", main)
    frame2 = tk.Frame(top)
    frame2.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=0.1, anchor='n')
    label2 = tk.Label(frame2)
    label2.place(relwidth=1, relheight=1)
    frame3 = tk.Frame(top)
    frame3.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.1, anchor='n')
    button = tk.Button(frame3, text="Krok dalej", state=tk.DISABLED, font=40, command=allow_moving)
    button.place(relheight=1, relwidth=1)
    frame3 = tk.Frame(top)
    frame3.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.1, anchor='n')
    label3 = tk.Label(frame3, text="Stan automatu: ")
    label3.place(relx=0, relwidth=0.5, relheight=1)
    label4 = tk.Label(frame3, text="q0")
    label4.place(relx=0.5, relwidth=0.5, relheight=1)
    frame4 = tk.Frame(top)
    frame4.place(relx=0.5, rely=0.45, relwidth=0.75, relheight=0.1, anchor='n')
    label5 = tk.Label(frame4, text="Taśma: ")
    label5.place(relx=0, relwidth=0.5, relheight=1)
    label6 = tk.Label(frame4, text="[]")
    label6.place(relx=0.5, relwidth=0.5, relheight=1)
    frame5 = tk.Frame(top)
    frame5.place(relx=0.5, rely=0.55, relwidth=0.75, relheight=0.1, anchor='n')
    label7 = tk.Label(frame5, text="Głowica: ")
    label7.place(relx=0, relwidth=0.5, relheight=1)
    label8 = tk.Label(frame5, text="0")
    label8.place(relx=0.5, relwidth=0.5, relheight=1)
    frame6 = tk.Frame(top)
    frame6.place(relx=0.5, rely=0.65, relwidth=0.75, relheight=0.1, anchor='n')
    label9 = tk.Label(frame6)
    label9.place(relwidth=1, relheight=1)
    top.mainloop()