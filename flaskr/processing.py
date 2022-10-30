
import random
from music21 import *
from IPython import embed
import pickle
import music21
from sklearn.neural_network import *
import numpy as np

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
    }

    base_range = {
        "1": {
            "Flute": ['71', '72', '74', '76', '77', '79', '81', '83'],
            "Piccolo": ['71', '72', '74', '76', '77', '79', '81', '83'],
            "Oboe": ['60', '62', '64', '65', '67', '69', '71', '72'],
            "Clarinet": ['59', '60', '62', '64', '65', '67', '69', '71'],
            "Alto Saxophone": ['65', '67', '69', '71', '72', '74', '76', '77'],
            "Tenor Saxophone": ['65', '67', '69', '71', '72', '74', '76', '77'],
            "Baritone Saxophone": ['65', '67', '69', '71', '72', '74', '76', '77'],
            "French Horn": ['59', '60', '62', '64', '65', '67', '69', '71'],
            "Trumpet": ['60', '62', '64', '65', '67', '69', '71', '72'],
            "Trombone": ['47', '48', '50', '52', '53', '55', '57', '59'],
            "Bassoon": ['47', '48', '50', '52', '53', '55', '57', '59'],
            "Tuba": ['35', '36', '38', '40', '41', '43', '45', '47'],
            "Baritone B.C.": ['47', '48', '50', '52', '53', '55', '57', '59'],
            "Baritone T.C.": ['60', '62', '64', '65', '67', '69', '71', '72'],
            "Alto Clarinet": ['59', '60', '62', '64', '65', '67', '69', '71'],
            "Bass Clarinet": ['59', '60', '62', '64', '65', '67', '69', '71']
        },
        "2": {
            "Flute": ['65', '67', '69', '71', '72', '74', '76', '77', '79', '81', '83', '84', '86', '88'],
            "Piccolo": ['65', '67', '69', '71', '64', '72', '74', '76', '77', '79', '81', '83', '84', '86', '88'],
            "Oboe": ['60', '62', '64', '65', '67', '69', '71', '72', '74', '76', '77', '79', '81', '83'],
            "Clarinet": ['53', '55', '57', '59', '60', '62', '64', '65', '67', '69', '71', '72', '74', '76', '77', '79', '81'],
            "Alto Saxophone": ['60', '62', '64', '65', '67', '69', '71', '72', '74', '76', '77', '79', '81', '83'],
            "Tenor Saxophone": ['60', '62', '64', '65', '67', '69', '71', '72', '74', '76', '77', '79', '81', '83'],
            "Baritone Saxophone": ['60', '62', '64', '65', '67', '69', '71', '72', '74', '76', '77', '79', '81', '83'],
            "French Horn": ['57', '59', '60', '62', '64', '65', '67', '69', '71', '72', '74', '76', '77'],
            "Trumpet": ['57', '59', '60', '62', '64', '65', '67', '69', '71', '72', '74', '76', '77', '79'],
            "Trombone": ['45', '47', '48', '50', '52', '53', '55', '57', '59', '60', '62', '64', '65'],
            "Bassoon": ['40', '41', '43', '45', '47', '48', '50', '52', '53', '55', '57', '59', '60', '62', '64'],
            "Tuba": ['31', '33', '35', '36', '38', '40', '41', '43', '45', '47', '48', '50', '52'],
            "Baritone B.C.": ['45', '47', '48', '50', '52', '53', '55', '57', '59', '60', '62', '64', '65'],
            "Baritone T.C.": ['59', '60', '62', '64', '65', '67', '69', '71', '72', '74', '76', '77', '79'],
            "Alto Clarinet": ['53', '55', '57', '59', '60', '62', '64', '65', '67', '69', '71', '72', '74', '76', '77', '79'],
            "Bass Clarinet": ['53', '55', '57', '59', '60', '62', '64', '65', '67', '69', '71', '72', '74', '76']
        },
        "3": {
            "Flute": ['60', '62', '64', '65', '67', '69', '71', '72', '74', '76', '77', '79', '81', '83', '84', '86', '88', '89', '91', '93', '95'],
            "Piccolo": ['62', '64', '65', '67', '69', '71', '64', '72', '74', '76', '77', '79', '81', '83', '84', '86', '88', '89', '91', '93', '95'],
            "Oboe": ['59', '60', '62', '64', '65', '67', '69', '71', '72', '74', '76', '77', '79', '81', '83', '84', '86'],
            "Clarinet": ['52', '53', '55', '57', '59', '60', '62', '64', '65', '67', '69', '71', '72', '74', '76', '77', '79', '81', '83', '84', '86'],
            "Alto Saxophone": ['59', '60', '62', '64', '65', '67', '69', '71', '72', '74', '76', '77', '79', '81', '83', '84', '86', '88', '89'],
            "Tenor Saxophone": ['59', '60', '62', '64', '65', '67', '69', '71', '72', '74', '76', '77', '79', '81', '83', '84', '86', '88', '89'],
            "Baritone Saxophone": ['57', '59', '60', '62', '64', '65', '67', '69', '71', '72', '74', '76', '77', '79', '81', '83', '84', '86'],
            "French Horn": ['55', '57', '59', '60', '62', '64', '65', '67', '69', '71', '72', '74', '76', '77', '79', '81'],
            "Trumpet": ['57', '59', '60', '62', '64', '65', '67', '69', '71', '72', '74', '76', '77', '79', '81', '83', '84'],
            "Trombone": ['43', '45', '47', '48', '50', '52', '53', '55', '57', '59', '60', '62', '64', '65', '67', '69', '71'],
            "Bassoon": ['35', '36', '38', '40', '41', '43', '45', '47', '48', '50', '52', '53', '55', '57', '59', '60', '62', '64', '65', '67'],
            "Tuba": ['29', '31', '33', '35', '36', '38', '40', '41', '43', '45', '47', '48', '50', '52', '53', '55'],
            "Baritone B.C.": ['43', '45', '47', '48', '50', '52', '53', '55', '57', '59', '60', '62', '64', '65', '67', '69', '71'],
            "Baritone T.C.": ['57', '59', '60', '62', '64', '65', '67', '69', '71', '72', '74', '76', '77', '79', '81', '83', '84'],
            "Alto Clarinet": ['52', '53', '55', '57', '59', '60', '62', '64', '65', '67', '69', '71', '72', '74', '76', '77', '79', '81', '83', '84'],
            "Bass Clarinet": ['52', '53', '55', '57', '59', '60', '62', '64', '65', '67', '69', '71', '72', '74', '76', '77', '79', '81']
        }
    }

    s = stream.Score()
    s1 = stream.Part(id='1')
    s2 = stream.Part(id='2')
    s.transpose(get_transposition[instrument])
    range_ = base_range[level][instrument]
    c = get_clef[instrument]
    k = key.Key(key_signature).transpose(get_transposition[instrument])
    return range_, c, k


