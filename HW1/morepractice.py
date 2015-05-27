complement = { 'A':'T', 'C':'G', 'G':'C', 'T':'A' }

queue=[]

def gen_codon(c):
	queue.append(c)
	return queue[-3:]


s = "ATCTGTATAACGAATATATACATTATC"
rcs = ''.join( map( lambda c: complement[c] , reversed(s) ) )
codon= map(gen_codon,s)
print rcs
print codon



codonf =  filter( lambda c: len(c)==3 ,codon)
print codonf

print"-----------------------------"
# Reduce a sequence to a count of each base pair
bp_counts = { 'A':0, 'C':0, 'G':0, 'T':0 }

def countit( acc, c ) : 
	acc[c] += 1
	return acc

reduce( countit, s, bp_counts )
print bp_counts

print "done"
