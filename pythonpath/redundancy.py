from grammar_rule import GrammarRule

rules = []

# rules.append( GrammarRule(pattern, suggestion, short_comment, full_comment, exceptions) )

# The following rules were derived from Graviax
# created by Matthew J. Strawbridge 2005, GNU Less General Public License
# https://sourceforge.net/projects/graviax/

# en-redundancies.xml

rules.append( 
  GrammarRule(
    r"\b(return(ed|ing|s)?) back\b",	# pattern
    r"\1",				# suggestion 
    "Redundant",			# short comment
    "The 'back' is implied by the use of 'return'.  Therefore it is redundant.",	# full comment 
    {}					# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\bhonest truth\b",	# pattern
    "truth",			# suggestion 
    "Redundant",		# short comment
    "All 'truth' is 'honest'.",	# full comment 
    {}				# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\btrue fact(s|)\b",	# pattern
    r"fact\1",			# suggestion 
    "Redundant",		# short comment
    "All 'facts' are 'true'.",	# full comment 
    {}				# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\b(dis|)agree with the fact that\b",			# pattern
    r"\1agree that",						# suggestion 
    "Redundant",						# short comment
    "If it's a 'fact' then it is not open to interpretation.",	# full comment 
    {}								# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\bfrom whence\b", 											# pattern
    "whence", 													# suggestion 
    "Redundant",												# short comment
    "The word 'whence' means from what place, source origin or cause.  Therefore 'from whence' is redundant.",	# full comment 
    {}														# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\b(start(ed|ing)?) first (by|in|with)\b", # pattern
    r"\1 \3", 					# suggestion 
    "Redundant",				# short comment
    r"The phrase '\1 first' is redundant.",	# full comment 
    {}						# exceptions
  )
)
  
rules.append( 
  GrammarRule(
    r"\bfirst (be |)(start(ed|ing|))(by|in|with|)\b",	# pattern
    r"\1\2 \4",						# suggestion 
    "Redundant",					# short comment
    r"The phrase 'first \1\2' is redundant.",		# full comment 
    {}							# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\b(repeat(ed|ing|s|))( it|) again\b",		# pattern
    r"\1\3",						# suggestion 
    "Redundant",					# short comment
    r"The word 'again' is redundant with '\1'.",	# full comment 
    {}							# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\balready has been\b", 				# pattern
    "has been", 					# suggestion 
    "Redundant",					# short comment
    "The word 'already' is redundant with 'has been'.",	# full comment 
    {}							# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\bconsensus of opinion\b", 			# pattern
    "consensus", 					# suggestion 
    "Redundant",					# short comment
    "A 'consensus' is, by definition, of 'opinion'.",	# full comment 
    {}							# exceptions
  )
)
  
rules.append( 
  GrammarRule(
    r"\b(join(ed|ing)?) together\b",			# pattern
    r"\1",						# suggestion 
    "Redundant",					# short comment
    "To 'join' things is to bring them 'together'.",	# full comment 
    {}							# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\bmight (perhaps|possibly)\b", 						# pattern
    "might", 									# suggestion 
    "Redundant",								# short comment
    r"The word 'might' already expresses doubt. Therefore '\1' is redundant.",	# full comment 
    {}										# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\bmust (definitely|inevitably|necessarily)\b", 				# pattern
    "must", 									# suggestion 
    "Redundant",								# short comment
    r"The word 'must' already expresses inevitability, so '\1' is redundant.",	# full comment 
    {}										# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\b(previous|prior) (experiences?)\b",					# pattern
    r"\2", 									# suggestion 
    "Redundant",								# short comment
    r"All experiences must have happened in the past, so '\1' is redundant.",	# full comment 
    {}										# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\bwill(,|, | ,| , | )in the future(,| ,|)\b", 						# pattern
    "will", 											# suggestion 
    "Redundant",										# short comment
    "If something 'will' happen, then it must be 'in the future' rather than the past.",	# full comment 
    {}												# exceptions
  )
)

rules.append( 
  GrammarRule(
    r"\bwork colleague\b",			# pattern
    "colleague",				# suggestion 
    "Redundant",				# short comment
    "'work' is already implied by 'colleague'",	# full comment 
    {}						# exceptions
  )
)

# The following rules were derived from Richard Nordquist's
# article "200 Common Redundancies"
# http://grammar.about.com/od/words/a/redundancies.htm)

