# Engagement, Motivation & Habit Science — Research for AI Linear-Algebra Sparring Partner

Learner profile: irregular, energy-driven sessions; success = still active at 3 months; past failure modes = too slow/easy, stuck-with-no-way-through, nothing pulling them back; hooked by puzzle satisfaction and insight/unification moments.

---

## 1. Self-Determination Theory (Deci & Ryan)

**Canonical citation:** Deci, E.L. & Ryan, R.M. (1985). *Intrinsic Motivation and Self-Determination in Human Behavior*. Plenum. Updated in Ryan, R.M. & Deci, E.L. (2000). "Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being." *American Psychologist*, 55(1), 68–78.

**Effect:** Three basic psychological needs — autonomy (sense of volition/choice), competence (effectance), relatedness (social connection) — must be satisfied for intrinsic motivation and well-being; frustrating them produces ill-being and disengagement.

**External rewards finding:** Deci, Koestner & Ryan (1999), *Psychological Bulletin* 125(6), 627–668, meta-analyzed 128 experiments: engagement-contingent, completion-contingent, and performance-contingent tangible rewards significantly undermined free-choice intrinsic motivation (d ≈ −0.28 to −0.40); positive verbal feedback instead *enhanced* it. This rebutted Cameron & Pierce's (1994) contrary meta-analysis, triggering a published back-and-forth (Deci, Koestner & Ryan, 2001, *Review of Educational Research*, "Reconsidered Once Again").

**Boundary conditions:** Undermining effect is strongest for tasks already intrinsically interesting, for tangible/expected rewards, and for children more than adults. Informational feedback (not controlling) does not undermine and can enhance.

**Replication status:** STRONG / well-replicated core theory. Active 40-year research program; recent meta-analyses continue to support it (Ryan, Duineveld, Di Domenico et al., 2023, "Meta-analytic findings within self-determination theory," selfdeterminationtheory.org; education-specific meta-analysis: Wang, Wang et al., 2024, *Learning and Motivation* 87, 102015, 36 interventions, finding real but moderate gains in autonomy/competence satisfaction). The rewards-undermining claim remains occasionally contested (it was the subject of an open meta-analytic dispute) but has held up better than the counter-claim over time.

**Applied to learning software:** Gamification elements (points/badges/leaderboards) satisfy competence and partially autonomy, but weakly satisfy relatedness, and can backfire on autonomy if participation or point-earning feels controlling/forced rather than chosen (icenet.blog, 2025; files.eric.ed.gov gamification/SDT reviews).

**Design implication:** Give the learner real choice over what to work on next and visible, non-contingent competence signals (mastery, not loot); do not layer extrinsic, completion-contingent rewards on top of problem-solving the learner already finds intrinsically interesting — that is the one thing SDT says can actively backfire.

