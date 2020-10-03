from __future__ import absolute_import

import random

CHARACTER_SET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
MAX_RANDOM_STRING_LENGTH = 32
MIN_RANDOM_STRING_LENGTH = 4
TRUES = ['1', 'on', 'true', 't', 'yes', 'y']
FALSES = ['0', 'off', 'false', 'f', 'no', 'n']


def get_random(length=MIN_RANDOM_STRING_LENGTH):
    if length < MIN_RANDOM_STRING_LENGTH:
        length = MIN_RANDOM_STRING_LENGTH
    if length > MAX_RANDOM_STRING_LENGTH:
        length = MAX_RANDOM_STRING_LENGTH
    s = ''
    for i in range(length):
        s += random.choice(CHARACTER_SET)
    return s


def is_blank(s):
    return s is None or not s.strip()


def is_boolean(s):
    s = lower_and_strip(s)
    return s in TRUES or s in FALSES


def lower_and_strip(s):
    return s if is_blank(s) else s.lower().strip()


def to_boolean(s):
    if is_blank(s):
        return False
    return lower_and_strip(s) in TRUES
