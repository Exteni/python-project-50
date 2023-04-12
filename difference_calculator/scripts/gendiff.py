from difference_calculator.generate_diff import generate_diff
from difference_calculator.cli import parse_args


def main():
    args = parse_args()
    generate_diff(args.first_file, args.second_file)


if __name__ == "__main__":
    main()
