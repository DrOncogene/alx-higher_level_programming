#!/usr/bin/python3
def multiple_returns(sent):
    if len(sent) == 0:
        ret = len(sent), None
    else:
        ret = len(sent), sent[0]
    return ret
