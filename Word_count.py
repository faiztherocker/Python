import  operator
"""
#Set basics
setone = {'again':1,'back':2}
print(setone['again'])"""

def start():
    word_list = []
    fr = open('FinalPaper.txt','r')
    content = fr.read()
    words = content.lower().split()
    for eachh_word in words:
        #print(eachh_word)
        word_list.append(eachh_word)
    clean_list(word_list)

def clean_list(word_list):
    clean_word_list=[]
    for word in word_list:
        clean_char='~!@#$%^&*(){}[]:";<>,./';
        for i in range(0,len(clean_char)):
            word=word.replace(clean_char[i]," ")
        if(len(word) > 0):

            clean_word_list.append(word)
    create_dictionary(clean_word_list)

def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            #Write 0 to sort by key 1 for value
    for key,value in sorted(word_count.items(),key= operator.itemgetter(0),reverse=False):
        print(key + '-->[ ' + str(value) + ' ]')

start()