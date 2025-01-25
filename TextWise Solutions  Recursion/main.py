def reverse_string(sentence):
    #Base case
    if len(sentence) <= 1:
        return sentence
    #recursive case: reverse the string and append the first letter
    return reverse_string(sentence[1:])+sentence[0]

#Time complexity: O(n)
#Space complexity: O(n)
#Will the code work with number in it?
#Will the code work with special case
#with nothing in it
#Does it matter if it is a sentence or a word
