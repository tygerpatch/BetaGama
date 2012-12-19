# The following rules were derived from Richard Nordquist's
# article "200 Common Redundancies"
# http://grammar.about.com/od/words/a/redundancies.htm)

from grammar_rule import GrammarRule

rules = []

# rules.append( GrammarRule(pattern, suggestion, short_comment, full_comment, exceptions) )

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





