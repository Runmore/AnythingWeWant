#find reverse and complement of string
#given a DNA string pattern

DNA= "AGACACATTTTATCCAGCCCTCGTCCTGTACGTGAAAATCTGGTACTAACGATTCGAAGCAGAGCACAACCTTACGTGCCTGCTACTGCGACAAAGCTCAGTCTGCCGACTCTGGCAATCTACCCGCGATTTCTCGTCTCGCCCTCAGTGGGTTATCGATAGGCTACTACTACTCCTGCCCACGGCTCTTGACACGTAGTAACCCAGCCCCCGCTGTATTACGATTCTGGCACCACTCACTCTGCTTCAACCGGACGACCGCGTTTATTGGACCGACTTATGCTCCGAGGGATTGAACGGCCCGCTGATCCGGCTGCTTTTGCTGAATCCGCCGCGCTATGTACGGTTCGTAAGTGATGTGTACCATTGGAAAGTCCGTAAGGTAGGAATTGAAATCCCTTTTTCTTTCTCCTCTTGATTCACCCGGCGTTACGATTAGATAGTTTTGTGCCCACCGCGATTAGACAACTTAAACTCACTATAAAAGCACTGTCGGTAGGCGTGCTTTATAGTGCGCTTGCACTTAAGGGAGCCGGGTACAGCCTGCGAGGGGTATCCGCTGGGATCACACCTCCGATAGTGAGTCTTGGTGGCCGTGTGTTCTTAGGCACGCCCCTCACTGCCAGGTGACACAGGGACCCCAGACTACGTGCGACGTGGGAGCATACAAAACCGACGACGAGTAGTAACCGATTTCCTACAGGAGTGGCTCCCGTGGACGGACATAAGGACTCCGGTCAGCCACTGACAGCCTAAAGTTAGGTGCAATAGCATGTTAGCTCAAGGAGCCGTAAAGAGCAGCATCACCACATTTCGGCTAACGTACTATTATCCCTTATCCCATCGGCGGTTATAGCGGTTCTGCACGTTGTATGGGGGCGAAGAGTTATCTCCCTAAATTTCTGGAGGTCCTACATGGACGGCTCGCTTGGTGGCTATTAAGGTAAATCCTATCCTTTCGATTTAGGGAAACTCTGGACAGTAACAAAGCCCGAGGCAACCAATATACCTATTTAGTGCTTAAACCCCGGAGCGCCAGTGCCCAAAGCCTAATAAAGAGGCGGAGTGCTAGAGACTGCTCATTCCCTTGGTACAACGCTATCGCTACGATTGACTTACAAGGATGTGTGACCTCCCGGTTTCGAAACTAGGCACATTCGAACTTGCTGCCGTTACACTGTATGGAGTTGAAGACATTGTGGGGCATGCGTCAATGGGTTAGTCGAGCCGATCAGTTTCGGCGTTTAAGTATAAACCCGGAGGCCAAGAATCGCTGTAGGCGGAGGTACACACCTACTAAGCGTCGCTAATTTGCGCGATTGGCATTGTAACTAGTCGCGGGAGGAGTGGTGCCGGTTAGAATTCGTGCAATGAGGCCGTCCTCTCTCCTGTGAGGAGCGAACAGGACGGTCCAGTCCATCCGGCGAGAATAGAATTAACTAGCAATATCGGACGAGTAACTGGCATGCAAGGCTTTTCGCCTAGTGTGGACCAAATTCAGAAACTCCTAGCTCTTAACTGCTGCGAAACCTCTTCATGTCGACCTGGGTCTCTTAGAATTCCAGAGTTGGAGTCTGTGCTGCGAACCCAAGGAATCCTATGCGTTTTACGCTCTATATCATCTCATACCTTTGCCGCTAGCCACCATAACACAGTGTTTGGAATTCCTGAGCGGCTCCGAACGCATCGACCGACATTGATAGAACGGAAGAGAAAGTCGAATGTGAGACGCAACCCCTGACTACCACTATCCTGTTCAAAATCAATTACGGCAAGGCCACCATGCTACTGTTATTCACTAAGCAATTCTGAACCATCCCATGCATGGACTTCGCGTCATATTTTTCTCTATCGAAGGGAATCGGGTGAGTCCATGTAATTGTATTGGGCACCTTAGCATCAGAGGGCACATACCCGTAATTGGTGTAACTTGAGTCCAGCCCAGCGACCTCTCGTCGGTTGTACGTAAAGAAACTATCGCGAGCTAGGAGCCTCAGAGTCAAAGGCACATACACTCGAAGTCCTCCAGGAGATCGTAAATGAAGAATGGAAAGCTTTGCCCGCTCAGAGCCACTACATCTTCATGGAGCCGAATTGGGGGACTGCTCATATTTTTCTTATCGGATTGTTTTCCGAACCTTTAGACGTAGCTCCTGTATCGACCCCTTTCATTCAGAGTGGAGCGTAATCCTAGCACTGGAAGACGGTAAGCTTTGGTCAGTGAAATTGACACTTCGCTACCACCCCAACACGCTCCCGGCTCTAGATACTGCCAGAATGTCCACGATTATCCGTACATGTGAGCCTCCGTGATAAAACTGTTGATACCACTACGGCAGCCGTGTGCCCTAATGCCCGTCCGGCTAGTGGACGCCGGCTCTAGAAGTAGTCCGTCGGATATTTCCTGTAATTATAATCCGTAAGCTACGCTGCGCGCCCCACTCCATGGAGTGCCTGAAGTGGGCATAACTATCCCTGTTAGCGGGAAGTAATAATGGGGGCATATATGCAATAGTATATTGCACGATCCTAGCTAATCGGGATCGGAATTGTGGACTGTGCAGGACCACCATTCCACTACGGAGGACGAAGGAATCTAATCTGAAGATCTGCTGTAACTAGCCTAGTTTAGATCAAGCGGCAGAAGAAACCGTCGCCTCTGGTCGTTATACATGCAGCATGGAGCCCTCACCCCATTTCAAGGGTGCGGACGGCCCTGTCGCTCTCATATATGTACAACTAAGGGGACAGACATCCCAACTTGATTGTGAAGCACTATCTGACCACTGTAGGACCGTAAGTTCCAATGCTGAAGGGTCCCAAGTCTAAAAGAGTTCTCGTGCATGAACCTTAAAGATTGGCGTGCCCATCAAAGCCGGCATGCTGGTCTCCACTCACTGCTAGCATAATTTCTTAACGTTCTCCCCTTTGCGGAGTGCCGAGGACGAACCGACCACCGGCACGAAGCAAGAAGGTATGGTGGCCCTTTCGAATCAGCTGGACAAACTGCAATTGACCACAAGCGGCCGAAACCCACGCAGGAAGGTAATATCTTTGTTGCGATACCAGAAGTCCGCCGGCGCGAACCCATTGTACATATGCTAAGGTACGCATTCGGCTTCACTTCGCCACACAGACCGGTATAAAGTGAGGGACAATCAAAATGGAAGTTATATGAAAATATTAAGCTTTCGTAGCGAACACTTCCCGACATGGAAACTGATCAACTCGTCAGACTTTGTGCGTCATGCGACACCTATTGCTAGCTGATGATATCCACACGTAATGGCTTATGGATATGGCTCCGAACCATAAGGCTCAGCGAATCGCGCCAACTTACGCACAAACCGGCGTTGCGATTTGTTCACGTCATGCTCGATGCATTCGAACTGTTGATTCTTCAACTATGAACCTCAAGACCCGCCTAGCCGTGAGTGGTCGGGGCTCTCTTGTCTGAGTCGGATCTTCCATATGATCTTTGCCACCATGTCGTGTGAAGTTCTGACATAGTGCCCATCCCGACGTGATGCGAGTCCAGTGGGATATTGATGCGCTATTATGACACATTTAAGTCGGGAAACACGTCTCCACTTAGCTCCTTCCCCAGCTTATAATGGTTCTAGTCGGACCCAAGGGCAAATCACATTTAGAGGCCCCTTGGTCCTCCTTTGTTCGGCGTTCGAGAATTCAAGTACTTACCCGACCTCACAGACTTGGCAACCTCTATATGCTTTCTTCATAAGTATTTTTTATCACCAATGCCCACCCCTGTAGCTCTTCTTGGTCATGCGGGAAATTATTACGCTGTGTTCTGGTTAGTGCCGATTAAGACGCGCATCGCTCAAGGTGGACGATGGTACCCTGGAAGCACATTGCCCGGAAGGTTGAATCCCTATAGACGGTTATGCCACTCGTGAGCGAACAAGTCCAGTAGCGACTACCTAGAGCTATAGACAAGATACTCTAGCACGACGTACTCCTTTGTCCAATGCCTGCCCTAAGCTCTATATGGGGGGAGCCAATCCCGGAATGTAGGAGGCGACGTAGGGGATCATTTTTCGTTACTAGTGAGTATAGGATATTGCCCTAAGACACGGCCGCATTGGTATTCAAGGGCGATTAAAGCACCGGATTACACGTAAACGCGTCATGGGAGGACCGAGCTTCTGCGCAGGTCGCCACGCGCAGTTTTCGAGAATTCAACGACGGGGGGCCGAAGCGCCGGCCCCAACTTCGAGGACGTCGCTAGCGGGCTCACCTTGGGGGTCAAATTTTGGGCTCACACCTCTCGAGGGCGAGTTTACTGTGATTTGAGTCCATAATCAGGTCAAAGATGGAATGTACTGGTCTCCCGGACGTCATCGGCAGCAAAGCTAAGTATTCTCCTTGTTCCCGTACATGCAACCCGCAAATTATTCAACATTTGAAACTAATTGGGTATTCGTAGCGCACAAATGGTACTCCCTTTCGTGCGATAAGTAGTAGCTGCCACGAGGGGGCACAGACGTGGTAGTACTAGGATCATGGTGTGACGATACAGACGTTTATTGCAGGAGTGCGCTTGCCTAGACCTCCGTTGGAGCCGTCCGTAGTTATACAACTGATACCGGGGTTGCAGGGCATCCGGGGGCGGTGATTTTCCATCGTGTACGTCGATCAGCACATTTAATAAAGCCTTATGGTCCAGTCATGACACGGGACTACTATCAAGCGGAGCAGCGTCAACAGTTGGGCTGGTCTTCAGCACACTTCAGGTTGACAACTACTTGAGTCTCGAGGCTCCGGTGACCTACGGGAGGAGTCAAAGTAGGAGAGTACTCTAAGCAATATCAGACACGGGTCAGGGAACAGGACACTGCCAAGCCGCAGGAGTGCTACGCGATCTATTGGTACGAAGTCAGGATTTCGGTAAGCCTGTAGCGGCTGACACACCCCTGTAGGCGCTCTAGTCGGAGAATTATCTGTGCCATTAGGGGGGAATGGTTTTCAGTAGCCGGGGTGGCAAGGACATCAAACAGACGACTACATTTTGCCTGGTCATCTAGATACAAACCGTAGGTGTACGAGTGGTCGTTTGTATGGATTTATTTGGGTAGATGAGCGAAACGAACACGGAGTCGTTGTCATTGGTCCTGGAGCGGACCGTTCAAAACACCGAAGCCCAAGCAGGTCCAAAATGGCCAATCTTTAGCTGCATATTGTACCCATACTAGTTAACGCGGTGGATGCCAGAAGTTTTTGGCGGAAAAGGACCCCGTTAGGTTCGACTCTACTACCCATCACCAAGCGTCCATTCGGCGGACGAACGAATTCGTCCGGGATTAGGTGTTAAGCTAGGGTTTCACGCGAACAGCTTCTCTGCGTTTACGAAGACAGGCTACTGGGTTGGCGTACAGATACGGAGGCAGATCTGCGTCTCAGCGGTGGCACCTGTAAGGACTTAAGCGGGTGACAAATGCATAATTCTTCTCTGGAGGAGGCGGGCTCTAAACGCTCGCCAAAATTATTAGGGGACTTTGAAGCGCACAATTCTGATCTACTTGAGATGTCGGATCGGCCGAATCAACACCGGTGATGTCAAAAGGCGTTATAGCAGAGAAAAGCCACTTCATCGTTGATGCGCACTTAGTTGACAGCTGCCGCAGTAAAATCGAACGTAAGTCTTTCGCGCCGGTACCCTTTCTACCGGAGCGCTTGGTACTCTTGCTGCTCTTAGCGCAAGACTGCTAGCGACTACAGATCGTACGGTCATGAAACCGCAAGAACGAGCAAAGAGTGACGGCACGATAAACCACTGTTCAACCTTTCCAGGGACTGTTCGAGCTATTTCTCAAACCCTGTGGCCCTCGGTAGGCGATCCTTTTGACTATCTCTCGTCGTGGGGGTGAGCGCCAACTTTCTGCGTCACCCAGAGACCGACCACCGCACATGCACTATCGCCTCGCAGCTGGCGTCGAATCTCGAGCCTAGGTAGCAGCGCGCTACTGCGCTTGGGGGTTCGGGGTCAGGTAAACTTTAGTCGAGCCGCTCCAGGTCCCTGTTGGTTTAGTGTTACATTCTGTCTCGGGCGATGTTTAAACTTCGTTTAATACAGAAAGCCGTGGCTCGGTCACGGAAACATAATGAATGTATGTGATGCTCAAATCATCTAGACGACCCAGTGGGCGATCACGGCGTCGATATTACAGCTGCGTAACATGAGGTATGAGAATTAGTATTGAACCTGTGACACCTCCGCAGTTCTGGCGGCATATGCAGATAAGCGAGGAGTCACGACCTCAAAACCTTATCAGCCAACCAAGTTGCACATTTCGCGGCCTTACTGCTGTTTATTTGCGCAGCATTGCCATTGACACCTTTGGTCAAGTTTGACCTGAAGGATGATTTATTCCGGCCTATCTTAGATTGCGTCGTAATTTATTGGATGTCCACATTTCGGTGCTGACGTTGCGACCTCAGGTATCTGCATCTGGAAGGAGATTATTCTGAGCCCCAACCCCGGACTCCATTCTGTAGGCAATATGTTTTCCGCACAACACATCCACTGAACTGAGCGGATCCCTCGGCCACCGACTGCCCACACTCCCACAGCGCCGGGATCGCGGTGACTGGGCACCGTCTGTATAGCCGTCCCCGTCGTAGCTCGGCGAACCCATCGAGGAGCCGTAGGAGTCCCGTAGCGTCCCGACTCCGGCAGGTGATCTCCGCACAGGGGTCTAGGCGGTGCGACTTATTTTTACCTAATTGCTAGTTGCAGACCTAGTGCCTTTCCTGTGGTTAACAGAGGCTTTTCCAATCTCCCAATGCGGTACGAGACCCCGTTCAAGTCCGGTCGCTATGTGTGTCAAAGACGGGCAAAGACCTATTTCAAGTTTCGGGATCAGCCCGAGGCTTACATGCATTGGTCTAATGTTTTGTATCGACTTATGCATGTTCTTTACTACGCAGTACTTGGGGACATTAACGTGACCCTTTCACGAGTGCAAATCGAGTTGTATAGGATTGCGACCGCCGCCCTCAGAGGTTTCAGCAAAGTGCGTGGGACGTGAATACGAGCAGGACTCTACTCTGTAGACAATTAGTTGTTTTAGATTGCGTCAGGGAGTACAGTTCGTAACACGAAGGTAAGTCACGCCCATATGGTTGCAAGACTAGAAGATTCGTACAGTGAACAGCGGATCCCGGTGACCTACCTCTAAGTCGCGGCATCTGAGCCACTGAAGTCAGTGAATTAAATTAACATATCGCTGCCCTGATCACAAACCTAGTGAATTTCGAAAACTAGGTGATTATCCGGCTTGGGTCCGCGGGTTTATTGGTCTTGGCTTGGCGACAGAGCTGCTAAGGATGTCAATGGCCTCATTAATGCCGATACGGGGAGTCTTATTGCCCGAAGCCGTAGGATGCGTAATCCCAGTCTGAAGTGACGCAGATGGGTCAGGATTGTGTCTTCATACTGCGAGGTCACATTCATGTGTTTTGAAGTGTGCCGCAGCATCTTTTAAAAAAAACGTCATCACGCGATTTCGGAAGGTGACCTATGGGTCCCTTCTGAAACGGGTCAGCAGAGCTGTATAAGTTTATCTAATCAAAATGAAGCGCAGCCCTGTATTCGATCTGTACCATTTATGCTGTACTTTCATGACCGAACATTTTACTAGTGAGTCCGAATGATACACGAAGAATGCTCCGGAAAGGACCCCTAGAAGTGCTCACATGCCTTTGCGCTTAAATGCCACATCGCACCACGGATATATCTGTCTCCACAAGGTGTGTTAAGGAAGTCATTTTGCGATTGGGTCATGCCCCTCCGCCCTGTATGGTGCACAGTGAAAAAGCTTGACTATCCCCACGTGTATTGAGAGTTGACCAACAAAGACTGTCGGGATGCGCCGATCTCGGGGTCACCTCCCTCGTTTCAGGCCCCATTAGGGTTTGTGAACCCGGCGGGGAGACGATGTGCGAACAGTGTGGACGATTTGTTCCGAACCGGTGCAGGCCCCGTTTTCTTCCTGGACGCCGTGCATATTCACATATGCATCCCCGATGTACTTGTGCCAATTTTGGTAATTCTCCGACTAACATTCCTACCTTCTCAAGGCTATCCCTATGGAAGTCCATTGCCCATATCCCGTGATATAATGTAAGCCCCAGGACAGTTAGGGCTACTTTCCTCCCCCAGAACGTAACCGTCAGATGCAGAAGTGGCGGCGCTGAGTACTATCCGATGAATACAGAGCCGTGCGTGGCCCCATAGTGACGCCTGTCGGGTATTTTCTAGGAGGATTCTGGACTCTTCTGAGGTGAGAGGGCTGAACCGAGAACCCAGACTTACGGTACGGGCCGGGACCCTTGGGCTAGGCAACAGCCTCCGACCCAGGCAATTAGCAAGACAGTTTAAACCTTGGACTCAGGCCGAATGCACTGGCGGCCAATCGCCCGACCG"




#output pattern, then reverse complement of pattern

basecomplement = {'A': 'T', 'C': 'G','G': 'C', 'T': 'A'}
s = DNA
complement_s = []
for base in s :
	complement_s.append( basecomplement[base])
scomp = ''.join(complement_s)
#print s
#print scomp
print scomp[::-1]




