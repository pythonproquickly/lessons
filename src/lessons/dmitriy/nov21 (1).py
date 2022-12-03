#dictionary stores the size of different people's shoes
"""key is peoples, values are shoe sizes sizes, calculate average shoe size 

"""

"""peoples_shoes = {
    "Fred": 8,
    "Dan": 10.5,
    "Christina": 7.5,
    "Thomas": 9.5
}

def calculate_average(values):
    values = sum(values)/len(values)
    values = int(values)
    return values 

print(calculate_average([1,2,25,60,100,125]))"""
    
"""average = []

for name, size in peoples_shoes.items():
    average.append(size)
    
print(average)

print(sum(average)/len(average))
"""
#average[8,10.5]
#def average(x)

#variable called sentence 

sentence = "The dog jumps over the fox in the river bed at night during a storm. The dog was named Evan. The storm was a level 5 hurricane"
#create dictionary that will have key the word and the value is the number of times it occurs in the sentence 

sentence = sentence.lower()
words = sentence.split(" ")

#counter = 0 

#this create a list of words 
word_count = {}

"""while counter < len(words):
    for word in words:
    #word_count_list = words.count(word)
        word_count["word"] = words.count(word)
    counter += 1

print(word_count)"""

for word in words: 
    word_count[word] = [words.count(word)]

print(word_count)
    
#this actually prints every letter in the sentence
#when you get a value from a key it has to exist 
