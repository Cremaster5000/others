"""This excersise consist in that you can how many times
a word is in the text, it doesn't matter if is uppercase o lowercase,
dots, comas, iterrogation signs, either spaces."""

raw_text = "Lorem ipsum ipsum lorem this is a test text, it doesn't. Have¿ to make the the the the sense asijgl"



def remakeText(raw_text):
	new_text = raw_text.lower().replace("'","").replace("?","").replace(",","").replace(".","").replace("¿","")
	list_words = new_text.split(" ")
	countWords(list_words)

def countWords(text):
	list_words={}
	for word in text:
		if word in list_words.keys():
			list_words[word] += 1  
		else:
			list_words[word] = 1
	print(list_words)

remakeText(raw_text)