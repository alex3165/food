import json
import sys
import uuid
import os

from pprint import pprint
from random import randint

FILE_PATH = os.path.abspath('Development/food/data_food.json')

def commands():
  for com in ALL_COMMANDS:
    print('[{0}] command {1}'.format(com['name'], com['description']))


def addElement(data):
  if len(sys.argv) < 4:
    pprint('Please add the name and the type');
  else:
    name = sys.argv[2]
    typee = sys.argv[3]

    data['options'][str(uuid.uuid4())] = {
    'name': name,
    'type': typee
    }

    with open(FILE_PATH, 'w') as outfile:
      json.dump(data, outfile)

def getList(data):
  for key, value in data['options'].items():
    print('Today you can eat {0} at {1}'.format(value['type'], value['name']))


def random(data):
  options = data['options']
  limit = len(options);
  ran = randint(0, limit)
  count = 0
  choice = None

  for key, value in options.items():
    if(count == ran):
      choice = value
      break
    count = count + 1

  pprint('Today let\'s eat {0} at {1}'.format(choice['type'], choice['name']))

ALL_COMMANDS = [{
  'name': 'list',
  'method': getList,
  'description': 'List all the possible options'
},
{
  'name': 'add',
  'method': addElement,
  'description': 'Add a new food option, take 2 parameters: [place_name] [food_type]'
},
{
  'name': 'help',
  'method': commands,
  'description': 'Food helper'
},
{
  'name': 'random',
  'method': random,
  'description': 'Pick a place randomly'
}]

def main():
  with open(FILE_PATH) as data_file:
    data = json.load(data_file)

  if(len(sys.argv) > 1):
    switch(sys.argv[1])(data)
  else:
    commands()


def switch(opt):
  for com in ALL_COMMANDS:
    if opt == com['name']:
      return com['method']


main()
