#Given strings pattern and Genome

Pat="TAGTCCGTA"
DNA="TAGTCCGTTAGTCCGAGGTAGTCCGACGACCGGCTTAGTCCGTAGTCCGTTAGTCCGTAGTCCGTTGTAGTCCGGTCTTTAGGAGAAACATTAGCTAGTCCGTAGTCCGAATAGTCCGATAGTCCGTCATAGTCCGATTAGTCCGGCCAATGGTGTAGTCCGTAGTCCGTTCTAGTCCGCCTACTAGTCCGTAGTCCGCTAGTCCGTAGTCCGATAGTCCGGTAGTCCGTTTAGTCCGCACTAGTCCGCTAGTCCGGTAGTCCGTAGTCCGACAATAGTCCGGTAGTCCGTAGTCCGTTCCCTAGTCCGAGTAGTCCGTAGTCCGTGCTAGTCCGAGTCAGGTAGTCCGACCTCTCGTAGTCCGGACGTTAGTCCGGTTAGTCCGAAGTAGTCCGACCTTTTTAGTCCGTTAGTCCGGTAGTCCGGTAGTCCGTAGTCCGTAGTCCGGTGTAGTCCGCTAGTCCGGAGCTAGTCCGTAGTCCGGTTAGTCCGATCTAGTCCGTAGTCCGTCTGCTAGTCCGCTAGTCCGATAGTCCGCAGATAGTCCGTAGTCCGTTGGTAGTCCGTACCTAGTCCGAGGTAGTCCGGTTAGTCCGGTAGTCCGGGGGGTAGTCCGATTAGTCCGGTTAGTCCGGTAGTCCGTAGTCCGCCCTCTAGTCCGGTAGTCCGTAGTCCGTAGTTTAGTCCGGGTAGTCCGTAGTCCGTAGTCCGCTAGTCCGTAGTCCGTCCTACAACTAGTCCGTAGTCCGTAGTCCGGATAGTCCGAGCTAGTCCGCGGATACTAGTCCGTAGTCCGTCGAGAGTAGTCCGAAGTTGGGTAGTCCGTTAGTCCGTAGTCCGCGGTAGTCCGGTAGTCCGAGTAGTCCGTAGTCCGACTAGTCCGTAGTCCGGGGTAGTCCGCCTGTAGTCCGAATAGTCCGAGGCTTAGTCCGATAGTCCGATAGTCCGTAGTCCGAGTTGTTAGTCCGTAGTCCGTAGTCCGGAACCTTAGTCCGCTAGTCCGTAGTCCGCATCGCGACCCTAGTCCGATAGTCCGTAGTCCGCGTAGTCCGTAGTCCGTAGTCCGAATCCAAGATTAGTCCGGTAGTCCGTATAATAGTCCGAGTTATCTTTAGTCCGTAGTCCGCAATAGTCCGGCAGTAGTCCGGTAGTCCGAACGACTTAGTCCGCTGTGCCCTAGTCCGGTTTAGTCCGTAGTCCGAGTGATTAGTCCGATTTGATAGTCCGAGTAGTCCGCGCTAGTCCGGTAGTCCGAACTAACCCTAGTCCGATCATCCGATCAACCTAGTCCGGTTTAGAATAGTCCGACTAGTCCGAGAGTAGTCCGTAGTCCGTCGTAGTCCGGGTAGTCCGTAACTAGTCCGAGTCAATACCTTTTAGTCCGCCTAGTCCGCATAGTCCGGTCTAGTCCGGAGTGAAGATAGTCCGTTAGTCCGATCGATATGGTAGTCCGGCAATACCAACTAGTCCGCCTAGTCCGGTAGTCCGTCTGCTTTAGTCCGTAGTCCGCCCCGTGTGAATAGTCCGAGACTAGTCCGTAGTCCGTCGATAGTAGTCCGTCCCTAGTCCGGCTAGTCCGCTCCGTTAGTTAGTCCGCTAGTCCGTAGTCCGGGATATAATAGTCCGCATTAGTCCGCTAGTCCGTAGTCCGTAGTCCGATTTAGTCCGACCTCTTAGTCCGCAGAGTAGTCCGCCTAGTCCGCTAGTCCGGTAGTCCGTAGTCCGTAGTCCGCTAGTCCGGTATATATAGTCCGATTAGTCCGATAGTCCGTAGTCCGGTAGTCCGCTAGTCCGTATACGCGATTTAGTCCGACTTGATAACATAGTCCGGCCTGTAGTCCGGTAGTCCGCTAGTCCGCAGATAGTCCGTAGTCCGCTAGTCCGGGTTTAGTCCGTAGTCCGTTACTAGTCCGCTAGTCCGATAGTCCGAAAGTGGGACATAGTCCGTTTAGTCCGCGAGCTGGTCATAGTCCGGAATGCTAGTCCGTAGTCCGCATAGTCCGCTTCAGGTTAGTCCGGAATTTTAGTCCGTTAGTCCGATAGTCCGCCTTCTTAGTCCGTAGTCCGATGATAATCTGGGGCCGTAGTCCGCTGTAGTCCGCTAGTCCGTAGTCCGATTAGTCCGACCACCCTAGTCCGGTAGTCCGGCGTGCTAGTCCGGGGTAGTCCGTATCTGTAGTCCGAGTAGTCCGGCTAGTCCGAGTAGTCCGTAGTCCGCCATAGTCCGCTAGTCCGTAGTCCGTAGTCCGCTATAGTCCGTGTAGTCCGTCAAGTAGTCCGCTAGTCCGCGTAGTCCGCTAGTCCGTAGTCCGTGACCTAGTCCGTGTAGTCCGGTTAGTCCGCCTAGTCCGACCGCGTAGTCCGCAGTAGTCCGGCTTTAGTCCGTTAGTCCGTAGTCCGCCTAGTCCGAATAGTCCGTTAGTCCGAGTAGTCCGATTAGTCCGGTAGTCCGAGGCTAGTCCGTAGTCCGTAGTCCGTAGTCCGCTAGTCCGCGTAGTCCGGTAGTCCGTTAGTCCGTTAGTCCGGCTAGTCCGTAGTCCGTAGTCCGTGCTCCAGTAGTCCGGATAGTCCGCTAGTCCGCCAAGGGGTTAGTCCGCCAACAATAGTCCGTAGTAGTCCGCATTTAGTCCGAACATAGTCCGATAGTCCGACGTAGTCCGGCGGTTATTAGTCCGCCCGTAGTCCGTGTTCCTAGTCCGCCCGAATTAGTCCGTAGTCCGGGTAGTCCGACCTAGTCCGATAGTCCGTAGTCCGACTAGTCCGATTAGTCCGTAGTCCGTTTGGTAGTCCGCCACTAGTCCGTCTAGTCCGGAGTAGTCCGATAGTCCGTAGTCCGATTAGCGAATAGTCCGCCGCAATAGTATAGTCCGCATAGTCCGTAGTCCGGCTAGTCCGACGTAGTCCGGGGATAGTCCGCTCCTAATAGTCCGCACACCGCCGTAGTCCGAGAGATAGTCCGGTAGTCCGTAGTCCGAGCAGTAGTCCGTAGTCCGTGTCTAGTCCGTTGTAGTCCGTAGTCCGTAGTCCGCTAATAATCCCGTAGTCCGAGGCTAGTCCGATTAGTCCGTAGTCCGACATTTAGTCCGTAGTCCGGCGATAGTCCGCTCATTAGTCCGCGCGTAGTCCGCCGTAGTCCGATAGTCCGGATAGTCCGTTAGTCCGTAGTCCGTAGTCCGCCTAGTCCGCTAGTCCGATTTGTAGTCCGTAGTCCGATGGTTAGTCCGCCTAGTCCGTAGTCCGGAGTCTTCTAGTCCGCTAGTCCGAATAAGTTAGTCCGTAGTCCGCTTAGTCCGTATCACGTAGTCCGAGATAGTCCGACTTAGTCCGGATAGTCCGGTTCTTAGTCCGTAGTCCGGAACCTAGTCCGTAGTCCGTCTAGTCCGTGAGGGTAGTCCGGGATAGTCCGGCTTTAGTCCGATATAGTCCGGTATTAGTCCGGGGGGCGACTCGTAGTCCGTAGAACTAGTCCGGGCGATCTAGTAGTCCGTTAGTCCGGTAGTCCGTAGTCCGTAGTCCGGTGACTTTAGTCCGTAGTCCGCTAGTAAAGCGGGTAGTCCGGCTAGTCCGCACAAAGCAATTAGTCCGGCTAGTCCGTAGTCCGCCCTAGTCCGTAGTCCGGATAGTCCGTTAGTCCGCGAGTAGTCCGTTTAGTCCGAGCCATAGTCCGATAGTCCGATAGTCCGTAGTCCGTAGTCCGATAGTCCGATAGTCCGAGAGCACGGATAGTCCGCTAGTCCGTGTAGTCCGAAGCTAGTCCGAGGTGGACAGTAGTCCGTAGTCCGCTAGTCCGCTAGTCCGTCCTAGTCCGAACCTTAGTCCGTCTGGTAGTCCGTAGTCCGGCTAGTCCGATATAGTCCGTAGTCCGTAGTCCGGATTCCTAGTCCGACTAGTCCGCCGCAGTAGTCCGGGTAGTCCGTTAGTCCGTAGTCCGGTTAGTCCGGTTAGTCCGCGACTATAGTCCGCTTTAGTCCGTAGTCCGTTGCGTCCTTCGTAGTCCGAGTAGTCCGCGTGGATTATTAGTCCGACCAAGTTAGTCCGCCTGCGTAGTCCGGGATAGTCCGGATAGTCCGGCACTAGTCCGGCTAGTCCGTGACGTAGTCCGCAGTTTAGTCCGAACCTGTTAGTCCGCCCATAGTCCGACCGATTTCTTAGTCCGACGTAGTCCGCCTAGTCCGTTAGTCCGGGCATAGTCCGGTAGTCCGTTAGTCCGCTAGTCCGTAGGTAGTCCGCCACTAGATAGTCCGATAGTCCGGGATAGTCCGTAGTCCGATTAGTCCGGGTCCTAGTCCGATAGTCCGATCTTAGTCCGTAGTCCGAGAAATAGTCCGGTAGTCCGTAGTCCGAGGTGTAGTCCGTAGTCCGGTAGTCCGGTATACTATAGTCCGTAGTCCGCTTTTAGTCCGTCTCCTAGTCCGTAGTCCGATAGTCCGCTAGTCCGCTAGTCCGTAGTCCGGTTAGTCCGATAGTCCGTAGTCCGTTGGCGTAGTCCGAGCTAGTCCGGCTAGTCCGGTAGTCCGCATTAGTCCGTAGTCCGCTTTATTTTAGTCCGTATAGTCCGTAGTCCGATAGTCCGCCACTCGGATTAGTCCGTAGTCCGCTAGTCCGCGAACTAGTCCGAAGTTACTAGTCCGGCTGCTTAGTCCGTAGTCCGTGGTTCTAGTCCGTCTACACGTAGTCCGACTCATTTTAGTCCGTAGTCCGTTAGTCCGCTAGTCCGGTAGTCCGTGCTTAGTCCGTAGTCCGCGTAGTCCGTAGTCCGTTAGTCCGCGTAGTCCGATGGCGCTAGTCCGAAATAGTCCGTAGTCCGTAGTCCGGCTCCAACTAGTCCGTAGTCCGCTTAGTCCGGGATTAGTCCGTGGTTCCGACGTAGTCCGTAGTCCGATTGCCTCCTAGTCCGGTAGTCCGCTAGTCCGCTAGTCCGCGTAGTCCGTAGTCCGTAGTCCGTAGTCCGGCGCTTGTTTAGTCCGTTAGTCCGTATGGATAGTCCGGGTAGTCCGATTAGTCCGTCTAGTCCGTTAGTCCGGCCTAGTCCGCGCTCTAGTCCGCAAATGTTAGTCCGAGTCGCAAAGCTAGTCCGCTAGTCCGTAGTCCGGGTAGTCCGTTTAGTCCGTAGTCCGATAGTCCGGCTAACCTAGTCCGATAGTCCGTAGTCCGAGATTAGTCCGGAATAGTCCGCAGCATAGTCCGCTCTTAGTCCGGTAGTCCGCTCATAGTCCGATAGTCCGTAGTCCGCTAGTCCGTAGTCCGCGTAGTCCGGTAGTCCGCTGTCTAGTCCGCCTCTTTAGTCCGCACTCGGATACGAGTAGTCCGCTAGTCCGGGCTGATAGTCCGGCTAGTCCGTAGTCCGCTAGTCCGACATTAGTCCGTATAGTCCGTCGGTAGTCCGGGTAGTCCGCACGTGGTCCTAGTCCGTAGTCCGAGTAGTCCGTAGTCCGTCGGTCTGTTAGTCCGGCCGGAAAGTAGTCCGTGCAGGGTTAGTAGTCCGCTAGTCCGACCCGGCTTCAACGATAGTCCGTGCCTGATAGTCCGTAGTCCGTAGTCCGTAGGAATAGTCCGAGTAGTCCGCGACTAGTCCGATAGTCCGGCCCTGCATAGTCCGTAGTCCGTAGTCCGTAGTCCGTAGTCCGGGATAGTCCGAAGTAGTCCGGTTAGTCCGTAGTCCGCAAGCCTCTAGTCCGGAAAACTACCTGTCCGCTTCTAGTCCGTAGGCCCTAGTCCGTGTCTATAGCTATAGTCCGCGTAGTCCGTAGTCCGGGTAGTCCGATCTAGTCCGCGACCTCCTAATCTAGTCCGGTAGTCCGCCCGTAGTCCGCGGGGATAGTCCGGGGTGTAGTCCGGTCTAGTCCGAATTCTAGTCCGCTAGTCCGACATTAACTAGTCCGTTTAGTCCGTAGTCCGTTTTTTAGTCCGCCTAGTCCGTAGTCCGGTAGTCCGTAGTCCGTAGTCCGCTTAGTCCGCATTTAGTCCGACCAGTAGTCCGTAGTCCGTAGTCCGATAGTCCGGATAGTCCGATTAGTCCGCAAGTCTTAGTCCGATAGTCCGTAGTCCGGTAGTCCGGAATATTTAGTCCGGTAGTCCGGTAGTCCGGGTATAGTCCGTAGTCCGCATAGTCCGTCGTAGTCCGCCCTAGTCCGATAGTCCGAGTAGTCCGATAGTCCGTTTAGTCCGCATAGTCCGTAGTCCGTATAGTCCGGACCACCAATACACTAGTCCGTTAGTCCGTGTAGTCCGCCTAATAGTCCGCGGCTAGTCCGTAGTCCGACCTCTAGTCCGAGCGAATAGTCCGGCTAGTCCGTTATAAAACTAGTCCGTTTAGTCCGCGTTAGTCCGTTAGTCCGTAGTCCGATAGTCCGGTAGTCCGGTGTAGTCCGAAGTAGTCCGTAGTCCGATATAGTCCGCTAGTCCGTAGTCCGGACGATAGTTAGTCCGTATAGTCCGGGGATAGTCCGATACGGCTTAGTCCGCTAGTCCGTGATATAGTCCGAACTCTCCATTTAGTCCGGTACCTAGTCCGTTATAGTCCGTAGTCCGTCATAGTCCGCGAGACTAGTCCGTAGTCCGTAATTAGTCCGTTAGTCCGTAGTCCGGTTAGTCCGTTAGTCCGTAGTCCGGGCTCTAGAGGCGATTAGTCCGTTAGTCCGGGCTAGTCCGAAGAAATAGTCCGTCTAGTCCGTAGTCCGGAGTAGTCCGCCCGTGTACGTAGTCCGCCTAGTCCGGTTCACTAGTCCGCTAGTCCGGCTTAGTCCGTTAGTCCGTAGTCCGCCTAGTCCGTTAGTCCGTAGTCCGGCTATAGTCCGGGGTAGTCCGTTTAGTCCGGTTCTAGTCCGTAGTCCGGTGTAGTCCGTAGTCCGTAGTCCGAAAGATAGTCCGCGGTAGTCCGTGTCAAGCGGCTAGTCCGTCTCGTAGTCCGCCACCCTAGTCCGTAGTCCGCAGCTTAGTCCGAGATAGTCCGGTAGTCCGGAGAGGACTTAGTCCGTTAGTCCGTAGTCCGTTTAGTCCGTAGTCCGTAGTCCGTAGTCCGTAGTCCGAATAACGTAGTCCGGTGCTTAGTCCGTAGTCCGTAGGCTGTAGTCCGTTGCTAGTCCGCTCGTGGCCCGTGTAGTCCGTTTGTAGTCCGGATTACACGTAGTCCGACTTATAGTCCGCTAGTCCGTAGTCCGATAGTCCGCGAGTAGTCCGAGTACGAGTTAGTCCGTTTAAGTGTAAGTTAGTCCGTAGTCCGACGAATAGTCCGTTATAGTCCGTGTAGTCCGTAGTCCGTTAGTCCGTTAGTCCGGTAAATAGTGAGCTAAGTAGTCCGGCCTTGCGGTTTAGTCCGTAGTCCGTCATAGTCCGATAGTCCGACTAGTCCGTAGTCCGTGAGGTGCTGTAGTCCGATAGTCCGTCTAGTCCGATTCTGTTCTAGTCCGGCTGTAGTCCGGGTATAGTCCCTAGTCCGTAGTAGTCCGGTAGTCCGGTAGTCCGGTAGTCCGCCTAGTCCGTCCTCCTGACCGTGCTAGTCCGCTTAATAGTCCGGTAGTCCGGAGTAGTCCGTAGTCCGGCCAGGCCAGTAGTCCGTAGTCCGCGCTAGTCCGTCTTAGTCCGAAAGAGCTTTAGTCCGCTAGTCCGTAGTCCGTACTAGTCCGGAGTAGTCCGTATAGTCCGCTTAGTCCGGAACCTAGTCCGCACTAGTCCGCCTTAGTCCGCAATAGTCCGTAGTCCGTAGTCCGGAGCTAGTCCGTAGTCCGCTGATAGTCCGTTGCTAGTCCGTCCCTAGTCCGGTAGTCCGCTAGTCCGATATAGTCCGTAGTTAGTCCGCAAGTAGTCCGTCATAGTCCGTAGTCCGTAGTCCGTACTAGTCCGTAGTCCGGCGTAGTCCGATAGTCCGACTAGTCCGGTTCGAAGTTAGTCCGCCTAGTCCGCTAGTCCGTAGTCCGCTCCAGTAGTCCGTAGTCCGGATGTCGACTAGTCCGTAGTCCGCGGACGGATGCCGATAGTCCGCCAGCGGGCTAGTCCGGGCTAGTCCGTAGTCCGCGTAGTCCGCGCAATTGCTAGTCCGCTTGTTAGTCCGTAGTCCGGATGCGTGTAGTCCGTTAGTCCGTAAATATAGTCCGACGGTAGTCCGTAGTCCGTTAGTCCGCTTAGTCCGGTTAGTCCGCGGAAATAGTCCGGATAGTCCGTAGTCCGAATCAGAGTAGTCCGTAGTCCGCTTTAGTCCGGTAGTCCGTAGTCCGAATATAGTCCGAGTTAGTCCGTTAGTCCGCTAGTCCGGTAGTCCGAATAGTCCGGGTAGTCCGACAATTCGTCTTAGTCCGTAGTCCGTTATCCTAGTCCGCTTAGTCCGGATCAGTAGTCCGTTTTTCTCTAGTCCGTAGTCCGTTTAGTCCGGCCGTAGTCCGACTAGTCCGCATCTAATAGTCCGTCTAGTCCGGTAGTCCGTAGTCCGTAGTCCGACTGTAGTCCGATAGTCCGGTAGTCCGCTAGTCCGAGTTAGTCCGGTTAGTCCGTTAGTCCGTTTCCGGATAGTCCGTAGTCCGGTAGTCCGATAGTCCGTCAATGTCAGTAATAGTCCGTAGTCCGTAGTCCGGCCGGTGTAGAATCGTGGTAGTCCGATAGTCCGCGTAGTCCGTAGTCCGATGTGTAGTCCGTAAGTTAGTCCGTTACTAGTCCGATCATAGTCCGTAGTCCGTTATAGTCCGGTAGTCCGCTAGTCCGCAGAGTAGTCCGACCCCTAGTCCGAGTAGTCCGCATAGTCCGTACATAGTCCGTGAAATAGTCCGTAGTCCGCTTTTGCTTCTTAGTCCGTAGTCCGCTAGTCCGCAGTAGTCCGTTGCATAGTCCGTTAGTCCGGTGGCTAGTCCGCGGTAGTCCGTTAGTCCGAGATTAGTCCGGACCTTCTGCGGTAGTCCGGATAGTCCGGCGCTTAGTCCGCAGTCGCCTCTAGTCCGTCCCTAGTCCGAATAGTCCGCGTTCTACGGTAGTCCGGAGTCTGCTAATAGAATGTTATTTAGTCCGGGGGCTATATAGTCCGTAGTCCGTCATAGTCCGATATAGTCCGTGATAGTCCGAATAGTCCGGAATTAGTCCGTAGTCCGTAGTTGACGTAGTCCGCAACCGGAAAAGCTCGATTTAGTCCGGTGTAGTCCGTAGTCCGGGTGCTAGTCCGTGCGTAGTCCGTAGTCCGCTTAGTCCGGTTAGTCCGTAGTCCGTAGTCCGAGATGGAGTAGTCCGAACAAGTAGTCCGGTTAGTCCGTAGTCCGGGTATAGTCCGGCCAAGGATTTAGTCCGCACACTCTAGTCCGTGTAGTCCGCTTAGTCCGATAGTCCGATTAGTCCGGGCGGTAGTCCGTAGTCCGTTAGTCCGACTAGTCCGTAGTCCGTAGTCCGAGTAGTCCGTAGTCCGTTAGTCCG"

#Return starting position of pattern in Genome using 0-based indexing

for i in range (len(DNA)-len(Pat)+1):
	kword= DNA[i:i+len(Pat)]
	if (kword==Pat):
		#print kword
		print i