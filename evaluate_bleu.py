#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 08:58:13 2020

@author: siva
"""
from bleu import list_bleu

def get_score_v1(caplist,result):
    gt=[' '.join([tokenizer.index_word[i] for i in caplist if i not in [0]])]
    print(gt)
    print(result)
    return list_bleu([gt],[' '.join(result)])
        
score=get_score_v1(cap_val[0], result)


