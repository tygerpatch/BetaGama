# The following rules were derived from Graviax
# created by Matthew J. Strawbridge 2005, GNU Less General Public License
# https://sourceforge.net/projects/graviax/

from grammar_rule import GrammarRule

rules = []

# rules.append( GrammarRule(pattern, suggestion, short_comment, full_comment, exceptions) )

# *** en-GB-cliches.xml

rules.append( 
  GrammarRule(
    r"\bleave no stone unturned\b",	# pattern 
    "",  				# suggestion 
    "Cliche",				# short comment
    "You should avoid using cliches",	# full comment 
    {}					# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\blike a bull in a china shop\b",	# pattern
    "", 				# suggestion 
    "Cliche", 				# short comment
    "You should avoid using cliches", 	# full comment 
    {}					# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bis no exception\b",		# pattern
    "", 				# suggestion 
    "Cliche", 				# short comment
    "You should avoid using cliches",	# full comment 
    {}					# exceptions
  ) 
)

# *** en-badstyle.xml

# Stressed 'And' before 'Therefore'
rules.append( 
  GrammarRule(
    r"\band(,|, | ,| , )therefore(,| ,|)",					# pattern
    "and therefore",								# suggestion 
    "Bad Style",								# short comment
    "The comma emphasizes the 'and.'  Therefore, it should be removed.",	# full comment 
    {}										# exceptions
  )
)

# Double negatives
rules.append( 
  GrammarRule(
    r"\b(are|is|has|was|do|does|wo|would|could|should|have)n't not\b",	# pattern
    r"\1",								# suggestion 
    "Double Negative",							# short comment
    "Double Negative",							# full comment 
    {}									# exceptions
  )
)

# Vowels

exceptions = {1 :  ("unifiable", "unified", "uniformed", "unifying", "united", "undulated", "universalised", "universalized")} 

rules.append( 
  GrammarRule(
    r"\bnot (un(([aeiou][a-z]{2})[a-z]*([ai]ble|ed|ing)))\b",	# pattern
    r"\2",							# suggestion 
    "Bad Style",						# short comment
    "Double negative",						# full comment 
    exceptions							# exceptions
  )
) 

rules.append( 
  GrammarRule(
    r"\bnot an (un(([aeiou][a-z]{2})[a-z]*([ai]ble|ed|ing)))\b",	# pattern
    r"an \2",								# suggestion 
    "Double Negative",							# short comment
    "Double Negative",							# full comment 
    exceptions								# exceptions
  )
)

# Consonants

exceptions = {3 : ("der")}

rules.append( 
  GrammarRule(
    r"\bnot (un(([^aeiou][a-z]{2})[a-z]*([ai]ble|ed|ing)))\b",	# pattern
    r"\2",							# suggestion 
    "Bad Style",						# short comment
    "Double negative",						# full comment 
    exceptions							# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\bnot an (un(([^aeiou][a-z]{2})[a-z]*([ai]ble|ed|ing)))\b",	# pattern
    r"a \2",								# suggestion 
    "Double Negative",							# short comment
    "Double Negative",							# full comment 
    exceptions								# exceptions
  )
)

# Have to have
srules.append( 
  GrammarRule(
    r"\bhave to have\b",					# pattern
    "must have",						# suggestion 
    "Bad Style",						# short comment
    "The phrase 'must have' is clearer than 'have to have'.",	# full comment 
    {}								# exceptions
  ) 
)

# Comparing absolutes

rules.append( 
  GrammarRule(
    r"\b(a little( bit)?|almost|astonishingly|completely|exceedingly|extremely|highly|incredibly|more than|nearly|partly|partially|quite|somewhat|totally|unbelievably|very) (dead|disappeared|empty|false|full|gone|illegal|infinite|invaluable|legal|perfect|pervasive|pregnant|professional|true|whole|vanished|(omni[a-z]+))\b",	# pattern
    r"\3",								# suggestion 
    "Bad Style", 							# short comment
    r"'\3' is an absolute.  Something is either '\3' or it is not.",	# full comment 
    {}									# exceptions
  )
)  

# Like -> As if

rules.append( 
  GrammarRule(
    r"\blike it was yesterday\b", 					# pattern
    "as if it were yesterday", 						# suggestion 
    "Bad Style", 							# short comment
    "The correct phrase for reminiscing is 'as if it were yesterday'.",	# full comment 
    {}									# exceptions
  )
)

# *** en-GB-homophones.xml

