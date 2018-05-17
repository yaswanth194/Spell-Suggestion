# Code for part 2
#Name: Yaswanth Reddy Vayalpati
#ZID:Z1805553
#ID: VAYA

#All necessary imports for part 2

import pickle
import sys
import string


# In[ ]:
#Opening the pickle file

f1 = open("pickled_data2.dat", "rb")   
my = pickle.load(f1)


# Getting word list , unigram and bigram dictionaries

mydict=my[0]
N=sum(my[0].values())
unique=len(my[0].keys())
uni=my[1]
bi=my[2]


#Function to add each character from the alphabets at all positions,one position at a time to the provided word 
#This function also prunes the list of words we got after adding. Pruning is nothing but checking the word we got after adding exists in the word list we got from corpus

def addingWord(word):
    word=word.lower()
    prunedAdd=[]
    addList=[]
    for each in string.ascii_lowercase:
        for one in range(len(word)):
            set1=word[0:one+1]
            set2=word[one+1:]
            addList.append(set1+each+set2)
            if(one>=(len(word)-1)):
                addList.append(each+set1+set2)
    for wor in addList:
        if wor in mydict:
            prunedAdd.append(wor)
    return addList,prunedAdd


# This function generates a list of bunch of words after deleting one character at a time to the word provided and prunes the list.

def deleteWord(word):
    delList=[]
    pruneDel=[]
    for one in range(len(word)):
        set1=word[0:one]
        set2=word[one+1:]
        delList.append(set1+set2)
    for wor in delList:
        if wor in mydict:
            pruneDel.append(wor)
    return delList,pruneDel
    


# This function substitues every letter in the word with every letter from a to z

def substituteWord(word):
    subList=[]
    pruneSub=[]
    word=word.lower()
    for each in string.ascii_lowercase:
        for one in range(len(word)):
            set1=word[0:one]
            set2=word[one+1:]
            if((set1+each+set2)!=word):
                subList.append(set1+each+set2)
    for wor in subList:
        if wor in mydict:
            pruneSub.append(wor)
    return subList,pruneSub
            
            
        


# This function transposes every consecutive pair of letters in the word provided and prunes the list.

def transposeWord(word):
    listTransp=[]
    prunTransp=[]
    for one in range(len(word)):
        part1=word[0:one]
        part2=word[one:one+1]
        part3=word[one+1:one+2]
        part4=word[one+2:]
        full=part1+part3+part2+part4
        #if(full!=word):
        if(one!=(len(word)-1)):
            listTransp.append(part1+part3+part2+part4)
    for each in listTransp:
        if each in mydict:
            prunTransp.append(each)
    return listTransp,prunTransp

#if no words are given ,then print error message	
if(len(sys.argv)<=1):
	print()
	print("Please provide words to get spelling suggestions")
	print()
