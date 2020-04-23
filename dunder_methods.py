"""
#An intro to Dunder Methods.

__init__ #the double underscore deals with private and protected methods.
class string

    private/protected methods #would have limited visability outside of that class.

"""

class Invoice:
    def __init__(self, client, total):
        self.client = client
        self.total = total

    def __str__(self):
        return f'Invoice from {self.client} for {self.total}'

    def __repr__(self):
        return f'Invoice <value: client: {self.client}, total: {self.total}>'

inv = Invoice('Google', 500)
print(str(inv))
print(repr(inv))
