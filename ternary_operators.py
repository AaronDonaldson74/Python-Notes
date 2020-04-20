role = 'admin'

# One line ternary operator statment
auth = 'can access' if role == 'admin' else 'cannot access'

print(auth)

# Traditional coding method for the same thing.
if role == 'admin':
  auth = 'can access'
else:
  auth = 'cannot access'

print(auth)


""" second example """

role = 'Mickey'

love = 'loves Daisy' if role == 'Donald' else "isn't Daisy's lover"

print(f'{role} {love}')