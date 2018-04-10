import os
import pretty_midi

from collections import defaultdict, Counter


def leaders(xs, sort_id=0):
    counts = defaultdict(int)
    for x in xs:
        counts[x] += 1
    return sorted(counts.items(), key=lambda tup: tup[sort_id])


note_list = []

dir = '2'

for dir_name in os.listdir(dir):
    for filename in os.listdir(dir + os.sep + dir_name):
        file_path = dir + os.sep + dir_name + os.sep + filename
        with open(file_path, 'rt') as f:
            try:
                pm = pretty_midi.PrettyMIDI(file_path)
                note_list.extend(pm.instruments[0].notes)
            except:
                continue

    note_duration = []
    note_pitch = []
    for _ in note_list:
        if _.end > _.start:
            note_duration.append(round((_.end - _.start)*8))
            note_pitch.append(pretty_midi.note_number_to_name(_.pitch)[:-1])

    pitch_dist = leaders(note_pitch)
    duration_dist = leaders(note_duration)
    print('\n', dir_name)
    for _, __ in enumerate(pitch_dist[3:] + pitch_dist[:3]):
        print("({}, {})".format(_, __[1]), end='')

    print('\n')
    for _ in duration_dist:
        if float(_[0]) <= 32:
            print("({},{})".format(_[0], _[1]), end='')
