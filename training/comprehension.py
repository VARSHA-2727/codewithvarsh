review="it was horrible"
review1=review.split()
banned_words=["bad","horrible"]
result=[True if w in banned_words else False if w in review1]
print(result)