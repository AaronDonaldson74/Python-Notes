
#This attribute applies only to the instance of ws and ws_two.
class Website:
  def __init__(self, title):
    self.title = title


ws = Website('My Website Title')
print(ws.__dict__)

ws_two = Website('My Second Title')
print(ws_two.__dict__)


#This class has an attribute.
class DifferentWebsite:
    title ='My Class Title'

dw = DifferentWebsite()
print(dw.title)