NOTES = { 
    "A": (41, 50),
    "B": (31, 40),
    "C": (21, 30),
    "D": (11, 20),
    "E": (0, 10)
}

def ma_note(note): 
    for key, (inf, sup) in NOTES.items():
        if (note > inf and note <= sup):
            return key

print(ma_note(40))