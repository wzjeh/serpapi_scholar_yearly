# SerpAPI Google Scholar Fetcher

To overcome Google's maximum query page limit of 100,  this Python package enables you to fetch Google Scholar data year by year using SerpAPI. It allows you to retrieve scholarly article information based on your query and a specified year range. The package automatically generates JSON files containing the search results.
## Features

- **Get Total Search Results**: The function `get_total_results` helps you retrieve the total number of results for a given search query.
- **Fetch Scholar Data**: The function `fetch_google_scholar_data` allows you to fetch scholarly articles from Google Scholar within a specified year range and save them to a JSON file.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/serpapi-scholar-fetcher.git
    cd serpapi-scholar-fetcher
    ```

## Usage

### 1. `get_total_results`: Get the Total Number of Search Results

This function retrieves the total number of results for a given search query on Google Scholar.

 ```python
from serpapi_scholar import get_total_results

API_KEY = "your-serpapi-api-key"
QUERY = "nitration AND 'mixed acid'"

total_results = get_total_results(API_KEY, QUERY)
print(f"Total results found: {total_results}")
    ```

### 2. `fetch_google_scholar_data`: Fetch Google Scholar Data and Save to JSON
 ```python
from serpapi_scholar import fetch_google_scholar_data

API_KEY = "your-serpapi-api-key"
QUERY = 'nitration AND "mixed acid"'
START_YEAR = 2016
END_YEAR = 2020
YEAR_STEP = 2

fetch_google_scholar_data(API_KEY, QUERY, START_YEAR, END_YEAR, YEAR_STEP)
```
