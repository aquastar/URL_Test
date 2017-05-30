import os
import random
from glob import glob

test_music = glob('1/*')
base_music = glob('2/*/*')

base_link = 'https://github.com/aquastar/URL_Test/blob/master/'
para = '?raw=true'

with open('amt_input.csv', "wb") as csv_file:
    # write the header
    csv_file.write('baseline_name,jazz_link,baseline_link\n')

    for _ in xrange(100):
        t = random.choice(test_music)
        b = random.choice(base_music)
        line = '{},{}{}{}, {}{}{}\n'.format(b.split(os.sep)[1], base_link, t, para, base_link, b, para)
        csv_file.write(line)
