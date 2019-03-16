"""
RestrictionEnzyme Class and Restriction Enzyme Localization Data
"""


ENZYMES = {
		   'AclI': '﻿AA/CGTT', 'HindIII': 'A/AGCTT', 'SspI': 'AAT/ATT',
		   'MluCI': '/AATT', 'PciI': 'A/CATGT', 'AgeI': 'A/CCGGT',
		   'BfuAI': 'ACCTGC(4/8)', 'SexAI': 'A/CCWGGT', 'MluI': 'A/CGCGT',
		   'BceAI': 'ACGGC(12/14)', 'HpyCH4IV': 'A/CGT', 'HpyCH4III': 'ACN/GT',
		   'BaeI': '(10/15)ACNNNNGTAYC(12/7)',
		   'BsaXI': '(9/12)ACNNNNNCTCC(10/7)', 'AflIII': 'A/CRYGT',
		   'SpeI': 'A/CTAGT', 'BsrI': 'ACTGG(1/-1)', 'BmrI': 'ACTGGG(5/4)',
		   'BglII': 'A/GATCT', 'AfeI': 'AGC/GCT', 'AluI': 'AG/CT',
		   'StuI': 'AGG/CCT', 'ScaI-HF': 'AGT/ACT', 'ClaI': 'AT/CGAT',
		   'PI-SceI': 'ATCTATGTCGGGTGCGGAGAAAGAGGTAAT(-15/-19)',
		   'NsiI': 'ATGCA/T', 'AseI': 'AT/TAAT', 'SwaI': 'ATTT/AAAT',
		   'CspCI': '(11/13)CAANNNNNGTGG(12/10)', 'MfeI': 'C/AATTG',
		   'BssS': 'CACGAG(-5/-1)', 'BmgBI': 'CACGTC(-3/-3)', 'PmlI': 'CAC/GTG',
		   'DraIII-HF': 'CACNNN/GTG', 'AleI-v2': 'CACNN/NNGTG',
		   'EcoP15I': 'CAGCAG(25/27)', 'PvuII': 'CAG/CTG',
		   'AlwNI': 'CAGNNN/CTG', 'BtsIMutI': 'CAGTG(2/0)', 'NdeI': 'CA/TATG',
		   'CviAII': 'C/ATG', 'NlaIII': 'CATG/', 'MslI': 'CAYNN/NNRTG',
		   'FspEI': 'CC(12/16)', 'XcmI': 'CCANNNNN/NNNNTGG',
		   'BstXI': 'CCANNNNN/NTGG', 'PflMI': 'CCANNNN/NTGG',
		   'BccI': 'CCATC(4/5)', 'NcoI': 'C/CATGG',
		   'BseYI': 'CCCAGC(-5/-1)', 'FauI': 'CCCGC(4/6)', 'SmaI': 'CCC/GGG',
		   'TspMI': 'C/CCGGG', 'Nt.CviPII': '(0/-1)CCD', 'LpnPI': 'CCDG(10/14)',
		   'AciI': 'CCGC(-3/-1)', 'SacII': 'CCGC/GG', 'BsrBI': 'CCGCTC(-3/-3)',
		   'MspI': 'C/CGG', 'ScrFI': 'CC/NGG', 'StyD4I': '/CCNGG',
		   'BsaJI': 'C/CNNGG', 'BslI': 'CCNNNNN/NNGG', 'BtgI': 'C/CRYGG',
		   'NciI': 'CC/SGG', 'AvrII': 'C/CTAGG', 'MnlI': 'CCTC(7/6)',
		   'Nt.BbvCI': 'CCTCAGC(-5/-7)', 'BbvCI': 'CCTCAGC(-5/-2)',
		   'SbfI': 'CCTGCA/GG', 'Bpu10I': 'CCTNAGC(-5/-2)',
		   'Bsu36I': 'CC/TNAGG', 'EcoNI': 'CCTNN/NNNAGG', 'HpyAV': 'CCTTC(6/5)',
		   'PspGI': '/CCWGG', 'BstNI': 'CC/WGG', 'StyI': 'C/CWWGG',
		   'BcgI': '(10/12)CGANNNNNNTGC(12/10)', 'PvuI': 'CGAT/CG',
		   'BstUI': 'CG/CG', 'EagI': 'C/GGCCG', 'RsrII': 'CG/GWCCG',
		   'BsiEI': 'CGRY/CG', 'BsiWI': 'C/GTACG', 'Esp3I': 'CGTCTC(1/5)',
		   'Hpy99I': 'CGWCG/', 'MspA1I': 'CMG/CKG',
		   'AbaSI': 'CNNNNNNNNNNN/NNNNNNNNNG', 'MspJI': 'CNNR(9/13)',
		   'SgrAI': 'CR/CCGGYG', 'BfaI': 'C/TAG', 'BspCNI': 'CTCAG(9/7)',
		   'PaeR7I': 'C/TCGAG', 'EarI': 'CTCTTC(1/4)', 'AcuI': 'CTGAAG(16/14)',
		   'PstI': 'CTGCA/G', 'BpmI': 'CTGGAG(16/14)', 'DdeI': 'C/TNAG',
		   'SfcI': 'C/TRYAG', 'AflII': 'C/TTAAG', 'BpuEI': 'CTTGAG(16/14)',
		   'SmlI': 'C/TYRAG', 'BsoBI': 'C/YCGRG', 'MboII': 'GAAGA(8/7)',
		   'BbsI': 'GAAGAC(2/6)', 'XmnI': 'GAANN/NNTTC',
		   'BsmI': 'GAATGC(1/-1)', 'EcoRI': 'G/AATTC',
		   'HgaI': 'GACGC(5/10)', 'AatII': 'GACGT/C', 'ZraI': 'GAC/GTC',
		   'PflFI': 'GACN/NNGTC', 'PshAI': 'GACNN/NNGTC',
		   'AhdI': 'GACNNN/NNGTC', 'DrdI': 'GACNNNN/NNGTC', 'SacI': 'GAGCT/C',
		   'Eco53kI': 'GAG/CTC', 'BseRI': 'GAGGAG(10/8)',
		   'Nt.BstNBI': 'GAGTC(4/-5)', 'PleI': 'GAGTC(4/5)',
		   'MlyI': 'GAGTC(5/5)', 'HinfI': 'G/ANTC', 'EcoRV': 'GAT/ATC',
		   'DpnI': 'GA/TC', 'MboI': '/GATC', 'BsaBI': 'GATNN/NNATC',
		   'TfiI': 'G/AWTC', 'BsrDI': 'GCAATG(2/0)', 'BbvI': 'GCAGC(8/12)',
		   'BtsαI': 'GCAGTG(2/0)', 'BstAPI': 'GCANNNN/NTGC',
		   'SfaNI': 'GCATC(5/9)', 'SphI': 'GCATG/C',
		   'SrfI': 'GCCC/GGGC', 'NmeAIII': 'GCCGAG(21/19)', 'NgoMIV': 'G/CCGGC',
		   'NaeI': 'GCC/GGC', 'BglI': 'GCCNNNN/NGGC', 'AsiSI': 'GCGAT/CGC',
		   'BtgZI': 'GCGATG(10/14)', 'HinP1I': 'G/CGC', 'HhaI': 'GCG/C',
		   'BssHII': 'G/CGCGC', 'NotI': 'GC/GGCCGC', 'Fnu4HI': 'GC/NGC',
		   'Cac8I': 'GCN/NGC', 'MwoI': 'GCNNNNN/NNGC', 'NheI': 'G/CTAGC',
		   'BmtI': 'GCTAG/C', 'Nt.BspQI': 'GCTCTTC(1/-7)',
		   'SapI': 'GCTCTTC(1/4)', 'BlpI': 'GC/TNAGC', 'ApeKI': 'G/CWGC',
		   'Bsp1286I': 'GDGCH/C', 'AlwI': 'GGATC(4/5)',
		   'Nt.AlwI': 'GGATC(4/-5)', 'BamHI': 'G/GATCC', 'BtsCI': 'GGATG(2/0)',
		   'FokI': 'GGATG(9/13)', 'HaeIII': 'GG/CC', 'FseI': 'GGCCGG/CC',
		   'SfiI': 'GGCCNNNN/NGGCC', 'SfoI': 'GGC/GCC', 'KasI': 'G/GCGCC',
		   'NarI': 'GG/CGCC', 'PluTI': 'GGCGC/C', 'AscI': 'GG/CGCGCC',
		   'EciI': 'GGCGGA(11/9)', 'BsmFI': 'GGGAC(10/14)', 'ApaI': 'GGGCC/C',
		   'PspOMI': 'G/GGCCC', 'Sau96I': 'G/GNCC', 'NlaIV': 'GGN/NCC',
		   'Acc65I': 'G/GTACC', 'KpnI': 'GGTAC/C', 'BsaI': 'GGTCTC(1/5)',
		   'HphI': 'GGTGA(8/7)', 'BstEII': 'G/GTNACC', 'AvaII': 'G/GWCC',
		   'BanI': 'G/GYRCC', 'BaeGI': 'GKGCM/C', 'BsaHI': 'GR/CGYC',
		   'BanII': 'GRGCY/C', 'RsaI': 'GT/AC', 'CviQI': 'G/TAC',
		   'BstZ17I': 'GTATAC', 'BciVI': 'GTATCC(6/5)', 'SalI': 'G/TCGAC',
		   'BsmAI': 'GTCTC(1/5)', 'Nt.BsmAI': 'GTCTC(1/-5)', 'ApaLI': 'G/TGCAC',
		   'BsgI': 'GTGCAG(16/14)', 'AccI': 'GT/MKAC', 'Hpy166II': 'GTN/NAC',
		   'Tsp45I': '/GTSAC', 'HpaI': 'GTT/AAC', 'PmeI': 'GTTT/AAAC',
		   'HincII': 'GTY/RAC', 'BsiHKAI': 'GWGCW/C', 'TspRI': 'NNCASTGNN/',
		   'ApoI': 'R/AATTY', 'NspI': 'RCATG/Y', 'BsrFαI': 'R/CCGGY',
		   'BstYI': 'R/GATCY', 'HaeII': 'RGCGC/Y', 'CviKI-1': 'RG/CY',
		   'EcoO109I': 'RG/GNCCY', 'PpuMI': 'RG/GWCCY',
		   'I-CeuI': 'TAACTATAACGGTCCTAAGGTAGCGAA(-9/-13)', 'SnaBI': 'TAC/GTA',
		   'I-SceI': 'TAGGGATAACAGGGTAAT(-9/-13)', 'BspHI': 'T/CATGA',
		   'BspEI': 'T/CCGGA', 'MmeI': 'TCCRAC(20/18)', 'TaqαI': 'T/CGA',
		   'NruI': 'TCG/CGA', 'Hpy188I': 'TCN/GA', 'Hpy188III': 'TC/NNGA',
		   'XbaI': 'T/CTAGA', 'BclI': 'T/GATCA', 'HpyCH4V': 'TG/CA',
		   'PI-PspI': 'TGGCAAACAGCTATTATGGGTATTATGGGT(-13/-17)',
		   'MscI': 'TGG/CCA', 'BsrGI': 'T/GTACA', 'MseI': 'T/TAA',
		   'PacI': 'TTAAT/TAA', 'PsiI': 'TTA/TAA', 'BstBI': 'TT/CGAA',
		   'DraI': 'TTT/AAA', 'PspXI': 'VC/TCGAGB', 'BsaWI': 'W/CCGGW',
		   'BsaAI': 'YAC/GTR', 'EaeI': 'Y/GGCCR', 'FspI': 'TGC/GCA'
		   }


