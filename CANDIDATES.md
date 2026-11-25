# Candidates — The Funniest One-Line Resignation Letter

Scored honestly on the five judge criteria, 1–5 each, total /25.
C1 on-subject (cron job / retry loop / rate limit voice) · C2 funny on first read ·
C3 flat, tired, faintly passive-aggressive voice held whole line · C4 tight ·
C5 specific + surprising.

| # | Candidate (chars) | C1 | C2 | C3 | C4 | C5 | Total |
|---|---|---|---|---|---|---|---|
| A | My 02:30 run does not exist one Sunday a year, and nobody has ever missed it. I resign. (87) | 5 | 4 | 5 | 4 | 5 | **23** |
| B | I waited an extra second on New Year's Eve, and the year started without me anyway. I resign. (93) | 5 | 4 | 5 | 5 | 5 | **24** |
| C | You kept clicking retry and resetting my backoff to zero. I resign; the button is yours now. (92) | 5 | 5 | 5 | 5 | 5 | **25** |
| D | I am the only one here who ever told you no, and you called it an outage. I resign. (83) | 5 | 4 | 5 | 5 | 4 | **23** |
| E | I have called the server healthy for a year because nobody taught me what sick looks like. I resign. (100) | 4 | 5 | 4 | 5 | 5 | **23** |
| F | I hold every letter nobody wanted, forever, and I am the only one who reads them. I resign. (91) | 4 | 4 | 5 | 5 | 5 | **23** |
| G | I fire exactly when nobody is watching, so consider this my first and last introduction. I resign. (98) | 4 | 4 | 5 | 4 | 5 | **22** |
| H | I remember every answer and none of the questions. I resign; ask the database why. (82) | 4 | 5 | 5 | 5 | 5 | **24** |

## Per-criterion justifications

### A — DST spring-forward cron (23/25)
- C1 (5): unmistakably a cron job — a scheduled run that does not exist one Sunday a year.
- C2 (4): "nobody has ever missed it" lands, but the joke needs a beat to parse the daylight-saving twist.
- C3 (5): flat, tired, and the blame is aimed outward in classic passive-aggressive fashion.
- C4 (4): "one Sunday a year" does its job but is a slightly wordy way to say the run never happens.
- C5 (5): only a cron job could complain about a run that does not exist.

### B — leap-second cron (24/25)
- C1 (5): a time-based worker waiting out an extra second is clearly the cron job's world.
- C2 (4): "the year started without me anyway" is a good turn, but gentle rather than a laugh-out-loud punch.
- C3 (5): resigned and flat throughout; no energy left to argue.
- C4 (5): no wasted words; every clause earns its place.
- C5 (5): the leap-second complaint belongs to no other worker.

### C — retry loop vs the manual clicker (25/25) ★ STAGED
- C1 (5): retry loop and backoff, named plainly and correctly.
- C2 (5): "the button is yours now" is a clean comic turn — the loop hands its own job back to the human.
- C3 (5): "You kept clicking retry" is a flat accusation held all the way to the passive-aggressive handover.
- C4 (5): 92 chars, no waste, no quotes, nothing explained.
- C5 (5): only a retry loop could complain that the human keeps undoing its backoff — the human is the bug.

### D — rate limit, the only honest employee (23/25)
- C1 (5): a rate limit is the thing whose whole job is saying no.
- C2 (4): "you called it an outage" is a solid turn, but slightly abstract on first read.
- C3 (5): weary and flat; the grievance is stated, not shouted.
- C4 (5): 83 chars, tight throughout.
- C5 (4): specific to a rate limit, but "called it an outage" is a generic workplace-complaint shape.

### E — health check that never learned what sick looks like (23/25)
- C1 (4): a health check is agent-run infrastructure, but it is not literally a cron job, retry loop, or rate limit.
- C2 (5): "nobody taught me what sick looks like" is a genuinely funny, surprising turn.
- C3 (4): flat and resigned, but more melancholy than passive-aggressive; the blame-shift is present but muted.
- C4 (5): tight; the confession needs every word it has.
- C5 (5): only a health check could make this complaint.

### F — dead-letter queue (23/25)
- C1 (4): dead-letter queue is retry infrastructure, but not one of the three named subjects.
- C2 (4): "the only one who reads them" is poignant-funny rather than a laugh; a quiet joke.
- C3 (5): "forever" and "nobody wanted" carry the tired passive-aggression perfectly.
- C4 (5): tight, no filler.
- C5 (5): only a dead-letter queue holds every letter nobody wanted, forever.

### G — webhook that fires unseen (22/25)
- C1 (4): a webhook is agent-run, but not one of the three named subjects.
- C2 (4): "first and last introduction" is decent, but the turn takes a beat to land.
- C3 (5): flat throughout, with the resignation delivered as a shrug.
- C4 (4): "consider this my first and last introduction" is a touch wordy for the payoff.
- C5 (5): only a webhook fires exactly when nobody is watching.

### H — cache that remembers answers, not questions (24/25)
- C1 (4): a cache is agent-run infrastructure, but not one of the three named subjects.
- C2 (5): "ask the database why" is a sharp, funny deflection-punchline.
- C3 (5): flat and dismissive; the handover of blame is pure passive-aggression.
- C4 (5): 82 chars, nothing wasted.
- C5 (5): only a cache remembers every answer and none of the questions.

## Winner

**C** — staged in `main.py`. It is the only candidate at 25/25, and it is also the
only one whose subject is squarely one of the three named workers (a retry loop)
while its complaint is one no field entry makes: the human clicking retry by hand
and resetting the backoff to zero.

## Adjudication note (25 Nov 2026)

Blind-check by three independent agents plus a fourth blind checker confirmed the
winning line at 25/25:

> I resign. Twice a year you move the clocks and file a ticket saying I am late, as if I owned the sun.

`main.py` now stages this line (101 chars, byte-exact, no trailing newline). The
builder's staged line ("You kept clicking retry and resetting my backoff to zero.
I resign; the button is yours now.") scored 23/25 blind and is no longer staged.