#if words are provided then do this
else:
#for every misspelt word provided
	for each in sys.argv[1:]:
		a=each
		#below statements call add, delete, substitute and transpose functions
		add,prune_add=addingWord(a)
		dele,prune_del=deleteWord(a)
		sub,prune_sub=substituteWord(a)
		trans,prune_trans=transposeWord(a)
		print()
		print("Word is:", each)
		print("Number of Words after adding letters:",      len(add))
		print("Number of Words after adding and pruning: ", len(prune_add))
		print("Number of Words after deleting letters",     len(dele))
		print("Number of Words after deletion and pruning:",len(prune_del))
		print("Number of Words after substituting letters:",len(sub))
		print("Number of Words after substituting and pruning",len(prune_sub))
		print("Number of Words after transposing letters",len(trans))
		print("Number of Words after transposing and pruning ",len(prune_trans))
		print()
		print()

		# In[ ]:

		#!/usr/bin/python3

		# del[X, Y] = Deletion of Y after X  
		# outer subscript = X
		# inner subscript = Y (deleted letter)  

		del_table = [['a',0,7,58,21,3,5,18,8,61,0,4,43,5,53,0,9,0,98,28,53,62,1,0,0,2,0],
		['b',2,2,1,0,22,0,0,0,183,0,0,26,0,0,2,0,0,6,17,0,6,1,0,0,0,0],
		['c',37,0,70,0,63,0,0,24,320,0,9,17,0,0,33,0,0,46,6,54,17,0,0,0,1,0],
		['d',12,0,7,25,45,0,10,0,62,1,1,8,4,3,3,0,0,11,1,0,3,2,0,0,6,0],
		['e',80,1,50,74,89,3,1,1,6,0,0,32,9,76,19,9,1,237,223,34,8,2,1,7,1,0],
		['f',4,0,0,0,13,46,0,0,79,0,0,12,0,0,4,0,0,11,0,8,1,0,0,0,1,0],
		['g',25,0,0,2,83,1,37,25,39,0,0,3,0,29,4,0,0,52,7,1,22,0,0,0,1,0],
		['h',15,12,1,3,20,0,0,25,24,0,0,7,1,9,22,0,0,15,1,26,0,0,1,0,1,0],
		['i',26,1,60,26,23,1,9,0,1,0,0,38,14,82,41,7,0,16,71,64,1,1,0,0,1,7],
		['j',0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0],
		['k',4,0,0,1,15,1,8,1,5,0,1,3,0,17,0,0,0,1,5,0,0,0,1,0,0,0],
		['l',24,0,1,6,48,0,0,0,217,0,0,211,2,0,29,0,0,2,12,7,3,2,0,0,11,0],
		['m',15,10,0,0,33,0,0,1,42,0,0,0,180,7,7,31,0,0,9,0,4,0,0,0,0,0],
		['n',21,0,42,71,68,1,160,0,191,0,0,0,17,144,21,0,0,0,127,87,43,1,1,0,2,0],
		['o',11,4,3,6,8,0,5,0,4,1,0,13,9,70,26,20,0,98,20,13,47,2,5,0,1,0],
		['p',25,0,0,0,22,0,0,12,15,0,0,28,1,0,30,93,0,58,1,18,2,0,0,0,0,0],
		['q',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,18,0,0,0,0,0],
		['r',63,4,12,19,188,0,11,5,132,0,3,33,7,157,21,2,0,277,103,68,0,10,1,0,27,0],
		['s',16,0,27,0,74,1,0,18,231,0,0,2,1,0,30,30,0,4,265,124,21,0,0,0,1,0],
		['t',24,1,2,0,76,1,7,49,427,0,0,31,3,3,11,1,0,203,5,137,14,0,4,0,2,0],
		['u',26,6,9,10,15,0,1,0,28,0,0,39,2,111,1,0,0,129,31,66,0,0,0,0,1,0],
		['v',9,0,0,0,58,0,0,0,31,0,0,0,0,0,2,0,0,1,0,0,0,0,0,0,1,0],
		['w',40,0,0,1,11,1,0,11,15,0,0,1,0,2,2,0,0,2,24,0,0,0,0,0,0,0],
		['x',1,0,17,0,3,0,0,1,0,0,0,0,0,0,0,6,0,0,0,5,0,0,0,0,1,0],
		['y',2,1,34,0,2,0,1,0,1,0,0,1,2,1,1,1,0,0,17,1,0,0,1,0,0,0],
		['z',1,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
		['@',20,14,41,31,20,20,7,6,20,3,6,22,16,5,5,17,0,28,26,6,2,1,24,0,0,2]]

		# add[X Y] = Insertion of Y after X
		# outer subscript = X
		# inner subscript = Y (Inserted Letter)

		add_table = [['a',15,1,14,7,10,0,1,1,33,1,4,31,2,39,12,4,3,28,134,7,28,0,1,1,4,1],
		['b',3,11,0,0,7,0,1,0,50,0,0,15,0,1,1,0,0,5,16,0,0,3,0,0,0,0],
		['c',19,0,54,1,13,0,0,18,50,0,3,1,1,1,7,1,0,7,25,7,8,4,0,1,0,0],
		['d',18,0,3,17,14,2,0,0,9,0,0,6,1,9,13,0,0,6,119,0,0,0,0,0,5,0],
		['e',39,2,8,76,147,2,0,1,4,0,3,4,6,27,5,1,0,83,417,6,4,1,10,2,8,0],
		['f',1,0,0,0,2,27,1,0,12,0,0,10,0,0,0,0,0,5,23,0,1,0,0,0,1,0],
		['g',8,0,0,0,5,1,5,12,8,0,0,2,0,1,1,0,1,5,69,2,3,0,1,0,0,0],
		['h',4,1,0,1,24,0,10,18,17,2,0,1,0,1,4,0,0,16,24,22,1,0,5,0,3,0],
		['i',10,3,13,13,25,0,1,1,69,2,1,17,11,33,27,1,0,9,30,29,11,0,0,1,0,1],
		['j',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
		['k',2,4,0,1,9,0,0,1,1,0,1,1,0,0,2,1,0,0,95,0,1,0,0,0,4,0],
		['l',3,1,0,1,38,0,0,0,79,0,2,128,1,0,7,0,0,0,97,7,3,1,0,0,2,0],
		['m',11,1,1,0,17,0,0,1,6,0,1,0,102,44,7,2,0,0,47,1,2,0,1,0,0,0],
		['n',15,5,7,13,52,4,17,0,34,0,1,1,26,99,12,0,0,2,156,53,1,1,0,0,1,0],
		['o',14,1,1,3,7,2,1,0,28,1,0,6,3,13,64,30,0,16,59,4,19,1,0,0,1,1],
		['p',23,0,1,1,10,0,0,20,3,0,0,2,0,0,26,70,0,29,52,9,1,1,1,0,0,0],
		['q',0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
		['r',15,2,1,0,89,1,1,2,64,0,0,5,9,7,10,0,0,132,273,29,7,0,1,0,10,0],
		['s',13,1,7,20,41,0,1,50,101,0,2,2,10,7,3,1,0,1,205,49,7,0,1,0,7,0],
		['t',39,0,0,3,65,1,10,24,59,1,0,6,3,1,23,1,0,54,264,183,11,0,5,0,6,0],
		['u',15,0,3,0,9,0,0,1,24,1,1,3,3,9,1,3,0,49,19,27,26,0,0,2,3,0],
		['v',0,2,0,0,36,0,0,0,10,0,0,1,0,1,0,1,0,0,0,0,1,5,1,0,0,0],
		['w',0,0,0,1,10,0,0,1,1,0,1,1,0,2,0,0,1,1,8,0,2,0,4,0,0,0],
		['x',0,0,18,0,1,0,0,6,1,0,0,0,1,0,3,0,0,0,2,0,0,0,0,1,0,0],
		['y',5,1,2,0,3,0,0,0,2,0,0,1,1,6,0,0,0,1,33,1,13,0,1,0,2,0],
		['z',2,0,0,0,5,1,0,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,4],
		['@',46,8,9,8,26,11,14,3,5,1,17,5,6,2,2,10,0,6,23,2,11,1,2,1,1,2]]

		# sub[X Y] = Substitution of X (incorrect) for Y (correct)
		# outer subscript = X
		# inner subscript = Y (correct)

		sub_table = [['a',0,0,7,1,342,0,0,2,118,0,1,0,0,3,76,0,0,1,35,9,9,0,1,0,5,0],
		['b',0,0,9,9,2,2,3,1,0,0,0,5,11,5,0,10,0,0,2,1,0,0,8,0,0,0],
		['c',6,5,0,16,0,9,5,0,0,0,1,0,7,9,1,10,2,5,39,40,1,3,7,1,1,0],
		['d',1,10,13,0,12,0,5,5,0,0,2,3,7,3,0,1,0,43,30,22,0,0,4,0,2,0],
		['e',388,0,3,11,0,2,2,0,89,0,0,3,0,5,93,0,0,14,12,6,15,0,1,0,18,0],
		['f',0,15,0,3,1,0,5,2,0,0,0,3,4,1,0,0,0,6,4,12,0,0,2,0,0,0],
		['g',4,1,11,11,9,2,0,0,0,1,1,3,0,0,2,1,3,5,13,21,0,0,1,0,3,0],
		['h',1,8,0,3,0,0,0,0,0,0,2,0,12,14,2,3,0,3,1,11,0,0,2,0,0,0],
		['i',103,0,0,0,146,0,1,0,0,0,0,6,0,0,49,0,0,0,2,1,47,0,2,1,15,0],
		['j',0,1,1,9,0,0,1,0,0,0,0,2,1,0,0,0,0,0,5,0,0,0,0,0,0,0],
		['k',1,2,8,4,1,1,2,5,0,0,0,0,5,0,2,0,0,0,6,0,0,0,.4,0,0,3],
		['l',2,10,1,4,0,4,5,6,13,0,1,0,0,14,2,5,0,11,10,2,0,0,0,0,0,0],
		['m',1,3,7,8,0,2,0,6,0,0,4,4,0,180,0,6,0,0,9,15,13,3,2,2,3,0],
		['n',2,7,6,5,3,0,1,19,1,0,4,35,78,0,0,7,0,28,5,7,0,0,1,2,0,2],
		['o',91,1,1,3,116,0,0,0,25,0,2,0,0,0,0,14,0,2,4,14,39,0,0,0,18,0],
		['p',0,11,1,2,0,6,5,0,2,9,0,2,7,6,15,0,0,1,3,6,0,4,1,0,0,0],
		['q',0,0,1,0,0,0,27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		['r',0,14,0,30,12,2,2,8,2,0,5,8,4,20,1,14,0,0,12,22,4,0,0,1,0,0],
		['s',11,8,27,33,35,4,0,1,0,1,0,27,0,6,1,7,0,14,0,15,0,0,5,3,20,1],
		['t',3,4,9,42,7,5,19,5,0,1,0,14,9,5,5,6,0,11,37,0,0,2,19,0,7,6],
		['u',20,0,0,0,44,0,0,0,64,0,0,0,0,2,43,0,0,4,0,0,0,0,2,0,8,0],
		['v',0,0,7,0,0,3,0,0,0,0,0,1,0,0,1,0,0,0,8,3,0,0,0,0,0,0],
		['w',2,2,1,0,1,0,0,2,0,0,1,0,0,0,0,7,0,6,3,3,1,0,0,0,0,0],
		['x',0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0],
		['y',0,0,2,0,15,0,1,7,15,0,0,0,2,0,6,1,0,7,36,8,5,0,0,1,0,0],
		['z',0,0,0,7,0,0,0,0,0,0,0,7,5,0,0,0,0,2,21,3,0,0,0,0,3,0]]

		# transpose[X  Y] = Reversal of XY
		# outer subscript = X
		# inner subscript = Y

		transpose_table = [['a',0,0,2,1,1,0,0,0,19,0,1,14,4,25,10,3,0,27,3,5,31,0,0,0,0,0],
		['b',0,0,0,0,2,0,0,0,0,0,0,1,1,0,2,0,0,0,2,0,0,0,0,0,0,0],
		['c',0,0,0,0,1,0,0,1,85,0,0,15,0,0,13,0,0,0,3,0,7,0,0,0,0,0],
		['d',0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,1,0,0,2,0,0,0,0,0],
		['e',1,0,4,5,0,0,0,0,60,0,0,21,6,16,11,2,0,29,5,0,85,0,0,0,2,0],
		['f',0,0,0,0,0,0,0,0,12,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		['g',4,0,0,0,2,0,0,0,0,0,0,1,0,15,0,0,0,3,0,0,3,0,0,0,0,0],
		['h',12,0,0,0,15,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,0,0,0,0,0,0],
		['i',15,8,31,3,66,1,3,0,0,0,0,9,0,5,11,0,1,13,42,35,0,6,0,0,0,3],
		['j',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		['k',0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		['l',11,0,0,12,20,0,1,0,4,0,0,0,0,0,1,3,0,0,1,1,3,9,0,0,7,0],
		['m',9,0,0,0,20,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,4,0,0,0,0,0],
		['n',15,0,6,2,12,0,8,0,1,0,0,0,3,0,0,0,0,0,6,4,0,0,0,0,0,0],
		['o',5,0,2,0,4,0,0,0,5,0,0,1,0,5,0,1,0,11,1,1,0,0,7,1,0,0],
		['p',17,0,0,0,4,0,0,1,0,0,0,0,0,0,1,0,0,5,3,6,0,0,0,0,0,0],
		['q',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		['r',12,0,0,0,24,0,3,0,14,0,2,2,0,7,30,1,0,0,0,2,10,0,0,0,2,0],
		['s',4,0,0,0,9,0,0,5,15,0,0,5,2,0,1,22,0,0,0,1,3,0,0,0,16,0],
		['t',4,0,3,0,4,0,0,21,49,0,0,4,0,0,3,0,0,5,0,0,11,0,2,0,0,0],
		['u',22,0,5,1,1,0,2,0,2,0,0,2,1,0,20,2,0,11,11,2,0,0,0,0,0,0],
		['v',0,0,0,0,1,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		['w',0,0,0,0,0,0,0,4,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,8,0],
		['x',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
		['y',0,1,2,0,0,0,1,0,0,0,0,3,0,0,0,2,0,1,10,0,0,0,0,0,0,0],
		['z',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


		# Below for loops convert tables from list of list to dict of dict

		delDict_table={}
		for each in del_table:
			inde=each[0]
			tempDict={}
			for one in range(1,26):
				i=string.ascii_lowercase[one-1]
				tempDict[i]=each[one]
			delDict_table[inde]=tempDict
			
		addDict_table={}
		for each in add_table:
			inde=each[0]
			tempDict={}
			for one in range(1,26):
				i=string.ascii_lowercase[one-1]
				tempDict[i]=each[one]
			addDict_table[inde]=tempDict


		subDict_table={}
		for each in sub_table:
			inde=each[0]
			tempDict={}
			for one in range(1,26):
				i=string.ascii_lowercase[one-1]
				tempDict[i]=each[one]
			subDict_table[inde]=tempDict

		transDict_table={}
		for each in transpose_table:
			inde=each[0]
			tempDict={}
			for one in range(1,26):
				i=string.ascii_lowercase[one-1]
				tempDict[i]=each[one]
			transDict_table[inde]=tempDict

				
				
				
				


		# Creating a class with all the variables that we will be printing for each word

		class PrintObj(object):
			word="a"
			correct=""
			error=""
			represen=""
			xbyword=0
			p_word=0
			power=0
			
			def __init__(self,word,correct,error,represen,xbyword,p_word,power):
				self.word=word
				self.correct=correct
				self.error=error
				self.represen=represen
				self.xbyword=xbyword
				self.p_word=p_word
				self.power=power
				
			def display(self):
				print('{:20s}  {:14s}  {:14s}  {:5s}  {:1.9f}  {:1.9f}  {:1.9f}'.format(self.word,self.correct,self.error,self.represen,self.xbyword,self.p_word,self.power))
			


		# below object list is where we store details of each word as objects
        # Below loop compares the words that are left after addition and pruning with misspelt word and calculates probabilty based the formula
		objectList=[]
		for each in prune_add:
			missing=""
			prefix=""
			look=""
			count=0
			val=0
			for one in range(len(a)):
				if(a[one]!=each[val]):
					missing=each[one]
					if(one!=0):
						prefix=each[one-1]
						look=each[one-1]
					else:
						prefix='<'
						look='@'
					count=count+1
					val=val+1
				val=val+1
			if(count==0):
				indexValue=len(each)-1
				missing=each[indexValue]
				prefix=each[indexValue-1]
				look=prefix
			represenVal=prefix+'|'+prefix+missing
			t1=delDict_table[look][missing]
			t2=bi[prefix+missing]
			value1=t1/t2
			#obj.xbyword=value1
			value2=mydict[each]
			p_wordVal=((value2+0.5)/(N+(unique*0.5)))
			powerVal=(10**9)*((value2+0.5)/(N+(unique*0.5)))*value1
			objectList.append(PrintObj(each,missing,'-',represenVal,value1,p_wordVal,powerVal))
			
					


		# # Below loop compares the words that are left after deletion and pruning with misspelt word and calculates probabilty based the formula

		rep_check=[]
		for each in prune_del:
			error=""
			prefix=""
			bval=0
			count=0
			for one in range(len(each)):
				if(a[one]!=each[bval]):
					error=a[one]
					bval=bval-1
					if(bval==0):
						prefix='@'
					else:
						prefix=each[bval]
					count=count+1
					if((prefix+error) not in rep_check):
						rep_check.append(prefix+error)
				bval=bval+1
			if(count==0):
				error=a[len(a)-1]
				prefix=a[len(a)-2]
				if((prefix+error) not in rep_check):
						rep_check.append(prefix+error)
				else:
					prefix=a[len(a)-3]
					error=a[len(a)-2]
					rep_check.append(prefix+error)
			represenVal=prefix+error+'|'+prefix
			t1=addDict_table[prefix][error]
			t2=uni[prefix]
			value1=t1/t2
			value2=mydict[each]
			p_wordVal=((value2+0.5)/(N+(unique*0.5)))
			powerVal=(10**9)*((value2+0.5)/(N+(unique*0.5)))*value1
			
			objectList.append(PrintObj(each,'-',error,represenVal,value1,p_wordVal,powerVal))


		# # Below loop compares the words that are left after substitution and pruning with misspelt word and calculates probabilty based the formula

		for each in prune_sub:
			missing=""
			error=""
			for one in range(len(each)):
				if(a[one]!=each[one]):
					missing=each[one]
					error=a[one]
			presenVal=error+'|'+missing
			t1=subDict_table[error][missing]
			t2=uni[missing]
			value1=t1/t2
			value2=mydict[each]
			p_wordVal=((value2+0.5)/(N+(unique*0.5)))
			powerVal=(10**9)*((value2+0.5)/(N+(unique*0.5)))*value1
			objectList.append(PrintObj(each,missing,error,presenVal,value1,p_wordVal,powerVal))
			
					


		# # Below loop compares the words that are left after transpose and pruning with misspelt word and calculates probabilty based the formula

		for each in prune_trans:
			missing=""
			error=""
			for one in range(len(each)):
				if(each[one]!=a[one]):
					missing=missing+each[one]
					error=error+a[one]
			
			represenVal=error+'|'+missing
			t1=transDict_table[missing[0]][missing[1]]
			t2=bi[missing]
			value1=t1/t2
			value2=mydict[each]
			p_wordVal=((value2+0.5)/(N+(unique*0.5)))
			powerVal=(10**9)*((value2+0.5)/(N+(unique*0.5)))*value1
			objectList.append(PrintObj(each,missing,error,represenVal,value1,p_wordVal,powerVal))


			# Sorting and printing all the objects
		objectList.sort(key=lambda x: x.power, reverse=True)
		print('{:20s}  {:14s}  {:14s}  {:5s}  {:10s}   {:10s}   {:10s}'.format("Candidate Correction","Correct Letter","Error Letter","x/w","P(x|word)","P(word)","10^9 *P(x|w)P(w)"))
		for each in objectList:
			each.display()
