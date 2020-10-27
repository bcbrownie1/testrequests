import pytest
import requests

actual_list = {
    'Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe',
    'Jackson', 'Buren', 'Harrison', 'Tyler', 'Polk',
    'Taylor', 'Fillmore', 'Pierce', 'Buchanan', 'Lincoln',
    'Johnson', 'Grant', 'Hayes', 'Garfield', 'Arthur',
    'Cleveland', 'Harrison', 'McKinley', 'Roosevelt', 'Taft',
    'Wilson', 'Harding', 'Coolidge', 'Hoover', 'Truman',
    'Eisenhower', 'Kennedy', 'Nixon', 'Ford', 'Carter',
    'Reagan', 'Bush', 'Clinton', 'Obama', 'Trump'
}

def test_ddg_presidents_query():
    response = requests.get('https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json')
    data = response.json()['RelatedTopics']

    presidents = []
    for topic in data:
        name = topic['Text'].split(' - ')[0]
        last_name = name.split(' ')
        last_name = last_name[len(last_name) - 1]
        presidents.append(last_name)

    presidents = set(presidents)

    assert presidents.issuperset(actual_list) #duckduckgo query will (probably) end up having more results, but make sure it includes all of the presidents
