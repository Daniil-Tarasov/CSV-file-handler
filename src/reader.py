import csv


def get_data_from_csv(path_to_file):
    """Функция, которая возвращает данные (country, gdp) из файла csv"""
    all_country_gdps = {}

    for file_path in path_to_file:
        country_gdps = {}
        try:
            with open(file_path, encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    country = row["country"]
                    gdp = int(row["gdp"])
                    if country not in country_gdps:
                        country_gdps[country] = []
                    country_gdps[country].append(gdp)

                for country, gdps in country_gdps.items():
                    if country not in all_country_gdps:
                        all_country_gdps[country] = []
                    all_country_gdps[country].extend(gdps)

        except FileNotFoundError:
            print(f"Файл не найден: {file_path}")
            continue

    return all_country_gdps
