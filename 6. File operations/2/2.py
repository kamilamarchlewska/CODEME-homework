import json
import random

import json

filename = 'user4.json'
with open(filename, 'r') as f:
  data = json.loads(f.read())

starts = random.choice(data['starts'])
middles = random.choice(data['middles'])
qualifiers = random.choice(data['qualifiers'])
finishes = random.choice(data['finishes'])


conference_name = f' Nazwa konferencji: {starts}{middles}{qualifiers}{finishes}'
width = len(conference_name)

print('*' * width)
print('GENERATOR KONFERENCJI'.center(width))
print('*' * width)
print(conference_name.center(width))
print('*' * width)