def make_random_music(time_signature, key_signature, measures, instrument, level, save_to='im/image.pdf'):
        range_,k,c = create_range(instrument, key_signature, level)
        length = []
        length1 = []

        loaded_model = pickle.load(open('flaskr/static/finalized_model6.sav', 'rb'))

        if level == "1":
            options = [4.0, 3.0, 2.0, 1.5, 1.0, 0.5]
        elif level == "2":
            options = [4.0, 3.0, 2.0, 1.5, 1.0, 0.5, 0.25]
        elif level == "3":
            options = [4.0, 3.0, 2.0, 1.5, 1.0, 0.5, 1.0/3.0, 0.25]
        time_signature_length = {'6/4': 6.0, '5/4': 5.0, '4/4': 4.0, '3/4': 3.0, '2/4': 2.0}

        for i in range(int(measures)):
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

        set = []
        set1 = []
        last_note_ix = random.choice(range_)




        for i in range(5):
                if level == "1":
                    rand_direction = random.randint(-3,3)
                elif level == "2":
                    rand_direction = random.randint(-5,5)
                elif level == "3":
                    rand_direction = random.randint(-7,7)
                this_note_ix = int(last_note_ix) + rand_direction

                if this_note_ix > int(range_[-1]):
                    this_note_ix = int(range_[-1])
                elif this_note_ix < int(range_[0]):
                    this_note_ix = int(range_[0])

                next_note = this_note_ix
                set.append([next_note, length[i]])
                last_note_ix = this_note_ix
        prediction = loaded_model.predict([[set[0][0], set[1][0], set[2][0], set[3][0], set[4][0]]])
        set.append([prediction[0], length[5]])

        direction_dict = {
            "1": 3,
            "2": 5,
            "3": 7
        }
        range_as_ints = [int(x) for x in range_]
        top_range = last_note_ix+direction_dict[level]
        bottom_range = last_note_ix-direction_dict[level]
        if top_range > range_as_ints[-1]:
            top_range  = range_as_ints[-1]
        elif bottom_range < range_as_ints[0]:
            bottom_range = range_as_ints[0]

        note_range = [ bottom_range  , top_range  ]
        for i in range(len(length)-6):
            #embed()
            probs = loaded_model.predict_proba([[set[i+1][0], set[i+2][0], set[i+3][0], set[i+4][0], set[i+5][0]]])[0]
            #prediction = np.argmax(temp[0])
            elements = [22 + i for i in range(len(probs))]
            #note_range = [last_note_ix-7, last_note_ix+7]

            elements = elements[note_range[0]-22:note_range[1]-22]
            probs = probs[note_range[0]-22:note_range[1]-22]
            probs /= sum(probs)

            #embed()
            prediction = np.random.choice(elements, 1, p=probs)[0]
            #if int(prediction) > int(range_)[-1]:
            #prediction = loaded_model.predict([[set[m-4][0], set[m-3][0], set[m-2][0], set[m-1][0], set[m][0]]])
            set.append([prediction, length[i+6]])
            last_note_ix = int(prediction)



        print(set)
        print(set1)
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
            "Alto Clarinet": music21.instrument.BassClarinet(),
            "Bass Clarinet": music21.instrument.BassClarinet(),
        }

        s = stream.Stream()
        s.insert(0, metadata.Metadata())
        s.metadata.title = instrument + ' Sample'
        s.metadata.composer = ' '
        d = duration.Duration()
        ts = meter.TimeSignature(time_signature)
        dynamic_choice = random.choice(['pp', 'p', 'mp', 'mf', 'f', 'ff'])
        s.append(ts)
        s.append(k)
        s.append(c)
        s.append(instrument_midi[instrument])
        s.append(dynamics.Dynamic(dynamic_choice))


        last_rhythm = 0.0
        for i in set:
            the_option = random.choice(['n', 'r'])
            if the_option == 'n':
                n = note.Note(i[0], quarterLength=float(i[1]))
                acce = articulations.Accent()
                stac = articulations.Staccato()
                tenu = articulations.Tenuto()
                chance_accent = random.randint(1, 9)
                if chance_accent < 2:
                    n.articulations = [random.choice([acce, stac, tenu])]
                else:
                    print("")
                for no in s.notes:
                    no.pitch.accidental = no.getContextByClass(key.KeySignature).accidentalByStep(no.step)
                s.append(n)
                last_rhythm = i[1]
            elif the_option == 'r' and i[1] == 3.0 or i[1] == 1.5 or i[1] == 0.5 or i[1] == 1.0/3.0 or i[1] == 0.25:
                n = note.Note(i[0], quarterLength=float(i[1]))
                acce = articulations.Accent()
                stac = articulations.Staccato()
                tenu = articulations.Tenuto()
                chance_accent = random.randint(1, 9)
                if chance_accent < 2:
                    n.articulations = [random.choice([acce, stac, tenu])]
                else:
                    print("")
                for no in s.notes:
                    no.pitch.accidental = no.getContextByClass(key.KeySignature).accidentalByStep(no.step)
                s.append(n)
                last_rhythm = i[1]
            elif the_option == 'r' and last_rhythm == 0.25 or last_rhythm == 0.5 or last_rhythm == 1.0/3.0:
                n = note.Note(i[0], quarterLength=float(i[1]))
                acce = articulations.Accent()
                stac = articulations.Staccato()
                tenu = articulations.Tenuto()
                chance_accent = random.randint(1, 9)
                if chance_accent < 2:
                    n.articulations = [random.choice([acce, stac, tenu])]
                else:
                    print("")
                for no in s.notes:
                    no.pitch.accidental = no.getContextByClass(key.KeySignature).accidentalByStep(no.step)
                s.append(n)
                last_rhythm = i[1]
            elif the_option == 'r' and i[1] == 4.0 or i[1] == 2.0 or i[1] == 1.0:
                r = note.Rest(quarterLength=float(i[1]))
                s.append(r)
        last_rhythm = 0.0

        s.write('musicxml.pdf', fp='flaskr/static/image.pdf')
        s.write('midi', fp='flaskr/static/music_output.mid')

        paths = corpus.getComposer('bach')
        print(paths)

        print('wrote new music!')


        from music21 import converter




        def make_image(music):
            return 0

#def make_composer_music(songname):
    #return songname

if __name__=='__main__':
    print('Hello World')
    make_random_music('3/4', 'Bb', '64', 'French Horn', '1')
