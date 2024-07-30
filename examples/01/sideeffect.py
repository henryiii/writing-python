#!/usr/bin/env python3

# Remember to make this executable if you want to run it directly!

"""
This is an example of a script. It contains an import side effect! A message is
printed on import.
"""

# This is printed even if this is just imported!
print("Import side effect!")

if __name__ == "__main__":
    # This is only printed when run
    print("Okay here")
