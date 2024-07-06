import requests


# deprecated
def fetch_html(url):
    # print(datetime.datetime.now(), "------ start fetch_html")
    try:
        response = requests.get(url)
        response.encoding = response.apparent_encoding
        response.raise_for_status()
        return {
            "message": response.status_code,
            "status_code": 200
        }
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return {
            "message": str(e),
            "status_code": 400
        }
