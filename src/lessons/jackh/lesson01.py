#!/usr/bin/env python
# -*- coding: utf-8 -*-

scores = [10, 20, 30]


def record_score(scores, player_number, player_score):
    scores[player_number] += player_score


record_score(scores, 1, 2)
print(scores)


def high_score(scores):
    return scores.index(max(scores)), max(scores)


highest = high_score(scores)


def print_winner(highest):
    print(f"The winner is player #{highest[0]} with a score of {highest[1]}")


print_winner(highest)
