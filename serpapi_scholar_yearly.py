import requests
import json
import os

def get_total_results(api_key, query):
    """
    Gets the total number of search results for a given query using SerpAPI.

    Parameters:
    - api_key (str): Your SerpAPI API key.
    - query (str): The search query for Google Scholar.

    Returns:
    - int: Total number of results for the query.
    """
    params = {
        "engine": "google_scholar",
        "q": query,
        "api_key": api_key,
        "num": 10  # Fetch first page for total results
    }
    response = requests.get("https://serpapi.com/search", params=params)
    if response.status_code == 200:
        results = response.json()
        total_results = results.get("search_information", {}).get("total_results", 0)
        print(f"搜索结果总数: {total_results}")
        return total_results
    else:
        print(f"请求失败，状态码: {response.status_code}")
        print(f"错误信息: {response.text}")
        return 0

def fetch_google_scholar_data(api_key, query, start_year, end_year, year_step=2):
    """
    Fetches Google Scholar data using SerpAPI and saves the results into a single JSON file.

    Parameters:
    - api_key (str): Your SerpAPI API key.
    - query (str): The search query for Google Scholar.
    - start_year (int): The starting year for the search.
    - end_year (int): The ending year for the search.
    - year_step (int, optional): The year range for each query. Default is 2.

    Returns:
    - None
    """
    base_params = {
        "engine": "google_scholar",
        "q": query,
        "api_key": api_key,
        "num": 10,  # Number of results per page
    }

    all_results = []
    total_fetched = 0

    # 自动生成输出文件名
    output_file = f"results_{start_year}_{end_year}.json"

    # Iterate through year ranges
    for year in range(start_year, end_year + 1, year_step):
        print(f"Fetching results for {year} to {year + year_step - 1}...")
        params = base_params.copy()
        params["as_ylo"] = year  # Starting year
        params["as_yhi"] = year + year_step - 1  # Ending year
        params["start"] = 0  # Start from the first result

        has_next_page = True

        while has_next_page:
            response = requests.get("https://serpapi.com/search", params=params)
            if response.status_code == 200:
                results = response.json()
                organic_results = results.get("organic_results", [])
                if not organic_results:
                    print(f"No more data available for {year}-{year + year_step - 1}.")
                    break

                all_results.extend(organic_results)

                pagination = results.get("serpapi_pagination", {})
                next_page = pagination.get("next", None)
                if next_page:
                    params["start"] += params["num"]
                else:
                    has_next_page = False
            else:
                print(f"Request failed with status code: {response.status_code}")
                print(f"Error message: {response.text}")
                has_next_page = False

        total_fetched += len(all_results)

    # Save all results to a single JSON file
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(all_results, file, ensure_ascii=False, indent=4)

    print(f"Total results fetched: {total_fetched}. Results saved to {output_file}.")
