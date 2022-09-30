import requests
from bs4 import (
    BeautifulSoup,
)


pages_list: list[str] = [
    "https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW",
    "https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW&offset=200",
    "https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW&offset=400",
    "https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW&offset=600",
    "https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW&offset=800",
    "https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW&offset=1000",
    # "https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW&offset=1200",
    # "https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW&offset=1400",
    # "https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW&offset=1600",
    # "https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW&offset=1800",
]

for page_url in pages_list:
    page = requests.get(page_url)

    if page.status_code == 200:
        print(f"> {page_url} Downloaded.")

        soup = BeautifulSoup(
            page.content,
            "html.parser",
        )
        movies_rank_list = soup.select("td.a-text-right.mojo-header-column.mojo-truncate.mojo-field-type-rank")
        movies_name_list = soup.select("td.a-text-left.mojo-field-type-title")
        movies_year_list = soup.select("td.a-text-left.mojo-field-type-year")
        movies_money_list = soup.select("td.a-text-right.mojo-field-type-money")

        with open("top_movies_list.csv", "a") as file:
            for (rank, name, year, money,) in zip(
                movies_rank_list,
                movies_name_list,
                movies_year_list,
                movies_money_list,
            ):
                money_formatted = money.text.replace(",","")
                file.write(f'{rank.text},{name.text},{year.text},{money_formatted}\n')

        print(f"> Wrote {len(movies_rank_list)} Movies.\n")

    else:
        raise Exception("Problem loading the page!")