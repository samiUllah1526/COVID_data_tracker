import requests


# API call
def api_response(url):
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()



def api_data_parser(data):
    #Parsing the flag url
    country_info = data.get("countryInfo", "Some error")
    flag_url = country_info.get("flag", "Some error in getting flag url")

    #Parsing the data from api response
    country_name = data.get("country", "Country name is not available")
    todayCases = data.get("todayCases", "todayCases data is not available")
    todayDeaths = data.get("todayDeaths", "todayDeaths data is not available")
    todayRecovered = data.get("todayRecovered", "todayRecovered data is not available")
    active = data.get("active", "active cases data is not available")
    critical = data.get("critical", "critical cases data is not available")

    stats = [todayCases, todayDeaths, todayRecovered, active, critical]
    return stats, country_name, flag_url



