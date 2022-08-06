import random
#from myly import CreateMusicXML
from music21 import *
from IPython import embed

def create_range(instrument, key_signature):

    if instrument == "French Horn":
        k = key.Key(key_signature).transpose(-5)
        c = clef.TrebleClef()
        range_ = ['F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5']
        if key_signature == "bFlat":
            range_.extend(['B-3', 'B-4'])
        elif key_signature == "eFlat":
            range_.extend(['B-3', 'B-4', 'E-4', 'E-5'])
        elif key_signature == "aFlat":
            range_.extend(['B-3', 'B-4', 'E-4', 'E-5', 'A-3', 'A-4'])
        elif key_signature == "dFlat":
            range_.extend(['B-3', 'B-4', 'E-4', 'E-5', 'A-3', 'A-4', 'D-4', 'D-5'])
        elif key_signature == "gFlat":
            range_.extend(['B-3', 'B-4', 'E-4', 'E-5', 'A-3', 'A-4', 'D-4', 'D-5', 'G-3', 'G-4'])
        elif key_signature == "cFlat":
            range_.extend(['B-3', 'B-4', 'E-4', 'E-5', 'A-3', 'A-4', 'D-4', 'D-5', 'G-3', 'G-4', 'C-4', 'C-5'])
        elif key_signature == "E":
            range_.extend(['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'G#3', 'G#4', 'D#4', 'D#5', 'A#3', 'A#4'])
        elif key_signature == "A":
            range_.extend(['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'G#3', 'G#4', 'D#4', 'D#5'])
        elif key_signature == "D":
            range_.extend(['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'G#3', 'G#4'])
        elif key_signature == "G":
            range_.extend(['F#3', 'F#4', 'F#5', 'C#4', 'C#5'])
        elif key_signature == "C":
            range_.extend(['F#3', 'F#4', 'F#5'])
    elif instrument == "Trumpet" or instrument == "Baritone T.C.":
        k = key.Key(key_signature).transpose(2)
        c = clef.TrebleClef()
        range_ = ['G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5']
        if key_signature == "eFlat":
            range_.extend(['B-3', 'B-4'])
        elif key_signature == "aFlat":
            range_.extend(['B-3', 'B-4', 'E-4', 'E-5'])
        elif key_signature == "dFlat":
            range_.extend(['B-3', 'B-4', 'E-4', 'E-5', 'A-3', 'A-4'])
        elif key_signature == "gFlat":
            range_.extend(['B-3', 'B-4', 'E-4', 'E-5', 'A-3', 'A-4', 'D-4', 'D-5'])
        elif key_signature == "cFlat":
            range_.extend(['B-3', 'B-4', 'E-4', 'E-5', 'A-3', 'A-4', 'D-4', 'D-5', 'G-3', 'G-4', 'G-5'])
        elif key_signature == "E":
            range_.extend(['F#4', 'F#5', 'C#4', 'C#5', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4', 'E#4', 'E#5'])
        elif key_signature == "A":
            range_.extend(['F#4', 'F#5', 'C#4', 'C#5', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4'])
        elif key_signature == "D":
            range_.extend(['F#4', 'F#5', 'C#4', 'C#5', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5'])
        elif key_signature == "G":
            range_.extend(['F#4', 'F#5', 'C#4', 'C#5', 'G#3', 'G#4', 'G#5'])
        elif key_signature == "C":
            range_.extend(['F#4', 'F#5', 'C#4', 'C#5'])
        elif key_signature == "F":
            range_.extend(['F#4', 'F#5'])
    elif instrument == "Alto Saxophone" or instrument == "Baritone Saxophone":
        k = key.Key(key_signature).transpose(9)
        c = clef.TrebleClef()
        range_ = ['B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'F6']
        if key_signature == "aFlat":
            range_.extend(['B-3', 'B-4', 'B-5'])
        elif key_signature == "dFlat":
            range_.extend(['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6'])
        elif key_signature == "gFlat":
            range_.extend(['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5'])
        elif key_signature == "cFlat":
            range_.extend(['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'D-4', 'D-5', 'D-6'])
        elif key_signature == "E":
            range_.extend(['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6', 'A#4', 'A#5', 'E#4', 'E#5', 'E#6', 'B#3', 'B#4', 'B#5'])
        elif key_signature == "A":
            range_.extend(['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6', 'A#4', 'A#5', 'E#4', 'E#5', 'E#6'])
        elif key_signature == "D":
            range_.extend(['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6', 'A#4', 'A#5'])
        elif key_signature == "G":
            range_.extend(['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6'])
        elif key_signature == "C":
            range_.extend(['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5'])
        elif key_signature == "F":
            range_.extend(['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6'])
        elif key_signature == "bFlat":
            range_.extend(['F#4', 'F#5', 'F#6'])
    elif instrument == "Tenor Saxophone":
        k = key.Key(key_signature).transpose(2)
        c = clef.TrebleClef()
        range_ = ['B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'F6']
        if key_signature == "eFlat":
            range_.extend(['B-3', 'B-4', 'B-5'])
        elif key_signature == "aFlat":
            range_.extend(['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6'])
        elif key_signature == "dFlat":
            range_.extend(['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5'])
        elif key_signature == "gFlat":
            range_.extend(['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'D-4', 'D-5', 'D-6'])
        elif key_signature == "cFlat":
            range_.extend(['B-3', 'B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'D-4', 'D-5', 'D-6', 'G-4', 'G-5'])
        elif key_signature == "E":
            range_.extend(['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6', 'A#4', 'A#5', 'E#4', 'E#5', 'E#6'])
        elif key_signature == "A":
            range_.extend(['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6', 'A#4', 'A#5'])
        elif key_signature == "D":
            range_.extend(['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6'])
        elif key_signature == "G":
            range_.extend(['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5'])
        elif key_signature == "C":
            range_.extend(['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6'])
        elif key_signature == "F":
            range_.extend(['F#4', 'F#5', 'F#6'])

    elif instrument == "Clarinet":
        k = key.Key(key_signature).transpose(2)
        c = clef.TrebleClef()
        range_ = ['E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'F6']
        if key_signature == "eFlat":
            range_.extend(['B-3', 'B-4', 'B-5'])
        elif key_signature == "aFlat":
            range_.extend(['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'E-6'])
        elif key_signature == "dFlat":
            range_.extend(['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'E-6', 'A-3', 'A-4', 'A-5'])
        elif key_signature == "gFlat":
            range_.extend(['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'E-6', 'A-3', 'A-4', 'A-5', 'D-4', 'D-5', 'D-6'])
        elif key_signature == "cFlat":
            range_.extend(['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'E-6', 'A-3', 'A-4', 'A-5', 'D-4', 'D-5', 'D-6', 'G-3', 'G-4', 'G-5'])
        elif key_signature == "E":
            range_.extend(['F#3', 'F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6', 'A#3', 'A#4', 'A#5', 'E#3', 'E#4', 'E#5', 'E#6'])
        elif key_signature == "A":
            range_.extend(['F#3', 'F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6', 'A#3', 'A#4', 'A#5'])
        elif key_signature == "D":
            range_.extend(['F#3', 'F#4', 'F#5', 'F#6',  'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'D#6'])
        elif key_signature == "G":
            range_.extend(['F#3', 'F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5'])
        elif key_signature == "C":
            range_.extend(['F#3', 'F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6'])
        elif key_signature == "F":
            range_.extend(['F#3', 'F#4', 'F#5', 'F#6',])
    elif instrument == "Oboe":
        k = key.Key(key_signature)#.transpose(2)
        c = clef.TrebleClef()
        range_ = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6']
        if key_signature == "F":
            range_.extend(['B-4', 'B-5'])
        elif key_signature == "bFlat":
            range_.extend(['B-4', 'B-5', 'E-4', 'E-5'])
        elif key_signature == "eFlat":
            range_.extend(['B-4', 'B-5', 'E-4', 'E-5', 'A-4', 'A-5'])
        elif key_signature == "aFlat":
            range_.extend(['B-4', 'B-5', 'E-4', 'E-5', 'A-4', 'A-5', 'D-4', 'D-5'])
        elif key_signature == "dFlat":
            range_.extend(['B-4', 'B-5', 'E-4', 'E-5', 'A-4', 'A-5', 'D-4', 'D-5', 'G-4', 'G-5'])
        elif key_signature == "gFlat":
            range_.extend(['B-4', 'B-5', 'E-4', 'E-5', 'A-4', 'A-5', 'D-4', 'D-5', 'G-4', 'G-5', 'C-4', 'C-5', 'C-6'])
        elif key_signature == "cFlat":
            range_.extend(['B-4', 'B-5', 'E-4', 'E-5', 'A-4', 'A-5', 'D-4', 'D-5', 'G-4', 'G-5', 'C-4', 'C-5', 'C-6', 'F-4', 'F-5'])
        elif key_signature == "E":
            range_.extend(['F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'D#4', 'D#5'])
        elif key_signature == "A":
            range_.extend(['F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5'])
        elif key_signature == "D":
            range_.extend(['F#4', 'F#5', 'C#4', 'C#5', 'C#6'])
        elif key_signature == "G":
            range_.extend(['F#4', 'F#5'])
    elif instrument == "Piccolo":
        k = key.Key(key_signature)
        c = clef.TrebleClef()
        range_ = ['D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'E4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'F6', 'G6', 'A6']
        if key_signature == "F":
            range_.extend(['B-4', 'B-5'])
        elif key_signature == "bFlat":
            range_.extend(['B-4', 'B-5', 'E-4', 'E-5', 'E-6'])
        elif key_signature == "eFlat":
            range_.extend(['B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6'])
        elif key_signature == "aFlat":
            range_.extend(['B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6', 'D-4', 'D-5', 'D-6'])
        elif key_signature == "dFlat":
            range_.extend(['B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6', 'D-4', 'D-5', 'D-6', 'G-4', 'G-5', 'G-6'])
        elif key_signature == "gFlat":
            range_.extend(['B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6', 'D-4', 'D-5', 'D-6', 'G-4', 'G-5', 'G-6', 'C-5', 'C-6'])
        elif key_signature == "cFlat":
            range_.extend(['B-4', 'B-5', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6', 'D-4', 'D-5', 'D-6', 'G-4', 'G-5', 'G-6', 'C-5', 'C-6', 'F-4', 'F-5', 'F-6'])
        elif key_signature == "E":
            range_.extend(['F#4', 'F#5', 'F#6', 'C#5', 'C#6', 'G#4', 'G#5', 'G#6', 'D#4', 'D#5', 'D#6'])
        elif key_signature == "A":
            range_.extend(['F#4', 'F#5', 'F#6', 'C#5', 'C#6', 'G#4', 'G#5', 'G#6'])
        elif key_signature == "D":
            range_.extend(['F#4', 'F#5', 'F#6', 'C#5', 'C#6'])
        elif key_signature == "G":
            range_.extend(['F#4', 'F#5', 'F#6'])
    elif instrument == "Flute":
        k = key.Key(key_signature)#.transpose(2)
        c = clef.TrebleClef()
        range_ = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'F6', 'G6', 'A6', 'B6']
        if key_signature == "F":
            range_.extend(['B-4', 'B-5', 'B-6'])
        elif key_signature == "bFlat":
            range_.extend(['B-4', 'B-5', 'B-6', 'E-4', 'E-5', 'E-6'])
        elif key_signature == "eFlat":
            range_.extend(['B-4', 'B-5', 'B-6', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6'])
        elif key_signature == "aFlat":
            range_.extend(['B-4', 'B-5', 'B-6', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6', 'D-4', 'D-5', 'D-6'])
        elif key_signature == "dFlat":
            range_.extend(['B-4', 'B-5', 'B-6', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6', 'D-4', 'D-5', 'D-6', 'G-4', 'G-5', 'G-6'])
        elif key_signature == "gFlat":
            range_.extend(['B-4', 'B-5', 'B-6', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6', 'D-4', 'D-5', 'D-6', 'G-4', 'G-5', 'G-6', 'C-4', 'C-5', 'C-6'])
        elif key_signature == "cFlat":
            range_.extend(['B-4', 'B-5', 'B-6', 'E-4', 'E-5', 'E-6', 'A-4', 'A-5', 'A-6', 'D-4', 'D-5', 'D-6', 'G-4', 'G-5', 'G-6', 'C-4', 'C-5', 'C-6', 'F-4', 'F-5', 'F-6'])
        elif key_signature == "E":
            range_.extend(['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'G#6', 'D#4', 'D#5', 'D#6'])
        elif key_signature == "A":
            range_.extend(['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6', 'G#4', 'G#5', 'G#6'])
        elif key_signature == "D":
            range_.extend(['F#4', 'F#5', 'F#6', 'C#4', 'C#5', 'C#6'])
        elif key_signature == "G":
            range_.extend(['F#4', 'F#5', 'F#6'])
    elif instrument == "Trombone" or instrument == "Baritone B.C.":
        k = key.Key(key_signature)
        c = clef.BassClef()
        range_ = ['F2', 'G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4']
        if key_signature == "F":
            range_.extend(['B-2', 'B-3'])
        elif key_signature == "bFlat":
            range_.extend(['B-2', 'B-3', 'E-3', 'E-4'])
        elif key_signature == "eFlat":
            range_.extend(['B-2', 'B-3', 'E-3', 'E-4', 'A-2', 'A-3'])
        elif key_signature == "aFlat":
            range_.extend(['B-2', 'B-3', 'E-3', 'E-4', 'A-2', 'A-3', 'D-3', 'D-4'])
        elif key_signature == "dFlat":
            range_.extend(['B-2', 'B-3', 'E-3', 'E-4', 'A-2', 'A-3', 'D-3', 'D-4', 'G-2', 'G-3'])
        elif key_signature == "gFlat":
            range_.extend(['B-2', 'B-3', 'E-3', 'E-4', 'A-2', 'A-3', 'D-3', 'D-4', 'G-2', 'G-3', 'C-3', 'C-4'])
        elif key_signature == "cFlat":
            range_.extend(['B-2', 'B-3', 'E-3', 'E-4', 'A-2', 'A-3', 'D-3', 'D-4', 'G-2', 'G-3', 'C-3', 'C-4', 'F-2', 'F-3', 'F-4'])
        elif key_signature == "E":
            range_.extend(['F#2', 'F#3', 'F#4', 'C#3', 'C#4', 'G#2', 'G#3', 'D#3', 'D#4'])
        elif key_signature == "A":
            range_.extend(['F#2', 'F#3', 'F#4', 'C#3', 'C#4', 'G#2', 'G#3'])
        elif key_signature == "D":
            range_.extend(['F#2', 'F#3', 'F#4', 'C#3', 'C#4'])
        elif key_signature == "G":
            range_.extend(['F#2', 'F#3', 'F#4'])
    elif instrument == "Bassoon":
        k = key.Key(key_signature)
        c = clef.BassClef()
        range_ = ['D2', 'E2', 'F2', 'G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4']
        if key_signature == "F":
            range_.extend(['B-2', 'B-3'])
        elif key_signature == "bFlat":
            range_.extend(['B-2', 'B-3', 'E-2', 'E-3'])
        elif key_signature == "eFlat":
            range_.extend(['B-2', 'B-3', 'E-2', 'E-3', 'A-2', 'A-3'])
        elif key_signature == "aFlat":
            range_.extend(['B-2', 'B-3', 'E-2', 'E-3', 'A-2', 'A-3', 'D-2', 'D-3', 'D-4'])
        elif key_signature == "dFlat":
            range_.extend(['B-2', 'B-3', 'E-2', 'E-3', 'A-2', 'A-3', 'D-2', 'D-3', 'D-4', 'G-2', 'G-3'])
        elif key_signature == "gFlat":
            range_.extend(['B-2', 'B-3', 'E-2', 'E-3', 'A-2', 'A-3', 'D-2', 'D-3', 'D-4', 'G-2', 'G-3', 'C-3', 'C-4'])
        elif key_signature == "cFlat":
            range_.extend(['B-2', 'B-3', 'E-2', 'E-3', 'A-2', 'A-3', 'D-2', 'D-3', 'D-4', 'G-2', 'G-3', 'C-3', 'C-4', 'F-2', 'F-3'])
        elif key_signature == "E":
            range_.extend(['F#2', 'F#3', 'C#3', 'C#4', 'G#2', 'G#3', 'D#2', 'D#3', 'D#4'])
        elif key_signature == "A":
            range_.extend(['F#2', 'F#3', 'C#3', 'C#4', 'G#2', 'G#3'])
        elif key_signature == "D":
            range_.extend(['F#2', 'F#3', 'C#3', 'C#4'])
        elif key_signature == "G":
            range_.extend(['F#2', 'F#3'])
    elif instrument == "Tuba":
        k = key.Key(key_signature)
        c = clef.BassClef()
        range_ = ['F1', 'G1', 'A1', 'B1', 'C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3']
        if key_signature == "F":
            range_.extend(['B-1', 'B-2'])
        elif key_signature == "bFlat":
            range_.extend(['B-1', 'B-2', 'E-2', 'E-3'])
        elif key_signature == "eFlat":
            range_.extend(['B-1', 'B-2', 'E-2', 'E-3', 'A-1', 'A-2'])
        elif key_signature == "aFlat":
            range_.extend(['B-1', 'B-2', 'E-2', 'E-3', 'A-1', 'A-2', 'D-2', 'D-3'])
        elif key_signature == "dFlat":
            range_.extend(['B-1', 'B-2', 'E-2', 'E-3', 'A-1', 'A-2', 'D-2', 'D-3', 'G-1', 'G-2'])
        elif key_signature == "gFlat":
            range_.extend(['B-1', 'B-2', 'E-2', 'E-3', 'A-1', 'A-2', 'D-2', 'D-3', 'G-1', 'G-2', 'C-2', 'C-3'])
        elif key_signature == "cFlat":
            range_.extend(['B-1', 'B-2', 'E-2', 'E-3', 'A-1', 'A-2', 'D-2', 'D-3', 'G-1', 'G-2', 'C-2', 'C-3', 'F-1', 'F-2', 'F-3'])
        elif key_signature == "E":
            range_.extend(['F#1', 'F#2', 'F#3', 'C#2', 'C#3', 'G#1', 'G#2', 'D#2', 'D#3'])
        elif key_signature == "A":
            range_.extend(['F#1', 'F#2', 'F#3', 'C#2', 'C#3', 'G#1', 'G#2'])
        elif key_signature == "D":
            range_.extend(['F#1', 'F#2', 'F#3', 'C#2', 'C#3'])
        elif key_signature == "G":
            range_.extend(['F#1', 'F#2', 'F#3'])
    elif instrument == "Alto Clarinet":
        k = key.Key(key_signature).transpose(9)
        c = clef.TrebleClef()
        range_ = ['E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6']
        if key_signature == "aFlat":
            range_.extend(['B-3', 'B-4', 'B-5'])
        elif key_signature == "dFlat":
            range_.extend(['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5'])
        elif key_signature == "gFlat":
            range_.extend(['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5'])
        elif key_signature == "cFlat":
            range_.extend(['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5', 'D-4', 'D-5'])
        elif key_signature == "E":
            range_.extend(['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4', 'A#5', 'E#3', 'E#4', 'E#5', 'B#3', 'B#4', 'B#5'])
        elif key_signature == "A":
            range_.extend(['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4', 'A#5', 'E#3', 'E#4', 'E#5'])
        elif key_signature == "D":
            range_.extend(['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4', 'A#5'])
        elif key_signature == "G":
            range_.extend(['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5'])
        elif key_signature == "C":
            range_.extend(['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5'])
        elif key_signature == "F":
            range_.extend(['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6'])
        elif key_signature == "bFlat":
            range_.extend(['F#3', 'F#4', 'F#5'])
    elif instrument == "Bass Clarinet" or instrument == "Contrabass Clarinet":
        k = key.Key(key_signature).transpose(2)
        c = clef.TrebleClef()
        range_ = ['E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6']
        if key_signature == "eFlat":
            range_.extend(['B-3', 'B-4', 'B-5'])
        elif key_signature == "aFlat":
            range_.extend(['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5'])
        elif key_signature == "dFlat":
            range_.extend(['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5'])
        elif key_signature == "gFlat":
            range_.extend(['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5', 'D-4', 'D-5'])
        elif key_signature == "cFlat":
            range_.extend(['B-3', 'B-4', 'B-5', 'E-3', 'E-4', 'E-5', 'A-3', 'A-4', 'A-5', 'D-4', 'D-5', 'G-3', 'G-4', 'G-5'])
        elif key_signature == "E":
            range_.extend(['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4', 'A#5', 'E#3', 'E#4', 'E#5'])
        elif key_signature == "A":
            range_.extend(['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5', 'A#3', 'A#4', 'A#5'])
        elif key_signature == "D":
            range_.extend(['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5', 'D#4', 'D#5'])
        elif key_signature == "G":
            range_.extend(['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6', 'G#3', 'G#4', 'G#5'])
        elif key_signature == "C":
            range_.extend(['F#3', 'F#4', 'F#5', 'C#4', 'C#5', 'C#6'])
        elif key_signature == "F":
            range_.extend(['F#3', 'F#4', 'F#5'])
    return range_, k, c


def make_random_music(time_signature, key_signature, measures, instrument, save_to='im/image.pdf'):
    #return [[(34, 1/2), (37, 1/4), 33, ...], [(23, 1), ...] , ...]

    #41, 43, 45, 47, 48, 50, 52, 53, 55, 57, 59, 60, 62, 64, 65, respectively

    #NATURAL ACCIDENTALS TO BE REMOVED

    range_,k,c = create_range(instrument, key_signature)

    length = []
    #whole =
    #half = 2
    #quarter = 1
    for i in range(int(measures)):
        if time_signature == '4/4':
            options = ['whole', 'half', 'quarter']
            choice = random.choice(options)
            length.append(choice)
            if choice == 'whole':
                continue
            elif choice == 'half':
                options.remove('whole')
                optionone = ['quarter', 'quarter']
                optiontwo = ['half']
                length.extend(random.choice([optionone, optiontwo]))
            elif choice == 'quarter':
                options.remove('whole')
                optionthree = ['quarter', 'half']
                optionfour = ['quarter', 'quarter', 'quarter']
                optionfive = ['half', 'quarter']
                length.extend(random.choice([optionthree, optionfour, optionfive]))
        elif time_signature == '3/4':
                options = ['half', 'quarter']
                choice = random.choice(options)
                length.append(choice)
                if choice == 'half':
                    length.append('quarter')
                elif choice == 'quarter':
                    length.append('half')
        elif time_signature == '2/4':
                options = ['half', 'quarter']
                choice = random.choice(options)
                length.append(choice)
                if choice == 'half':
                    continue
                elif choice == 'quarter':
                    length.append('quarter')
    set = []
    for i in length:
        set_approach = [random.choice(range_), i]
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
    #k = key.Key(key_signature)
    s.append(k)
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
    make_random_music('4/4', 'F', 'Treble', '16', 'French Horn')
