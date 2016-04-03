#!/usr/bin/env python
# -*- coding: utf-8 -*-

# モジュール

def decision(A = 60, B = 85, C = 95):
    '''閾値判定

    判定する値はリストで用意する
    '''
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