rules.append( 
  GrammarRule(
    r"\blets (have|go|try|think|do|be|get|make)\b",	# pattern
    r" let's \1",					# suggestion 
    "Homophone", 					# short comment
    "Lets means allows or hires.  Let's means let us.",	# full comment 
    {}							# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\blet's (me|you|him|her|us|them|it)\b",		# pattern
    r"lets \1",						# suggestion 
    "Homophone",					# short comment
    "Lets means allows or hires.  Let's means let us.",	# full comment 
    {}							# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\bcause and affect\b",							# pattern
    "cause and effect",								# suggestion 
    "Homophone",								# short comment
    "A cause has an 'effect'.  You 'affect' something if you change it.",	# full comment 
    {}										# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\b(an|into|the|no|take|with) ((immediate|initial|eventual|overall|total) )?affect(s?)\b",	# pattern
    r"\1 \2effect\4", 										# suggestion 
    "Homophone", 										# short comment
    "Affect and effect have both noun and verb forms.  Most commonly you need the verb affect (influence) or the noun effect (result). The noun affect means mental or emotional state.  The verb affect means to bring about, as in effect change.",	# full comment 
    {}												# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\b(a|the|business|good|bad|best) practise([ds]|)\b",	# pattern
    r"\1 practice\2",						# suggestion 
    "Homophone",						# short comment
    "Practice is a noun; practise is a verb.", 			# full comment 
    {}								# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\b(I|she|he|we|they|you) practice([ds]|)\b",	# pattern
    r"\1 practise\2",					# suggestion 
    "Homophone", 					# short comment
    "Practice is a noun; practise is a verb.",		# full comment 
    {}							# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\bits not\b", 							# pattern
    "it's not", 							# suggestion 
    "Homophone",							# short comment
    "It's means 'it is or it has.'  Its means belonging to it.",	# full comment 
    {}									# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\b(about|around|at|by|for|from|in|near|of|on|over|through|to|towards|under|with|without) it's\b",	# pattern
    r"\1 its", 												# suggestion 
    "Homophone", 											# short comment
    "It's means 'it is or it has.'  Its means belonging to it.", 					# full comment 
    {}													# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\byour not\b", 						# pattern
    "you're not", 						# suggestion 
    "Homophone", 						# short comment
    "You're means you are.  Your means belonging to you.",	# full comment 
    {}								# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\b(about|around|at|by|for|from|in|near|of|on|over|through|to|towards|under|with|without) (you)'(r)e\b",	# pattern
    r"\1 \2\3", 												# suggestion 
    "Homophone", 												# short comment
    "You're means 'you are'.  Your means belonging to you.",							# full comment 
    {}														# exceptions
  )
)

exceptions = {1:("an", "in", "for", "the", "to")}

rules.append( 
  GrammarRule(
    r"\b([^ ]+) everyday\b", 				# pattern
    r"\1 every day", 					# suggestion 
    "Homophone",					# short comment
    "Everday means common.  Every day means daily.",	# full comment 
    exceptions						# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\btheir (is|are)\b", 					# pattern
    r"there \1", 						# suggestion 
    "Homophone", 						# short comment
    "There is a place.  Their means belonging to them.",	# full comment 
    {}								# exceptions
  )
)

exceptions = {1 : ("I", "you", "he", "she", "it", "they", "we")}

rules.append( 
  GrammarRule(
    r"\bthere ([^ ]+) (is|are|has|have|will|must)\b",		# pattern
    r"their \1 \2", 						# suggestion 
    "Homophone", 						# short comment
    "There is a place.  Their means belonging to them.",	# full comment 
    exceptions							# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\b(to|will|would) loose\b", 			# pattern
    r"\1 lose", 					# suggestion 
    "Homophone",					# short comment
    "Loose means not tight.  Lose means to not win.",	# full comment 
    {}							# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\b(for|in|takes?) awhile\b", 			# pattern
    r"\1 a while", 					# suggestion 
    "Homophone",					# short comment
    "Awhile is an adverb and a while is a noun.",	# full comment 
    {}							# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\bfaint ruled\b",				# pattern
    "feint ruled",				# suggestion 
    "Homophone",				# short comment
    "Paper is feint ruled not faint ruled.",	# full comment 
    {}						# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\bbefore hand\b([^-])",	# pattern
    r"beforehand\1",		# suggestion 
    "Homophone",		# short comment
    "Beforehand is one word.",	# full comment 
    {}				# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\bend-product(s?)\b",		# pattern
    r"end product\1",			# suggestion 
    "Homophone",			# short comment
    "End product is not hyphenated.",	# full comment 
    {}					# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\beveryone of\b",						# pattern
    "every one of",						# suggestion 
    "Homophone",						# short comment
    "Everyone is a pronoun (you couldn't say everybody of).",	# full comment 
    {}								# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\ban other\b",			# pattern
    "another",				# suggestion 
    "Homophone",			# short comment
    "Another is a single word.",	# full comment 
    {}					# exceptions
  )
)

