import random
import collections


Nucleotids=['A','G','C','T']

# def function(dnm_string):
#     dnm=dnm_string.upper()
#     for nuc in dnm:
#       if nuc not in Nucleotids:
#          return False
#       else:
#         return dnm
  
  
# nucleo='lGCT'
# print(function(nucleo))

# randomm= ''.join([random.choice(Nucleotids) for nuc in range(12)])
# print(randomm)

# def cout(seq):
#    dict={"A":0,"G":0,"C":0,"T":0}
#    for nuc in seq:
#        dict[nuc]+=1
#    return dict
       
       
       
   
    
#     # return dict(collections.Counter(seq))

# result=cout(randomm)
# print(result)
# str(result)
# # print(' '.join([val for key, val in result.items()]))
# output_str = ' '.join([str(val) for key, val in result.items()])
# print(output_str)


# a=6
# b=3
# print(f'{a}^2+{b}^2={a**2+b**2}')



# # text='CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC'
# # start=10
# # end=15
# # print(f'{text[start:end+1]}')


# start=1
# end=9                              
# result=0
# for x in range(start,end+1):
#     if x % 2 != 0:
#         result+=x
# print (result)
def colored(seq):
    bcolors = {
        'A': '\033[92m',  # Green
        'G': '\033[94m',  # Blue
        'C': '\033[93m',  # Yellow
        'T': '\033[91m',  # Red
        'U': '\033[91m'   # Red (same as 'T')
    }

    endcolor = '\033[0m'  # Reset color
    tmp=""
    for nuc in seq:
        if nuc in bcolors:
            tmp+=bcolors[nuc]+nuc
        else:
            tmp += endcolor+nuc
    return tmp+'\033[0m'


def caliddateseq(dna_seq):
    tempseq=dna_seq.upper()
    for nuc in tempseq:
        if nuc not in Nucleotids:
            return False
    return tempseq

def countNucFrequency(seq):
    return dict(collections.Counter(seq))

def transcription(seq):
    return seq.replace("T","U")

randDNASTR=''.join([random.choice(Nucleotids) for nuc in range(50)])

print(f'\nSequence: {randDNASTR}\n')
print(f'length-{len(randDNASTR)}')
print(colored(f'frequency {countNucFrequency(randDNASTR)}'))
print(f'transcription : {transcription(randDNASTR)}') 

DNA_RecerseComplement={'A':'T','T':'A','G':'C','C':'G'}

def reverse_compement(seq):
    return ' '.join([DNA_RecerseComplement[nuc] for nuc in seq])[::-1]


print("test"[::-1])
    
print(f'\nSequence: {colored(randDNASTR)}\n')
print(colored(reverse_compement(randDNASTR)))

def reverse(seq):
    mapping = str.maketrans('ATCG', 'TAGC')
    return seq.translate(mapping)[::-1]

# randDNASTR = "ATCGATCG"

print(colored(reverse(randDNASTR)))



# def gc_procent(str):
#     return round((str.count('C')+str.count('G'))/len(str)*100,6)

# print(f'{gc_procent(randDNASTR)}%')

# def gc_content_subsest(seq,k=20):
#     res=[]
#     for i in range(0,len(seq)-k+1,k):
#         subseq=seq[i:i+k]
#         res.append(gc_procent(subseq))
        
#     return res

# print(gc_content_subsest(randDNASTR,k=5))



# # def polindrom(str):
    
# #     leng=len(str)
# #     for i in range(leng//2):
# #         if (str[i]!=str[leng-1-i]):
# #             return False
# #     return True

# # word=input("write a word:\n")
# # if polindrom(word):
# #     print("The word is a palindrome.")
# # else:
# #     print("The word is not a palindrome.")
        
        
        
# def readfile(file):
#     with open(file,'r') as f:
#         return [l.strip() for l in f.readlines()]
    
    
# fastafile=readfile("rosalind_gc.txt")
# fastadict={}
# fastalabel=""


# for line in fastafile:
#     if '>' in line:
#         fastalabel=line
#         fastadict[fastalabel]=""
#     else:
#         fastadict[fastalabel] +=line
# print(fastadict)        
# resulttict={key: gc_procent(value) for (key,value)in fastadict.items()}
# print(resulttict)
        
# maxkey=max(resulttict,key=resulttict.get)

# print(f'{maxkey}:{resulttict[maxkey]}')
        


print(int(4+6/2+2*2))

mydna = 'acgt'
mydna = mydna + mydna
dna_counts={'t':mydna.count('t'),'c':mydna.count('c'),'g':mydna.count('g'),'a':mydna.count('a')}

max_freq=sorted(dna_counts.values())

fold=0
if fold > 2 : print('condition A’')

elif fold>100: print('’condition B’')

if fold> 2 or fold<2 : print('condition A')

else : print('’condition B’')

l3=[]
l1=[32,4,435]
l2=[32,4,435,5,7]
for elem in l1:
    if elem in l2:
        l3.append(elem)
print(l3)
# x=99999999
# if x>10 or x<-10: print('big')
# elif x>1000000: print('very big')
# elif x<-1000000: print('very big')
# else : print('small')
seq=[1,4,23,45,4]

d = {}
result = False
for x in seq:
 if x in d:
  result=True
 break
d[x] = True

print(d)

# for i in range(len(seq)) :     # line 1
#         for j in range(i+1) :        # line 2
#                 print(seq[j:i])     # line 3

x=-999999
if x>10 or x<-10: print('big')
elif x>1000000: print('very big')
elif x<-1000000: print('very big')
else : print('small')