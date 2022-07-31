import random
import js2py
import itertools

####
# create a list of notes
def make_random_music(time_signature, key_signature, num_measures=4):
    #return [[(34, 1/2), (37, 1/4), 33, ...], [(23, 1), ...] , ...]
    f1 = 1
    fsharp1 = 2
    gflat1 = 2
    g1 = 3
    gsharp1 = 4
    aflat1 = 4
    a1 = 5
    asharp1 = 6
    bflat1 = 6
    b1 = 7
    c1 = 8
    csharp1 = 9
    dflat1 = 9
    d1 = 10
    dsharp1 = 11
    eflat1 = 11
    e1 = 12
    f2 = 13
    fsharp2 = 14
    gflat2 = 14
    g2 = 15
    gsharp2 = 16
    aflat2 = 16
    a2 = 17
    asharp2 = 18
    bflat2 = 18
    b2 = 19
    c2 = 20
    csharp2 = 21
    dflat2 = 21
    d2 = 22
    dsharp2 = 23
    eflat2 = 23
    f3 = 24

    quarter = 0.25
    half = 0.5
    whole = 1

    notecount = [f1, fsharp1, gflat1, g1, gsharp1, aflat1, a1, asharp1, bflat1, b1, c1, csharp1, dflat1, d1, dsharp1, eflat1, e1, f2, fsharp2, gflat2, g2, gsharp2, aflat2, a2, asharp2, bflat2, b2, c2, csharp2, dflat2, d2, dsharp2, eflat2, f3]
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
        b = [random.choice(notecount), i]
        a.append(b)
    print(a)



def make_image(music):
    return 0

if __name__=='__main__':
    print('Hello World')
    make_random_music('4/4', 'F')
