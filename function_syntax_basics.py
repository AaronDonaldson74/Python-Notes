def full_name(first, last):
  print(f'{first} {last}')

full_name('Aaron', 'Donaldson')

def auth(email, password):
  if email == "aaron.donaldson74@gmail.com" and password == "secret":
    print('Authorized')
  else:
    print('Not authorized')

auth('aaron.donaldson74@gmail.com', 'secret')

def hundred():
  for num in range(1,10):
    print(num)

hundred()

def counter(max_value):
  for num in range(1, max_value):
    print(num)

counter(10)