# *** en-punctuation.xml

rules.append( 
  GrammarRule(
    ":[-]+",				# pattern
    ":",				# suggestion 
    "Punctuation",			# short comment
    "A colon does not need a dash.",	# full comment 
    {}					# exceptions
  )
)
    
rules.append( 
  GrammarRule(
    "\bold fashioned\b", 		# pattern
    "old-fashioned", 			# suggestion 
    "Punctuation",			# short comment
    "Old-fashioned takes a hyphen.",	# full comment 
    {}					# exceptions
  )
)

rules.append( 
  GrammarRule(
    "\bthe ((1\d)?\d\d)[']s\b", 		# pattern
    r"the \1s", 				# suggestion 
    "Punctuation",				# short comment
    "Plurals do not take an aprostrophe",	# full comment 
    {}						# exceptions
  )
)

# *** en-misc.xml

rules.append( 
  GrammarRule(
    r"\b([a-z]+) \1\b",	# pattern
    r"\1",		# suggestion 
    "Repeated Word",	# short comment
    "Repeated word",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bdifferent(ly|) (([^ ]+ ){0,5})than\b", 		# pattern
    r"different\1 \2from",				# suggestion 
    "Misc.", 						# short comment
    "The phrase 'different than' is never correct.",	# full comment 
    {}							# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\b(man|woman|girl|boy|people) (that|which)\b",		# pattern
    r"\1 who", 							# suggestion 
    "Misc.", 							# short comment
    r"Use 'who' instead of '\2' when talking about people",	# full comment 
    {}								# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bif (I|he|she|it) was\b", 						# pattern
    r"if \1 were", 								# suggestion 
    "Misc.", 									# short comment
    "You should use 'were' instead of 'was' for hypothetical situations.",	# full comment 
    {}										# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bif only (I|he|she|it) was\b", 						# pattern
    r"if only \1 were", 							# suggestion 
    "Misc.", 									# short comment
    "You should use 'were' instead of 'was' for hypothetical situations.",	# full comment 
    {}										# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bwish(e[ds]|) (that |)(I|he|she|it) was\b", 				# pattern
    r"wish\1 \2\3 were", 							# suggestion 
    "Misc.",									# short comment
    "You should use 'were' instead of 'was' for hypothetical situations.",	# full comment 
    {}										# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bis comprised of\b",						# pattern
    "comprises",							# suggestion 
    "Misc.", 								# short comment
    "The 'whole comprises the parts', not the other way around.",	# full comment 
    {}									# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\b(((centi|milli|kilo)?meters?)|inch|inches|foot|feet|yards?|miles?) squared?\b",	# pattern
    r"square \1", 									# suggestion 
    "Misc.", 										# short comment
    r"The units are square \1. If you mean a square, each side of which is this specific length, it would be a good idea to reword to remove the ambiguity.",	# full comment 
    {}											# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\b(((centi|milli|kilo)?meters?)|inch|inches|foot|feet|yards?|miles?) cubed?\b",	# pattern
    r"cubic \1", 									# suggestion 
    "Misc.", 										# short comment
    r"The units are cubic \1. If you mean a cube, each side of which is this specific length, it would be a good idea to reword to remove the ambiguity.",	# full comment 
    {}											# exceptions
  )
)

# *** rules.xml

rules.append( 
  GrammarRule(
    r"\bcome on-?board\b",				# pattern
    "come on board",					# suggestion 
    "Homophone",					# short comment
    "On-board is an adjective meaning on the board.",	# full comment 
    {}							# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\bonboard\b",									# pattern
    "on-board", 									# suggestion 
    "Homophone",									# short comment
    "On-board is an adjective meaning on the board.  Onboard is the US spelling.",	# full comment 
    {}											# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\bpasser(s |)( |)by\b", 				# pattern
    r"passer\1-by", 					# suggestion 
    "",							# short comment
    r"In British english, the term is passer\1-by.",	# full comment 
    {}							# exceptions
  )
)

rules.append( 
  GrammarRule(
    "([.!?]['])\.", 										# pattern
    r"\1", 											# suggestion 
    "Punctuation",										# short comment
    "You do not need a closing full stop if the quoted material ends with punctuation.",	# full comment 
    {}												# exceptions
  )
)
