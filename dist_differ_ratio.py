import numpy as np
import pretty_midi
from pyemd import emd_samples
from collections import defaultdict, Counter
import _pickle as pk
import os.path


def leaders(xs, sort_id=0):
    counts = defaultdict(int)
    for x in xs:
        counts[x] += 1
    return sorted(counts.items(), key=lambda tup: tup[sort_id])


def eud_dis(x, y):
    eud_dis = 0
    _cnt = [Counter(x), Counter(y)]
    left_big = len(_cnt[0]) < len(_cnt[1])
    for __ in _cnt[left_big].most_common():
        if __[0] in _cnt[0] and __[0] in _cnt[1]:
            eud_dis += (_cnt[1][__[0]] - _cnt[0][__[0]]) ** 2
    return eud_dis


# read A and B

# calculate pitch and duration distributions
ab_list_pitch = []
ab_list_duration = []
if os.path.exists('ab_list_duration.pk') and os.path.exists('ab_list_pitch.pk'):
    ab_list_duration = pk.load(open('ab_list_duration.pk', 'rb'))
    ab_list_pitch = pk.load(open('ab_list_pitch.pk', 'rb'))
else:
    dir = 'data'
    ab_list = []
    for dir_name in os.listdir(dir):
        note_list = []
        for filename in os.listdir(dir + os.sep + dir_name):
            file_path = dir + os.sep + dir_name + os.sep + filename
            with open(file_path, 'rt') as f:
                try:
                    pm = pretty_midi.PrettyMIDI(file_path)
                    note_list.extend(pm.instruments[0].notes)
                except:
                    continue
        ab_list.append(note_list)

    for _ in ab_list:
        note_duration = []
        note_pitch = []
        for __ in _:
            if __.end > __.start:
                note_duration.append(round((__.end - __.start) * 16))
                note_pitch.append(__.pitch % 12)
        ab_list_duration.append(note_duration)
        ab_list_pitch.append(note_pitch)

    pk.dump(ab_list_duration, open('ab_list_duration.pk', 'wb'))
    pk.dump(ab_list_pitch, open('ab_list_pitch.pk', 'wb'))

# iterate every baseline


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
            note_duration.append(round((_.end - _.start) * 16))
            note_pitch.append(_.pitch % 12)

    # pitch_dist = leaders(note_pitch)
    # duration_dist = leaders(note_duration)
    print('\n', dir_name)

    # # calculate note pitch/duration
    # ab_list_pitch = []
    # ab_list_duration = []

    print("Duration:")

    # A-x, B-x
    ab_x_emd = []
    ab_x_eud = []

    for _ in ab_list_duration:
        ab_x_emd.append(emd_samples(_, note_duration))
        ab_x_eud.append(eud_dis(_, note_duration))

    # A - B
    ab_emd = emd_samples(ab_list_duration[0], ab_list_duration[1])
    ab_eud = eud_dis(ab_list_duration[0], ab_list_duration[1])

    # diff and ratio
    diff_emd = sum(ab_x_emd) - ab_emd
    ratio_emd = sum(ab_x_emd) / ab_emd

    diff_eud = sum(ab_x_eud) - ab_eud
    ratio_eud = sum(ab_x_eud) / ab_eud

    print("diff_emd:{:.3f} ratio_emd:{:.3f} diff_eud:{:.3f} ratio_eud:{:.3f}".format(diff_emd, ratio_emd, diff_eud, ratio_eud))

    print("Pitch:")
    # A-x, B-x
    ab_x_emd = []
    ab_x_eud = []

    for _ in ab_list_pitch:
        ab_x_emd.append(emd_samples(_, note_pitch))
        ab_x_eud.append(eud_dis(_, note_pitch))

    # A - B
    ab_emd = emd_samples(ab_list_pitch[0], ab_list_pitch[1])
    ab_eud = eud_dis(ab_list_pitch[0], ab_list_pitch[1])

    # diff and ratio
    diff_emd = sum(ab_x_emd) - ab_emd
    ratio_emd = sum(ab_x_emd) / ab_emd

    diff_eud = sum(ab_x_eud) - ab_eud
    ratio_eud = sum(ab_x_eud) / ab_eud

    print("diff_emd:{:.3f} ratio_emd:{:.3f} diff_eud:{:.3f} ratio_eud:{:.3f}".format(diff_emd, ratio_emd, diff_eud, ratio_eud))
