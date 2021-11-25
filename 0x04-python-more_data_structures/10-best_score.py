#!/usr/bin/python3
def best_score(a_dict):
    if a_dict is None or len(a_dict) == 0:
        return None
    scores = [item[1] for item in a_dict.items()]
    keys = [item[0] for item in a_dict.items()]
    best = max(scores)
    return keys[scores.index(best)]
