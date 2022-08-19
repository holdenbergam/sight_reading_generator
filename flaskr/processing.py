
import random
#from myly import CreateMusicXML
from music21 import *
from IPython import embed

import music21

def note_to_midi(note):
    the_sum = 0
    letter_values = {
        "C": 0,
        "C#": 1,
        "D-": 1,
        "D": 2,
        "D#": 3,
        "E-": 3,
        "E": 4,
        "F": 5,
        "F#": 6,
        "G-": 6,
        "G": 7,
        "G#": 8,
        "A-": 8,
        "A": 9,
        "A#": 10,
        "B-": 10,
        "B": 11,
        "B#": 0,
        "C-": 11
    }
    number_values = {
        "-1": 0,
        "0": 12,
        "1": 24,
        "2": 36,
        "3": 48,
        "4": 60,
        "5": 72,
        "6": 84,
        "7": 96,
        "8": 108,
        "9": 120
    }
    for key in letter_values:
        if key in note:
            the_sum += letter_values[key]
    for jey in number_values:
        if jey in note:
            the_sum += number_values[jey]
    return the_sum

"""def midi_to_note(midi):
    letter_values = {
        "0": "C",
        "1": "C#",
        "1": "D-",
        "2": "D",
        "3": "D#",
        "3": "E-",
        "4": "E",
        "4": "F-",
        "5": "E#",
        "5": "F",
        "6": "F#",
        "6": "G-",
        "7": "G",
        "8": "G#",
        "8": "A-",
        "9": "A",
        "10": "A#",
        "10": "B-",
        "11": "B",
        "0": "B#",
        "11": "C-"
    }

    kaboom = midi % 12
    also_kaboom = letter_values
midi_to_note(52)"""

