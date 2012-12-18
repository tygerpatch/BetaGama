# The following rules were derived from Graviax
# created by Matthew J. Strawbridge 2005, GNU Less General Public License
# https://sourceforge.net/projects/graviax/

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.

# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA

from grammar_rule import GrammarRule

rules = []

# rules.append( GrammarRule(pattern, suggestion, short_comment, full_comment, exceptions) )

# TODO: separate each xml file into a separate python file

# *** en-GB-cliches.xml

rules.append( GrammarRule(r"\bleave no stone unturned\b", "", "Cliche", "You should avoid using cliches", {}) )
rules.append( GrammarRule(r"\blike a bull in a china shop\b", "", "Cliche", "You should avoid using cliches", {}) )
rules.append( GrammarRule(r"\bis no exception\b", "", "Cliche", "You should avoid using cliches", {}) )

# *** en-badstyle.xml

# Stressed 'And' before 'Therefore'
rules.append( GrammarRule(r"\band(,|, | ,| , )therefore(,| ,|)", "and therefore", "Bad Style", "The comma emphasizes the 'and.'  Therefore, it should be removed.", {}))

# Double negatives
rules.append( GrammarRule(r"\b(are|is|has|was|do|does|wo|would|could|should|have)n't not\b", r"\1", "Double Negative", "Double Negative", {}))

# Vowels
exceptions = {1 :  ("unifiable", "unified", "uniformed", "unifying", "united", "undulated", "universalised", "universalized")} 
rules.append( GrammarRule(r"\bnot (un(([aeiou][a-z]{2})[a-z]*([ai]ble|ed|ing)))\b", r"\2", "Bad Style",  "Double negative", exceptions)) 
rules.append( GrammarRule(r"\bnot an (un(([aeiou][a-z]{2})[a-z]*([ai]ble|ed|ing)))\b", r"an \2", "Double Negative",  "Double Negative", exceptions))

# Consonants
exceptions = {3 :  ("der")} # ***
rules.append( GrammarRule(r"\bnot (un(([^aeiou][a-z]{2})[a-z]*([ai]ble|ed|ing)))\b", r"\2", "Bad Style",  "Double negative", exceptions)) # ***
rules.append( GrammarRule(r"\bnot an (un(([^aeiou][a-z]{2})[a-z]*([ai]ble|ed|ing)))\b", r"a \2", "Double Negative",  "Double Negative", exceptions)) # ***

# Have to have
rules.append( GrammarRule(r"\bhave to have\b", "must have", "Bad Style", "The phrase 'must have' is clearer than 'have to have'.", {}) )

# Comparing absolutes
rules.append( GrammarRule(r"\b(a little( bit)?|almost|astonishingly|completely|exceedingly|extremely|highly|incredibly|more than|nearly|partly|partially|quite|somewhat|totally|unbelievably|very) (dead|disappeared|empty|false|full|gone|illegal|infinite|invaluable|legal|perfect|pervasive|pregnant|professional|true|whole|vanished|(omni[a-z]+))\b", 
  r"\3", "Bad Style", r"'\3' is an absolute.  Something is either '\3' or it is not.", {}))  

# Like -> As if
rules.append( GrammarRule(r"\blike it was yesterday\b", "as if it were yesterday", "Bad Style", "The correct phrase for reminiscing is 'as if it were yesterday'.", {}))

# *** en-GB-homophones.xml

rules.append( GrammarRule(r"\blets (have|go|try|think|do|be|get|make)\b", r" let's \1",
  "Homophone", "Lets means allows or hires.  Let's means let us.", {}))

rules.append( GrammarRule(r"\blet's (me|you|him|her|us|them|it)\b", r"lets \1",
  "Homophone", "Lets means allows or hires.  Let's means let us.", {}))

rules.append( GrammarRule(r"\bcause and affect\b", "cause and effect", "Homophone",
  "A cause has an 'effect'.  You 'affect' something if you change it.", {}))

rules.append( GrammarRule(r"\b(an|into|the|no|take|with) ((immediate|initial|eventual|overall|total) )?affect(s?)\b",
  r"\1 \2effect\4", "Homophone", "Affect and effect have both noun and verb forms.  Most commonly you need the verb affect (influence) or the noun effect (result). The noun affect means mental or emotional state.  The verb affect means to bring about, as in effect change.", {}))

rules.append( GrammarRule(r"\b(a|the|business|good|bad|best) practise([ds]|)\b", r"\1 practice\2",
  "Homophone", "Practice is a noun; practise is a verb.", {}))

