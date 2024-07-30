#!/usr/bin/env python3


import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--opt", help="An optional ArgumentParser")
    args = parser.parse_args()
    print(f"{args.opt=}")
