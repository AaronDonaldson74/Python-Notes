full_name = lambda first, last: f'{first} {last}'

print(full_name('Aaron', 'Donaldson'))

def greeting(name):
  print(f'HI there {name}')

greeting(full_name('Aaron', 'Donaldson'))