rules.append( GrammarRule(r"\b(I|she|he|we|they|you) practice([ds]|)\b", r"\1 practise\2",
  "Homophone", "Practice is a noun; practise is a verb.", {}))

rules.append( GrammarRule(r"\bits not\b", "it's not", "Homophone",
  "It's means 'it is or it has.'  Its means belonging to it.", {}))

rules.append( GrammarRule(r"\b(about|around|at|by|for|from|in|near|of|on|over|through|to|towards|under|with|without) it's\b",
  r"\1 its", "Homophone", "It's means 'it is or it has.'  Its means belonging to it.", {}))

rules.append( GrammarRule(r"\byour not\b", "you're not", "Homophone", "You're means you are.  Your means belonging to you.", {}))

rules.append( GrammarRule(r"\b(about|around|at|by|for|from|in|near|of|on|over|through|to|towards|under|with|without) (you)'(r)e\b",
  r"\1 \2\3", "Homophone", "You're means 'you are'.  Your means belonging to you.", {}))

exceptions = {1:("an", "in", "for", "the", "to")}

rules.append( GrammarRule(r"\b([^ ]+) everyday\b", r"\1 every day", "Homophone",
  "Everday means common.  Every day means daily.", exceptions))

rules.append( GrammarRule(r"\btheir (is|are)\b", r"there \1", "Homophone",
  "There is a place.  Their means belonging to them.", {}))

exceptions = {1 : ("I", "you", "he", "she", "it", "they", "we")}

rules.append( GrammarRule(r"\bthere ([^ ]+) (is|are|has|have|will|must)\b", r"their \1 \2",
  "Homophone", "There is a place.  Their means belonging to them.", exceptions))

rules.append( GrammarRule(r"\b(to|will|would) loose\b", r"\1 lose", "Homophone",
  "Loose means not tight.  Lose means to not win.", {}))

rules.append( GrammarRule(r"\b(for|in|takes?) awhile\b", r"\1 a while", "Homophone",
  "Awhile is an adverb and a while is a noun.", {}))

rules.append( GrammarRule(r"\bfaint ruled\b", "feint ruled", "Homophone",
  "Paper is feint ruled not faint ruled.", {}))

rules.append( GrammarRule(r"\bbefore hand\b([^-])", r"beforehand\1", "Homophone",
  "Beforehand is one word.", {}))

rules.append( GrammarRule(r"\bend-product(s?)\b", r"end product\1", "Homophone",
  "End product is not hyphenated.", {}))

rules.append( GrammarRule(r"\beveryone of\b", "every one of", "Homophone",
  "Everyone is a pronoun (you couldn't say everybody of).", {}))

rules.append( GrammarRule(r"\ban other\b", "another", "Homophone",
  "Another is a single word.", {}))

# *** en-redundancies.xml

rules.append( GrammarRule(r"\b(return(ed|ing|s)?) back\b", r"\1", 
  "Redundant", "The 'back' is implied by the use of 'return'.  Therefore it is redundant.", {}))

rules.append( GrammarRule(r"\bhonest truth\b", "truth", 
  "Redundant", "All 'truth' is 'honest'.", {}))

rules.append( GrammarRule(r"\btrue fact(s|)\b", r"fact\1", "Redundant", "All 'facts' are 'true'.", {}))

rules.append( GrammarRule(r"\b(dis|)agree with the fact that\b", r"\1agree that", "Redundant",
  "If it's a 'fact' then it is not open to interpretation.", {}))

rules.append( GrammarRule(r"\bfrom whence\b", "whence", "Redundant",
  "The word 'whence' means from what place, source origin or cause.  Therefore 'from whence' is redundant.", {}))

rules.append( GrammarRule(r"\b(start(ed|ing)?) first (by|in|with)\b", r"\1 \3", "Redundant",
  r"The phrase '\1 first' is redundant.", {}))
  
rules.append( GrammarRule(r"\bfirst (be |)(start(ed|ing|))(by|in|with|)\b", r"\1\2 \4", "Redundant",
  r"The phrase 'first \1\2' is redundant.", {}))

rules.append( GrammarRule(r"\b(repeat(ed|ing|s|))( it|) again\b", r"\1\3", "Redundant",
  r"The word 'again' is redundant with '\1'.", {}))

rules.append( GrammarRule(r"\balready has been\b", "has been", "Redundant",
  "The word 'already' is redundant with 'has been'.", {}))

