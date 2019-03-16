"""
The main script to handle arguments and run commands
"""

from dna import NucleotideSequence
from sys import argv


if __name__ == '__main__':
    if len(argv) == 1:
        print('========================================================================================================================')
        print('COMMANDS:\n--analyze <file.txt>\n--cut <file.txt> <enzyme>\n--search <file.txt> <sequence>\n--makereport <file.txt>')
        print('========================================================================================================================')
    else:
        if argv[1].lower() == '--analyze' or argv[1] == '-A':

            dna = ''
            with open(argv[2], 'r') as f:
                data = f.read()
                for char in data:
                    if char.upper() in 'ACGTYRWSKMDVHBXN-':
                        dna += char
                f.close()

            sequence = NucleotideSequence(dna, identify='USER')

            r_enzymes = sequence.search_restriction_enzymes()
            count = 0
            for enzyme in r_enzymes:
                if len(enzyme[1]) > 0:
                    count += 1

            o_enzymes = sequence.search_restriction_enzymes(threshhold=1)
            count2 = 0
            for enzyme in o_enzymes:
                if len(enzyme[1]) > 0:
                    count2 += 1

            print('========================================================================================================================')
            print('DNA SEQUENCE LENGTH: ' + str(sequence.get_length()) + 'b.p.')
            print('TOTAL RECOGNIZED RESTRICTION ENZYMES: ' + str(count))
            print('ONE-CUT RESTRICTION ENZYMES: ' + str(count2))
            print('========================================================================================================================')

            i = 1
            for item in o_enzymes:
                if len(item[1]) > 0:
                    print(str(i+1000)[1:] + ': ' + str(item))
                    i += 1

            print('========================================================================================================================')

        if argv[1].lower() == '--cut' or argv[1] == '-C':

            dna = ''
            with open(argv[2], 'r') as f:
                data = f.read()
                for char in data:
                    if char.upper() in 'ACGTYRWSKMDVHBXN-':
                        dna += char
                f.close()

            sequence = NucleotideSequence(dna, identify='USER')

            print('========================================================================================================================')

            cuts = sequence.cut(argv[3])
            print('LEFT OF CUT: '+str(cuts[0].get_length())+'b.p.'+'\n'+str(cuts[0]))
            print('RIGHT OF CUT: '+str(cuts[1].get_length())+'b.p.'+'\n'+str(cuts[1]))

            print('========================================================================================================================')

        if argv[1].lower() == '--search' or argv[1] == '-S':

            dna = ''
            with open(argv[2], 'r') as f:
                data = f.read()
                for char in data:
                    if char.upper() in 'ACGTYRWSKMDVHBXN-':
                        dna += char
                f.close()

            sequence = NucleotideSequence(dna, identify='USER')

            print('========================================================================================================================')

            print('FOUND QUERY SEQUENCE IN FOLLOWING LOCATIONS FROM LEFT = 0:')
            print(str(sequence.search(argv[3])))

            print('========================================================================================================================')

        if argv[1].lower() == '--makereport' or argv[1] == '-M':

            dna = ''
            with open(argv[2], 'r') as f:
                data = f.read()
                for char in data:
                    if char.upper() in 'ACGTYRWSKMDVHBXN-':
                        dna += char
                f.close()

            sequence = NucleotideSequence(dna, identify='USER')

            r_enzymes = sequence.search_restriction_enzymes()
            count = 0
            for enzyme in r_enzymes:
                if len(enzyme[1]) > 0:
                    count += 1

            o_enzymes = sequence.search_restriction_enzymes(threshhold=1)
            count2 = 0
            for enzyme in o_enzymes:
                if len(enzyme[1]) > 0:
                    count2 += 1

            with open(argv[2][:-4]+'_report.txt', 'w') as f:
                f.write('========================================================================================================================\n')
                f.write('DNA SEQUENCE LENGTH: ' + str(sequence.get_length()) + 'b.p.\n')
                f.write('TOTAL RECOGNIZED RESTRICTION ENZYMES: ' + str(count) + '\n')
                f.write('ONE-CUT RESTRICTION ENZYMES: ' + str(count2) + '\n')
                f.write('========================================================================================================================\n')

                i = 1
                for item in o_enzymes:
                    if len(item[1]) > 0:
                        f.write(str(i+1000)[1:] + ': ' + str(item) + '\n')
                        i += 1

                f.write('========================================================================================================================\n')
                print('========================================================================================================================')
                print('CREATING ' + argv[2][:-4]+'_report.txt: with all possible one-cuts...')
                print(str(count2) + ' restriction enzymes to process...')
                for item in o_enzymes:
                    if len(item[1]) > 0:
                        try:
                            print('========================================================================================================================')
                            print('Processing cut with ' + item[0].name)
                            cuts = sequence.cut(item[0].name)
                            for _ in range(2):
                                f.write('\n')
                        except IndexError:
                            print('Failed...')
                            continue
                        f.write(item[0].name+':\n\n')
                        f.write('LEFT OF CUT: '+str(cuts[0].get_length())+'b.p.'+'\n'+str(cuts[0])+'\n\n')
                        f.write('RIGHT OF CUT: '+str(cuts[1].get_length())+'b.p.'+'\n'+str(cuts[1])+'\n')
                        for _ in range(2):
                            f.write('\n')
                        f.write('========================================================================================================================\n')
                print('========================================================================================================================')
