import random


def get_num():
  tgt=[]
  for i in range(0,99):
      s='{:02d}'.format(i)
      if len(set(s))==2:
          tgt.append(s)
  num=random.choice(tgt)

  return num
