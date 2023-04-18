import string
def hash(text):
  s = string.printable
  i = list(text)
  sum = s.index(i[0])
  res = sum
  mod = 0
  mod2 = 0
  for j in range(1, len(i)):
    sum += s.index(i[j])+1
    res -= s.index(i[j])+1
    mod += s.index(i[j])+1 % 10
    print(s.index(i[j])+1)
    mod2 += round(s.index(i[j])+1 / 10)
  return str(sum * mod + mod2)+str(res * mod + mod2)
