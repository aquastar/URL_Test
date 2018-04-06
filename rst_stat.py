import csv
from collections import Counter
import os

stat = {}

dir = 'amt_rst'
for filename in os.listdir(dir):
    file_path = dir + os.sep+ filename
    with open(file_path, 'rt') as f:
        reader = csv.reader(f)
        next(reader)  # skip the header
        included_cols = [-6, -3, -2]
        for row in reader:
            if True:  # row[-1] == 'jazz':
                content = list(row[i] for i in included_cols)
                # print(content)
                if row[-6] not in stat:
                    stat[row[-6]] = []
                stat[row[-6]].append(row[-3:-1])

for k, v in stat.items():
    an_fusion = []
    an_novel = []
    for ans in v:
        an_fusion.append(ans[0])
        an_novel.append(ans[1])

    len_fusion = len(an_fusion)
    len_novel = len(an_novel)

    cnt_an_fusion = Counter(an_fusion)
    cnt_an_novel = Counter(an_novel)

    print(k, "{}".format(len_novel))

    print("[2nd question]")
    for ele in cnt_an_fusion:
        print("{}:{:.2f}".format(ele, float(cnt_an_fusion[ele]) / len_fusion), end='\t')
    fl = 1 - (abs(cnt_an_fusion['jazz'] - cnt_an_fusion['folk']) + cnt_an_fusion['none']) / len_fusion
    print('FL:{:.2f}'.format(fl))

    print("\n[3rd question]")
    # compatible
    cnt_an_novel['not'] += cnt_an_novel['robot']
    del cnt_an_novel['robot']
    cnt_an_novel['notvery'] += cnt_an_novel['newbie']/2
    cnt_an_novel['somewhat'] += cnt_an_novel['newbie']/2
    del cnt_an_novel['newbie']
    cnt_an_novel['extrem'] += cnt_an_novel['expert']
    del cnt_an_novel['expert']

    for ele in cnt_an_novel:
        print("{}:{:.2f}".format(ele, float(cnt_an_novel[ele]) / len_novel), end='\t')



    print('\n')
