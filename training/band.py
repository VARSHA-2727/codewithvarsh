review=input("enter the review:")
banned=["bad","hate","horrible"]
words=review.split()
new_rev=""
for w in words:
    if w in banned:
        new_rev+=" "+'*'*len(w)
    else:
        new_rev+=""+w
print(new_rev)
