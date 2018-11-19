from textblob import TextBlob
import re
fname=input("Enter file name")
#fname="review_demo.txt"
try:
  fhand=open(fname)
except:
  print("file can't open",fname)
  quit()

neg_count=0
neg_list=[]
pos_count=0
pos_list=[]
for line in fhand:
  
   line=re.sub('[^ a-zA-Z0-9]','',line)
   review_line=TextBlob(line)
   review=review_line.sentiment.polarity
   if(review>0.0):
      pos_count+=1
      pos_list.append(review_line)
   else:
      neg_count+=1
      neg_list.append(review_line)

for positive in pos_list:
   print(positive)
print("#"*10,"negative comment","#"*10)

for negative in neg_list:
   print(negative)
print(neg_count,pos_count)

