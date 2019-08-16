import json
import textblob as tb
import matplotlib.pyplot as plt
tweets = open('tweets_small.json','r')
tweetData = json.load(tweets)
tweets.close()
polarity=[]
subjectivity=[]

s=0
c=0
a1=0
a2=0
for i in tweetData:
    print(i["text"])
    cloud = tb.TextBlob(i["text"])
    print(cloud.subjectivity)
    print(cloud.polarity)
    polarity.append(cloud.polarity)
    subjectivity.append(cloud.subjectivity)
    s = s + cloud.subjectivity
    c = c + cloud.polarity
a1 = s/len(polarity)
a2 = c/len(polarity)
print(a1," ",a2)

#(data, bins, color)
plt.hist(polarity,bins = [-1,0,1], color = "green")
plt.title("Happy tweets")
plt.show()
plt.hist(subjectivity,bins = [-1,0,1], color = "red")
plt.title("Subjectibe tweets")
plt.show()
#(x, y, color)
plt.scatter(polarity,subjectivity,color="red")
plt.title("graph")
plt.show()
