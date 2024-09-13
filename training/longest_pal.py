def ispal(s):
    return s==s[::-1]
def isanagram(s1,s2):
    return sorted(s1)==sorted(s2)
banned=["bad","horrible","hate"]
def maskbanned_words(r):
    new_rev=""
    words=r.split()
    for w in words:
      if w in banned:
        new_rev+=" "+'*'*len(w)
      else:
        new_rev+=""+w
    return new_rev
reviews=["it was horrible ","i hate it"]
p_tags=["amazing","good","great"]
n_tags=["bad","worst","hate"]
negative=[]
positive=[]
neutral=[]
for r in reviews:
  words=r.split()
  for w in words:
      if w in p_tags:
          positive.append(r)
      elif w in n_tags:
          negative.append(r)
      else:
          neutral.append(r)
print(positive)
print(negative)
print(neutral)
