import random
from glob import glob

test_music = glob('1/*')
base_music = glob('2/*/*')

base_link = 'https://github.com/aquastar/URL_Test/blob/master/'
para = '?raw=true'

for _ in xrange(100):
    t = random.choice(test_music)
    b = random.choice(base_music)
    print '{}{}{}'.format(base_link, t, para)
    print '{}{}{}'.format(base_link, b, para)
