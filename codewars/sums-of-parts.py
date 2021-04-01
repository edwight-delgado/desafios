def parts_sums(ls):
  ls2 = list()
  ls2.append(sum(ls))
  for x in range(len(ls)):
    ls.pop(0)
    ls2.append(sum(ls))
  print(ls2)
print(parts_sums([0, 1, 3, 6, 10]))