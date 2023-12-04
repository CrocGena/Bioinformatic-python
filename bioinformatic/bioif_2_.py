from bioif import *
from collections import Counter 
import sys



import random
def create_dna(n, alphabet='acgt'):
    return ''.join([random.choice(alphabet) for i in range(n)])
dna = create_dna(1000000)
print(len(dna))

DNA_Codons = {
    # 'M' - START, '_' - STOP
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TGT": "C", "TGC": "C",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "TTT": "F", "TTC": "F",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAT": "H", "CAC": "H",
    "ATA": "I", "ATT": "I", "ATC": "I",
    "AAA": "K", "AAG": "K",
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATG": "M",
    "AAT": "N", "AAC": "N",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TGG": "W",
    "TAT": "Y", "TAC": "Y",
    "TAA": "_", "TAG": "_", "TGA": "_"
}


def translate_seq(seq,init_pas=0):
    return [DNA_Codons[seq[pos:pos+3]] for pos in range (init_pas,len(seq)-2,3)]

print(translate_seq("TGGGCCTCATATTTATCCTATATACCATGTTCGTATGGTGGCGCGATGTTCTACGTGAATCCACGTTCGAAGGACATCATACCAAAGTCGTACAATTAGGACCTCGATATGGTTTTATTCTGTTTATCGTATCGGAGGTTATGTTCTTTTTTGCTCTTTTTCGGGCTTCTTCTCATTCTTCTTTGGCACCTACGGTAGAG"))




def codon_usage(seq,aminoacid):
    translation = []
    for i in range(0,len(seq)-2,3):
        if DNA_Codons[seq[i:i+3]]==aminoacid:           
            translation.append(seq[i:i+3])
    freqdict=dict(Counter(translation))
    totalweight=sum(freqdict.values())
    freq_cop=freqdict.copy()
    for seq in freq_cop:
        freqdict[seq]=round(freqdict[seq]/totalweight,2)
        return freqdict
    

print(codon_usage(randDNASTR,"R"))




def fib(n):

  if n==1 or n==2:
    return 1
  
  bottom = [0]*(n+1)  

  bottom[1]=1
  bottom[2]=1

  for i in range(3, n+1):
    bottom[i] = bottom[i-1] + bottom[i-2]

  return bottom[n]
  
print(fib(5))



def fibb(n):
  if n ==1 or n==2:
   return 1
  buttom =[0]*(n+1)
  buttom[1]=1
  buttom[2]=1
  
  for i in range(3,n+1):
    buttom[i]=buttom[i-1]+buttom[i-2]
  return buttom[n]
print(fibb(5))
# def fib(n):
#     if n==1 or n==2:
  
#      bottom = [0] * (n+1)  
#      bottom[1] = 1
#      bottom[2] = 1
#      return 1
#   for i in range(3, n+1):
#     bottom[i] = bottom[i-1] + bottom[i-2]  

#   return bottom[n]

# print(fib(6))


def fibona(n):
    old=1
    new=1
    for itr in range(n-1):
        temp= new
        new=old
        old=old+temp
    return new
 
print(fibona(8))




proteins=['D', 'Y', 'M', 'V', 'L', 'Y', 'H', 'R', 'R', 'M', 'T', 'F', 'E', '_', 'A', 'A']

def protein(seq):
  current_pro=[]
  prot=[]
  
  for pro in seq:
    if pro=='_':
      if current_pro:
        for p in current_pro:
          prot.append(p)
        current_pro=[]
    else:
      if pro=='M':
        current_pro.append('')
        
      for i in range(len(current_pro)):
        current_pro[i]+=pro
  return prot

print(protein(proteins))
        
    
    




