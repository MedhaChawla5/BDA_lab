from collections import Counter 
import re
count = 0;
with open ('q1text.txt','r') as file:
	data = file.read().lower();
	lines = data.split();
	for i in lines:
		count = count + 1;
print(f"No of words in the file : {count}");

words = re.findall(r'\b\w+\b', data)

word_counts = Counter(words)

sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

for word,freq in sorted_word_counts:
	print(f"{word}:{freq}")