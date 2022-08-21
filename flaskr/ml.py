## TODO: process the dataset using pandas or something

## TODO: train and save the model (THIS IS WHERE THE EXPERIMENTATION HAPPENS)

## TODO: function for executing model to create new music
import pickle
import os
from music21 import *
import numpy as np
import pandas as pd
from tqdm import tqdm
from sklearn.neural_network import MLPClassifier
import json
from IPython import embed

MELODY_NOTE_OFF = 128 # (stop playing all previous notes)
MELODY_NO_EVENT = 129 # (no change from previous event)
def streamToNoteArray(stream):
    """
    Convert a Music21 sequence to a numpy array of int8s into Melody-RNN format:
        0-127 - note on at specified pitch
        128   - note off
        129   - no event
    """
    # Part one, extract from stream
    total_length = np.int(np.round(stream.flat.highestTime / 0.25)) # in semiquavers
    stream_list = []
    for element in stream.flat:
        if isinstance(element, note.Note):
            stream_list.append([np.round(element.offset / 0.25), np.round(element.quarterLength / 0.25), element.pitch.midi])
        elif isinstance(element, chord.Chord):
            stream_list.append([np.round(element.offset / 0.25), np.round(element.quarterLength / 0.25), element.sortAscending().pitches[-1].midi])
    np_stream_list = np.array(stream_list, dtype=object)
    df = pd.DataFrame({'pos': np_stream_list.T[0], 'dur': np_stream_list.T[1], 'pitch': np_stream_list.T[2]})
    df = df.sort_values(['pos','pitch'], ascending=[True, False]) # sort the dataframe properly
    df = df.drop_duplicates(subset=['pos']) # drop duplicate values
    # part 2, convert into a sequence of note events
    output = np.zeros(total_length+1, dtype=np.int16) + np.int16(MELODY_NO_EVENT)  # set array full of no events by default.
    # Fill in the output list
    for i in range(total_length):
        if not df[df.pos==i].empty:
            n = df[df.pos==i].iloc[0] # pick the highest pitch at each semiquaver
            output[i] = n.pitch # set note on
            output[i+n.dur] = MELODY_NOTE_OFF
    return output

'''counter = 0
notes_dict = {}
for foldername in tqdm(os.listdir('flaskr/static/musicset')):
    for fname in os.listdir('flaskr/static/musicset/' + foldername):
        full_path = 'flaskr/static/musicset/' + foldername + '/' + fname

        mf = midi.MidiFile()
        mf.open(full_path)
        mf.read()

        mf.close()
        s = midi.translate.midiFileToStream(mf)
        notes_arr = streamToNoteArray(s)

        notes_dict[fname] = notes_arr.tolist()
        counter += 1

import json
with open('notes_data.json', 'w') as fp:
    json.dump(notes_dict, fp)'''

def train_mode(data):
    songlist = list(data.values())
    X = []
    y = []
    for song in songlist:
        for i in range(len(song)-3):
            X.append([song[i], song[i+1], song[i+2]])
            y.append([song[i+3]])


    clf = MLPClassifier(hidden_layer_sizes=(5, 2))
    clf.fit(X, y)
    #print(clf)
    file_name = 'finalized_model.sav'
    pickle.dump(clf, open(file_name, 'wb'))
    #f.close
    return clf

f = open('flaskr/notes_data.json')
data = json.load(f)
clf = train_mode(data)
print('SUCCESS')
