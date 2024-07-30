#!/usr/bin/env python3

import argparse
import random

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    choices = ["a", "b", "c"]
    print(random.choice(choices))
