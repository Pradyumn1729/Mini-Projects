message=input(">")
words=message.split()
emojis={
"happy":"😀",
"sad":"😞",
"neutral":"😐",
"vomitting":"🤢",
"ninja":"🥷🏼",
}
op=" "
for word in words:
    op+=emojis.get(word,word)+" "
print(op)    
 