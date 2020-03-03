def superReducedString(s):
  res = []
  for i in s:
    if not res:
      res.append(i)
    elif res[-1]==i:
      res.pop()
    else:
      res.append(i)
  return ''.join(res)
