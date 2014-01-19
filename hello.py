#!/usr/bin/env python

"""
Federal law requires that every introductory talk include a 'hello world' example.
"""


def say_hello(times):
    for x in range(times):
        print("Hello #{}".format(x))

if __name__ == "__main__":
    say_hello(4)