def create_range(instrument, key_signature, level):


    get_clef = {
        "Flute": clef.TrebleClef(),
        "Piccolo": clef.TrebleClef(),
        "Oboe": clef.TrebleClef(),
        "Clarinet": clef.TrebleClef(),
        "Alto Saxophone": clef.TrebleClef(),
        "Tenor Saxophone": clef.TrebleClef(),
        "Baritone Saxophone": clef.TrebleClef(),
        "Trumpet": clef.TrebleClef(),
        "French Horn": clef.TrebleClef(),
        "Trombone": clef.BassClef(),
        "Bassoon": clef.BassClef(),
        "Tuba": clef.BassClef(),
        "Baritone B.C.": clef.BassClef(),
        "Baritone T.C.": clef.TrebleClef(),
        "Alto Clarinet": clef.TrebleClef(),
        "Bass Clarinet": clef.TrebleClef(),
        #"Contrabass Clarinet": clef.TrebleClef()
    }

    get_transposition = {
        "Flute": 0,
        "Piccolo": 0,
        "Oboe": 0,
        "Clarinet": 2,
        "Alto Saxophone": 9,
        "Tenor Saxophone": 2,
        "Baritone Saxophone": 9,
        "Trumpet": 2,
        "French Horn": -5,
        "Trombone": 0,
        "Bassoon": 0,
        "Tuba": 0,
        "Baritone B.C.": 0,
        "Baritone T.C.": -2,
        "Alto Clarinet": 9,
        "Bass Clarinet": 2,
        #"Contrabass Clarinet": 2
    }

    # Flute: bFlat4-bFlat5, F4-E6, C4-B6
    #Piccolo: bFlat4-bFlat5, F4-E6, D4-B6
    #Oboe: C4-C5, C4-bFlat5, bFlat3-D6
    #Clarinet: bFlat3-bFlat4, F3-A5, E3-D6
    #AltoSax: F4-F5, C4-B5, bFlat3-F6
    #TenorSax: F4-F5, C4-B5, bFlat3-F6
    #BariSax: F4-F5, C4-B5, A3-D6
    #Trumpet: C4-C5, A3-G5, A3-C6
    #Horn: bFlat3-bFlat4, A3-F5, G3-A5
    #Trombone: bFlat2-bFlat3, aFlat2-F4, G2-bFlat4
    #Bassoon: bFlat2-bFlat3, eFlat2-eFlat4, bFlat1-G4
    #Tuba: bFlat1-bFlat2, G1-eFlat3, F1-G3
    #Baritone B.C: bFlat2-bFlat3, aFlat2-F4, G2-bFlat4
    #Baritone T.C: C4-C5, bFlat3-G5, A3-C6
    #Alto Clarinet: bFlat3-bFlat4, F3-G5, E3-C6
    #bass Clarinet: bFlat3-bFlat4, F3-E5, E3-A5


    base_range = {
        "1": {
            "Flute": ['B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5'],
            "Piccolo": ['B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5'],
            "Oboe": ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5'],
            "Clarinet": ['B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4'],
            "Alto Saxophone": ['F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5'],
            "Tenor Saxophone": ['F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5'],
            "Baritone Saxophone": ['F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5'],
            "French Horn": ['B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4'],
            "Trumpet": ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5'],
            "Trombone": ['B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3'],
            "Bassoon": ['B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3'],
            "Tuba": ['B1', 'C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2'],
            "Baritone B.C.": ['B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3'],
            "Baritone T.C.": ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5'],
            "Alto Clarinet": ['B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4'],
            "Bass Clarinet": ['B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']
        },
        "2": {
            "Flute": ['F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'E6'],
            "Piccolo": ['F4', 'G4', 'A4', 'B4', 'E4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'E6'],
            "Oboe": ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5'],
            "Clarinet": ['F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5'],
            "Alto Saxophone": ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5'],
            "Tenor Saxophone": ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5'],
            "Baritone Saxophone": ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5'],
            "French Horn": ['A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5'],
            "Trumpet": ['A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5'],
            "Trombone": ['A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4'],
            "Bassoon": ['E2', 'F2', 'G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4'],
            "Tuba": ['G1', 'A1', 'B1', 'C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2', 'C3', 'D3', 'E3'],
            "Baritone B.C.": ['A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4'],
            "Baritone T.C.": ['B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5'],
            "Alto Clarinet": ['F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5'],
            "Bass Clarinet": ['F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5']
        },
        "3": {
            "Flute": ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'F6', 'G6', 'A6', 'B6'],
            "Piccolo": ['D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'E4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'F6', 'G6', 'A6', 'B6'],
            "Oboe": ['B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6'],
            "Clarinet": ['E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6'],
            "Alto Saxophone": ['B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'F6'],
            "Tenor Saxophone": ['B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'F6'],
            "Baritone Saxophone": ['A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6'],
            "French Horn": ['G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5'],
            "Trumpet": ['A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6'],
            "Trombone": ['G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4'],
            "Bassoon": ['B1', 'C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4'],
            "Tuba": ['F1', 'G1', 'A1', 'B1', 'C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3'],
            "Baritone B.C.": ['G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4'],
            "Baritone T.C.": ['A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6'],
            "Alto Clarinet": ['E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6'],
            "Bass Clarinet": ['E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5']
        }
    }


    s = stream.Stream()
    s.transpose(get_transposition[instrument])
    range_ = base_range[level][instrument]
    c = get_clef[instrument]
    k = key.Key(key_signature).transpose(get_transposition[instrument])
    return range_, c, k

import music21
def make_random_music(time_signature, key_signature, measures, instrument, level, save_to='im/image.pdf'):

    range_,k,c = create_range(instrument, key_signature, level)

    length = []
    #whole =
    #half = 2
    #quarter = 1

    loaded_model = pickle.load(open('static/finalized_model.sav', 'rb'))

    totalcounter = 0.0
    for i in range(int(measures)):
        options = [4.0, 3.0, 2.0, 1.5, 1.0, 0.5, 1.0/3.0, 0.25]
        time_signature_length = {
            '6/4': 6.0,
            '5/4': 5.0,
            '4/4': 4.0,
            '3/4': 3.0,
            '2/4': 2.0
        }

        beatcounter = 0.0
        while beatcounter < time_signature_length[time_signature]:
            valid_options = []
            for j in options:
                if j <= time_signature_length[time_signature] - beatcounter:
                    valid_options.append(j)
            choice_ = random.choice(valid_options)
            length.append(choice_)
            beatcounter += float(choice_)
            if choice_ == 1.5 or choice_ == 0.5:
                length.append(0.5)
                beatcounter += 0.5
            elif choice_ == 0.25:
                length.extend([0.25, 0.25, 0.25])
                beatcounter += 0.75
            elif choice_ == 1.0/3.0:
                length.extend([1.0/3.0, 1.0/3.0])
                beatcounter += 2.0/3.0
            print(beatcounter)
            print(options)

        totalcounter+=beatcounter


    set = []

    if level == "1":
        last_note_ix = random.randint(0, len(range_))
        for i in range(len(length)):
            rand_direction = random.randint(-3,3)
            this_note_ix = last_note_ix + rand_direction

            if this_note_ix > len(range_)-1:
                this_note_ix = len(range_)-1
            elif this_note_ix < 0:
                this_note_ix = 0

            next_note = range_[this_note_ix]
            set.append([next_note, length[i]])
            last_note_ix = this_note_ix
    if level == "2":
        last_note_ix = random.randint(0, len(range_))
        for i in range(len(length)):
            rand_direction = random.randint(-5,5)
            this_note_ix = last_note_ix + rand_direction

            if this_note_ix > len(range_)-1:
                this_note_ix = len(range_)-1
            elif this_note_ix < 0:
                this_note_ix = 0

            next_note = range_[this_note_ix]
            set.append([next_note, length[i]])
            last_note_ix = this_note_ix
    if level == "3":
        last_note_ix = random.randint(0, len(range_))
        for i in range(len(length)):
            rand_direction = random.randint(-7,7)
            this_note_ix = last_note_ix + rand_direction

            if this_note_ix > len(range_)-1:
                this_note_ix = len(range_)-1
            elif this_note_ix < 0:
                this_note_ix = 0

            next_note = range_[this_note_ix]
            set.append([next_note, length[i]])
            last_note_ix = this_note_ix

    print(set)

    instrument_midi = {
        "Flute": music21.instrument.Flute(),
        "Piccolo": music21.instrument.Piccolo(),
        "Oboe": music21.instrument.Oboe(),
        "Clarinet": music21.instrument.Clarinet(),
        "Alto Saxophone": music21.instrument.AltoSaxophone(),
        "Tenor Saxophone": music21.instrument.TenorSaxophone(),
        "Baritone Saxophone": music21.instrument.BaritoneSaxophone(),
        "Trumpet": music21.instrument.Trumpet(),
        "French Horn": music21.instrument.Horn(),
        "Trombone": music21.instrument.Trombone(),
        "Bassoon": music21.instrument.Bassoon(),
        "Tuba": music21.instrument.Tuba(),
        "Baritone B.C.": music21.instrument.Baritone(),
        "Baritone T.C.": music21.instrument.Baritone(),
        "Alto Clarinet": music21.instrument.EnglishHorn(),
        "Bass Clarinet": music21.instrument.BassClarinet(),
        #"Contrabass Clarinet": music21.instrument.BassClarinet()
    }

    s = stream.Stream()
    s.insert(0, metadata.Metadata())
    s.metadata.title = instrument + ' Sample'
    s.metadata.composer = ' '
    d = duration.Duration()
    ts = meter.TimeSignature(time_signature)
    s.append(ts)
    s.append(k)
    s.append(c)
    s.append(instrument_midi[instrument])
    s.append(dynamics.Dynamic(random.choice(['pp', 'p', 'mp', 'mf', 'f', 'ff'])))

    for i in set:
        the_option = random.choice(['n', 'r'])
        if the_option == 'n':
            n = note.Note(i[0], quarterLength=float(i[1]))
            acce = articulations.Accent()
            stac = articulations.Staccato()
            tenu = articulations.Tenuto()
            whatdoinamethis = random.randint(1, 9)
            if whatdoinamethis < 3:
                n.articulations = [random.choice([acce, stac, tenu])]
            else:
                print("")
            s.append(n)
        elif the_option == 'r' and i[1] == 3.0 or i[1] == 1.5 or i[1] == 0.5 or i[1] == 1.0/3.0 or i[1] == 0.25:
            n = note.Note(i[0], quarterLength=float(i[1]))
            acce = articulations.Accent()
            stac = articulations.Staccato()
            tenu = articulations.Tenuto()
            whatdoinamethis = random.randint(1, 9)
            if whatdoinamethis < 3:
                n.articulations = [random.choice([acce, stac, tenu])]
            else:
                print("")
            s.append(n)
            for no in s.notes:
                the_the_option = random.choice(['der', 'duh', 'duh'])
                if the_the_option == 'duh':
                    no.pitch.accidental = no.getContextByClass(key.KeySignature).accidentalByStep(no.step)
                else:
                    continue
        elif the_option == 'r' and i[1] == 4.0 or i[1] == 2.0 or i[1] == 1.0:
            r = note.Rest(quarterLength=float(i[1]))
            s.append(r)

    s.write('musicxml.pdf', fp='flaskr/static/image.pdf')
    s.write('midi', fp='flaskr/static/music_output.mid')

    print('wrote new music!')


'''from music21 import corpus'''
from music21 import converter

'''from midi2audio import FluidSynth'''


def make_image(music):
    return 0

if __name__=='__main__':
    print('Hello World')

'''    range_extension = {
        "French Horn": {
            "1": {
                "F": [],
                "bFlat": ['B-3', 'B-4'],
                "eFlat": ['B-3', 'B-4', 'E-4', 'E-5'],
                "aFlat": ['B-3', 'B-4', 'E-4', 'E-5', 'A-3', 'A-4'],
                "dFlat": ['B-3', 'B-4', 'E-4', 'E-5', 'A-3', 'A-4', 'D-4', 'D-5'],
                "gFlat": ['B-3', 'B-4', 'E-4', 'E-5', 'A-3', 'A-4', 'D-4', 'D-5', 'G-3', 'G-4'],
                "cFlat": ['B-3', 'B-4', 'E-4', 'E-5', 'A-3', 'A-4', 'D-4', 'D-5', 'G-3', 'G-4', 'C-4', 'C-5'],
                "E": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'G#3', 'G#4', 'D#4', 'D#5', 'A#3', 'A#4'],
                "A": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'G#3', 'G#4', 'D#4', 'D#5'],
                "D": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'G#3', 'G#4'],
                "G": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5'],
                "C": ['F#3', 'F#4', 'F#5']
            },
            "2": {
                "F": [],
                "bFlat": ['B-3', 'B-4', 'B-5'],
                "eFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5'],
                "aFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5'],
                "dFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5', 'D-3', 'D-4', 'D-5'],
                "gFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5', 'D-3', 'D-4', 'D-5', 'G-3', 'G-4', 'G-5'],
                "cFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5', 'D-3', 'D-4', 'D-5', 'G-3', 'G-4', 'G-5', 'C-3', 'C-4', 'C-5', 'C-6'],
                "E": ['F#3', 'F#4', 'F#5', 'C#3', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#3', 'D#4', 'D#5', 'A#3', 'A#4', 'A#5'],
                "A": ['F#3', 'F#4', 'F#5', 'C#3', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#3', 'D#4', 'D#5'],
                "D": ['F#3', 'F#4', 'F#5', 'C#3', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5'],
                "G": ['F#3', 'F#4', 'F#5', 'C#3', 'C#4', 'C#5', 'C#6'],
                "C": ['F#3', 'F#4', 'F#5']
            }
        },
        "Trumpet": {
            "1": {
                "bFlat": [],
                "eFlat": ['B-3', 'B-4'],
                "aFlat": ['B-3', 'B-4', 'E-4', 'E-5'],
                "dFlat": ['B-3', 'B-4', 'E-4', 'E-5', 'A-3', 'A-4'],
                "gFlat": ['B-3', 'B-4', 'E-4', 'E-5', 'A-3', 'A-4', 'D-4', 'D-5'],
                "cFlat": ['B-3', 'B-4', 'E-4', 'E-5', 'A-3', 'A-4', 'D-4', 'D-5', 'G-3', 'G-4', 'G-5'],
                "E": ['F#4', 'F#5', 'C#4', 'C#5', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4', 'E#4', 'E#5'],
                "A": ['F#4', 'F#5', 'C#4', 'C#5', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4'],
                "D": ['F#4', 'F#5', 'C#4', 'C#5', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5'],
                "G": ['F#4', 'F#5', 'C#4', 'C#5', 'G#3', 'G#4', 'G#5'],
                "C": ['F#4', 'F#5', 'C#4', 'C#5'],
                "F": ['F#4', 'F#5']
            },
            "2": {
                "bFlat": [],
                "eFlat": ['B-3', 'B-4', 'B-5'],
                "aFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5'],
                "dFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5'],
                "gFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5', 'D-4', 'D-5'],
                "cFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5', 'D-4', 'D-5', 'G-3', 'G-4', 'G-5'],
                "E": ['F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4', 'A#5', 'E#4', 'E#5'],
                "A": ['F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4', 'A#5'],
                "D": ['F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5'],
                "G": ['F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5'],
                "C": ['F#4', 'F#5', 'C#4', 'C#5', 'C#6'],
                "F": ['F#4', 'F#5']
            }

        },
        "Baritone T.C.": {
            "1": {
                "bFlat": [],
                "eFlat": ['B-3', 'B-4'],
                "aFlat": ['B-3', 'B-4', 'E-4', 'E-5'],
                "dFlat": ['B-3', 'B-4', 'E-4', 'E-5', 'A-3', 'A-4'],
                "gFlat": ['B-3', 'B-4', 'E-4', 'E-5', 'A-3', 'A-4', 'D-4', 'D-5'],
                "cFlat": ['B-3', 'B-4', 'E-4', 'E-5', 'A-3', 'A-4', 'D-4', 'D-5', 'G-3', 'G-4', 'G-5'],
                "E": ['F#4', 'F#5', 'C#4', 'C#5', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4', 'E#4', 'E#5'],
                "A": ['F#4', 'F#5', 'C#4', 'C#5', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4'],
                "D": ['F#4', 'F#5', 'C#4', 'C#5', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5'],
                "G": ['F#4', 'F#5', 'C#4', 'C#5', 'G#3', 'G#4', 'G#5'],
                "C": ['F#4', 'F#5', 'C#4', 'C#5'],
                "F": ['F#4', 'F#5']
            },
            "2": {
                "bFlat": [],
                "eFlat": ['B-3', 'B-4', 'B-5'],
                "aFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5'],
                "dFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5'],
                "gFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5', 'D-4', 'D-5'],
                "cFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5', 'D-4', 'D-5', 'G-3', 'G-4', 'G-5'],
                "E": ['F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4', 'A#5', 'E#4', 'E#5'],
                "A": ['F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4', 'A#5'],
                "D": ['F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5'],
                "G": ['F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5'],
                "C": ['F#4', 'F#5', 'C#4', 'C#5', 'C#6'],
                "F": ['F#4', 'F#5']
            }
        },
        "Alto Saxophone": {
            "1": {
                "eFlat": [],
                "aFlat": ['B-3', 'B-4', 'B-5'],
                "dFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6'],
                "gFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5'],
                "cFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'D-4', 'D-5', 'D-6'],
                "E": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6', 'A#4', 'A#5', 'E#4', 'E#5', 'E#6', 'B#3', 'B#4', 'B#5'],
                "A": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6', 'A#4', 'A#5', 'E#4', 'E#5', 'E#6'],
                "D": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6', 'A#4', 'A#5'],
                "G": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6'],
                "C": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5'],
                "F": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6'],
                "bFlat": ['F#4', 'F#5', 'F#6']
            },
            "2": {
                "eFlat": [],
                "aFlat": ['B-3', 'B-4', 'B-5'],
                "dFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6'],
                "gFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5'],
                "cFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'D-4', 'D-5', 'D-6'],
                "E": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6', 'A#4', 'A#5', 'E#4', 'E#5', 'E#6', 'B#3', 'B#4', 'B#5'],
                "A": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6', 'A#4', 'A#5', 'E#4', 'E#5', 'E#6'],
                "D": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6', 'A#4', 'A#5'],
                "G": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6'],
                "C": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5'],
                "F": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6'],
                "bFlat": ['F#4', 'F#5', 'F#6']
            }
        },
        "Baritone Saxophone": {
            "1": {
                "eFlat": [],
                "aFlat": ['B-3', 'B-4', 'B-5'],
                "dFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6'],
                "gFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5'],
                "cFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'D-4', 'D-5', 'D-6'],
                "E": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6', 'A#4', 'A#5', 'E#4', 'E#5', 'E#6', 'B#3', 'B#4', 'B#5'],
                "A": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6', 'A#4', 'A#5', 'E#4', 'E#5', 'E#6'],
                "D": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6', 'A#4', 'A#5'],
                "G": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6'],
                "C": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5'],
                "F": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6'],
                "bFlat": ['F#4', 'F#5', 'F#6']
            },
            "2": {
                "eFlat": [],
                "aFlat": ['B-3', 'B-4', 'B-5'],
                "dFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6'],
                "gFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5'],
                "cFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'D-4', 'D-5', 'D-6'],
                "E": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6', 'A#4', 'A#5', 'E#4', 'E#5', 'E#6', 'B#3', 'B#4', 'B#5'],
                "A": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6', 'A#4', 'A#5', 'E#4', 'E#5', 'E#6'],
                "D": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6', 'A#4', 'A#5'],
                "G": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6'],
                "C": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5'],
                "F": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6'],
                "bFlat": ['F#4', 'F#5', 'F#6']
            }
        },
        "Tenor Saxophone": {
            "1": {
                "bFlat": [],
                "eFlat": ['B-3', 'B-4', 'B-5'],
                "aFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6'],
                "dFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5'],
                "gFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'D-4', 'D-5', 'D-6'],
                "cFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'D-4', 'D-5', 'D-6', 'G-4', 'G-5'],
                "E": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6', 'A#4', 'A#5', 'E#4', 'E#5', 'E#6'],
                "A": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6', 'A#4', 'A#5'],
                "D": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6'],
                "G": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5'],
                "C": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6'],
                "F": ['F#4', 'F#5', 'F#6']
            },
            "2": {
                "bFlat": [],
                "eFlat": ['B-3', 'B-4', 'B-5'],
                "aFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6'],
                "dFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5'],
                "gFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'D-4', 'D-5', 'D-6'],
                "cFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'D-4', 'D-5', 'D-6', 'G-4', 'G-5'],
                "E": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6', 'A#4', 'A#5', 'E#4', 'E#5', 'E#6'],
                "A": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6', 'A#4', 'A#5'],
                "D": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6'],
                "G": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5'],
                "C": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6'],
                "F": ['F#4', 'F#5', 'F#6']
            }

        },
        "Clarinet": {
            "1": {
                "bFlat": [],
                "eFlat": ['B-3', 'B-4', 'B-5'],
                "aFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'E-6'],
                "dFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'E-6', 'A-3', 'A-4', 'A-5'],
                "gFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'E-6', 'A-3', 'A-4', 'A-5', 'D-4', 'D-5', 'D-6'],
                "cFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'E-6', 'A-3', 'A-4', 'A-5', 'D-4', 'D-5', 'D-6', 'G-3', 'G-4', 'G-5'],
                "E": ['F#3', 'F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6', 'A#3', 'A#4', 'A#5', 'E#3', 'E#4', 'E#5', 'E#6'],
                "A": ['F#3', 'F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6', 'A#3', 'A#4', 'A#5'],
                "D": ['F#3', 'F#4', 'F#5', 'F#6',  'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6'],
                "G": ['F#3', 'F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5'],
                "C": ['F#3', 'F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6'],
                "F": ['F#3', 'F#4', 'F#5', 'F#6']
            },
            "2": {
                "bFlat": [],
                "eFlat": ['B-3', 'B-4', 'B-5'],
                "aFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'E-6'],
                "dFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'E-6', 'A-3', 'A-4', 'A-5'],
                "gFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'E-6', 'A-3', 'A-4', 'A-5', 'D-4', 'D-5', 'D-6'],
                "cFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'E-6', 'A-3', 'A-4', 'A-5', 'D-4', 'D-5', 'D-6', 'G-3', 'G-4', 'G-5', 'G-6'],
                "E": ['F#3', 'F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'G#6', 'D#4', 'D#5', 'D#6', 'A#3', 'A#4', 'A#5', 'E#3', 'E#4', 'E#5', 'E#6'],
                "A": ['F#3', 'F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'G#6', 'D#4', 'D#5', 'D#6', 'A#3', 'A#4', 'A#5'],
                "D": ['F#3', 'F#4', 'F#5', 'F#6',  'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'G#6', 'D#4', 'D#5', 'D#6'],
                "G": ['F#3', 'F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'G#6'],
                "C": ['F#3', 'F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6'],
                "F": ['F#3', 'F#4', 'F#5', 'F#6']
            }

        },
        "Oboe": {
            "1": {
                "C": [],
                "F": ['B-4', 'B-5'],
                "bFlat": ['B-4', 'B-5', 'E-4', 'E-5'],
                "eFlat": ['B-4', 'B-5', 'E-4', 'E-5', 'A-4', 'A-5'],
                "aFlat": ['B-4', 'B-5', 'E-4', 'E-5', 'A-4', 'A-5', 'D-4', 'D-5'],
                "dFlat": ['B-4', 'B-5', 'E-4', 'E-5', 'A-4', 'A-5', 'D-4', 'D-5', 'G-4', 'G-5'],
                "gFlat": ['B-4', 'B-5', 'E-4', 'E-5', 'A-4', 'A-5', 'D-4', 'D-5', 'G-4', 'G-5', 'C-4', 'C-5', 'C-6'],
                "cFlat": ['B-4', 'B-5', 'E-4', 'E-5', 'A-4', 'A-5', 'D-4', 'D-5', 'G-4', 'G-5', 'C-4', 'C-5', 'C-6', 'F-4', 'F-5'],
                "E": ['F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5'],
                "A": ['F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5'],
                "D": ['F#4', 'F#5', 'C#4', 'C#5', 'C#6'],
                "G": ['F#4', 'F#5']
            },
            "2": {
                "C": [],
                "F": ['B-3', 'B-4', 'B-5'],
                "bFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6'],
                "eFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5'],
                "aFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'D-4', 'D-5', 'D-6'],
                "dFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'D-4', 'D-5', 'D-6', 'G-4', 'G-5'],
                "gFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'D-4', 'D-5', 'D-6', 'G-4', 'G-5', 'C-4', 'C-5', 'C-6'],
                "cFlat": ['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'D-4', 'D-5', 'D-6', 'G-4', 'G-5', 'C-4', 'C-5', 'C-6', 'F-4', 'F-5'],
                "E": ['F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6'],
                "A": ['F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5'],
                "D": ['F#4', 'F#5', 'C#4', 'C#5', 'C#6'],
                "G": ['F#4', 'F#5']
            }
        },
        "Piccolo": {
            "1": {
                "C": [],
                "F": ['B-4', 'B-5'],
                "bFlat": ['B-4', 'B-5', 'E-4', 'E-5', 'E-6'],
                "eFlat": ['B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6'],
                "aFlat": ['B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6', 'D-4', 'D-5', 'D-6'],
                "dFlat": ['B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6', 'D-4', 'D-5', 'D-6', 'G-4', 'G-5', 'G-6'],
                "gFlat": ['B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6', 'D-4', 'D-5', 'D-6', 'G-4', 'G-5', 'G-6', 'C-5', 'C-6'],
                "cFlat": ['B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6', 'D-4', 'D-5', 'D-6', 'G-4', 'G-5', 'G-6', 'C-5', 'C-6', 'F-4', 'F-5', 'F-6'],
                "E": ['F#4', 'F#5', 'F#6', 'C#5', 'C#6', 'G#4', 'G#5', 'G#6', 'D#4', 'D#5', 'D#6'],
                "A": ['F#4', 'F#5', 'F#6', 'C#5', 'C#6', 'G#4', 'G#5', 'G#6'],
                "D": ['F#4', 'F#5', 'F#6', 'C#5', 'C#6'],
                "G": ['F#4', 'F#5', 'F#6']
            },
            "2": {
                "C": [],
                "F": ['B-4', 'B-5', 'B-6'],
                "bFlat": ['B-4', 'B-5', 'B-6', 'E-4', 'E-5', 'E-6'],
                "eFlat": ['B-4', 'B-5', 'B-6', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6'],
                "aFlat": ['B-4', 'B-5', 'B-6', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6', 'D-4', 'D-5', 'D-6'],
                "dFlat": ['B-4', 'B-5', 'B-6', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6', 'D-4', 'D-5', 'D-6', 'G-4', 'G-5', 'G-6'],
                "gFlat": ['B-4', 'B-5', 'B-6', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6', 'D-4', 'D-5', 'D-6', 'G-4', 'G-5', 'G-6', 'C-5', 'C-6'],
                "cFlat": ['B-4', 'B-5', 'B-6', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6', 'D-4', 'D-5', 'D-6', 'G-4', 'G-5', 'G-6', 'C-5', 'C-6', 'F-4', 'F-5', 'F-6'],
                "E": ['F#4', 'F#5', 'F#6', 'C#5', 'C#6', 'G#4', 'G#5', 'G#6', 'D#4', 'D#5', 'D#6'],
                "A": ['F#4', 'F#5', 'F#6', 'C#5', 'C#6', 'G#4', 'G#5', 'G#6'],
                "D": ['F#4', 'F#5', 'F#6', 'C#5', 'C#6'],
                "G": ['F#4', 'F#5', 'F#6']
            }
        },
        "Flute": {
            "1": {
                "C": [],
                "F": ['B-4', 'B-5', 'B-6'],
                "bFlat": ['B-4', 'B-5', 'B-6', 'E-4', 'E-5', 'E-6'],
                "eFlat": ['B-4', 'B-5', 'B-6', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6'],
                "aFlat": ['B-4', 'B-5', 'B-6', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6', 'D-4', 'D-5', 'D-6'],
                "dFlat": ['B-4', 'B-5', 'B-6', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6', 'D-4', 'D-5', 'D-6', 'G-4', 'G-5', 'G-6'],
                "gFlat": ['B-4', 'B-5', 'B-6', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6', 'D-4', 'D-5', 'D-6', 'G-4', 'G-5', 'G-6', 'C-4', 'C-5', 'C-6'],
                "cFlat": ['B-4', 'B-5', 'B-6', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6', 'D-4', 'D-5', 'D-6', 'G-4', 'G-5', 'G-6', 'C-4', 'C-5', 'C-6', 'F-4', 'F-5', 'F-6'],
                "E": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'G#6', 'D#4', 'D#5', 'D#6'],
                "A": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'G#6'],
                "D": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6'],
                "G": ['F#4', 'F#5', 'F#6']
            },
            "2": {
                "C": [],
                "F": ['B-4', 'B-5', 'B-6'],
                "bFlat": ['B-4', 'B-5', 'B-6', 'E-4', 'E-5', 'E-6'],
                "eFlat": ['B-4', 'B-5', 'B-6', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6'],
                "aFlat": ['B-4', 'B-5', 'B-6', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6', 'D-4', 'D-5', 'D-6'],
                "dFlat": ['B-4', 'B-5', 'B-6', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6', 'D-4', 'D-5', 'D-6', 'G-4', 'G-5', 'G-6'],
                "gFlat": ['B-4', 'B-5', 'B-6', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6', 'D-4', 'D-5', 'D-6', 'G-4', 'G-5', 'G-6', 'C-4', 'C-5', 'C-6', 'C-7'],
                "cFlat": ['B-4', 'B-5', 'B-6', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6', 'D-4', 'D-5', 'D-6', 'G-4', 'G-5', 'G-6', 'C-4', 'C-5', 'C-6', 'C-7', 'F-4', 'F-5', 'F-6'],
                "E": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'C#7', 'G#4', 'G#5', 'G#6', 'D#4', 'D#5', 'D#6'],
                "A": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'C#7', 'G#4', 'G#5', 'G#6'],
                "D": ['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'C#7'],
                "G": ['F#4', 'F#5', 'F#6']
            }
        },
        "Trombone": {
            "1": {
                "C": [],
                "F": ['B-2', 'B-3'],
                "bFlat": ['B-2', 'B-3', 'E-3', 'E-4'],
                "eFlat": ['B-2', 'B-3', 'E-3', 'E-4', 'A-2', 'A-3'],
                "aFlat": ['B-2', 'B-3', 'E-3', 'E-4', 'A-2', 'A-3', 'D-3', 'D-4'],
                "dFlat": ['B-2', 'B-3', 'E-3', 'E-4', 'A-2', 'A-3', 'D-3', 'D-4', 'G-2', 'G-3'],
                "gFlat": ['B-2', 'B-3', 'E-3', 'E-4', 'A-2', 'A-3', 'D-3', 'D-4', 'G-2', 'G-3', 'C-3', 'C-4'],
                "cFlat": ['B-2', 'B-3', 'E-3', 'E-4', 'A-2', 'A-3', 'D-3', 'D-4', 'G-2', 'G-3', 'C-3', 'C-4', 'F-2', 'F-3', 'F-4'],
                "E": ['F#2', 'F#3', 'F#4', 'C#3', 'C#4', 'G#2', 'G#3', 'D#3', 'D#4'],
                "A": ['F#2', 'F#3', 'F#4', 'C#3', 'C#4', 'G#2', 'G#3'],
                "D": ['F#2', 'F#3', 'F#4', 'C#3', 'C#4'],
                "G": ['F#2', 'F#3', 'F#4']
            },
            "2": {
                "C": [],
                "F": ['B-2', 'B-3'],
                "bFlat": ['B-2', 'B-3', "E-2", 'E-3', 'E-4'],
                "eFlat": ['B-2', 'B-3', "E-2", 'E-3', 'E-4', 'A-2', 'A-3', 'A-4'],
                "aFlat": ['B-2', 'B-3', "E-2", 'E-3', 'E-4', 'A-2', 'A-3', 'A-4', 'D-3', 'D-4'],
                "dFlat": ['B-2', 'B-3', "E-2", 'E-3', 'E-4', 'A-2', 'A-3', 'A-4', 'D-3', 'D-4', 'G-2', 'G-3', 'G-4'],
                "gFlat": ['B-2', 'B-3', "E-2", 'E-3', 'E-4', 'A-2', 'A-3', 'A-4', 'D-3', 'D-4', 'G-2', 'G-3', 'G-4', 'C-3', 'C-4'],
                "cFlat": ['B-2', 'B-3', "E-2", 'E-3', 'E-4', 'A-2', 'A-3', 'A-4', 'D-3', 'D-4', 'G-2', 'G-3', 'G-4', 'C-3', 'C-4', 'F-2', 'F-3', 'F-4'],
                "E": ['F#2', 'F#3', 'F#4', 'C#3', 'C#4', 'G#2', 'G#3', 'G#4', 'D#3', 'D#4'],
                "A": ['F#2', 'F#3', 'F#4', 'C#3', 'C#4', 'G#2', 'G#3', 'G#4'],
                "D": ['F#2', 'F#3', 'F#4', 'C#3', 'C#4'],
                "G": ['F#2', 'F#3', 'F#4']
            }
        },
        "Baritone B.C.": {
            "1": {
                "C": [],
                "F": ['B-2', 'B-3'],
                "bFlat": ['B-2', 'B-3', 'E-3', 'E-4'],
                "eFlat": ['B-2', 'B-3', 'E-3', 'E-4', 'A-2', 'A-3'],
                "aFlat": ['B-2', 'B-3', 'E-3', 'E-4', 'A-2', 'A-3', 'D-3', 'D-4'],
                "dFlat": ['B-2', 'B-3', 'E-3', 'E-4', 'A-2', 'A-3', 'D-3', 'D-4', 'G-2', 'G-3'],
                "gFlat": ['B-2', 'B-3', 'E-3', 'E-4', 'A-2', 'A-3', 'D-3', 'D-4', 'G-2', 'G-3', 'C-3', 'C-4'],
                "cFlat": ['B-2', 'B-3', 'E-3', 'E-4', 'A-2', 'A-3', 'D-3', 'D-4', 'G-2', 'G-3', 'C-3', 'C-4', 'F-2', 'F-3', 'F-4'],
                "E": ['F#2', 'F#3', 'F#4', 'C#3', 'C#4', 'G#2', 'G#3', 'D#3', 'D#4'],
                "A": ['F#2', 'F#3', 'F#4', 'C#3', 'C#4', 'G#2', 'G#3'],
                "D": ['F#2', 'F#3', 'F#4', 'C#3', 'C#4'],
                "G": ['F#2', 'F#3', 'F#4']
            },
            "2": {
                "C": [],
                "F": ['B-2', 'B-3'],
                "bFlat": ['B-2', 'B-3', "E-2", 'E-3', 'E-4'],
                "eFlat": ['B-2', 'B-3', "E-2", 'E-3', 'E-4', 'A-2', 'A-3', 'A-4'],
                "aFlat": ['B-2', 'B-3', "E-2", 'E-3', 'E-4', 'A-2', 'A-3', 'A-4', 'D-3', 'D-4'],
                "dFlat": ['B-2', 'B-3', "E-2", 'E-3', 'E-4', 'A-2', 'A-3', 'A-4', 'D-3', 'D-4', 'G-2', 'G-3', 'G-4'],
                "gFlat": ['B-2', 'B-3', "E-2", 'E-3', 'E-4', 'A-2', 'A-3', 'A-4', 'D-3', 'D-4', 'G-2', 'G-3', 'G-4', 'C-3', 'C-4'],
                "cFlat": ['B-2', 'B-3', "E-2", 'E-3', 'E-4', 'A-2', 'A-3', 'A-4', 'D-3', 'D-4', 'G-2', 'G-3', 'G-4', 'C-3', 'C-4', 'F-2', 'F-3', 'F-4'],
                "E": ['F#2', 'F#3', 'F#4', 'C#3', 'C#4', 'G#2', 'G#3', 'G#4', 'D#3', 'D#4'],
                "A": ['F#2', 'F#3', 'F#4', 'C#3', 'C#4', 'G#2', 'G#3', 'G#4'],
                "D": ['F#2', 'F#3', 'F#4', 'C#3', 'C#4'],
                "G": ['F#2', 'F#3', 'F#4']
            }
        },
        "Bassoon": {
            "1": {
                "C": [],
                "F": ['B-2', 'B-3'],
                "bFlat": ['B-2', 'B-3', 'E-2', 'E-3'],
                "eFlat": ['B-2', 'B-3', 'E-2', 'E-3', 'A-2', 'A-3'],
                "aFlat": ['B-2', 'B-3', 'E-2', 'E-3', 'A-2', 'A-3', 'D-2', 'D-3', 'D-4'],
                "dFlat": ['B-2', 'B-3', 'E-2', 'E-3', 'A-2', 'A-3', 'D-2', 'D-3', 'D-4', 'G-2', 'G-3'],
                "gFlat": ['B-2', 'B-3', 'E-2', 'E-3', 'A-2', 'A-3', 'D-2', 'D-3', 'D-4', 'G-2', 'G-3', 'C-3', 'C-4'],
                "cFlat": ['B-2', 'B-3', 'E-2', 'E-3', 'A-2', 'A-3', 'D-2', 'D-3', 'D-4', 'G-2', 'G-3', 'C-3', 'C-4', 'F-2', 'F-3'],
                "E": ['F#2', 'F#3', 'C#3', 'C#4', 'G#2', 'G#3', 'D#2', 'D#3', 'D#4'],
                "A": ['F#2', 'F#3', 'C#3', 'C#4', 'G#2', 'G#3'],
                "D": ['F#2', 'F#3', 'C#3', 'C#4'],
                "G": ['F#2', 'F#3']
            },
            "2": {
                "C": [],
                "F": ['B-2', 'B-3'],
                "bFlat": ['B-2', 'B-3', 'E-2', 'E-3'],
                "eFlat": ['B-2', 'B-3', 'E-2', 'E-3', 'A-2', 'A-3'],
                "aFlat": ['B-2', 'B-3', 'E-2', 'E-3', 'A-2', 'A-3', 'D-2', 'D-3', 'D-4'],
                "dFlat": ['B-2', 'B-3', 'E-2', 'E-3', 'A-2', 'A-3', 'D-2', 'D-3', 'D-4', 'G-2', 'G-3'],
                "gFlat": ['B-2', 'B-3', 'E-2', 'E-3', 'A-2', 'A-3', 'D-2', 'D-3', 'D-4', 'G-2', 'G-3', 'C-3', 'C-4'],
                "cFlat": ['B-2', 'B-3', 'E-2', 'E-3', 'A-2', 'A-3', 'D-2', 'D-3', 'D-4', 'G-2', 'G-3', 'C-3', 'C-4', 'F-2', 'F-3'],
                "E": ['F#2', 'F#3', 'C#3', 'C#4', 'G#2', 'G#3', 'D#2', 'D#3', 'D#4'],
                "A": ['F#2', 'F#3', 'C#3', 'C#4', 'G#2', 'G#3'],
                "D": ['F#2', 'F#3', 'C#3', 'C#4'],
                "G": ['F#2', 'F#3']
            }
        },
        "Tuba": {
            "1": {
                "C": [],
                "F": ['B-1', 'B-2'],
                "bFlat": ['B-1', 'B-2', 'E-2', 'E-3'],
                "eFlat": ['B-1', 'B-2', 'E-2', 'E-3', 'A-1', 'A-2'],
                "aFlat": ['B-1', 'B-2', 'E-2', 'E-3', 'A-1', 'A-2', 'D-2', 'D-3'],
                "dFlat": ['B-1', 'B-2', 'E-2', 'E-3', 'A-1', 'A-2', 'D-2', 'D-3', 'G-1', 'G-2'],
                "gFlat": ['B-1', 'B-2', 'E-2', 'E-3', 'A-1', 'A-2', 'D-2', 'D-3', 'G-1', 'G-2', 'C-2', 'C-3'],
                "cFlat": ['B-1', 'B-2', 'E-2', 'E-3', 'A-1', 'A-2', 'D-2', 'D-3', 'G-1', 'G-2', 'C-2', 'C-3', 'F-1', 'F-2', 'F-3'],
                "E": ['F#1', 'F#2', 'F#3', 'C#2', 'C#3', 'G#1', 'G#2', 'D#2', 'D#3'],
                "A": ['F#1', 'F#2', 'F#3', 'C#2', 'C#3', 'G#1', 'G#2'],
                "D": ['F#1', 'F#2', 'F#3', 'C#2', 'C#3'],
                "G": ['F#1', 'F#2', 'F#3']
            },
            "2": {
                "C": [],
                "F": ['B-1', 'B-2'],
                "bFlat": ['B-1', 'B-2', 'E-1', 'E-2', 'E-3'],
                "eFlat": ['B-1', 'B-2', 'E-1', 'E-2', 'E-3', 'A-1', 'A-2', 'A-3'],
                "aFlat": ['B-1', 'B-2', 'E-1', 'E-2', 'E-3', 'A-1', 'A-2', 'A-3', 'D-2', 'D-3'],
                "dFlat": ['B-1', 'B-2', 'E-1', 'E-2', 'E-3', 'A-1', 'A-2', 'A-3', 'D-2', 'D-3', 'G-1', 'G-2', 'G-3'],
                "gFlat": ['B-1', 'B-2', 'E-1', 'E-2', 'E-3', 'A-1', 'A-2', 'A-3', 'D-2', 'D-3', 'G-1', 'G-2', 'G-3', 'C-2', 'C-3'],
                "cFlat": ['B-1', 'B-2', 'E-1', 'E-2', 'E-3', 'A-1', 'A-2', 'A-3', 'D-2', 'D-3', 'G-1', 'G-2', 'G-3', 'C-2', 'C-3', 'F-1', 'F-2', 'F-3'],
                "E": ['F#1', 'F#2', 'F#3', 'C#2', 'C#3', 'G#1', 'G#2', 'G#3,' 'D#2', 'D#3'],
                "A": ['F#1', 'F#2', 'F#3', 'C#2', 'C#3', 'G#1', 'G#2', 'G#3'],
                "D": ['F#1', 'F#2', 'F#3', 'C#2', 'C#3'],
                "G": ['F#1', 'F#2', 'F#3']
            }
        },
        "Alto Clarinet": {
            "1": {
                "eFlat": [],
                "aFlat": ['B-3', 'B-4', 'B-5'],
                "dFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5'],
                "gFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5'],
                "cFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5', 'D-4', 'D-5'],
                "E": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4', 'A#5', 'E#3', 'E#4', 'E#5', 'B#3', 'B#4', 'B#5'],
                "A": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4', 'A#5', 'E#3', 'E#4', 'E#5'],
                "D": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4', 'A#5'],
                "G": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5'],
                "C": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5'],
                "F": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6'],
                "bFlat": ['F#3', 'F#4', 'F#5']
            },
            "2": {
                "eFlat": [],
                "aFlat": ['B-3', 'B-4', 'B-5'],
                "dFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5'],
                "gFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5'],
                "cFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5', 'D-4', 'D-5'],
                "E": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4', 'A#5', 'E#3', 'E#4', 'E#5', 'B#3', 'B#4', 'B#5'],
                "A": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4', 'A#5', 'E#3', 'E#4', 'E#5'],
                "D": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4', 'A#5'],
                "G": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5'],
                "C": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5'],
                "F": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6'],
                "bFlat": ['F#3', 'F#4', 'F#5']
            }
        },
        "Bass Clarinet": {
            "1": {
                "bFlat": [],
                "eFlat": ['B-3', 'B-4', 'B-5'],
                "aFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5'],
                "dFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5'],
                "gFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5', 'D-4', 'D-5'],
                "cFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5', 'D-4', 'D-5', 'G-3', 'G-4', 'G-5'],
                "E": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4', 'A#5', 'E#3', 'E#4', 'E#5'],
                "A": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4', 'A#5'],
                "D": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5'],
                "G": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5'],
                "C": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6'],
                "F": ['F#3', 'F#4', 'F#5']
            },
            "2": {
                "bFlat": [],
                "eFlat": ['B-3', 'B-4', 'B-5'],
                "aFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5'],
                "dFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5'],
                "gFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5', 'D-4', 'D-5'],
                "cFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5', 'D-4', 'D-5', 'G-3', 'G-4', 'G-5'],
                "E": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4', 'A#5', 'E#3', 'E#4', 'E#5'],
                "A": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4', 'A#5'],
                "D": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5'],
                "G": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5'],
                "C": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6'],
                "F": ['F#3', 'F#4', 'F#5']
            }
        },
        "Contrabass Clarinet": {
            "1": {
                "bFlat": [],
                "eFlat": ['B-3', 'B-4', 'B-5'],
                "aFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5'],
                "dFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5'],
                "gFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5', 'D-4', 'D-5'],
                "cFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5', 'D-4', 'D-5', 'G-3', 'G-4', 'G-5'],
                "E": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4', 'A#5', 'E#3', 'E#4', 'E#5'],
                "A": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4', 'A#5'],
                "D": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5'],
                "G": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5'],
                "C": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6'],
                "F": ['F#3', 'F#4', 'F#5']
            },
            "2": {
                "bFlat": [],
                "eFlat": ['B-3', 'B-4', 'B-5'],
                "aFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5'],
                "dFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5'],
                "gFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5', 'D-4', 'D-5'],
                "cFlat": ['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5', 'D-4', 'D-5', 'G-3', 'G-4', 'G-5'],
                "E": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4', 'A#5', 'E#3', 'E#4', 'E#5'],
                "A": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4', 'A#5'],
                "D": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5'],
                "G": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5'],
                "C": ['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6'],
                "F": ['F#3', 'F#4', 'F#5']
            }
        }
    }'''
