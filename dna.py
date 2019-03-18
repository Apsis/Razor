"""
NucleotideSequence class and Base Pair Equivilency/Complementary Information
"""

from enzyme import ENZYMES, prepare_enzymes


NUCLEOTIDE_EQUALITIES = {
						 'A': ['A', 'N', 'X', 'R', 'W', 'M', 'D', 'V', 'H'],
				         'C': ['C', 'N', 'X', 'Y', 'S', 'M', 'V', 'H', 'B'],
						 'G': ['G', 'N', 'X', 'R', 'S', 'K', 'D', 'V', 'B'],
						 'T': ['T', 'N', 'X', 'Y', 'W', 'K', 'D', 'H', 'B'],
						 'Y': ['Y', 'N', 'X', 'C', 'T'],
						 'R': ['R', 'N', 'X', 'A', 'G'],
						 'W': ['W', 'N', 'X', 'A', 'T'],
						 'S': ['S', 'N', 'X', 'G', 'C'],
						 'K': ['K', 'N', 'X', 'T', 'G'],
						 'M': ['M', 'N', 'X', 'C', 'A'],
						 'D': ['D', 'N', 'X', 'A', 'G', 'T'],
						 'V': ['V', 'N', 'X', 'A', 'C', 'G'],
						 'H': ['H', 'N', 'X', 'A', 'C', 'T'],
						 'B': ['B', 'N', 'X', 'C', 'G', 'T'],
						 'X': ['X', 'N', 'A', 'C',
						 	   'G', 'T', 'Y', 'R',
							   'W', 'S', 'K', 'M',
							   'D', 'V', 'H', 'B'],
						 'N': ['N', 'X', 'A', 'C',
						 	   'G', 'T', 'Y', 'R',
							   'W', 'S', 'K', 'M',
							   'D', 'V', 'H', 'B'],
						 '-': ['-']
						 }

BASE_COMPLEMENTS = {
					'A': 'T',
				    'C': 'G',
					'G': 'C',
					'T': 'A',
					'Y': 'R',
					'R': 'Y',
					'W': 'W',
					'S': 'S',
					'K': 'M',
					'M': 'K',
					'D': 'H',
					'V': 'B',
					'H': 'D',
					'B': 'V',
					'X': 'X',
					'N': 'N',
					'-': '-'
					}

RESTRICTION_ENZYME_DATA = prepare_enzymes(ENZYMES)


