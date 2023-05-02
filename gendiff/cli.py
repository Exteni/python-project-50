import argparse


def parse_args():
    diff = argparse.ArgumentParser(
        "gendiff",
        description="Compares two configuration files and shows a difference."
    )
    diff.add_argument(
        "-f",
        "--format",
        metavar="FORMAT",
        help="set format of output"
    )
    diff.add_argument("first_file")
    diff.add_argument("second_file")
    return diff.parse_args()
