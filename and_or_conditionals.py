username = 'aaron donaldson'
email = 'aaron.donaldson74@gmail.com'
password = 'thenorth'

if username == 'aaron donaldson' and password == 'thenorth':
  print('Access Permitted')
else:
  print('You go no further!')

if username == 'aaron donaldson' or password == 'thenorth':
  print('Access Permitted')
else:
  print('You shall not pass!')

if username == 'aaron donaldson' or email == 'aaron.donaldson74@gmail.com' and password == 'thenorth':
  print('Access Permitted')
else:
  print('You shall not pass!')

  """
  You can use 'and not' in addition to and/or. 
  """

  
  