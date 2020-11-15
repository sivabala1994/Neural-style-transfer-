#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 08:58:13 2020

@author: siva
"""
from bleu import list_bleu
from jiwer import wer


def get_bleu_v1(caplist,result):
    gt=[' '.join([tokenizer.index_word[i] for i in caplist[1:] if i not in [0]])]
    print(gt)
    print(result)
    return list_bleu([gt],[' '.join(result)])

def get_wer_v1(caplist,result):
    gt=[' '.join([tokenizer.index_word[i] for i in caplist[1:] if i not in [0]])]
    print(gt)
    print(result)
    return wer(gt,[' '.join(result)])
        
score_blue=get_bleu_v1(cap_val[0], result)
score_wer=get_wer_v1(cap_val[0], result)


print(score_blue)
print(score_wer)