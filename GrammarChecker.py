import nltk
grammar = nltk.data.load('file:CheckGrammar.cfg') #loading cfg file 

for _ in range(int(input("Enter number of sentences you want to check: "))):
    sentence = input("Enter the Sentence you want to check : ")
    wrong=1  
    sent_split = sentence.split() #splitting sentences into words
    tagged = nltk.pos_tag(sent_split) #POS tagging of each word
    tags = [x[1].lower() for x in tagged] 
    
    #Using a Recursive Descent Parser for parsing sentences through cfg
    parser = nltk.RecursiveDescentParser(grammar)
    
    try:
        parser = nltk.RecursiveDescentParser(grammar)
        
        for tree in parser.parse(tags):
            s = tree
            print(s)
            wrong=0
            print("This sentence is grammatically Correct.")
            
        
        if wrong==1:
            print("This sentence is grammatically Inorrect.")
            print("*"*20)
    
    except ValueError:
        print("Sorry! Some words are not covered in the grammar yet.You can add if you want")
        
        
''' 
TAGS that are not covered:
    
RBR -> 'rbr'    
WRB -> 'wrb'
WDT -> 'wdt'
Adj_S -> 'jjs'
CC -> 'cc'
EX -> 'ex'
FW -> 'fw'
LS -> 'ls'
PDT -> 'pdt'
RBS -> 'rbs'
VBN -> 'vbn' 
RP -> 'rp'
SYM -> 'sym'
UH -> 'uh'
Card_No -> 'cd'
WP -> 'wp'
WP_D -> 'wp$'
POS -> 'pos'


'''  
