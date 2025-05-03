import RentCast
from openai import OpenAI
import json

client = OpenAI()

access_token = 'J7sh9IZ9adWAmH4-DIKXhtqo1rl7e9eWw-g9wFgr6to'
budgetData = RentCast.GetZestimates(AccessToken=access_token)

# parses the data and assigns it to a variable called budgetData_string
budgetData_string = json.dumps(budgetData, indent=4)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a budget assistant, skilled in explaining budget data, finding spending "
                                  "habits and analyze best budget approaches."},
    {"role": "user", "content": "Summarize the spending habits from this budget data below:"},
    {"role": "user", "content": budgetData_string}
  ]
)

print(completion.choices[0].message.content)