#STOCK PRICE API https://www.alphavantage.co =>
#API: https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo
#News API https://newsapi.org =>
#Twilio ATPI =>

import requests
from twilio.rest import Client

STOCK_NAME = "TSLA" #https://www.tradingview.com/symbols/NASDAQ-TSLA/
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "xxx"
NEWS_API_KEY = "xxx"

account_sid = 'xxx'
auth_token = 'xxx'

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock_news_normal_start price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock_news_normal_start price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

STOCK_PARAMS = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMS)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
# print(data) #http://jsonviewer.stack.hu
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

#TODO 2. - Get the day before yesterday's closing stock_news_normal_start price

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

# Python abs() Function: W3SCHOOL: get abs positive value
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if diffference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

diff_percent = round(difference / float(yesterday_closing_price)) * 100

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if abs(diff_percent) > 5:
    print("Get news")

    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

if abs(diff_percent) > 1:

    NEWS_PARAMS = {
        "qInTitle" : COMPANY_NAME,
        "apiKey" : NEWS_API_KEY,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMS)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    three_articles = articles[:3]
    print(three_articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

#TODO 9. - Send each article as a separate message via Twilio.

    client = Client(account_sid, auth_token)

#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

    for article in formatted_articles:

        message = client.messages.create(
            body= article,
            from_="xxx",
            to='xxx'
        )
    print(message.status)