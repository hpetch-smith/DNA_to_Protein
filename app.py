# The aim of this project is to translate the lactase genetic code into the corresponding amino acid sequence.
# files for the genetic code and protien mappings can be found on github

# Genetic code:http://hplgit.github.io/bioinf-py/data/lactase_gene.txt
# Amino acids: http://hplgit.github.io/bioinf-py/data/genetic_code.tsv
# Exon regions:http://hplgit.github.io/bioinf-py/data/lactase_exon.tsv

# define function that takes in dna file as argument
def get_DNA(DNA_file):
    #Create empty string to store DNA sequence
    DNA = ''
    #Loop through each line in the dna file
    for ln in open(DNA_file).readlines():
        #Add line to DNA string
        DNA += ln.split()[0]

    #Return the DNA sequence
    return DNA

#Save DNA string to variable
DNA = get_DNA('lactase_gene.txt')

#Check output
print(DNA)

#Define function that takes genetic code file as argument
def get_amino_acids(acid_filename):
    #Define empty dictionary
    Acids = {}
    #loop through each entry in the table
    for ln in open(acid_filename).readlines():
        #isolate line into list
        entry = ln.split()
        #insert list into acids dictionary
        Acids[entry[0]] = {'1-letter':entry[1],'3-letter':entry[2],'amino acid':entry[3]}
    return Acids

#Save the amino acids into a variable
amino_acids = get_amino_acids('genetic_code.tsv')
print(amino_acids)

#Get the exons from file
def get_exons(exon_filename):
    exons = []
    for ln in open(exon_filename).readlines():
        region = ln.split()
        exons.append({'start':int(region[0]),'end':int(region[1])})
    return exons

#Store exons in a variable
exons = get_exons('lactase_exon.tsv')
print(exons)

#Function to transcribe
def transcribe(gene,exons):
    mRNA = ''
    for exon in exons:
        mRNA += gene[exon['start']:exon['end']]
    return mRNA.replace('T','U')


mRNA = transcribe(DNA,exons)
print(mRNA)

# function to translate
def translate(mRNA,amino_acids):
    protein= ''
    start = mRNA.find('AUG')
    while(start < len(mRNA)):
        if (amino_acids[mRNA[start:start + 3]]['1-letter'] == 'X'):
            break
        protein += amino_acids[mRNA[start:start + 3]]['1-letter']
        start += 3
    return protein

protein = translate(mRNA,amino_acids)
print(len(protein))



























