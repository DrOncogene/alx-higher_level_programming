#!/usr/bin/python3
def best_score(a_dict):
    if a_dict is None or len(a_dict) == 0:
        return None
    scores = [item[1] for item in a_dict.items()]
    keys = [item[0] for item in a_dict.items()]
    for score in scores:
        index = scores.index(score)
        if index + 1 < len(scores):
            best = check(score, scores[scores.index(score) + 1])
    return keys[scores.index(best)]


def check(a, b):
    if a > b:
        return a
    return b
