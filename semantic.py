import spacy

nlp = spacy.load('en_core_web_md')

print('----------cat,monkey and banana simillarity----------')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2),'\n')
print(word3.similarity(word2),'\n')
print(word3.similarity(word1),'\n')

print('----------cat,apple,monkey and banana similarity-----------')
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2),'\n')

print('----------sentences simillarity----------')
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity,'\n')

note='''Cat and monkey seem to be very similar because they are both animals,
it was also really interesting how monkey and banana had a higher similarity  because monkeys eat banana,
Another interesting fact is that banana does not have any significant similarity with cat So ,
the model does not explicitly seem to recognise transitive relationships in its calculation.\n'''
print(note)
#my own example
print('----------dog,cat and mouse simillarity----------')
word1 = nlp("dog")
word2 = nlp("cat")
word3 = nlp("mouse")

print(word1.similarity(word2),'\n')
print(word3.similarity(word2),'\n')
print(word3.similarity(word1),'\n')

note_example='''when I ran the code found in the file example using the model en_core_web_sm,
I noticed that this model is very small, and did not respond to some of the simmilarity , I even got a warming saying:,
UserWarning: [W007] The model you are using has no word vectors loaded, so the result of the Doc.,
similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements.,
This may happen if you are using one of the small models, e.g. `en_core_web_sm`, which does not ship with word vectors,
and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
but when I used the model en_core_web_md, everything ran perfectly and it gave usefullsimillarities because this model is more advanced,
and it has word vectors loaded.\n'''
print(note_example)


