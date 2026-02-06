def calculate_average_gdp(country_gdps):
    """Вычисляет средний ВВП по странам и сортирует по убыванию."""
    averages = []
    for country, gdps in country_gdps.items():
        avg_gdp = sum(gdps) / len(gdps)
        averages.append((country, round(avg_gdp, 2)))

    return sorted(averages, key=lambda x: x[1], reverse=True)
