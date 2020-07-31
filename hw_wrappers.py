
def wrap_brackets( text ):
  return "(" + text + ")"

def wrap_brackets_sq( text ):
  return "["*3 + text + "]"*3

def wrap_brackets_tr( text ):
  return "<"*3 + text + ">"*3

print(wrap_brackets_tr(wrap_brackets_sq(wrap_brackets("12345"))))