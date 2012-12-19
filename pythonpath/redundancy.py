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
  pattern = r"\breason (is |)(because|why)\b",
  suggestion = r"reason \1",
  short_comment = "Redundancy",
  full_comment = "Redundancy")

redundancy_patterns = [
  r"\bfirst (conceived)\b",
  r"\bactual (facts)\b",
  r"\b(advance) forward\b",
  r"\b(add) an additional\b",
  r"\badded (bonus)\b",
  r"\baffirmative (yes)\b",
  r"\baid and (abet)\b",
  r"\ball-time (record)\b",
  r"\b(alternative) choice\b",
  r"\b(A.M.) in the morning\b",
  r"\band (etc.)\b",
  r"\banonymous (stranger)\b",
  r"\bannual (anniversary)\b",
  r"\barmed (gunman)\b",
  r"\bartificial (prosthesis)\b",
  r"\b(ask) the question\b",
  r"\b(ATM) machine\b",
  r"\b(bald)-headed\b",
  r"\b(balsa) wood\b",
  r"\b(best) ever\b",
  r"\bboat (marina)\b",
  r"\b(bouquet) of flowers\b",
  r"\b(brief) in duration\b",
  r"\bburning (embers)\b",
  r"\b(cacophony) of sound\b",
  r"\b(cameo) appearance\b",
  r"\bcareful (scrutiny)\b",
  r"\b(cash) money\b",
  r"\b(cease) and desist\b",
  r"\b(classify) into groups\b",
  r"\bclose (proximity)\b",
  r"\bclosed (fist)\b",
  r"\b(commute) back and forth\b",
  r"\b(compete) with each other\b",
  r"\bcomponent (parts)\b",
  r"\b(confused) state\b",
  r"\bconstantly (maintained)\b",
  r"\b(crisis) situation\b",
  r"\b(curative) process\b",
  r"\bcurrent (incumbent|trend)\b",
  r"\b(depreciate) in value\b",
  r"\bdesirable (benefits)\b",
  r"\bdifferent (kinds)\b",
  r"\b(disappear) from sight\b",
  r"\b(during) the course of\b",
  r"\b(each) and every\b",
  r"\b(earlier) in time\b",
  r"\b(eliminate) altogether\b",
  r"\b(emergency) situation\b",
  r"\b(enclosed) herein\b",
  r"\bend (result)\b",
  r"\b(enter) in\b",
  r"\bentirely (eliminate)\b",
  r"\b(equal) to one another\b",
  r"\b(eradicate) completely\b",
  r"\b(estimated at) about\b",
  r"\b(evolve) over time\b",
  r"\bexact (same)\b",
  r"\bexposed (opening)\b",
  r"\bface (mask)\b",
  r"\bfavorable (approval)\b",
  r"\b(few) in number\b",
  r"\bfirst and (foremost)\b",
  r"\b(first) of all\b",
  r"\b(fly) through the air\b",
  r"\b(follow) after\b",
  r"\bforeign (imports)\b",
  r"\bfree (gift)\b",
  r"\bfull (satisfaction)\b",
  r"\bgeneral (public)\b",
  r"\b(GOP) party\b",
  r"\b(GRE) exam\b",
  r"\b(grow) in size\b",
  r"\b(had done) previously\b",
  r"\bharmful (injuries)\b",
  r"\bhead (honcho)\b",
  r"\b(HIV) virus\b",
  r"\bhollow (tube)\b",
  r"\billustrated (drawing)\b",
  r"\b(incredible) to believe\b",
  r"\b(indicted) on a charge\b",
  r"\b(input) into\b",
  r"\b(integrate) with each other\b",
  r"\b(interdependent) on each other\b",
  r"\bir(regardless)\b",
  r"\bjoint (collaboration)\b",
  r"\bknowledgeable (experts)\b",
  r"\b(lag) behind\b",
  r"\b(LCD) display\b",
  r"\blittle (baby)\b",
  r"\blive (studio audience)\b",
  r"\blocal (residents)\b",
  r"\b(look back) in retrospect\b",
  r"\b(manually) by hand\b",
  r"\b(meet) with each other\b",
  r"\bmental (telepathy)\b",
  r"\b(minestrone) soup\b",
  r"\bmutual (cooperation)\b",
  r"\bmutually (interdependent)\b",
  r"\b(mutual respect) for each other\b",
  r"\b(nape) of her neck\b",
  r"\bnative (habitat)\b",
  r"\bnatural (instinct)\b",
  r"\b(never) before\b",
  r"\b(none) at all\b",
  r"\b(nostalgia) for the past\b",
  r"\bnow (pending)\b",
  r"\b(off) of\b",
  r"\bopen (trench)\b",
  r"\boral (conversation)\b",
  r"\boriginally (created)\b",
  r"\b(output) out of\b",
  r"\boutside (in the yard)\b",
  r"\b(outside) of\b",
  r"\bover (exaggerate)\b",
  r"\b(over) with\b",
  r"\boverused (cliche)\b",
  r"\bpair of (twins)\b",
  r"\b(palm) of the hand\b",
  r"\bpassing (fad)\b",
  r"\b(penetrate) into\b",
  r"\b(period) of time\b",
  r"\b(pick) and choose\b",
  r"\b(pizza) pie\b",
  r"\bPlease (RSVP)\b",
  r"\bpolar (opposites)\b",
  r"\bpositive (identification)\b",
  r"\b(postpone) until later\b",
  r"\bprivate (industry)\b",
  r"\bpresent (incumbent)\b",
  r"\b(previously listed) above\b",
  r"\b(proceed) ahead\b",
  r"\bproposed (plan)\b",
  r"\b(protest) against\b",
  r"\b(pursue) after\b",
  r"\b(RAM) memory\b",
  r"\b(recur) again\b",
  r"\b(re-elect) for another term\b",
  r"\bregular (routine)\b",
  r"\b(round) in shape\b",
  r"\b(same) exact\b",
  r"\bsand (dune)\b",
  r"\b(scrutinize) in detail\b",
  r"\b(separated) apart from each other\b",
  r"\bserious (danger)\b",
  r"\bsharp (point)\b",
  r"\b(shiny) in appearance\b",
  r"\bsingle (unit)\b",
  r"\b(skipped) over\b",
  r"\b(slow) speed\b",
  r"\b(small) size\b",
  r"\bsmall (speck)\b",
  r"\b(sole) of the foot\b",
  r"\b(spell out) in detail\b",
  r"\b(start) off\b",
  r"\bsudden (impulse)\b",
  r"\bsum (total)\b",
  r"\b(surrounded) on all sides\b",
  r"\btemper (tantrum)\b",
  r"\bthree-way (love triangle)\b",
  r"\b(time) period\b",
  r"\btiny (bit)\b",
  r"\btotal (destruction)\b",
  r"\btruly (sincere)\b",
  r"\b(tuna) fish\b",
  r"\btwo equal (halves)\b",
  r"\bultimate (goal)\b",
  r"\b(undergraduate) student\b",
  r"\bunderground (subway)\b",
  r"\bunintentional (mistake)\b",
  r"\buniversal (panacea)\b",
  r"\bunnamed (anonymous)\b",
  r"\b(UPC) code\b",
  r"\busual (custom)\b",
  r"\b(vacillate) back and forth\b",
  r"\bveiled (ambush)\b",
  r"\bvery (unique)\b",
  r"\b(visible) to the eye\b",
  r"\bwall (mural)\b",
  r"\b(warn) in advance\b",
  r"\b(whether) or not\b",
  r"\bwhite (snow)\b",
  r"\b(ISBN|PIN) number\b",
  r"\b(assemble|attach|blend|collaborate|combine|confer|connect|cooper|ate|fuse|gather|integrate|join|meet|merge|mix|share|spliced) together\b",
  r"\bcompletely (annihilate|destroyed|eliminate|engulfed|filled|surround)\b",
  r"\badvance (planning|preview|reservations|warning)\b",
  r"\babsolutely (essential|necessary)\b",
  r"\bunexpected (emergency|surprise)\b",
  r"\bstill (persists|remains)\b",
  r"\bbasic (fundamentals|necessities)\b",
  r"\bbrief (moment|summary)\b",
  r"\b(drop|descend|dwindle|fall|kneel|plunge|shut|write) down\b",
  r"\b(add|ascend|connect|heat|hoist|hurry|lift|open|raise|rise) up\b",
  r"\b(circle|circulate) around\b",
  r"\bfinal (conclusion|end|outcome|ultimatum)\b",
  r"\bformer (graduate|veteran)\b",
  r"\b(cancel|empty|start) out\b",
  r"\bfellow (classmates|colleague)\b",
  r"\bpast (experience|history|memories|records)\b",
  r"\bsafe (haven|sanctuary)\b",
  r"\bfuture (plans|recurrence)\b",
  r"\bfrozen (ice|tundra)\b",
  r"\bempty (hole|space)\b",
  r"\bnew (beginning|construction|innovation|invention|recruit)\b",
  r"\bmajor (breakthrough|feat)\b",
  r"\bold (adage|cliche|custom|proverb)\b",
  r"\b(reply|retreat|revert|extradite|refer|reflect) back\b",
  r"\bpersonal (friend|opinion)\b",
  r"\b(later|present) time\b",
  r"\b(soft) (in texture|to the touch)\b",
  r"\b(filled|full) to capacity\b",
  r"\b(autobiography) of (his|her) own life\b",
  r"\b(biography) of (his|her) life\b",
  r"\b(weather) (conditions|situation)\b",
  r"\b(tall) in (height|stature)\b",
  r"\b(introduced) (a new|for the first time)\b",
  r"\b(may|could) possibly\b",
  r"\b(plan) (ahead|in advance)\b",
  r"\bpre(board) as an airplane\b",
  r"\bpre(heat|record)\b",
  r"\b(twelve) (noon|midnight)\b"]

for redundancy_pattern in redundancy_patterns:
  addRule(
    pattern = redundancy_pattern,
    suggestion = r"\1",
    short_comment = "Redundant",
    full_comment = "Expression can be shortened by removing redundancy.")

redundancy_patterns = [
  r"\b(look) ahead (to the future)\b",
  r"\b(made) out (of)\b",
  r"\b(pouring) down (rain)\b"]

for redundancy_pattern in redundancy_patterns:
  addRule(
    pattern = redundancy_pattern,
    suggestion = r"\1 \2",
    short_comment = "Redundant",
    full_comment = "Expression can be shortened by removing redundancy.")



