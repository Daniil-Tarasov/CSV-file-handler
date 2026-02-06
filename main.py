from src.parser import parse_arguments
from src.reader import get_data_from_csv
from src.report import generate_report


def main():
    try:
        args = parse_arguments()
        print(f"Генерирую отчет '{args.report}' из файлов: {args.files}")

        country_gdps = get_data_from_csv(args.files)

        report = generate_report(country_gdps, args.report)
        print(report)

    except Exception as e:
        print(f"Ошибка выполнения: {e}")


if __name__ == "__main__":
    main()
