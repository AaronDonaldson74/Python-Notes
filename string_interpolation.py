"""
heading_generator(title, heading_type)
heading_generator('Greeting', '1')
<h1>Greeting</h1>

heading_generator('Hi there', '3')
<h3>Hi there</h3>
"""

# Set up a dictionary named greetings
# use the greeting as the key, and the heading type as the value.
#Make a statment that prints the key associated with the value. 

greeting_one = ["Aaron's Birthday", "Dan's Birthday", "Brian's Birthday"]

heading_size = ['1', '2', '3']

  for x in greeting_one:

  for y in heading_size:



print('<h'+ y + '>' + x + '</h'+ y + '>')

# Below is the final answer.

def heading_generator(title, heading_type):
  return f'<h{heading_type}>{title}</h{heading_type}>'

print(heading_generator('Greeting', '1'))