class NucleotideSequence:
    """
	NucleotideSequence Class

	=== ATTRIBUTES ===

	type identify: str
		Sequence identifyer.

	type nucleotides: str
        The sequence of base pairs

    type complement: str
        The complementary sequence to nucleotides
	"""
    def __init__(self, sequence, complement=None, identify=None):
        """
		Initialization of RestrictionEnzyme with provided cut locations

        === Parameters ===

        type self: NucleotideSequence
            The object itself

        type sequence: str | list[str]
            Either a string of nucleotides or a list of bases (as strings)
            (5' to 3')

        type id: str | None
            An identifier for the sequence

        type complement: str
            Complementary sequence to nucleotides provided (auto generated)

        rtype: None
		"""
        self.identify = identify

        self.nucleotides = ''
        if type(sequence) is str:
            for base in sequence:
                if base.upper() in 'ACGTYRWSKMDVHBXN-':
                    self.nucleotides += base.upper()
                else:
                    self.nucleotides += '-'
        elif type(sequence) is list:
            for base in sequence:
                if base.upper() in 'ACGTYRWSKMDVHBXN-':
                    self.nucleotides += base.upper()
                else:
                    self.nucleotides += '-'

        if complement is None:
            self.complement = self.make_complement()
        else:
            self.complement = complement

    def __str__(self):
        """
        Overriding str representation of class

        === Parameters ===

        type self: NucleotideSequence
            The object itself

        rtype: str
        """
        if self.identify == 'LEFT':
            formatted = ""
            if self.get_length() <= 70:
                formatted += "5' > " + self.nucleotides + " > 3'\n"
                formatted += "3' < " + self.complement + " < 5'"
            else:
                formatted += "5' > ..." + self.nucleotides[-70:] + "... > 3'\n"
                formatted += "3' < ..." + self.complement[-70:] + "... < 5'"
        elif self.identify == 'RIGHT':
            formatted = ""
            if self.get_length() <= 70:
                formatted += "5' > " + self.nucleotides + " > 3'\n"
                formatted += "3' < " + self.complement + " < 5'"
            else:
                formatted += "5' > ..." + self.nucleotides[:70] + "... > 3'\n"
                formatted += "3' < ..." + self.complement[:70] + "... < 5'"
        else:
            formatted = ""
            if self.get_length() <= 70:
                formatted += "5' > " + self.nucleotides + " > 3'\n"
                formatted += "3' < " + self.complement + " < 5'"
            else:
                cen = int(self.get_length()/2)
                formatted += "5' > ..." + self.nucleotides[-cen:] + "... > 3'\n"
                formatted += "3' < ..." + self.complement[-cen:] + "... < 5'"

        return formatted

    def __repr__(self):
        """
        Overriding str representation of class

        === Parameters ===

        type self: NucleotideSequence
            The object itself

        rtype: str
        """
        if self.identify == 'LEFT':
            formatted = ""
            if self.get_length() <= 70:
                formatted += "5' > " + self.nucleotides + " > 3'\n"
                formatted += "3' < " + self.complement + " < 5'"
            else:
                formatted += "5' > ..." + self.nucleotides[-70:] + "... > 3'\n"
                formatted += "3' < ..." + self.complement[-70:] + "... < 5'"
        elif self.identify == 'RIGHT':
            formatted = ""
            if self.get_length() <= 70:
                formatted += "5' > " + self.nucleotides + " > 3'\n"
                formatted += "3' < " + self.complement + " < 5'"
            else:
                formatted += "5' > ..." + self.nucleotides[:70] + "... > 3'\n"
                formatted += "3' < ..." + self.complement[:70] + "... < 5'"
        else:
            formatted = ""
            if self.get_length() <= 70:
                formatted += "5' > " + self.nucleotides + " > 3'\n"
                formatted += "3' < " + self.complement + " < 5'"
            else:
                cen = int(self.get_length()/2)
                formatted += "5' > ..." + self.nucleotides[-cen:] + "... > 3'\n"
                formatted += "3' < ..." + self.complement[-cen:] + "... < 5'"

        return formatted

    def make_complement(self):
        """
        Creates the complementary sequence of nucleotides for self.nucleotides

        === Parameters ===

        type self: NucleotideSequence
            The object itself

        rtype: str
        """
        complement = str()
        for base in self.nucleotides:
            complement += BASE_COMPLEMENTS[base]

        return complement

    def get_length(self):
        """
        Returns the length of the nucleotide sequence

        === Parameters ===

        type self: NucleotideSequence
            The object itself

        rtype: int
        """
        return len(self.nucleotides)

    def search(self, query):
        """
        Searches the sequence for a provided subsequence

        === Parameters ===

        type self: NucleotideSequence
            The object itself

        type query: str
            A string such that len(query) < len(nucleotides)

        rtype: list[int]
        """
        query = query.upper()

        invalid = False
        for char in query:
            if char not in 'ACGTYRWSKMDVHBXN-':
                invalid = True
        if invalid:
            print('WARNING: Query contains invalid characters')

        if len(query) > self.get_length():
            return []

        indices = list()
        for i in range(0, self.get_length()-len(query)+1):
            window = self.nucleotides[i:i+len(query)]
            equal = True
            for j in range(len(window)):
                if query[j] not in NUCLEOTIDE_EQUALITIES[window[j]]:
                    equal = False
            if equal:
                indices.append(i)

        return indices

    def search_restriction_enzymes(self, threshhold=None):
        """
        Returns the length of the nucleotide sequence

        === Parameters ===

        type self: NucleotideSequence
            The object itself

        type threshhold: int | None
            Filters for enzymes that only cut <threshhold> times or less
            Setting this value to one will provide all one-cut enzymes

        rtype: list[list[RestrictionEnzyme, int]]
        """
        enzyme_objects = prepare_enzymes(ENZYMES)

        cut_data = list()
        for enzyme in enzyme_objects:
            cuts = self.search(enzyme.sequence)
            if threshhold is not None and len(cuts) <= threshhold:
                cut_data.append([enzyme, cuts])
            elif threshhold is None:
                cut_data.append([enzyme, cuts])

        return cut_data

    def cut(self, enzyme):
        """
        Returns two NucleotideSequence objects in a list containing
        the sides of a one cut from a provided restriction enzyme.
        Cut will only be made if the enzyme is a one cut enzyme (cuts
        in one place). If the enzyme is not a one cut enzyme then the
        function returns [None, None].If the cut site is too close to
        one endge of the sequence it will also return [None, None].

        === Parameters ===

        type self: NucleotideSequence
            The object itself

        type restriction_enzyme: str
            The one cut restriction enzyme of choice

        rtype: list[NucleotideSequence, NucleotideSequence]
        """
        one_cuts = self.search_restriction_enzymes(threshhold=1)

        valid_query = False
        for item in one_cuts:
            if item[0].name == enzyme:
                valid_query = True
                cut_info = item

        if valid_query:
            left_of_cut = cut_info[1][0]
            right_of_cut = self.get_length() - \
             (left_of_cut + len(cut_info[0].sequence))

            if cut_info[0].mid_cut is not None:
                left_strand = self.nucleotides[:cut_info[0].mid_cut \
				                              + cut_info[1][0]]
                right_strand = self.nucleotides[cut_info[0].mid_cut \
				                              + cut_info[1][0]:]
                return [NucleotideSequence(left_strand, identify='LEFT'),
				        NucleotideSequence(right_strand, identify='RIGHT')]
            elif cut_info[0].left_cuts is not None \
             and cut_info[0].right_cuts is not None:
                left_5, left_3 = cut_info[0].left_cuts
                right_3, right_5 = cut_info[0].right_cuts
                if max(left_5, left_3) < left_of_cut \
               and max(right_3, right_5) < right_of_cut:
                    left_top_strand = self.nucleotides[:cut_info[1][0]-left_5]
                    right_top_strand = self.nucleotides[cut_info[1][0] \
                                      + len(cut_info[0].sequence)+right_3:]
                    left_bot_strand = self.complement[:cut_info[1][0]-left_3]
                    right_bot_strand = self.complement[cut_info[1][0] \
									  + len(cut_info[0].sequence)+right_5:]

                    while len(left_top_strand) != len(left_bot_strand):
                        if len(left_top_strand) < len(left_bot_strand):
                            left_top_strand += '-'
                        else:
                            left_bot_strand += '-'

                    while len(right_top_strand) != len(right_bot_strand):
                        if len(right_top_strand) < len(right_bot_strand):
                            right_top_strand = '-' + right_top_strand
                        else:
                            right_bot_strand = '-' + right_bot_strand

                    return [NucleotideSequence(left_top_strand,
                                               complement=left_bot_strand,
                                               identify='LEFT'),
                            NucleotideSequence(right_top_strand,
                                               complement=right_bot_strand,
                                               identify='RIGHT')]
                else:
                    return [None, None]

            elif cut_info[0].right_cuts is not None:
                right_3, right_5 = cut_info[0].right_cuts
                if max(right_3, right_5) < right_of_cut:
                    left_top_strand = self.nucleotides[:cut_info[1][0] \
                                      + len(cut_info[0].sequence)+right_3]
                    right_top_strand = self.nucleotides[cut_info[1][0] \
                                      + len(cut_info[0].sequence)+right_3:]
                    left_bot_strand = self.complement[:cut_info[1][0] \
                                       + len(cut_info[0].sequence)+right_5]
                    right_bot_strand = self.complement[cut_info[1][0] \
                                       + len(cut_info[0].sequence)+right_5:]

                    while len(left_top_strand) != len(left_bot_strand):
                        if len(left_top_strand) < len(left_bot_strand):
                            left_top_strand += '-'
                        else:
                            left_bot_strand += '-'

                    while len(right_top_strand) != len(right_bot_strand):
                        if len(right_top_strand) < len(right_bot_strand):
                            right_top_strand = '-' + right_top_strand
                        else:
                            right_bot_strand = '-' + right_bot_strand

                    return [NucleotideSequence(left_top_strand,
                                               complement=left_bot_strand,
                                               identify='LEFT'),
					        NucleotideSequence(right_top_strand,
                                               complement=right_bot_strand,
                                               identify='RIGHT')]
                else:
                    return [None, None]

        else:
            return [None, None]
