#Flatten Dictionary
#Given a nested dictionary, flatten the dictionary, where nested dictionary keys can be represented through dot notation.
#You can assume there will be no arrays, and all keys will be strings.

import collections

def flatten_dictionary(d, parent_key='', sep='.'):
  # Fill this in.
  items = []
  for k, v in d.items():
      new_key = parent_key + sep + k if parent_key else k
      if isinstance(v, collections.MutableMapping):
          items.extend(flatten_dictionary(v, new_key, sep=sep).items())
      else:
          items.append((new_key, v))
  return dict(items)

d = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3
        }
    }
}
print(flatten_dictionary(d))
# {'a': 1, 'b.c': 2, 'b.d.e': 3}
