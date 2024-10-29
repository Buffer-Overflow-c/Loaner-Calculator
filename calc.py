import datetime
import sys


def get_delta(starting_date: list[str], ending_date: list[str]) -> int:
    delta = datetime.date(
        int(ending_date[0]), int(ending_date[1]), (int(ending_date[2]) - 1)
    ) - datetime.date(
        int(starting_date[0]), int(starting_date[1]), int(starting_date[2])
    )

    return int(str(delta).split(",")[0].split(" ")[0])


def print_results(days_delta: int) -> None:
    print(f"Number of days used: {days_delta} days")
    print(f"Loaner price based on days used: ${int(days_delta)*5}")


def main() -> None:
    try:
        starting_date = sys.argv[1].split("-")
        ending_date = sys.argv[2].split("-")
    except IndexError:
        print("You must provide a starting date and ending date.\n")
        print("python calc.py starting:year-mm-dd ending:year-mm-dd")
        print("eg. python calc.py 2024-01-01 2024-12-12")
        sys.exit()

    if starting_date[1] > ending_date[1] and starting_date[0] >= ending_date[0]:
        print("starting date cannot be later than the ending date")
        sys.exit()

    print_results(get_delta(starting_date, ending_date))


if __name__ == "__main__":
    main()
