base_pitch = 440.0
semitone_scale = {"A4": base_pitch, "E5": 1.0, "B5": 1.0, "F♯6": 1.0, "C♯7": 1.0, "G♯8": 1.0, "D♯9": 1.0, "A♯9": 1.0, "F10": 1.0, "C11": 1.0, "G11": 1.0, "D12": 1.0}

A4 = semitone_scale.pop("A4")

note_names = ["A4", "E5", "B5", "F♯6", "C♯7", "G♯7", "D♯8", "A♯9", "F10", "C11", "G11", "D12"]
note_pitches = [440.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

notes = {}

power = 0

for note_pitch in note_pitches:
    note_pitch = base_pitch * pow(3/2, power)
    notes.update({note_names[power] : note_pitch})
    power += 1
    print(note_pitch)
    
print()
    
for note_name, note_pitch in notes.items():
    print(note_name + ' : ' + str(note_pitch))
    