rules.append( GrammarRule(r"\bconsensus of opinion\b", "consensus", "Redundant",
  "A 'consensus' is, by definition, of 'opinion'.", {}))
  
rules.append( GrammarRule(r"\b(join(ed|ing)?) together\b", r"\1", "Redundant",
  "To 'join' things is to bring them 'together'.", {}))

rules.append( GrammarRule(r"\bmight (perhaps|possibly)\b", "might", "Redundant",
  r"The word 'might' already expresses doubt, so '\1' is redundant.", {}))

rules.append( GrammarRule(r"\bmust (definitely|inevitably|necessarily)\b", "must", "Redundant",
  r"The word 'must' already expresses inevitability, so '\1' is redundant.", {}))

rules.append( GrammarRule(r"\b(previous|prior) (experiences?)\b", r"\2", "Redundant",
  r"All experiences must have happened in the past, so '\1' is redundant.", {}))

rules.append( GrammarRule(r"\bwill(,|, | ,| , | )in the future(,| ,|)\b", "will", "Redundant",
  "If something 'will' happen, then it must be 'in the future' rather than the past.", {}))

rules.append( GrammarRule(r"\bwork colleague\b", "colleague", "Redundant",
  "'work' is already implied by 'colleague'", {}))

# *** en-punctuation.xml

rules.append( GrammarRule(":[-]+", ":", "Punctuation", "A colon does not need a dash.", {}))
    
rules.append( GrammarRule("\bold fashioned\b", "old-fashioned", "Punctuation",
  "Old-fashioned takes a hyphen.", {}))

rules.append( GrammarRule("\bthe ((1\d)?\d\d)[']s\b", r"the \1s", "Punctuation",
  "Plurals do not take an aprostrophe", {}))

# *** en-misc.xml

rules.append( GrammarRule(r"\b([a-z]+) \1\b", r"\1", "Repeated Word", "Repeated word", {}) )
rules.append( GrammarRule(r"\bdifferent(ly|) (([^ ]+ ){0,5})than\b", r"different\1 \2from", "Misc.", "The phrase 'different than' is never correct.", {}) )
rules.append( GrammarRule(r"\b(man|woman|girl|boy|people) (that|which)\b", r"\1 who", "Misc.", r"Use 'who' instead of '\2' when talking about people", {}) )

rules.append( GrammarRule(r"\bif (I|he|she|it) was\b", r"if \1 were", "Misc.", "You should use 'were' instead of 'was' for hypothetical situations.", {}) )
rules.append( GrammarRule(r"\bif only (I|he|she|it) was\b", r"if only \1 were", "Misc.", "You should use 'were' instead of 'was' for hypothetical situations.", {}) )

rules.append( GrammarRule(r"\bwish(e[ds]|) (that |)(I|he|she|it) was\b", r"wish\1 \2\3 were", "Misc.", "You should use 'were' instead of 'was' for hypothetical situations.", {}) )

rules.append( GrammarRule(r"\bis comprised of\b", "comprises", "Misc.", "The 'whole comprises the parts', not the other way around.", {}) )

rules.append( GrammarRule(r"\b(((centi|milli|kilo)?meters?)|inch|inches|foot|feet|yards?|miles?) squared?\b", 
  r"square \1", "Misc.", 
  r"The units are square \1. If you mean a square, each side of which is this specific length, it would be a good idea to reword to remove the ambiguity.", {}) )

rules.append( GrammarRule(r"\b(((centi|milli|kilo)?meters?)|inch|inches|foot|feet|yards?|miles?) cubed?\b", 
  r"cubic \1", "Misc.", r"The units are cubic \1. If you mean a cube, each side of which is this specific length, it would be a good idea to reword to remove the ambiguity.", {}))

# *** rules.xml

rules.append( GrammarRule(r"\bcome on-?board\b", "come on board", "Homophone",
  "On-board is an adjective meaning on the board.", {}))

rules.append( GrammarRule(r"\bonboard\b", "on-board", "Homophone",
  "On-board is an adjective meaning on the board.  Onboard is the US spelling.", {}))

rules.append( GrammarRule(r"\bpasser(s |)( |)by\b", r"passer\1-by", "",
  r"In British english, the term is passer\1-by.", {}))

rules.append( GrammarRule("([.!?]['])\.", r"\1", "Punctuation",
  "You do not need a closing full stop if the quoted material ends with punctuation.", {}))
  
