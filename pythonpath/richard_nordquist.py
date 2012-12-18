# The following rules were derived from Richard Nordquist's
# article "200 Common Redundancies"
# http://grammar.about.com/od/words/a/redundancies.htm)

from grammar_rule import GrammarRule

rules = []

# rules.append( GrammarRule(pattern, suggestion, short_comment, full_comment, exceptions) )

rules.append( 
  GrammarRule(
    r"\b(assemble|attach|blend|collaborate|combine|confer|connect|cooper|ate|fuse|gather|integrate|join|meet|merge|mix|share|spliced) together\b",					# pattern
    r"\1",						# suggestion 
    "Redundancy",				# short comment
    "Redundancy",				# full comment 
    {}						# exceptions
  ) 
)