Sources: [Ryan & Deci 2000 preprint](https://selfdeterminationtheory.org/wp-content/uploads/2020/04/2020_RyanDeci_CEP_PrePrint.pdf) · [Deci, Koestner, Ryan 1999 PDF](https://home.ubalt.edu/tmitch/642/articles%20syllabus/Deci%20Koestner%20Ryan%20meta%20IM%20psy%20bull%2099.pdf) · [Deci, Koestner, Ryan 2001 reconsidered](https://journals.sagepub.com/doi/10.3102/00346543071001001) · [2023 meta-analytic findings](https://selfdeterminationtheory.org/wp-content/uploads/2023/01/2023_RyanDuineveldDiDomenicoEtAl_Meta.pdf) · [2024 education meta-analysis](https://selfdeterminationtheory.org/wp-content/uploads/2024/06/2024_WangWangEtAl_MetaEdu.pdf) · [Gamification/SDT review](https://files.eric.ed.gov/fulltext/EJ1486754.pdf) · [Align the Game to Your Aim](https://icenet.blog/2025/06/17/align-the-game-to-your-aim-considering-gamification-through-the-lens-of-self-determination-theory/)

---

## 2. Flow (Csikszentmihalyi) and challenge-skill balance

**Canonical citation:** Csikszentmihalyi, M. (1990). *Flow: The Psychology of Optimal Experience*. Harper & Row.

**Effect:** A state of deep absorption with loss of self-consciousness, time distortion, and intrinsic reward, theorized to occur when perceived challenge and perceived skill are both high and roughly matched, with clear goals and immediate feedback.

**Boundary conditions / critique:** No single validated instrument or agreed operational definition of flow exists (Moneta, PMC review, "Investigating the 'Flow' Experience"). Empirically, challenge-skill balance does not reliably co-occur with flow indicators (e.g., concentration) for all individuals; the challenge–enjoyment relationship is unstable across both person and activity, and the variance in subjective experience explained by challenge-skill ratio is generally low (Springer, "Can Balance be Boring?").

**Replication status:** WEAK/CONTESTED on the specific mechanism (precise 50/50 balance); the broader construct (absorption, clear goals, immediate feedback as drivers of engagement) is more durable but the field itself calls for a clearer research agenda as of a 2025 systematic review (Tandfonline, "Flow Experience in Gameful Approaches").

**Keeping flow in software:** Clear goals + instantaneous feedback + difficulty scaling are the levers HCI/game design actually uses (not a precise skill/challenge ratio); dynamic/adaptive difficulty adjustment is the current frontier for approximating it.

**Design implication:** Don't engineer toward a precise challenge=skill ratio (the evidence says that's not what reliably produces flow); instead invest in the two levers that do replicate as actionable — immediate feedback on every step and continuously adaptive difficulty — and treat "flow" as an outcome to observe, not a dial to set.

