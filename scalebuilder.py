base_pitch = 440.0
# semitone_scale = {"A4": base_pitch, "E5": 1.0, "B5": 1.0, "F♯6": 1.0, "C♯7": 1.0, "G♯8": 1.0, "D♯9": 1.0, "A♯9": 1.0, "F10": 1.0, "C11": 1.0, "G11": 1.0, "D12": 1.0}

# A4 = semitone_scale.pop("A4")

note_names = ["A4", "E5", "B5", "F♯/G♭6", "C♯/D♭7", "G♯/A♭7", "D♯/E♭8", "A♯/B♭8", "F9", "C10", "G10", "D11"]
note_pitches = [base_pitch, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
note_octaves = [4, 5, 5, 6, 7, 7, 8, 9, 10, 11, 11, 12]

note_dict = {}

for i in range(0, 12):
    note_pitches[i] = base_pitch * pow(3/2, i)
    note_dict.update({note_names[i] : note_pitches[i]})

# for note_name, note_pitch in notes.items():
#     print(note_name + ' : ' + str(note_pitch))
    
    
def split_values(note_name):
    note_letter = ''.join(filter(lambda c: not c.isdigit(), note_name))
    note_octave = int(''.join(filter(lambda d: d.isdigit(), note_name)))
    
    return note_letter, note_octave
    
    
def find_octave_interval_pitches(note_name, note_pitch, note_octave):
    note_letter, note_octave = split_values(note_name)
    note_pitch_in_0th_octave = note_pitch / (pow(2, note_octave))
    
    note_names = [note_name, "", "", "", "", "", "", "", "", ""]
    note_pitches = [note_pitch_in_0th_octave, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    
    note_dict = {note_letter + '0' : note_pitch_in_0th_octave}
    
    for i in range(0, 10):
        note_names[i] = note_letter + str(i)
        note_pitches[i] = note_pitch_in_0th_octave * pow(2, i)
        # print(note_names[i] + ':' + str(note_pitches[i]))
        note_dict.update({note_names[i] : note_pitches[i]})
        
    return note_dict
        

for i in range(0, 12):
    note_dict.update(find_octave_interval_pitches(note_names[i], note_pitches[i], note_octaves[i]))
    
note_list = sorted(note_dict.items(), key=lambda x:x[1])
note_dict = dict(note_list)

for note, pitch in note_dict.items():
    print(note, end='')
    if len(note) == 2:
        print('    ', end='')
    elif len(note) == 3:
        print('   ', end='')
    print(" : " + str(pitch))
