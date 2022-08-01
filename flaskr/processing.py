import random
#from myly import CreateMusicXML
from music21 import note, stream
import itertools

def make_random_music(time_signature, key_signature, num_measures=4):
    #return [[(34, 1/2), (37, 1/4), 33, ...], [(23, 1), ...] , ...]
    F3 = [41, 'F3']
    G3 = [43, 'G3']
    A3 = [45, 'A3']
    B3 = [47, 'B3']
    C4 = [48, 'C4']
    D4 = [50, 'D4']
    E4 = [52, 'E4']
    F4 = [53, 'F4']
    G4 = [55, 'G4']
    A4 = [57, 'A4']
    B4 = [59, 'B4']
    C5 = [60, 'C5']
    D5 = [62, 'D5']
    E5 = [64, 'E5']
    F5 = [65, 'E5']

    quarter = 0.25
    half = 0.5
    whole = 1

    notecount = [F3, G3, A3, B3, C4, D4, E4, F4, G4, A4, B4, C5, D5, E5, F5]
    chosen = []
    for i in range(num_measures):
        options = [whole, half, quarter]
        choice = random.choice(options)
        chosen.append(choice)
        if choice == whole:
            continue
        elif choice == half:
            options.remove(whole)
            optionone = [quarter, quarter]
            optiontwo = [half]
            chosen.append(random.choice([optionone, optiontwo])[0])
        elif choice == quarter:
            options.remove(whole)
            optionthree = [quarter, half]
            optionfour = [quarter, quarter, quarter]
            optionfive = [half, quarter]
            chosen.append(random.choice([optionthree, optionfour, optionfive])[0])
    chain = itertools.chain(*chosen)
    print(chosen)
    a = []
    for i in chosen:
        b = [random.choice(notecount)[1], i]
        a.append(b)
    print(a)

    s = stream.Stream()
    for i in a:
        s.append(note.Note(a[i][0][1]))
    s.show()



def make_image(music):
    return 0

if __name__=='__main__':
    print('Hello World')
    make_random_music('4/4', 'F')
