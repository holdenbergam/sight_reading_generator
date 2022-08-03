import random
#from myly import CreateMusicXML
from music21 import *

def make_random_music(time_signature, key_signature, clef_, measures, instrument, save_to='im/image.pdf'):
    #return [[(34, 1/2), (37, 1/4), 33, ...], [(23, 1), ...] , ...]

    #41, 43, 45, 47, 48, 50, 52, 53, 55, 57, 59, 60, 62, 64, 65, respectively

    #NATURAL ACCIDENTALS TO BE REMOVED
    if key_signature == "C":
        pitch = ['F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5']
    if key_signature == "F":
        pitch = ['F3', 'G3', 'A3', 'B-3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B-4', 'B4', 'C5', 'D5', 'E5', 'F5']
    if key_signature == "bFlat":
        pitch = ['F3', 'G3', 'A3', 'B-3', 'B3', 'C4', 'D4', 'E-4', 'E4', 'F4', 'G4', 'A4', 'B-4', 'B4', 'C5', 'D5', 'E-5', 'E5', 'F5']
    if key_signature == "eFlat":
        pitch = ['F3', 'G3', 'A-3', 'A3', 'B-3', 'B3', 'C4', 'D4', 'E-4', 'E4', 'F4', 'G4', 'A-4', 'A4', 'B-4', 'B4', 'C5', 'D5', 'E-5', 'E5', 'F5']
    if key_signature == "aFlat":
        pitch = ['F3', 'G3', 'A-3', 'A3', 'B-3', 'B3', 'C4', 'D-4', 'D4', 'E-4', 'E4', 'F4', 'G4', 'A-4', 'A4', 'B-4', 'B4', 'C5', 'D-5', 'D5', 'E-5', 'E5', 'F5']
    if key_signature == "G":
        pitch = ['F3', 'F#3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'F#4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'F#5']
    if key_signature == "D":
        pitch = ['F3', 'F#3', 'G3', 'A3', 'B3', 'C4', 'C#4', 'D4', 'E4', 'F4', 'F#4', 'G4', 'A4', 'B4', 'C5', 'C#5', 'D5', 'E5', 'F5', 'F#5']
    if key_signature == "A":
        pitch = ['F3', 'F#3', 'G3', 'G#3', 'A3', 'B3', 'C4', 'C#4', 'D4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'B4', 'C5', 'C#5', 'D5', 'E5', 'F5', 'F#5']
    if key_signature == "E":
        pitch = ['F3', 'F#3', 'G3', 'G#3', 'A3', 'B3', 'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'B4', 'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5']
    length = []
    #whole =
    #half = 2
    #quarter = 1
    for i in range(int(measures)):
        options = ['whole', 'half', 'quarter']
        choice = random.choice(options)
        length.append(choice)
        if choice == 'whole':
            continue
        elif choice == 'half':
            options.remove('whole')
            optionone = ['quarter', 'quarter']
            optiontwo = ['half']
            length.append(random.choice([optionone, optiontwo])[0])
        elif choice == 'quarter':
            options.remove('whole')
            optionthree = ['quarter', 'half']
            optionfour = ['quarter', 'quarter', 'quarter']
            optionfive = ['half', 'quarter']
            length.append(random.choice([optionthree, optionfour, optionfive])[0])
    '''elif time_signature == '3/4':
        for i in range(int(measures)):
            options = ['half', 'quarter']
            choice = random.choice(options)
            length.append(choice)
            if choice == 'half':
                length.append('quarter')
            elif choice == 'quarter':
                length.append('half')
    elif time_signature == '2/4':
        for i in range(int(measures)):
            options = ['half', 'quarter']
            choice = random.choice(options)
            length.append(choice)
            if choice == 'half':
                continue
            elif choice == 'quarter':
                length.append('quarter')'''
    set = []
    for i in length:
        set_approach = [random.choice(pitch), i]
        set.append(set_approach)
    print(set)



    s = stream.Stream()
    s.insert(0, metadata.Metadata())
    s.metadata.title = instrument + ' Sample'
    s.metadata.composer = ' '
    d = duration.Duration()
            #Problem showed up when I changed this command from a direct string to this mess. Fix.
    ts = meter.TimeSignature(time_signature)
    s.append(ts)
    k = key.Key(key_signature)
    s.append(k)
    if clef_ == "treble":
        c = clef.TrebleClef()
        s.append(c)
    elif clef_ == "bass":
        c = clef.BassClef()
        s.append(c)


    for i in set:
        n = note.Note(i[0], type=i[1])

        r = note.Rest()
        options = [n, n, n, r]
        #quarterLength = i[1]
        #n.duration = duration.Duration(float(quarterLength))
        s.append(random.choice(options))
        #WHAT DO I DO HERE
    #s.show()

    s.write('musicxml.pdf', fp='flaskr/static/image.pdf')
    print('wrote new music!')



def make_image(music):
    return 0

if __name__=='__main__':
    print('Hello World')
    make_random_music('4/4', 'F', 'Treble', '16')
