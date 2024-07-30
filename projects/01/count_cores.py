import os


def count_cores():
    return os.cpu_count()


print(f"This computer has {count_cores()} cores")
