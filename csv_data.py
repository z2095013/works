#!/usr/bin/env python
# -*- coding: utf-8 -*-

# モジュール
import datetime
import os, sys, csv, fileinput



def time_select(self,F_TIME, T_TIME):
    '''集計期間

    前後1日ずつ含める
    '''
    self.f = F_TIME
    self.t = T_TIME

    DIR = []     # 対象ディレクトリをリスト化
    CSVS = []    # DIRからファイルのリスト化

    [d + f for d in DIR for f in CSVS]





    list(zip(*mat)) # リストを行から列へ

    c = sum(1 for line in open('filename')) # ファイルの行数
    c = len(sys.stdin.readlines())

    [x for v in len(c)]



def data_select(self, DIR):
    '''グループ選択

    グループ情報から対象デバイス、メトリックをを抜き出す
    '''

### neta
#import sys, fileinput, argparse
#
#parser = argparse.ArgumentParser()
#parser.add_argument('-e', '--encoding', default=None)
#parser.add_argument('search', help="search word")
#parser.add_argument('files', nargs="+")
#
#args = parser.parse_args()
#
#
#search = args.search
#def enc_open(filename, mode):
#    return open(filename, mode=mode, encoding  = args.encoding )
#
#with fileinput.FileInput(files=args.files, openhook=enc_open) as f:
#    for line in f:
#    if line.find(search) > -1:
#            print("{0:20}:{1:4} {2}".format( f.filename(), f.lineno(), line), end="")
###

    for line in fileinput.input():
        process(line)


    for f in os.listdir(DIR):
        cf = open(os.path.join(DIR, f), 'r')





    [CSVS for f in d for d in os.listdir(DIR)]

    for f in CSVS:




    s = a.sort()   # リスト内の値をソートする


    a = range(100)
    b = range(200)
    c = range(150)
    thA = len([x for x in a if x >= A])    # Aより大きい値の数
    thB = len([x for x in b if x >= B])    # Aより大きい値の数
    thC = len([x for x in c if x >= C])    # Aより大きい値の数
#    print("集計期間:", TIME)
    print("閾値:", A, B, C)
    print("閾値超過数:", thA, thB, thC)
    print("注視閾値超過機器:", thA, thB, thC)
    print("増設閾値超過機器:", thA, thB, thC)
    print("限界閾値超過機器:", thA, thB, thC)