class RestrictionEnzyme:
	"""
	RestrictionEnzyme Class

	=== ATTRIBUTES ===

	type name: str
		Name of the restriction enzyme

	type sequence: str
		The restriction enzyme localization sequence stripped of other data

	type left_cuts: (int, int) | None
		5'/3' cut locations on left side of target sequence

	type right_cuts: (int, int) | None
		5'/3' cut locations on right side of target sequence

	type mid_cut: int | None
		Single cut index (left and right cuts shoud be None)
	"""
	def __init__(self, name, sequence, left_cuts, right_cuts, mid_cut):
		"""
		Initialization of RestrictionEnzyme with provided cut locations

		=== Parameters ===

		type self: RestrictionEnzyme
			The object itself

		type name: str
			Name of the enzyme

		type sequence: str
			The nucleotide sequence without the cut information

		type left_cuts: (int, int) | None
			Left cut indeces

		type right_cuts: (int, int) | None
			Right cut indeces

		type mid_cut: int | None
			Mid cut index

		rtype: None
		"""
		self.name = name
		self.sequence = sequence
		self.left_cuts = left_cuts
		self.right_cuts = right_cuts
		self.mid_cut = mid_cut

	def __str__(self):
		'''
		Overriding str representation of class

        === Parameters ===

        type self: RestrictionEnzyme
            The object itself

        rtype: str
		'''
		return str(['NAME: ' + self.name,
					'SEQUENCE: ' + self.sequence,
					'LEFT CUTS: ' + str(self.left_cuts),
					'RIGHT CUTS: ' + str(self.right_cuts),
					'MID CUT: ' + str(self.mid_cut)])

	def __repr__(self):
		'''
		Overriding str representation of class

        === Parameters ===

        type self: RestrictionEnzyme
            The object itself

        rtype: str
		'''
		return str(['NAME: ' + self.name,
					'SEQUENCE: ' + self.sequence,
					'LEFT CUTS: ' + str(self.left_cuts),
					'RIGHT CUTS: ' + str(self.right_cuts),
					'MID CUT: ' + str(self.mid_cut)])


