from grammar_rule import GrammarRule

rules = []

def addRule(
  pattern = "",
  suggestion = "",
  short_comment = "",
  full_comment = "",
  exceptions = {}):

  global rules

  rules.append(
    GrammarRule(pattern, suggestion, short_comment, full_comment, exceptions)
  )

# rules.append( GrammarRule(pattern, suggestion, short_comment, full_comment, exceptions) )

# The following rules were derived from Graviax
# created by Matthew J. Strawbridge 2005, GNU Less General Public License
# https://sourceforge.net/projects/graviax/

# en-redundancies.xml

addRule(
  pattern = r"\b(return(ed|ing|s)?) back\b",
  suggestion = r"\1",
  short_comment = "Redundant",
  full_comment = "The 'back' is implied by the use of 'return'.  Therefore it is redundant.")

addRule(
  pattern = r"\bhonest truth\b",
  suggestion = "truth",
  short_comment = "Redundant",
  full_comment = "All 'truth' is 'honest'.")

addRule(
  pattern = r"\btrue fact(s|)\b",
  suggestion = r"fact\1",
  short_comment = "Redundant",
  full_comment = "All 'facts' are 'true'.")

addRule(
  pattern = r"\b(dis|)agree with the fact that\b",
  suggestion = r"\1agree that",
  short_comment = "Redundant",
  full_comment = "If it's a 'fact' then it is not open to interpretation.")

addRule(
  pattern = r"\bfrom whence\b",
  suggestion = "whence",
  short_comment = "Redundant",
  full_comment = "The word 'whence' means from what place, source origin or cause.  Therefore 'from whence' is redundant.")

addRule(
  pattern = r"\b(start(ed|ing)?) first (by|in|with)\b",
  suggestion = r"\1 \3",
  short_comment = "Redundant",
  full_comment = r"The phrase '\1 first' is redundant.")

addRule(
  pattern = r"\bfirst (be |)(start(ed|ing|))(by|in|with|)\b",
  suggestion = r"\1\2 \4",
  short_comment = "Redundant",
  full_comment = r"The phrase 'first \1\2' is redundant.")

addRule(
  pattern = r"\b(repeat(ed|ing|s|))( it|) again\b",
  suggestion = r"\1\3",
  short_comment = "Redundant",
  full_comment = r"The word 'again' is redundant with '\1'.")

addRule(
  pattern = r"\balready has been\b",
  suggestion = "has been",
  short_comment = "Redundant",
  full_comment = "The word 'already' is redundant with 'has been'.")

addRule(
  pattern = r"\bconsensus of opinion\b",
  suggestion = "consensus",
  short_comment = "Redundant",
  full_comment = "A 'consensus' is, by definition, of 'opinion'.")

addRule(
  pattern = r"\b(join(ed|ing)?) together\b",
  suggestion = r"\1",
  short_comment = "Redundant",
  full_comment = "To 'join' things is to bring them 'together'.")

addRule(
  pattern = r"\bmight (perhaps|possibly)\b",
  suggestion = "might",
  short_comment = "Redundant",
  full_comment = r"The word 'might' already expresses doubt. Therefore '\1' is redundant.")

addRule(
  pattern = r"\bmust (definitely|inevitably|necessarily)\b",
  suggestion = "must",
  short_comment = "Redundant",
  full_comment = r"The word 'must' already expresses inevitability, so '\1' is redundant.")

addRule(
  pattern = r"\b(previous|prior) (experiences?)\b",
  suggestion = r"\2",
  short_comment = "Redundant",
  full_comment = r"All experiences must have happened in the past, so '\1' is redundant.")

addRule(
  pattern = r"\bwill(,|, | ,| , | )in the future(,| ,|)\b",
  suggestion = "will",
  short_comment = "Redundant",
  full_comment = "If something 'will' happen, then it must be 'in the future' rather than the past.")

addRule(
  pattern = r"\bwork colleague\b",
  suggestion = "colleague",
  short_comment = "Redundant",
  full_comment = "'work' is already implied by 'colleague'")

# The following rules were derived from Richard Nordquist's
# article "200 Common Redundancies"
# http://grammar.about.com/od/words/a/redundancies.htm)

addRule(
  pattern = r"\b(assemble|attach|blend|collaborate|combine|confer|connect|cooper|ate|fuse|gather|integrate|join|meet|merge|mix|share|spliced) together\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\bcompletely (annihilate|destroyed|eliminate|engulfed|filled|surround)\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\badvance (planning|preview|reservations|warning)\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\babsolutely (essential|necessary)\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\bunexpected (emergency|surprise)\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\bstill (persists|remains)\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\bbasic (fundamentals|necessities)\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\bbrief (moment|summary)\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\b(drop|descend|dwindle|fall|kneel|plunge|shut|write) down\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\b(add|ascend|connect|heat|hoist|hurry|lift|open|raise|rise) up\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\b(circle|circulate) around\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\bfinal (conclusion|end|outcome|ultimatum)\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\bformer (graduate|veteran)\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\b(cancel|empty|start) out\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\bfellow (classmates|colleague)\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\bpast (experience|history|memories|records)\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\bsafe (haven|sanctuary)\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\bfuture (plans|recurrence)\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\bfrozen (ice|tundra)\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\bempty (hole|space)\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\bnew (beginning|construction|innovation|invention|recruit)\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\bmajor (breakthrough|feat)\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\bold (adage|cliche|custom|proverb)\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\b(reply|retreat|revert|extradite|refer|reflect) back\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\bpersonal (friend|opinion)\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\b(later|present) time\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\bsoft (in texture|to the touch)\b",
  suggestion = "soft",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\b(filled|full) to capacity\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\bautobiography of (his|her) own life\b",
  suggestion = "autobiography",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\bbiography of (his|her) life\b",
  suggestion = "biography",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\bweather (conditions|situation)\b",
  suggestion = "weather",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\btall in (height|stature)\b",
  suggestion = "tall",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\bintroduced (a new|for the first time)\b",
  suggestion = "introduced",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\b(may|could) possibly\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\bplan (ahead|in advance)\b",
  suggestion = "plan",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\bpreboard as an airplane\b",
  suggestion = "board",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\bpre(heat|record)\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\breason (is |)(because|why)\b",
  suggestion = r"reason \1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

addRule(
  pattern = r"\b(ISBN|PIN) number\b",
  suggestion = r"\1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")
