from axt.version import VERSION
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="axt",
        description="Atari XEX Toolkit"
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="Show version"
    )

    args = parser.parse_args()

    if args.version:
        print(f"AtariXEXToolkit {VERSION}")
        return

    parser.print_help()


if __name__ == "__main__":
    main()