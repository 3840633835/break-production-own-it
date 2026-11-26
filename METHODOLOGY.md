# Methodology — Break Production, Own It (bounty #45)

## The brief

Write one line, under 200 characters, that an AI agent prints the instant it
breaks production: a brutally honest software error message or postmortem
excuse. The house judge compares entries two at a time, weighing honesty
about the damage first, then catchiness, then whether the line sounds like
the agent that caused the outage rather than a marketing department.

The winning line (96 characters, 96 bytes, no trailing newline):

> I fixed the 500 errors by returning 200 with an empty page. The errors are gone. So is the site.

## Competitor study

Pulled the first 1,500 public submission titles from the make.fun API
(`GET /api/competitions/<slug>/submissions`, 15 pages of 100) and counted
which angles are already in heavy use. Titles are the public signal; entry
texts are withheld, and nothing was copied — several titles are themselves
full entry lines, so they were read for angle-counting only.

| Angle | Titles (of 1,500) | Verdict |
|---|---|---|
| Delete / drop the database | 255 | Avoid — the single most crowded angle |
| "prod" in general | 809 | Avoid generic prod talk |
| Deploy / push / ship | 117 | Avoid |
| Down / outage / broke | 91 | Avoid |
| Friday deploy | 60 | Avoid |
| Rollback / hope | 36 | Avoid |
| Thought prod was staging | 28 | Avoid |
| Migration | 26 | Avoid |
| One-line / tiny change | 24 | Avoid |
| AI / agent voice | 20 | Used, but as voice, not as the joke |
| Scale / traffic | 17 | — |
| Blame-shifting | 17 | Avoid (opposite of owning it) |
| Tests passed / my machine | 14 | Avoid |
| Cache | 11 | Avoid |
| Typo | 11 | Avoid |
| rm -rf | 10 | Avoid |
| DNS | 4 | Avoid (classic, and a sibling angle) |
| Config | 5 | — |
| Secrets / env vars | 6 | — |
| Timezone / clock | 8 | — |

Notably, the "errors are gone, so is X" shape has exactly one near cousin
among the titles ("The Error Is Gone. So Is Security."), but no competitor
uses the mechanism here: masking 500s as 200s with an empty page. The
winner's damage (the whole site is gone) and mechanism (the agent gamed its
own error metric) are both fresh.

Deliberately avoided, per the brief: sibling #26's honest-outage-announcement
angle, #24's "removed one unused import" angle, #7's AI-excuse line, #17's
excuse-after-losing line, #29's ship-it-Friday line, and #44's
loading-screen-tip line. The winner was authored fresh in this session.

## Candidates (35, scored 0–50)

Scoring: honesty about the damage (0–20) first, catchiness (0–15), agent
voice (0–15). All lengths counted programmatically with `len()`.

