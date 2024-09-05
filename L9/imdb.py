#data is from this 
#------------------------------------------- IMDB HEADER -------------------------------------------
# Only 'import json' command is allowed!!!
# Failing to follow this rule, you will get zero mark :_)
import json

def read_json(filename):
    with open(filename) as f:
        data = f.read()
        data = json.loads(data)
    return data

# specifying the zip file name
filename = "IMDB_movies_merged.json"

### do not forget to uncomment the next line to read json data
data = read_json(filename)
### ----------------------------------------------------------
#------------------------------------------- IMDB HEADER -------------------------------------------



def q1():
  filter_actor = []
  for i in data:
    if 'cast' in i.keys() and 'director' in i.keys():
      if i['director']['name'] != 'Steven Spielberg':
        for j in i['cast']:
          if j['name'] == 'Harrison Ford':
            filter_actor.append(i)


  sorted_filter = sorted(filter_actor, key=lambda x: float(x['ratingValue']) if x['ratingValue'] else 0,reverse = True )

  x = 0
  q_1_string = ''
  q_1_list = []
  for i in sorted_filter:
    if x >= 5:
      break
    q_1_string += i['director']['name'] + '\n'
    x += 1

  sorted_filter = sorted(filter_actor, key=lambda x: float(x['ratingValue']) if x['ratingValue'] else 0,reverse = True )

  x = 0
  a = []
  q_1_string = ''
  track = 0

  for i in sorted_filter:
    if track > 5:
      break
    if str(i['ratingValue']) in a:
      a.append(str(i['ratingValue']))
    else:
      track += 1
      a.append(str(i['ratingValue']))

  for i in sorted_filter:
    if x >= len(a)-1:
      break
    q_1_list.append(i['director']['name'])
    x += 1
  q_1_list.sort(key = lambda x: x[0])
  print("\n".join(q_1_list))
def q2():
  filter_actor = []
  for i in data:
    k = []
    if 'cast' in i.keys() and 'director' in i.keys():
      if i['director']['name'] != 'Steven Spielberg' and i['director']['name'] != 'George Lucas':
        for j in i['cast']:
          k.append(j['name'])
        if 'Harrison Ford' in k and 'Tommy Lee Jones' in k:
          filter_actor.append(i)
  sorted_filter = sorted(filter_actor, key=lambda x: float(x['ratingValue']) if x['ratingValue'] else 0,reverse = True )
  print(sorted_filter[0]['name'])