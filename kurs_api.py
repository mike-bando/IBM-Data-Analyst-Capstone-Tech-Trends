import requests
import json
import pprint
import webbrowser
from datetime import datetime, timedelta

#API - Application Programming Interface
timeBefore = timedelta(weeks=12)
searchDate = datetime.today() - timeBefore
print(datetime.timestamp(searchDate))

# params = {
#     "site":"stackoverflow",
#     "order":'desc',
#     "min":15,
#     "sort": "votes",
#     # "fromdate":"2025-08-01",
#     "fromdate":int(datetime.timestamp(searchDate)),
#     "tagged":'python'
# }

# r = requests.get("https://api.stackexchange.com/2.2/questions/",params)

params={
    "?number=":1,

}

r = requests.get('https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/',params)

try: 
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format.")
else:
    # pprint.pprint(questions)
    for question in questions['items']:
        webbrowser.open_new_tab(question['link'])



