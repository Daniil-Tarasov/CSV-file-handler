from tabulate import tabulate

from src.utils import calculate_average_gdp


def generate_average_gdp_report(country_gdps):
    """Формирует таблицу отчета 'average-gdp'."""
    if not country_gdps:
        return "Нет данных для отчета"

    avg_data = calculate_average_gdp(country_gdps)

    headers = ["Страна", "Средний ВВП (млрд $)"]
    table_data = [[country, f"{avg_gdp:,.0f}"] for country, avg_gdp in avg_data]

    return tabulate(
        table_data,
        headers=headers,
        tablefmt="grid",
        floatfmt=".0f"
    )


def generate_report(country_gdps, report_type) -> str:
    """Расширяемая функция для разных типов отчетов."""
    reports = {
        "average-gdp": generate_average_gdp_report
    }

    if report_type not in reports:
        return f"Отчет '{report_type}' не реализован. Доступно: {list(reports.keys())}"

    return reports[report_type](country_gdps)
