def wrap_brackets( text ):
  return "<"*3 + "["*3 + "(" + text + ")" + "]"*3 + ">"*3

print( wrap_brackets("12345") )