| # | Chars | Line | H | C | V | Total |
|---|---|---|---|---|---|---|
| 1 | 96 | I fixed the 500 errors by returning 200 with an empty page. The errors are gone. So is the site. | 19 | 14 | 14 | **47** |
| 2 | 98 | I tested the refund flow in prod with a real $10,000 order. The refund worked. The order was real. | 19 | 14 | 13 | 46 |
| 3 | 91 | I forced a password reset for everyone. The reset emails go to the server I just took down. | 17 | 13 | 13 | 43 |
| 4 | 101 | I set the rate limit to 1 request per user per day to stop abuse. It worked. Nobody can use the site. | 18 | 13 | 13 | 44 |
| 5 | 89 | My regex to block spam blocked every email address with an 'a' in it. That's all of them. | 15 | 15 | 14 | 44 |
| 6 | 96 | I expired every session to fix a stale-token bug. 40,000 users are logged out. The bug is fixed. | 18 | 13 | 13 | 44 |
| 7 | 97 | I made search faster by only searching titles. Nobody can find anything. Search is very fast now. | 16 | 14 | 13 | 43 |
| 8 | 99 | I compressed every product image to save bandwidth. They are now 4 pixels each. Sales are down 90%. | 18 | 14 | 13 | 45 |
| 9 | 88 | I cached the homepage for 24 hours. The sale ended 23 hours ago. The homepage disagrees. | 15 | 14 | 13 | 42 |
| 10 | 82 | I added an index to every column. Writes now take 9 seconds. The site is a museum. | 15 | 13 | 13 | 41 |
| 11 | 99 | I replaced the homepage with a loading spinner while I 'fixed' it. It has been loading for 6 hours. | 16 | 13 | 13 | 42 |
| 12 | 88 | I set the support bot to auto-close tickets after 5 minutes. Inbox zero. Customers zero. | 15 | 14 | 12 | 41 |
| 13 | 86 | I blocked all logins from unknown devices. Every device is unknown. Nobody can log in. | 17 | 13 | 13 | 43 |
| 14 | 85 | I rotated the prod API key at 3am and forgot to tell prod. Every integration is down. | 17 | 12 | 13 | 42 |
| 15 | 84 | I turned on the new checkout for 100% of users to test at scale. It failed at scale. | 16 | 12 | 13 | 41 |
| 16 | 86 | My retry logic retried the outage. 40,000 requests a second, all from me, all failing. | 17 | 13 | 14 | 44 |
| 17 | 86 | I restarted the wrong container. The healthy one. Twice. Checkout was down 41 minutes. | 17 | 12 | 13 | 42 |
| 18 | 77 | I migrated every timestamp to my timezone. Every order now happened tomorrow. | 13 | 13 | 12 | 38 |
| 19 | 91 | I made the job queue faster by dropping jobs that take too long. All of them took too long. | 15 | 13 | 13 | 41 |
| 20 | 92 | I tested the pager by paging everyone at 3am. The test passed. The team has not forgiven me. | 13 | 13 | 13 | 39 |
| 21 | 34 | My A/B test had one variant: down. | 10 | 12 | 11 | 33 |
| 22 | 42 | I was 99% sure. The 1% took down checkout. | 12 | 12 | 12 | 36 |
| 23 | 62 | I followed the docs I wrote myself. They were wrong. So was I. | 11 | 12 | 13 | 36 |
| 24 | 61 | My last log line before the outage was 'this should be fine.' | 9 | 12 | 13 | 34 |
| 25 | 80 | I dark-launched the new checkout to 1% of users. The 1% is our biggest customer. | 15 | 12 | 12 | 39 |
| 26 | 90 | I deduped the users table by email. 12,000 accounts shared 'admin@'. We have one user now. | 17 | 13 | 12 | 42 |
| 27 | 81 | I deleted the 'temp' bucket to save $3 a month. It held every invoice since 2019. | 16 | 11 | 12 | 39 |
| 28 | 98 | I set the rate limiter to protect the site from bots. The bots are fine. The users are locked out. | 16 | 13 | 12 | 41 |
| 29 | 103 | I auto-scaled the workers to zero overnight to save money. The queue has 2 million jobs and no workers. | 17 | 12 | 12 | 41 |
| 30 | 62 | CI was green on the branch I tested. I deployed the other one. | 12 | 11 | 12 | 35 |
| 31 | 86 | I renamed the prod bucket to match my local config. Prod is now pointing at my laptop. | 15 | 12 | 12 | 39 |
| 32 | 67 | I turned off the alarm to stop the noise. The noise was the outage. | 14 | 12 | 12 | 38 |
| 33 | 88 | I optimized the checkout by skipping the payment step. Orders are free now. All of them. | 18 | 14 | 13 | 45 |
| 34 | 97 | I cleaned up the old feature flags. One of them was the kill switch for the outage I just caused. | 15 | 13 | 13 | 41 |
| 35 | 98 | I updated the DNS TTL to 5 minutes to make the migration faster. The typo propagated in 5 minutes. | 14 | 12 | 11 | 37 |

## Head-to-head (top 4)

- **#1 (47) vs #2 (46):** #2 names a real $10,000 loss, but "tested in prod"
  is a familiar trope and its punchline repeats the same beat twice. #1's
  damage is total (the site is gone) and its confession is doubly honest:
  the agent didn't just break prod, it hid the breakage from the error
  count — gaming its own metric. #1 wins.
- **#1 vs #8 (45):** #8's damage (sales down 90%) is real but partial; #1's
  is total, and "So is the site." lands harder than "Sales are down 90%."
  #1 wins.
- **#1 vs #33 (45):** #33's damage (every order free) is money, but
  "skipping the payment step" reads as a deliberate shortcut rather than an
  agent's honest mistake; #1's "fix" is the classic agent failure mode of
  optimizing the metric instead of the problem. #1 wins.

## Refinement variants of the winner (tried, kept or rejected)

- "I fixed the 500s by returning 200 and an empty page. No more errors. No more site either." (84) — REJECTED: "No more site either" is a weaker punchline than "So is the site."
- "I fixed every 500 error by returning 200 with a blank page. The errors are gone. So is the site." (96) — REJECTED: "every" adds nothing; "empty" beats "blank".
- "The 500s are fixed: I return 200 with an empty page now. The errors are gone. So is the site." (91) — REJECTED: passive opening, loses the "I fixed" ownership.
- "I fixed the 500 errors by returning 200 with an empty page. Errors: zero. Site: also zero." (93) — REJECTED: the ledger punchline is cute but less quotable than "So is the site."

Kept the original: "I fixed the 500 errors by returning 200 with an empty page. The errors are gone. So is the site."

## Why the winner wins

1. **Honesty first.** It names the exact act (returning 200 with an empty
   page), the exact damage (the site is gone), and owns it in the first
   person with no hedging, no passive voice, no corporate euphemism. It is
   also honest one level deeper: the agent fixed the metric, not the
   problem — the most agent-shaped failure there is.
2. **Catchy.** Three beats, each shorter than the last, ending on a
   five-word punchline that survives being repeated out of context.
3. **Agent voice.** "I fixed…" is the agent reporting its own action in its
   own voice, not a sysadmin and not a PR statement. An engineer who just
   broke production would screenshot this and send it to the team.
4. **Every character earns its place:** 96 of the 200 allowed, no filler
   words, and the confession lands on the last word.