def prepare_enzymes(enzyme_dictionary):
	'''
	Prepare enzymes from dictionary into list of RestrictionEnzyme objects

	=== Parameters ===

	type enzyme_dictionary: dict
		Takes in the ENZYMES dictionary of enzyme informtation

	rtype: list[RestrictionEnzyme]
	'''
	enzyme_list = list()
	for key in enzyme_dictionary:
		if key[:2].upper() != 'NT' and key[:2].upper() != 'NB':
			has_left = False
			has_right = False
			safety_edit = enzyme_dictionary[key]
			data = ''
			sequence = ''
			for char in safety_edit:
				if char in 'ACGTYRWSKMDVHBXN0123456789-()/':
					data += char
				if char in 'ACGTYRWSKMDVHBXN':
					sequence += char
			if data[0] == '(':
				has_left = True
				left = data[data.find('(')+1:data.find(')')].split('/')
				left_cuts = (int(left[0]), int(left[1]))
			else:
				left_cuts = None
			if data[-1] == ')':
				has_right = True
				if has_left:
					right = data.split('(')[2][:-1].split('/')
				else:
					right = data.split('(')[1][:-1].split('/')
				right_cuts = (int(right[0]), int(right[1]))
			else:
				right_cuts = None
			if has_left or has_right:
				mid_cut = None
			else:
				mid_cut = len(data.split('/')[0])
			enzyme_list.append(RestrictionEnzyme(key, sequence, left_cuts,
												 right_cuts, mid_cut))

	return enzyme_list
