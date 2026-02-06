import csv


def get_data_from_csv(path_to_the_file: str):
    """Функция, которая возвращает данные из файла csv"""
    country_gdps = {}
    try:
        with open(path_to_the_file, encoding="utf-8") as file:
            csv.DictReader(file)

    except ValueError:

        return []

    except FileNotFoundError:

        return []

    else:
        with open(path_to_the_file, encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                country = row["country"]
                gdp = row["gdp"]
                if country not in country_gdps:
                    country_gdps[country] = []
                country_gdps[country].append(gdp)
        return country_gdps
