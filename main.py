import requests
import base64

data = {"url": "https://www.amazon.com/dp/B09LNW3CY2", "httpResponseBody": True}

headers = {
    "Content-Type": "application/json",
    "X-Api-Key": "replace with your api key",
}

response = requests.post(
    "https://api.proxyscrape.com/v3/accounts/freebies/scraperapi/request",
    headers=headers,
    json=data,
)

if response.status_code == 200:
    json_response = response.json()
    if "browserHtml" in json_response["data"]:
        html_content = json_response["data"]["browserHtml"]
    else:
        html_content = base64.b64decode(json_response['data']['httpResponseBody']).decode()

    with open("index.html", "w", encoding="utf-8") as file:
        file.write(html_content)
else:
    print("Error:", response.status_code)