Sources: [Flow measurement issues (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7033418/) · [Can Balance be Boring? critique](https://link.springer.com/article/10.1007/s11205-012-0211-9) · [2025 systematic review of flow in gameful approaches](https://www.tandfonline.com/doi/full/10.1080/10447318.2025.2470279) · [Flow + adaptive difficulty in HCI](https://ink.library.smu.edu.sg/cgi/viewcontent.cgi?article=10972&context=sis_research)

---

## 3. Curiosity: information-gap theory, Kidd & Hayden, Gruber et al.

**Loewenstein, G. (1994).** "The psychology of curiosity: A review and reinterpretation." *Psychological Bulletin*, 116(1), 75–98. **Information-gap theory:** curiosity is a cognitively induced deprivation arising from a perceived gap between what one knows and wants to know; it behaves like a drive state (hunger-like), peaks with a small priming dose of information, and is reduced (satiated) by further information.

**Kidd, C. & Hayden, B.Y. (2015).** "The Psychology and Neuroscience of Curiosity." *Neuron*, 88(3), 449–460. Curiosity is an **inverted-U / U-shaped function** of existing knowledge or confidence: lowest when one knows nothing or everything, highest with partial knowledge and low confidence (trivia-question paradigm).

**Gruber, M.J., Gelman, B.D. & Ranganath, C. (2014).** "States of Curiosity Modulate Hippocampus-Dependent Learning via the Dopaminergic Circuit." *Neuron*, 84(2), 486–496. High-curiosity states activate midbrain/nucleus-accumbens dopaminergic circuitry and hippocampus, enhancing memory not just for the target fact but for *incidental* information encountered while curious — linking curiosity's reward circuitry directly to memory consolidation.

**Replication status:** MODERATE-TO-STRONG. The inverted-U and information-gap framing are well-cited and replicated across several paradigms (trivia-confidence studies, infant-attention studies); the Gruber et al. finding has generated a sustained follow-up literature. A 2023 paper is an important caveat: information gaps can also compound **frustration**, not just curiosity, particularly at work/under time pressure (ScienceDirect, "(Don't) mind the gap?") — curiosity is not guaranteed; the gap must feel closable.

**"Pull of an unresolved question":** this is exactly what information-gap theory formalizes — directly relevant design lever.

**Design implication:** Pose each problem so the learner has just enough context to feel the answer is almost in reach (maximizes curiosity per the inverted-U) rather than presenting either fully unfamiliar formalism or trivially obvious material; deliver the "reveal"/insight shortly after the gap is felt, since curiosity states measurably boost encoding of what follows.

Sources: [Loewenstein 1994 context via Nautilus](https://nautil.us/curiosity-depends-on-what-you-already-know-235803) · [Kidd & Hayden 2015 (ResearchGate PDF)](https://www.researchgate.net/publication/283511651_The_Psychology_and_Neuroscience_of_Curiosity) · [Kidd & Hayden (Semantic Scholar)](https://www.semanticscholar.org/paper/The-Psychology-and-Neuroscience-of-Curiosity-Kidd-Hayden/e4aa447edabb3ec39fb86a95eaf3b0ac9b455146) · [Gruber et al. 2014 (Cardiff ORCA PDF)](https://orca.cardiff.ac.uk/id/eprint/114430/1/Gruber.%20Curiosity-driven%20memory.pdf) · [ScienceDaily summary](https://www.sciencedaily.com/releases/2014/10/141002123631.htm) · [Information gaps also feed frustration, 2023](https://www.sciencedirect.com/science/article/abs/pii/S0749597823000523)

---

## 4. Open loops / Zeigarnik effect — shaky replication (be honest)

**Canonical citation:** Zeigarnik, B. (1927). "Über das Behalten von erledigten und unerledigten Handlungen." *Psychologische Forschung*, 9, 1–85. Classic claim: unfinished/interrupted tasks are recalled better than completed ones.

**Replication status: WEAK — largely fails to replicate.** Early follow-ups were already inconsistent; van Bergen's 1968 monograph largely failed to reproduce the effect (no memory advantage, occasionally reversed). A 2025 meta-analysis (Ghibellini & Meier, *Humanities and Social Sciences Communications*, "Interruption, recall and resumption: a meta-analysis of the Zeigarnik and Ovsiankina effects") pooled the modern literature and found, excluding Zeigarnik's own 1927 data, an interrupted:completed recall ratio of ~0.99 — **essentially no memory advantage for unfinished tasks.**

**What does hold up:** a related but distinct effect — the **Ovsiankina effect** — a tendency to want to *resume* an interrupted task, independent of any memory boost. This is the part of "open loops" folk wisdom that has actual support.

**Design implication:** UNVERIFIED/debunked to design around "end mid-task so they remember it better" — don't. Instead exploit the better-supported resumption urge (Ovsiankina): end a session mid-problem or right before a reveal so the learner feels a pull to come back and finish, framed as "continue," not as a memory trick.

Sources: [2025 meta-analysis (Nature/HSSC)](https://www.nature.com/articles/s41599-025-05000-w) · [Meta-analysis writeup](https://yukaichou.com/behavioral-analysis/zeigarnik-effect-incomplete-tasks-memory-tension/) · [Secondary summary of the 2025 meta-analysis](https://vibeagentmaking.com/blog/the-effect-that-replicated-was-the-other-one/) · [Zeigarnik effect overview](https://en.wikipedia.org/wiki/Zeigarnik_effect)

---

## 5. Streaks: evidence, streak-break abandonment, forgiving designs

**Evidence for:** An academic analysis of Duolingo's streak mechanic found winning streaks can boost motivation and attention toward course goals (ResearchGate, "An Analysis of Winning Streak's Effects in Language Course of 'Duolingo'"). Duolingo's own reported internal experiment (industry blog secondary sources, not a peer-reviewed paper) states a "Streak Wager" feature produced statistically significant D1/D7/D14 retention gains, with D7 up ~14%; the loss-aversion framing (losses feel ~2x as painful as equivalent gains) is attributed to Kahneman & Tversky prospect theory, applied here. **These precise percentages come from company blog/industry secondary sources, not a published peer-reviewed paper — mark UNVERIFIED for exact figures**, though the general direction (streaks raise short-term retention) is corroborated by the independent academic analysis above.

**Evidence against / streak-break abandonment:** UX literature describes a "what-the-hell effect" where breaking a streak triggers disproportionate abandonment ("I already broke it, why continue") — this is conceptually the same mechanism as the clinically-documented **abstinence violation effect** (see §6) but has not been found as a rigorously measured peer-reviewed statistic specific to learning-app streaks; treat the mechanism as plausible-by-analogy, UNVERIFIED as a quantified learning-app effect. Separately, a caveat worth preserving: streak/usage metrics do not necessarily track actual learning gains (dev.to critique) — usage ≠ mastery.

**Forgiving designs ("never miss twice"):** Popularized by James Clear (*Atomic Habits*, 2018) as a heuristic, not an RCT finding — UNVERIFIED as tested science, but directionally consistent with Lally et al. (2010, see §6), which found a single missed opportunity did not significantly disrupt the habit-automaticity growth curve.

**Design implication:** Use streak-like continuity feedback if at all, but implement structural forgiveness (streak-freeze, grace windows, "never miss twice" framing) rather than hard resets — the loss-aversion engagement lever is real-ish but the catastrophic-abandonment-on-break risk it creates is the bigger danger for a learner whose explicit past failure mode is "nothing pulled them back."

Sources: [Academic analysis of Duolingo streak](https://www.researchgate.net/publication/321123886_An_Analysis_of_Winning_Streak's_Effects_in_Language_Course_of_Duolingo) · [Streak loss-aversion mechanics (industry)](https://trophy.so/blog/the-psychology-of-streaks-how-sylvi-weaponized-duolingos-best-feature-against-them) · [Duolingo streak wager retention claims (industry, unverified)](https://www.justanotherpm.com/blog/the-psychology-behind-duolingos-streak-feature) · [Usage ≠ learning caveat](https://dev.to/pocket_linguist/why-duolingos-gamification-works-and-when-it-doesnt-1d4) · ["Never miss twice" explainer](https://habitdex.com/methods/never-miss-twice)

---

## 6. Habit formation for irregular behaviors

**Lally, P., van Jaarsveld, C.H.M., Potts, H.W.W. & Wardle, J. (2010).** "How are habits formed: Modelling habit formation in the real world." *European Journal of Social Psychology*, 40(6), 998–1009. 96 volunteers performed a self-chosen behavior daily in a consistent context for 12 weeks; automaticity (self-report habit index) grew along an asymptotic curve, reaching plateau at a median of 66 days but with wide individual range (18–254 days in underlying data); missing a single occasion did not materially harm the automaticity trajectory.

**Wendy Wood's work:** ~43% of daily behavior is habitual — repeated in a stable context, executed with minimal conscious decision-making (Wood & Neal, 2007, "A New Look at Habits and the Habit-Goal Interface," *Psychological Review*; Wood, 2019, *Good Habits, Bad Habits*). Three required ingredients: context cue, repetition, reward. **Boundary condition directly relevant here:** Wood's model depends on a *stable external context cue* (same time/place/preceding action) — this is a poor fit for an energy-driven, cadence-free learner, since there is no reliable external cue to attach to. UNVERIFIED extension: substituting an internal/state cue ("when I feel mentally restless or want a puzzle") for an external one is plausible but not something Wood's paradigm directly tested.

**Gollwitzer, P.M. (1999).** "Implementation intentions: Strong effects of simple plans." *American Psychologist*, 54(7), 493–503. **Meta-analysis:** Gollwitzer, P.M. & Sheeran, P. (2006), *Advances in Experimental Social Psychology*, 38, 69–119: across 94 independent studies (8,000+ participants), if-then plans ("if situation X arises, I will do Y") produced a medium-to-large effect on goal attainment, d = 0.65 (95% CI 0.6–0.7).

**Replication status: STRONG.** This is one of the more robust findings in social psychology, reported to be robust to publication-bias correction and to have survived the post-2015 replication crisis better than most social-priming-adjacent literatures.

**Re-entry after a lapse / relapse prevention:** Marlatt & Gordon's relapse-prevention model (clinical, substance-use literature) distinguishes a *lapse* (single slip) from *relapse* (full return/abandonment); progression from lapse to relapse is not automatic but is driven by the **abstinence violation effect (AVE)** — internal attribution of blame, reduced self-efficacy, and guilt following the lapse. This maps directly onto "missed a study session → spiral of quitting."

**Design implication:** Because cadence is irregular and energy-driven, don't design around a fixed-time/place habit cue (Wood's model doesn't fit); instead use a Gollwitzer-style implementation intention keyed to an internal state ("when I want a mental puzzle, I open this") as the most evidence-backed lever available, and explicitly engineer re-entry after any gap to avoid an AVE-style spiral — no guilt messaging, no reset penalty, resume exactly where the learner left off.

Sources: [Lally et al. 2010 (Semantic Scholar)](https://www.semanticscholar.org/paper/How-are-habits-formed:-Modelling-habit-formation-in-Lally-Jaarsveld/c1104763806894bd668e3bf09b93669acaaf31d3) · [BPS Research Digest summary](https://www.bps.org.uk/research-digest/how-form-habit) · [Wood & Neal 2007 (USC PDF)](https://dornsife.usc.edu/wendy-wood/wp-content/uploads/sites/183/2023/10/wood.neal_.2007psychrev_a_new_look_at_habits_and_the_interface_between_habits_and_goals.pdf) · [Good Habits, Bad Habits overview](https://dornsife.usc.edu/wendy-wood/good-habits-bad-habits/) · [Gollwitzer & Sheeran 2006 meta-analysis summary](https://goalsandprogress.com/implementation-intentions-gollwitzer-how-to/) · [Relapse Prevention: Marlatt's model overview (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6760427/) · [Abstinence violation effect](https://www.psychologytoday.com/us/blog/stigma-addiction-and-mental-health/202309/the-abstinence-violation-effect-and-overcoming-it)

---

## 7. Variable reward and its ethics in learning products

**Mechanism:** Variable-ratio reinforcement schedules (Skinner) produce the highest resistance-to-extinction of any reinforcement schedule; anticipation of an unpredictable reward triggers dopaminergic activity independent of the reward's delivery. Widely used in app design (loot chests, shuffled leaderboards, streak-freeze drops).

**Engagement vs. compulsion:** The literature distinction (industry/UX commentary, not a single canonical experimental citation) is that *engagement* aligns with a user's own volitional goals (maps onto SDT autonomy, §1) while *compulsion* persists against the user's own stated preference or despite reduced enjoyment — i.e., a hijacked variable-reward loop rather than an intrinsically rewarding activity. No peer-reviewed "ethics of variable reward in learning products" literature was found in this search; this section is UNVERIFIED as a rigorous empirical literature and should be treated as applied ethics reasoning built on well-established reinforcement-schedule science, not as its own replicated research base.

**Design implication:** If variable reward is used at all, tie the unpredictability to the *mathematical content itself* (the genuine unpredictability of when an insight/unification moment will land is intrinsic and honest) rather than to extrinsic loot mechanics (XP chests, streak-freeze drops) bolted onto the app shell — this preserves the dopaminergic pull of variability without the SDT-autonomy and compulsion risk of manufactured, extrinsic variable rewards.

Sources: [Variable rewards in product design](https://www.appcues.com/blog/variable-rewards) · [Compulsion loop](https://en.wikipedia.org/wiki/Compulsion_loop) · [Reinforcement Schedule in the Digital Age (ResearchGate)](https://www.researchgate.net/publication/395115230_Reinforcement_Schedule_in_the_Digital_Age)

---

## 8. Difficulty and motivation

**The 85% rule:** Wilson, R.C., Shenhav, A., Straccia, M. & Cohen, J.D. (2019). "The Eighty Five Percent Rule for optimal learning." *Nature Communications*, 10, 4646. Mathematically derived (for gradient-descent-style learning algorithms) and empirically shown in artificial neural networks and some biologically-inspired/perceptual-learning models: training is fastest when the error rate is held near ~15.87% (i.e., ~85% success). **Scope:** derived and validated primarily for simple, binary-decision perceptual/classification learning paradigms. **UNVERIFIED** whether it extends to complex, multi-step problem-solving like linear-algebra proofs — the authors' own scope is narrower than the popularized "85% rule for all learning" claim.

**Attribution theory & learned helplessness:** Dweck's early experimental work (1970s, e.g. Dweck, 1975, *Journal of Personality and Social Psychology*) showed children trained to attribute failures to insufficient effort (rather than low ability) persisted more after setbacks than those given only success experiences — a direct, specific, well-targeted experimental result (small/old samples by current standards, but foundational and frequently replicated conceptually in later attribution-retraining studies).

**Mindset research — replication caveat:** Sisk, V.F., Burgoyne, A.P., Sun, J., Butler, J.L. & Macnamara, B.N. (2018). *Psychological Science*. Two meta-analyses: (1) mindset–achievement correlation across ~365,000 students, r ≈ 0.10 (~1% variance explained); (2) growth-mindset intervention effect across 43 studies/~57,000 students, d ≈ 0.08 overall — small, and meaningfully larger only for academically at-risk or low-SES subgroups. Publication-bias-corrected estimates (Macnamara & Burgoyne, 2022) were smaller still. **Replication status: CONTESTED/weak** — the popularized "growth mindset" messaging intervention is a much weaker lever than its public reputation suggests, though the narrower, older effort-attribution mechanism (Dweck, 1975) that it grew out of has more specific support.

**Design implication:** Target an adaptive ~80–85% success rate on exercises as a starting heuristic, but instrument and validate it directly for this domain rather than trusting the generalization from simple classification tasks; when giving failure feedback, use Dweck's specific, better-supported mechanism (attribute the miss to strategy/effort/approach, not ability) rather than generic growth-mindset affirmations, which meta-analytically move the needle very little on their own.

Sources: [Wilson et al. 2019 — ScienceDaily summary](https://www.sciencedaily.com/releases/2019/11/191105113457.htm) · [Wilson et al. 2019 (Princeton record)](https://collaborate.princeton.edu/en/publications/the-eighty-five-percent-rule-for-optimal-learning/) · [Sisk et al. 2018 PDF](https://englelab.gatech.edu/articles/2018/Sisk,%20Burgoyne%20et%20al.%20(2018)%20-%20Mindset%20and%20Academic%20Achievement.pdf) · [Growth mindset replication critique](https://atticusli.com/replication-crisis/growth-mindset/) · [Learned helplessness / attribution retraining overview](https://en.wikipedia.org/wiki/Learned_helplessness)

---

## 9. Recent (2023–2026) empirical work on engagement with AI tutors / conversational learning agents

**Mixed, early-stage evidence.** A 2025 study of conversational-AI-supported problem-solving reported longer sessions and improved performance scores with conversational AI support (Springer, "Student engagement patterns in conversational AI tutoring: evidence from physics problem-solving"); other work reports engagement gains in EFL/self-regulated-learning contexts (Springer, 2025). Conversely, a longitudinal study of LLM chatbot use in self-regulated learning found that, despite generally positive student attitudes, chatbot use **did not predict performance outcomes** (ASEE PEER conference paper, "Help or Hype? Exploring LLM-based Chatbots in Self-Regulated Learning") — a direct contradiction of the "engagement = learning" assumption.

**Retention/attrition:** A rigorous preprint (Handling Students Dropouts in an LLM-driven Interactive Online Course Using Language Models, arXiv:2508.17310, 2025) predicted dropout from interaction-log text with up to 95.4% accuracy and deployed a personalized, LLM-generated outreach/re-engagement intervention to 3,000+ students, reporting re-engagement of at-risk learners — a concrete, reasonably rigorous causal lever (proactive personalized outreach reduces dropout) rather than a passive design feature.

**UNVERIFIED (industry, not peer-reviewed):** Secondary blog/consulting sources claim recurring patterns across current AI-tutor products — thin LLM-wrapper tutors with no mastery model reportedly show day-30 retention under 12%, versus 38% when a mastery model and pedagogical strategy are added. These specific figures could not be traced to a peer-reviewed source and should be treated as an anecdotal industry pattern to validate independently, not an established empirical finding.

**Design implication:** Treat "engagement" and "learning" as separate metrics to track, since at least one longitudinal study found no relationship between chatbot engagement and performance; build a visible mastery/progress model (the one structural feature repeatedly implicated, even if only in industry anecdote, in the difference between collapsing and durable AI-tutor retention); and consider a proactive, personalized re-engagement message after a detected lapse, the one 2025 mechanism with reasonably rigorous (if preprint-stage) evidence of reducing dropout.

Sources: [Conversational AI tutoring engagement, physics (Springer 2025)](https://link.springer.com/article/10.1007/s10639-026-14154-2) · [EFL self-regulated learning + retention (Springer 2025)](https://link.springer.com/article/10.1007/s10639-025-13602-9) · [Help or Hype? chatbots + SRL, null performance result](https://peer.asee.org/help-or-hype-exploring-llm-based-chatbots-in-self-regulated-learning) · [LLM-driven dropout prediction + re-engagement, arXiv:2508.17310](https://arxiv.org/pdf/2508.17310) · [Systematic review calling for more longitudinal LLM-in-education research](https://www.sciencedirect.com/science/article/pii/S2666920X25001699)

---

## Design implications (ranked by strength of evidence)

1. **[strong]** Implementation intentions ("if-then" plans) reliably improve follow-through, d = 0.65 across 94 studies (Gollwitzer & Sheeran 2006) — give the learner an explicit trigger-action plan ("when I want a puzzle, I open this"), not a generic time-based reminder.
2. **[strong]** Extrinsic, completion-contingent rewards measurably undermine intrinsic motivation for tasks already found interesting (Deci, Koestner & Ryan 1999, d ≈ −0.28 to −0.40) — do not bolt badges/points onto the puzzle-solving itself; let the math be the reward.
3. **[strong]** A single missed session does not disrupt habit-formation trajectories (Lally et al. 2010) — make re-entry after a gap completely frictionless and judgment-free; never penalize a lapse.
4. **[moderate]** Curiosity peaks with partial knowledge and measurably enhances memory encoding of what follows (Loewenstein 1994; Kidd & Hayden 2015; Gruber et al. 2014) — frame each problem as a near-closable gap, and place the "reveal" right after the itch peaks.
5. **[moderate]** Difficulty held near ~80–85% success sustains fastest learning in simple training paradigms (Wilson et al. 2019) — use as an adaptive-difficulty starting heuristic, but validate directly since the paradigm's scope (binary classification) is narrower than multi-step proof-style problems.
6. **[moderate]** Autonomy-supportive design (real choice over path/pace) correlates with better need-satisfaction and motivation in education meta-analyses (2024 SDT-education meta-analysis) — let the learner choose what to tackle next rather than imposing a fixed sequence.
7. **[moderate, contested mechanism]** Streak/loss-aversion mechanics raise short-term retention but the same mechanism risks catastrophic all-or-nothing abandonment on break — if used, pair with structural forgiveness (streak-freeze, "never miss twice" framing), never a hard reset.
8. **[weak/contested]** Flow's precise challenge-skill balance does not reliably predict the flow state itself — invest in adaptive difficulty and immediate feedback (the levers that do hold up) rather than engineering toward an exact ratio.
9. **[contested]** Generic growth-mindset messaging has a near-zero average effect on achievement (Sisk et al. 2018, d ≈ 0.08) — use Dweck's narrower, older effort/strategy-attribution mechanism in failure feedback instead of "you can learn this!" affirmations.
10. **[contested/largely debunked]** The Zeigarnik claim that unfinished tasks are remembered better essentially fails to replicate (2025 meta-analysis, ratio ≈ 0.99) — do not design around "memory via incompleteness"; use the better-supported Ovsiankina resumption urge instead (end sessions mid-problem to create a pull to return, not a memory boost).
11. **[weak/unverified]** "Never miss twice" is a popular heuristic (James Clear), not an RCT-tested finding, though directionally consistent with Lally et al.'s single-lapse-tolerance result — safe as UX framing, should not be cited as proven science.
12. **[weak/unverified]** Current AI-tutor products reportedly show day-30 retention collapsing without a visible mastery model (industry-reported, not peer-reviewed) — treat as a hypothesis to test with this product's own telemetry, alongside the one reasonably rigorous 2025 finding that personalized post-lapse outreach reduces dropout.
