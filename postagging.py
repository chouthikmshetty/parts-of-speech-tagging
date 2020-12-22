import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')
from nltk import word_tokenize
from nltk import pos_tag
#user input
questioninput=input("Enter the proper sentence")
#tokenizes the input that is entered by the user
text =nltk. word_tokenize(questioninput)
#nltk tags are assigned
tags = nltk.pos_tag(text,tagset='universal')
#print(tags) gives the output in the list of tuple format
print(tags)
list_dict = dict() #creates an empty dictonary
for i in tags:
	x =i[0] 
	y =i[1]
	list_dict[x] = y  #list gets converted to dictonary format
print(list_dict)