rules.append( 
  GrammarRule(
    r"\b(assemble|attach|blend|collaborate|combine|confer|connect|cooper|ate|fuse|gather|integrate|join|meet|merge|mix|share|spliced) together\b",	# pattern
    r"\1",					# suggestion 
    "Redundancy",				# short comment
    "Redundancy",				# full comment 
    {}						# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bcompletely (annihilate|destroyed|eliminate|engulfed|filled|surround)\b",	# pattern
    r"\1",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\badvance (planning|preview|reservations|warning)\b",	# pattern
    r"\1",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\babsolutely (essential|necessary)\b",	# pattern
    r"\1",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bunexpected (emergency|surprise)\b",	# pattern
    r"\1",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bstill (persists|remains)\b",	# pattern
    r"\1",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bbasic (fundamentals|necessities)\b",	# pattern
    r"\1",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bbrief (moment|summary)\b",	# pattern
    r"\1",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\b(drop|descend|dwindle|fall|kneel|plunge|shut|write) down\b",	# pattern
    r"\1",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\b(add|ascend|connect|heat|hoist|hurry|lift|open|raise|rise) up\b",	# pattern
    r"\1",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\b(circle|circulate) around\b",	# pattern
    r"\1",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bfinal (conclusion|end|outcome|ultimatum)\b",	# pattern
    r"\1",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bformer (graduate|veteran)\b",	# pattern
    r"\1",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\b(cancel|empty|start) out\b",	# pattern
    r"\1",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bfellow (classmates|colleague)\b",	# pattern
    r"\1",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bpast (experience|history|memories|records)\b",	# pattern
    r"\1",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bsafe (haven|sanctuary)\b",	# pattern
    r"\1",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bfuture (plans|recurrence)\b",	# pattern
    r"\1",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bfrozen (ice|tundra)\b",	# pattern
    r"\1",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bempty (hole|space)\b",	# pattern
    r"\1",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bnew (beginning|construction|innovation|invention|recruit)\b",	# pattern
    r"\1",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bmajor (breakthrough|feat)\b",	# pattern
    r"\1",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bold (adage|cliche|custom|proverb)\b",	# pattern
    r"\1",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\b(reply|retreat|revert|extradite|refer|reflect) back\b",	# pattern
    r"\1",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bpersonal (friend|opinion)\b",	# pattern
    r"\1",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\b(later|present) time\b",	# pattern
    r"\1",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bsoft (in texture|to the touch)\b",	# pattern
    "soft",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\b(filled|full) to capacity\b",	# pattern
    r"\1",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bautobiography of (his|her) own life\b",		# pattern
    r"autobiography",					# suggestion 
    "Redundancy",					# short comment
    "Redundancy",					# full comment 
    {}							# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bbiography of (his|her) life\b",	# pattern
    r"biography",			# suggestion 
    "Redundancy",			# short comment
    "Redundancy",			# full comment 
    {}					# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bweather (conditions|situation)\b",	# pattern
    "weather",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\btall in (height|stature)\b",	# pattern
    "tall",		# suggestion 
    "Redundancy",	# short comment
    "Redundancy",	# full comment 
    {}			# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bintroduced (a new|for the first time)\b",	# pattern
    "introduced",					# suggestion 
    "Redundancy",					# short comment
    "Redundancy",					# full comment 
    {}							# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\b(may|could) possibly\b",	# pattern
    r"\1",				# suggestion 
    "Redundancy",			# short comment
    "Redundancy",			# full comment 
    {}					# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bplan (ahead|in advance)\b",	# pattern
    "plan",				# suggestion 
    "Redundancy",			# short comment
    "Redundancy",			# full comment 
    {}					# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bpreboard as an airplane\b",		# pattern
    "board",					# suggestion 
    "Redundancy",				# short comment
    "Redundancy",				# full comment 
    {}						# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\bpre(heat|record)\b",	# pattern
    r"\1",			# suggestion 
    "Redundancy",		# short comment
    "Redundancy",		# full comment 
    {}				# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\breason (is |)(because|why)\b",	# pattern
    r"reason \1",					# suggestion 
    "Redundancy",					# short comment
    "Redundancy",					# full comment 
    {}							# exceptions
  ) 
)

rules.append( 
  GrammarRule(
    r"\b(ISBN|PIN) number\b",	# pattern
    r"\1",					# suggestion 
    "Redundancy",					# short comment
    "Redundancy",					# full comment 
    {}							# exceptions
  ) 
)
