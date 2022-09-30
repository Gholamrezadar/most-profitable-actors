# Most Profitable Actors
Finds the list of actors with the most boxoffice profit using TMDB API.

First, I crawl the [Box Office Mojo](https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW) website to gather a list of the best selling movies.
Then, for each movie, I use TMDB's API to get the `movie_id` by `movie's name` and `release year`, and finally I get the list of actors of that movie.
The profit for each actor gets accumulated and displayed.

## Results

## Features
- [x] Crawl boxofficemojo and get a list of best selling movies
- [x] Use Multiprocessing to make the crawling faster
- [] Export the final data as json
- [] Display as webapp

## How to use
First, install these modules:
- requests
- beautifulsoup4
- python-dotenv
- pandas

If you want, you can use the provided data and go straight to the notebook called `most_profitable_actors_multiprocessing.ipynb`.
But if you want to update the data, run these files in order:
1. `boxoffice_scraper.py` that uses requests and bs4 to extract the best selling movies.
2. `gather_data_multiprocessing.py` that uses TMDB's API to get the list of actors for each movie extracted by the last step.
3. `most_profitable_actors_multiprocessing.ipynb` open the notebook and read the comments. Make sure to set `is_data_available` to `False` if you want to recalculate everything.

## Credits
By Gholamreza Dar - Fall 2022
