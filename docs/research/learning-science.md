# Learning-science foundations for a commit → break → repair sparring-partner mechanic

Context: adult relearner, half-forgotten linear algebra, irregular sessions, goal = general mathematical maturity. Mechanic: learner commits to a prediction → prediction is broken by simulation/counterexample → concept introduced as repair.

---

## 1. Desirable difficulties (Bjork & Bjork)

**Citation:** Bjork, E. L., & Bjork, R. A. (2011). Making things hard on yourself, but in a good way: Creating desirable difficulties to enhance learning. In M. A. Gernsbacher, R. W. Pew, L. M. Hough, & J. R. Pomerantz (Eds.), *Psychology and the Real World* (pp. 56–64). Worth Publishers. (Builds on R. A. Bjork, 1994, "Memory and metamemory considerations in the training of human beings," in Metcalfe & Shimamura, *Metacognition*, MIT Press.)

**Effect:** Conditions that slow acquisition and increase errors during learning (spacing, interleaving, testing, varied conditions of practice) can nonetheless produce superior long-term retention and transfer, because they engage the same retrieval/reconstruction processes needed later. "Desirable" is conditional, not intrinsic.

**Boundary conditions / moderators:** The Bjorks are explicit that a difficulty is desirable only if (a) the learner has enough prior knowledge/resources to productively engage with it, and (b) it is introduced at a level and timing matched to the learner — otherwise it becomes merely "undesirable difficulty" (confusion, disengagement) with no compensating retention benefit. This is a theoretical framework/umbrella term, not itself a single tested hypothesis — its empirical support rests on the component effects below (spacing, testing, interleaving, generation).

**Replication status (2026):** The umbrella concept is not "replicated" per se since it's an organizing framework; its component phenomena have mixed replication records (strong: testing effect, spacing; moderate: interleaving in math; contested: desirable-difficulty framing applied broadly to self-regulated/online learning, where several studies find the predicted difficulty manipulations fail to help or actively hurt low-prior-knowledge or low-motivation learners).

**Bearing on mechanic:** Directly frames the whole design: the "break" is only desirable if the learner has enough schema to notice the break and reconstruct from it — this is the single biggest risk in the spec (see dosage/assistance-dilemma below).

Sources: [structural-learning.com summary](https://www.structural-learning.com/post/robert-bjork-teachers-guide-desirable), [ResearchGate PDF](https://www.researchgate.net/publication/284097727_Making_things_hard_on_yourself_but_in_a_good_way_Creating_desirable_difficulties_to_enhance_learning)

---

## 2. Productive failure (Kapur) and Sinha & Kapur 2021 meta-analysis

**Citation (meta-analysis):** Sinha, T., & Kapur, M. (2021). When problem solving followed by instruction works: Evidence for productive failure. *Review of Educational Research*, 91(5), 761–798. DOI: 10.3102/00346543211019105. (Foundational: Kapur, M. (2008). Productive failure. *Cognition and Instruction*, 26(3), 379–424; Kapur, M. (2010, 2012, 2014) design-principle papers.)

**Effect:** Across 53 studies / 166 comparisons / >12,000 participants, having students attempt (unsuccessful) problem-solving *before* explicit instruction produced better conceptual understanding and transfer than instruction-first sequencing (Cohen's d = 0.36, 95% CI [0.20, 0.51]), with no cost to procedural fluency. Effect is specifically for the "problem-solving-then-instruction" sequence, not failure/struggle in general.

**Design principles of a productive-failure activity (Kapur):** (1) activate and differentiate relevant prior knowledge against the target concept; (2) draw attention to critical features/sub-goals of the target concept (even though students can't yet solve correctly); (3) explicit instruction afterward explains and elaborates those features, contrasting students' generated (failed) solutions with the canonical one; (4) consolidate/assemble the differentiated features into the correct concept. Critically, the design requires the *comparison and explicit instruction* step — failure alone, without the targeted follow-up instruction, is not sufficient and in several studies is harmful.

**Boundary conditions / moderators:** Benefit emerges mainly for conceptual understanding/transfer measures, not immediate procedural performance (where instruction-first can win short-term). Requires: well-designed problems that are "solvable enough" to generate partial/incorrect-but-relevant solutions (not impossible or trivial), and a knowledgeable instructor/agent who can do the comparison-and-consolidation step well. Sinha & Kapur report heterogeneity — effect is weaker/absent in some designs, especially when instruction phase fails to explicitly contrast student-generated solutions with the target concept.

**Replication status (2026):** The meta-analysis itself is the replication-status instrument (quantitative synthesis across already-published independent studies) — this is a confirmed, fairly robust effect for well-designed PF activities. However, there is an active counter-literature from cognitive-load-theory researchers (Kalyuga, Likourezos, Sweller) arguing the opposite sequencing (worked examples/instruction first for novices) is superior, with mediational evidence that problem-solving-first imposes extraneous load that can suppress learning — see item 8 and "Weak or contested" below. "When Productive Failure Fails" (Chowrira et al., and other individual studies) documents null/negative replications in specific contexts (e.g., poorly scaffolded online or low-prior-knowledge settings).

**Bearing on mechanic:** This is the closest direct precedent for the full commit→break→repair loop at curriculum-design grain — it validates the *shape* (struggle before being told) but insists the repair step must explicitly contrast the learner's committed prediction against the correct concept, not just reveal the correct concept in isolation.

Sources: [RER (SAGE) abstract](https://journals.sagepub.com/doi/10.3102/00346543211019105), [ERIC EJ1308129](https://eric.ed.gov/?id=EJ1308129), [Kapur & Roll overview PDF](https://boldscience.org/wp-content/uploads/2025/04/Productive-Failure.pdf), [Kapur design principles summary](https://www.manukapur.com/productive-failure/), ["When Productive Failure Fails"](https://www.researchgate.net/publication/333005127_When_Productive_Failure_Fails)

---

## 3. Generation effect (Slamecka & Graf 1978) and its limits

**Citation:** Slamecka, N. J., & Graf, P. (1978). The generation effect: Delineation of a phenomenon. *Journal of Experimental Psychology: Human Learning and Memory*, 4(6), 592–604.

**Effect:** Items self-generated from a cue/rule (e.g., supplying an antonym from the first letter) are recalled/recognized better than the same items simply read. Demonstrated across 5 experiments, cued recall, free recall, recognition.

**Boundary conditions / moderators (its limits):** The effect depends on "generation constraint" and task-processing match (transfer-appropriate processing). A meta-analytic review (Bertsch et al.-type syntheses referenced in later work) finds the effect shrinks or reverses under high generation difficulty/high constraint, for context/source memory (negative generation effect: read > generate for *source* memory even when item memory shows the normal effect), and when the generation task's processing doesn't match what the later test requires. It is primarily an item-memory, single-item-level effect from verbal-learning paradigms — generalization to complex conceptual/procedural material (like deriving a linear-algebra proof) is much thinner and less direct than for word pairs.

**Replication status (2026):** One of the most robustly replicated findings in memory research for its original word-pair paradigm; boundary conditions (negative generation effect, constraint moderators) are an active, still-developing area of theoretical synthesis (e.g., 2020 meta-analytic reviews in *Psychonomic Bulletin & Review*) rather than settled.

**Bearing on mechanic:** Supports asking the learner to generate/commit to a prediction (vs. being shown it) as inherently more memorable encoding — but the boundary conditions warn that if the "commit" step is too unconstrained or mismatched to what's tested later, the expected memory benefit may not transfer to the actual target (the repaired concept).

Sources: [Springer PDF of original](https://link.springer.com/content/pdf/10.3758/BF03198475.pdf), [generation effect meta-analytic review](https://link.springer.com/article/10.3758/s13423-020-01762-3), [Wikipedia overview](https://en.wikipedia.org/wiki/Generation_effect)

---

## 4. Predict-observe-explain (White & Gunstone 1992) and cognitive conflict / conceptual change (Posner et al. 1982); Limón 2001 critique

**Citations:**
- White, R. T., & Gunstone, R. F. (1992). *Probing Understanding*. Falmer Press.
- Posner, G. J., Strike, K. A., Hewson, P. W., & Gertzog, W. A. (1982). Accommodation of a scientific conception: Toward a theory of conceptual change. *Science Education*, 66(2), 211–227.
- Limón, M. (2001). On the cognitive conflict as an instructional strategy for conceptual change: A critical appraisal. *Learning and Instruction*, 11(4–5), 357–380.

**Effect:** POE is a three-step instructional technique (predict an outcome and justify it; observe what actually happens; explain any discrepancy) used to surface and confront students' prior conceptions. Posner et al.'s model specifies four necessary conditions for conceptual change: dissatisfaction with existing conception, the new conception must be intelligible, initially plausible, and fruitful/extendable.

**Boundary conditions / moderators / critique:** Limón's critical appraisal (and subsequent literature, e.g., Chinn & Brewer, Dole & Sinatra) argues that *cognitive conflict alone is frequently insufficient* to produce durable conceptual change: learners can experience the anomaly as discrepant, dismiss or compartmentalize it, misattribute the anomaly to error, or exhibit "status" change at a surface/verbal level without deep restructuring. Limón identifies both theoretical gaps (conflict is underspecified — how much, what counts as "dissatisfaction") and practical/methodological problems (many studies don't verify students actually experienced conflict, vs. assuming the instructional manipulation produced it). Motivational/affective and epistemological factors (students' views of knowledge, social context) moderate whether conflict triggers accommodation vs. avoidance.

**Replication status (2026):** POE as a technique is widely used and has many positive but largely small-sample, single-study demonstrations across science-education venues (chemistry, physics); it has not been subjected to a quantitative meta-analysis on the scale of Sinha & Kapur. The core theoretical critique (conflict-alone is necessary-not-sufficient) is broadly accepted in the conceptual-change literature as of the most recent reviews and essentially unchallenged — this is a consensus critique, not a contested one.

**Bearing on mechanic:** This is the most important cautionary citation for the design: "break the prediction" (the conflict) is necessary but Posner/Limón jointly imply it is not sufficient — the repair step must actively make the new concept intelligible, plausible, and fruitful, or the learner will explain away the break rather than restructure.

Sources: [POE overview, arbs.nzcer.org.nz](https://arbs.nzcer.org.nz/predict-observe-explain-poe), [Posner et al. citation record](https://sedl.org/pubs/pic02/picbib-output.cgi?searchuniqueid=51), [Limón 2001 PDF](https://sbnec.org.br/gene/Limon%202001.pdf), [ERIC EJ636384](https://eric.ed.gov/?id=EJ636384)

---

## 5. Hypercorrection effect (Butterfield & Metcalfe 2001)

**Citation:** Butterfield, B., & Metcalfe, J. (2001). Errors committed with high confidence are hypercorrected. *Journal of Experimental Psychology: Learning, Memory, and Cognition*, 27(6), 1491–1494. (Extension: Butterfield, B., & Metcalfe, J. (2006). The correction of errors committed with high confidence. *Metacognition and Learning*.)

**Effect:** When learners answer confidently and incorrectly, and then receive corrective feedback, that error is *more* likely to be corrected (remembered correctly later) than a low-confidence error — counter to the naive assumption that confident errors are entrenched misconceptions resistant to correction. The surprise/mismatch between confident belief and feedback appears to drive deeper encoding of the correction.

**Boundary conditions / moderators:** Requires (a) a genuine, explicit confidence judgment prior to feedback, and (b) clear corrective feedback. Butler et al. (2011) found the hypercorrection effect persists over a week, but high-confidence errors show some tendency to "return" (regress) at longer delays relative to immediately-tested gains — i.e., the benefit is robust but not unconditionally permanent. Later studies show it generalizes across populations (children, classroom settings) and modalities but can interact with whether the original error is a genuine misconception vs. a careless slip.

**Replication status (2026):** Very high — described in the literature itself as "a highly replicable phenomenon... independently observed... by several different research groups" (young adults, immediate/delayed testing, multiple-choice, children, classroom settings, fMRI delayed-feedback variants). I found no formal multi-lab Registered Replication Report specifically for this effect, but convergent independent replications across many labs and paradigms over two decades constitute strong replication evidence by the standards of this literature. Mark as **verified, strongly replicated, but without a single large-scale RRR** (that specific claim is UNVERIFIED).

**Bearing on mechanic:** This is the single strongest direct empirical anchor for "commit before break": the mechanism only works if the learner commits with genuine confidence first — a tentative or hedged prediction will not produce the hypercorrection benefit when it's broken.

Sources: [JEP:LMC 2001 study summary](http://www.columbia.edu/cu/psychology/metcalfe/PDFs/Butterfield_Metcalfe_2006.pdf), [Butler et al. 2011, persists over a week](https://link.springer.com/article/10.3758/s13423-011-0173-y), [ResearchGate replication discussion](https://www.researchgate.net/publication/11641193_Errors_Committed_with_High_Confidence_Are_Hypercorrected), [classroom replication](https://www.researchgate.net/publication/325252938_Hypercorrection_of_high-confidence_errors_in_the_classroom)

---

## 6. Testing effect / retrieval practice (Roediger & Karpicke 2006) and pretesting / errorful generation (Kornell, Hays & Bjork 2009; Richland, Kornell & Kao 2009)

**Citations:**
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science*, 17(3), 249–255 (companion theoretical piece same year in *Perspectives on Psychological Science*).
- Kornell, N., Hays, M. J., & Bjork, R. A. (2009). Unsuccessful retrieval attempts enhance subsequent learning. *Journal of Experimental Psychology: Learning, Memory, and Cognition*, 35(4), 989–998.
- Richland, L. E., Kornell, N., & Kao, L. S. (2009). The pretesting effect: Do unsuccessful retrieval attempts enhance learning? *Journal of Experimental Psychology: Applied*, 15(3), 243–257.

**Effect:** Practicing retrieval (being tested) produces more durable long-term retention than equivalent restudy time, even though restudy often *feels* more effective and can win on immediate tests (Roediger & Karpicke's classic dissociation: repeated study wins at 5 min, repeated testing wins at 1 week — 61% vs 40% retention). Kornell/Hays/Bjork and Richland/Kornell/Kao show that even *failed* retrieval attempts (guessing before being told the answer), provided feedback follows, enhance later learning more than simply studying the material — an "errorful generation"/pretesting benefit.

**Boundary conditions / moderators:** The pretesting/errorful-generation benefit is conditional on feedback being given afterward — unsuccessful retrieval without feedback does not reliably help and can entrench the error. Richland et al. found the benefit is specific to the pretested material (doesn't transfer to non-pretested content). The testing effect itself is moderated by test format (recall > recognition for subsequent benefit), delay before final test (benefit grows with longer retention intervals), and whether corrective feedback accompanies retrieval practice.

**Replication status (2026):** Among the most replicated effects in cognitive/educational psychology; it survived the 2010s replication-crisis scrutiny well and is a cornerstone of "Make It Stick"-style evidence-based study guidance. Pretesting/errorful-generation is somewhat newer and more actively studied (still generating new boundary-condition papers through 2023–2025, e.g., "metacognitive awareness of the pretesting effect"), but the core finding (feedback-contingent benefit of failed retrieval) is well-replicated, not contested.

**Bearing on mechanic:** Directly underwrites the "commit to a prediction" step as a form of pretesting/errorful generation — the design's break-then-repair structure is essentially Richland/Kornell/Kao's paradigm scaled up to conceptual math content, with the critical design requirement (confirmed by this literature) that the repair step must function as unambiguous corrective feedback.

Sources: [Roediger & Karpicke PDF](https://colinallen.dnsalias.org/Readings/2006_Roediger_Karpicke_PsychSci.pdf), [Kornell Hays Bjork 2009 PDF](https://web.williams.edu/Psychology/Faculty/Kornell/Publications/Kornell.Hays.Bjork.2009.pdf), [pretesting effect overview](https://www.structural-learning.com/post/pretesting-effect-testing-before-teaching), [2023 pretesting metacognition follow-up](https://sc-pan.github.io/pdf/PR_2023.pdf)

---

## 7. Spacing and interleaving (Cepeda et al. 2006; Rohrer & Taylor 2007)

**Citations:**
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin*, 132(3), 354–380.
- Rohrer, D., & Taylor, K. (2007). The shuffling of mathematics problems improves learning. *Instructional Science*, 35(6), 481–498.

**Effect:** Cepeda et al.'s meta-analysis (317 experiments, 184 articles) establishes that spaced practice beats massed practice for retention, and critically that the **optimal inter-study interval scales with the desired retention interval** — gaps that are too short *or* too long both underperform an interval tuned to how long you want the material remembered. Rohrer & Taylor show interleaved (shuffled) practice of different math problem-types (e.g., volume-of-shapes problems) produces much better scores on a test one week later than blocked practice, even though interleaving *hurts* performance during practice itself.

**Boundary conditions / moderators:** The Cepeda et al. ISI-scales-with-retention-interval finding is itself the boundary condition — there is no universally "best" gap; the right spacing depends on how long retention needs to last. Rohrer & Taylor's interleaving benefit is specifically about discriminating between problem types (requiring the learner to first identify which procedure applies) — it is weaker or absent when problems are not genuinely confusable, and it reliably *costs* immediate/practice-session performance, which is a known adoption barrier (misleads learners' fluency judgments).

**Replication status (2026):** Both lines are well-replicated and are foundational, uncontested parts of the evidence-based-learning canon (reconfirmed in later Cepeda et al. 2008 *Psychological Science* follow-up, and numerous Rohrer-lab math-interleaving replications through the 2010s, including multi-year classroom field studies).

**Bearing on mechanic:** For irregular session gaps specifically: Cepeda et al.'s ISI-retention-interval scaling implies irregular (learner-driven, sometimes long) gaps are not necessarily bad — if anything, longer natural gaps may better match long-horizon retention goals than a rigid daily schedule would — but the system should track elapsed time and resurface/interleave prior concepts' predictions rather than only ever introducing new ones, since blocked single-topic sessions forgo the interleaving benefit.

Sources: [Cepeda et al. 2006 synthesis](https://www.yorku.ca/ncepeda/publications/CPVWR2006.html), [Rohrer & Taylor shuffling paper](https://digitalcommons.usf.edu/psy_facpub/1767/), [interleaved practice follow-up](http://uweb.cas.usf.edu/~drohrer/pdfs/Taylor&Rohrer2010ACP.pdf)

---

## 8. Worked examples and the expertise reversal effect (Sweller; Kalyuga 2003/2007)

**Citation:** Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist*, 38(1), 23–31. (Also: Kalyuga, S. (2007). Expertise reversal effect and its implications for learner-tailored instruction. *Educational Psychology Review*, 19(4), 509–539.)

**Effect:** Worked examples (full step-by-step solutions studied rather than attempted) strongly help novices by reducing extraneous cognitive load — but the same scaffolding that helps novices measurably *hurts* learners with higher prior knowledge in the same domain, who do better with unguided or minimally-guided problem solving. The crossover ("reversal") was demonstrated with electrical-trade apprentices reading wiring diagrams (integrated vs. separated text/diagram format helped novices, hurt advanced apprentices) and replicates the general cognitive-load pattern (redundancy effect, split-attention effect) reversing sign with expertise.

**Boundary conditions / moderators:** The reversal point is domain- and task-specific prior knowledge, not generic "smartness" or overall experience — it's about whether the learner already has a schema that makes the worked example's guidance redundant (and thus merely effortful/boring/distracting) rather than informative. For a given learner, expertise reversal effects can appear mid-course as a single topic's instruction progresses from novice to developing competence, meaning fixed scaffolding levels are inherently mistimed for at least part of any learning trajectory.

**Replication status (2026):** Well-replicated as a general phenomenon across multiple content domains (electrical apprenticeships, language learning, mathematics) since the early 2000s; it remains one of the most-cited, least-contested findings from cognitive load theory. It is, however, in direct theoretical tension with productive failure (item 2) — Kalyuga/Likourezos-style mediational work argues problem-solving-first imposes extraneous load that specifically disadvantages novices, which is the opposite sequencing recommendation from Sinha & Kapur for the same novice population. This is an unresolved theoretical disagreement in the field, not a case where one side has been debunked.

**Bearing on mechanic:** Most load-bearing citation for "the learner quits when things are too slow" — expertise reversal predicts that an adult *relearner* with half-forgotten but real prior exposure sits in a genuinely ambiguous zone: too much scaffolding before the break (e.g., heavy hand-holding toward the prediction) may bore/frustrate them exactly because fragments of real prior knowledge make the scaffolding redundant, while too little may leave true novicelike gaps unaddressed — the system needs per-concept, not per-learner, calibration of how much guidance precedes the commit step.

Sources: [Kalyuga et al. 2003 reference record](https://www.scirp.org/reference/ReferencesPapers?ReferenceID=747628), [Expertise reversal effect, Wikipedia](https://en.wikipedia.org/wiki/Expertise_reversal_effect), [Kalyuga 2007 implications overview](https://theelearningcoach.com/learning/novice-versus-expert-design-strategies/), [productive-failure vs CLT mediational critique](https://link.springer.com/article/10.1007/s11251-016-9399-4)

---

## 9. Self-explanation (Chi et al. 1989, 1994) and illusion of explanatory depth (Rozenblit & Keil 2002)

**Citations:**
- Chi, M. T. H., Bassok, M., Lewis, M. W., Reimann, P., & Glaser, R. (1989). Self-explanations: How students study and use examples in learning to solve problems. *Cognitive Science*, 13(2), 145–182.
- Chi, M. T. H., de Leeuw, N., Chiu, M.-H., & LaVancher, C. (1994). Eliciting self-explanations improves understanding. *Cognitive Science*, 18(3), 439–477.
- Rozenblit, L., & Keil, F. (2002). The misunderstood limits of folk science: An illusion of explanatory depth. *Cognitive Science*, 26(5), 521–562.

**Effect:** Chi et al. 1989: among 8 college students studying worked physics examples, the 4 who spontaneously generated far more self-explanations while studying (15.3/example vs 2.8/example) scored much higher on a later problem-solving posttest (82% vs 46%) — self-explanation quality/quantity, not just time-on-task, predicts learning from examples. Chi et al. 1994 shows this is causal and trainable: prompting 8th-graders to self-explain a biology text (vs. simply re-reading) produced significantly greater understanding, especially for students who generated many explanations. Rozenblit & Keil: people systematically overrate how well they understand mechanistic/causal systems (e.g., zippers, toilets) until forced to produce a detailed causal explanation, at which point their self-rated understanding drops sharply — the "illusion of explanatory depth" (IOED). IOED is specific to explanatory/mechanistic knowledge; it does not apply to facts, procedures, or narratives.

**Boundary conditions / moderators:** Self-explanation's benefit is driven specifically by generating *explanatory* inferences (connecting steps to underlying principles), not by any verbalization — paraphrasing/restating without inference adds little. IOED is most pronounced for complex causal-mechanical systems and is reduced for knowledge people have genuinely engaged with generatively before (consistent with generation-effect themes above).

**Replication status (2026):** Both self-explanation effects are long-standing, highly cited, and broadly replicated across domains (physics, biology, more recently mathematics/vector calculus self-explanation studies); meta-analytic work (e.g., Bisra et al.) confirms a reliable moderate effect of self-explanation prompts. IOED is also well replicated as a general phenomenon, though its magnitude and exact boundary conditions (which types of knowledge show it, developmental onset) are still being refined in ongoing work through the 2010s–2020s.

**Bearing on mechanic:** Doubly relevant: self-explanation findings argue the repair step should require the learner to explain *why* their prediction broke (not just observe that it did) for the benefit to materialize; IOED argues that eliciting an explicit prediction with justification *before* the break is itself a mechanism for puncturing false confidence about linear-algebra intuitions the learner has quietly been overrating.

Sources: [Chi et al. 1989 self-explanation summary](https://education.asu.edu/sites/g/files/litvpz656/files/lcl/instruction_based_on_self_explanation.pdf), [Chi et al. 1994, Wiley](https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1803_3), [Rozenblit & Keil, Wikipedia](https://en.wikipedia.org/wiki/Illusion_of_explanatory_depth), [IOED original study discussion](https://thedecisionlab.com/biases/the-illusion-of-explanatory-depth)

---

## 10. Multiple external representations: Ainsworth's DeFT framework (2006)

**Citation:** Ainsworth, S. (2006). DeFT: A conceptual framework for considering learning with multiple representations. *Learning and Instruction*, 16(3), 183–198.

**Effect:** DeFT (Design, Functions, Tasks) is a framework, not a single tested effect — it organizes when/why multiple external representations (e.g., matrix notation, geometric vector picture, system-of-equations form) help learning via three complementary **functions**: (1) complementary roles (different representations support different processes or contain different information), (2) constraining interpretation (a familiar representation constrains misinterpretation of an unfamiliar one), (3) constructing deeper understanding (abstraction/relating across representations). It also specifies **design parameters** (number of representations, how information is distributed across them, representation format/modality, sequencing, and translation support) that determine whether multiple representations help or overload.

**Boundary conditions / moderators (help vs. overload):** The framework's core caution is that multiple representations impose their own learning burden — the learner must learn to interpret each representation *and* learn to translate between them, which is a documented source of extraneous cognitive load if representations are introduced simultaneously without translation support, especially for novices who haven't yet mastered any single representation. Benefit is contingent on adequate sequencing/scaffolding of translation (e.g., introduce representations one at a time, with explicit mapping prompts) rather than simultaneous presentation.

**Replication status (2026):** As a conceptual framework it's not "replicated" in the effect-size sense, but it is the standard citation (highly cited, ~2,000+ citations) organizing a large empirical literature; the overload risk it predicts is independently supported by cognitive-load-theory split-attention/redundancy findings (see item 8), and recent (2020s) registered-report-style work on "concreteness fading" (e.g., Lichtenberger et al. 2024 in physics) is actively testing sequencing predictions the framework makes, with mixed-to-positive results for fading over simultaneous presentation.

**Bearing on mechanic:** Linear algebra is a canonical multiple-representation domain (symbolic/matrix, geometric/vector, systems-of-equations) — DeFT implies the commit-break-repair cycle should let the learner predict in one representation and have the break delivered in a *different but already-translated* representation (e.g., predict algebraically, break geometrically) rather than introducing an unfamiliar representation and new content simultaneously.

Sources: [DeFT paper PDF](https://nschwartz.yourweb.csuchico.edu/Ainsworth_2006_Learning-and-Instruction.pdf), [ERIC record](https://eric.ed.gov/?id=EJ737858), [concreteness fading vs simultaneous, 2024](https://onlinelibrary.wiley.com/doi/full/10.1002/tea.21947)

---

## 11. Bloom's 2-sigma (1984) and VanLehn 2011 reassessment

**Citations:**
- Bloom, B. S. (1984). The 2 sigma problem: The search for methods of group instruction as effective as one-to-one tutoring. *Educational Researcher*, 13(6), 4–16.
- VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist*, 46(4), 197–221.

**Effect:** Bloom (reporting on his students Anania and Burke's dissertations) found one-to-one mastery tutoring produced outcomes ~2 standard deviations above conventional classroom instruction (tutored average student outperforms ~98% of classroom-taught students), posing the "2-sigma problem" of finding scalable methods matching tutoring's effect.

**VanLehn's reassessment:** Surveying studies from 1975–2010, VanLehn found the commonly cited belief (adult human tutoring d≈2.0 vs. no-tutoring, ITS d≈1.0) is **not supported** by the actual literature. His meta-analytic estimate for human tutoring vs. no-tutoring control is d≈0.79, and step-based intelligent tutoring systems (that require students to produce intermediate reasoning steps, not just final answers) achieve d≈0.76 — nearly matching human tutors — while answer-based ITS (only final-answer level interaction) only reach d≈0.31.

**Boundary conditions / moderators:** VanLehn's central moderator finding is *interaction granularity*: ITS that engage students at the step level (requiring them to externalize intermediate reasoning, closer to tutoring dialogue) close most of the gap with human tutors; systems that only check final answers do not. This is a direct, mechanism-level argument for why dialogue/step-level engagement (not just answer-checking) is what makes tutoring work.

**Replication status (2026):** Bloom's original 2-sigma figure is now widely understood in the field as an overstated/non-representative effect size based on a small number of studies under optimal mastery-learning conditions, not a robust population parameter — VanLehn's paper is the standard corrective citation and is itself well-established/uncontested as of 2026 (frequently re-cited in the 2020s ITS and LLM-tutoring literature as the benchmark figure). No one has since produced a meta-analysis overturning VanLehn's more modest, better-grounded estimates.

**Bearing on mechanic:** Sets realistic expectations (don't oversell "2 sigma"-scale gains) and gives a concrete design lever: VanLehn's granularity finding implies the sparring partner should require the learner to externalize the predicted step/reasoning (not just a final numeric prediction) before breaking it, since that step-level engagement is specifically what closes the human-tutor gap.

Sources: [Bloom's 2 sigma problem, Wikipedia](https://en.wikipedia.org/wiki/Bloom's_2_sigma_problem), [ERIC EJ303699](https://eric.ed.gov/?id=EJ303699), [VanLehn 2011, Taylor & Francis abstract](https://www.tandfonline.com/doi/abs/10.1080/00461520.2011.611369), [VanLehn 2011 discussion](https://scite.ai/reports/the-relative-effectiveness-of-human-vkdEwJ)

---

## 12. Dosage: assistance dilemma (Koedinger & Aleven 2007) and impasse-driven learning (VanLehn et al. 2003)

**Citations:**
- Koedinger, K. R., & Aleven, V. (2007). Exploring the assistance dilemma in experiments with cognitive tutors. *Educational Psychology Review*, 19(3), 239–264.
- VanLehn, K., Siler, S., Murray, C., Yamauchi, T., & Baggett, W. B. (2003). Why do only some events cause learning during human tutoring? *Cognition and Instruction*, 21(3), 209–249.

**Effect:** Koedinger & Aleven formalize the "assistance dilemma": help/scaffolding trades off between withholding (risking frustration, wasted time, impasses that don't resolve productively) and giving (risking shallow processing, reduced self-generation, lower long-term transfer) — there is no help level that's unconditionally optimal, and their Cognitive Tutor work shows the optimum is reached by an adaptive policy (withhold by default, add hints/feedback only as needed) rather than a fixed dosage. VanLehn et al., analyzing ~125 hours of expert human-tutoring dialogue, found that learning occurred almost exclusively when the student had actually reached an **impasse** (got stuck or detected their own error) — tutorial explanations given absent an impasse rarely produced learning, regardless of explanation quality.

**Boundary conditions / moderators:** Impasse-driven learning implies struggle is necessary but the *type* of struggle matters — a genuine, self-detected impasse (not confusion imposed by a confusing explanation) is the trigger condition. The assistance dilemma implies the right dosage is dynamic and individual/task-specific, not a fixed global parameter — too little help after an impasse leaves students stuck unproductively (thrashing, guessing, disengaging) rather than learning, which is the mechanism by which "too much struggle" becomes counterproductive.

**Replication status (2026):** Both are foundational, frequently-cited (and frequently re-validated) findings within the intelligent-tutoring-systems literature; follow-on Koedinger-lab and others' work through the 2010s–2020s (Hint Factory, data-driven HelpNeed predictors) continues to build on and confirm the core assistance-dilemma framing rather than overturn it. Impasse-driven learning is similarly treated as settled/foundational in ITS design, though it originates from a single (if extensive) tutoring-dialogue corpus rather than a multi-study meta-analysis.

**Bearing on mechanic:** This is the direct answer to "how much break is too much": the break should be sized to produce a genuine, self-detected impasse (not a confusing or overwhelming one), and the repair/assistance that follows should be adaptively minimal — enough to let the learner move past the impasse, not a full re-teaching — to avoid both quitting (too much unresolved struggle) and shallow non-learning (too much given away).

Sources: [ERIC EJ785065](https://eric.ed.gov/?id=EJ785065), [assistance dilemma overview](https://arxiv.org/html/2207.03025), [VanLehn et al. 2003, ERIC EJ675271](https://eric.ed.gov/?id=EJ675271), [VanLehn tutoring effectiveness PDF](https://www.emergingedtech.com/-kvanlehn/Stringent/PDF/EffectivenessOfTutoring_Vanlehn.pdf)

---

## 13. Mathematical maturity / habits of mind (Cuoco, Goldenberg & Mark 1996); linear algebra misconceptions (Dorier, Sierpinska et al.)

**Citations:**
- Cuoco, A., Goldenberg, E. P., & Mark, J. (1996). Habits of mind: An organizing principle for mathematics curricula. *Journal of Mathematical Behavior*, 15(4), 375–402.
- Dorier, J.-L., & Sierpinska, A. (2001). Research into the teaching and learning of linear algebra. In D. Holton (Ed.), *The Teaching and Learning of Mathematics at University Level: An ICMI Study* (pp. 255–273). Kluwer. (Synthesizes Dorier, Sierpinska, and others' earlier 1990s empirical/theoretical work, including the edited volume Dorier (Ed.) (2000), *On the Teaching of Linear Algebra*.)

**Effect / content:** Cuoco, Goldenberg & Mark propose organizing a math curriculum not around topic coverage but around "habits of mind" — the dispositions and modes of thought mathematicians actually use (pattern-sniffing, experimenting, visualizing, conjecturing, tinkering, seeking invariants, generalizing from examples) — arguing that durable mathematical maturity comes from practicing these habits across content rather than from content itself. Dorier & Sierpinska's synthesis identifies linear algebra as a site of specific, well-documented student difficulty: the "formalism obstacle" (students struggle with the sudden shift to axiomatic, highly general, symbol-heavy definitions after more computational earlier math), a pervasive "obstacle of generalization/formalization" where students can compute (e.g., row-reduce) without grasping underlying structural concepts (basis, span, linear independence, subspace), and a documented tendency to fall back on purely algorithmic/computational engagement that masks absence of conceptual (geometric/structural) understanding.

**Boundary conditions / moderators:** The Dorier/Sierpinska literature is specifically about students coming from a procedural/computational prior background (e.g., a first course heavy on Gaussian elimination and determinant computation) encountering the more abstract/axiomatic treatment later — which closely matches the target learner's profile (half-forgotten first course). The "habits of mind" framework is a curricular philosophy backed by extensive case studies and widespread adoption (e.g., the CME Project curriculum) rather than a single controlled-outcome study with an effect size.

**Replication status (2026):** Both are foundational/canonical within their sub-fields (math-education curriculum theory; RUME/linear-algebra-education research) and remain actively cited and extended (e.g., ongoing RUME conference work through the 2020s on span/basis/linear-independence misconceptions, Possani/Stewart/Thomas-style APOS-theory studies of linear algebra). Neither is the kind of claim subject to "replication" in the experimental-psychology sense; their status is closer to "well-established descriptive/theoretical consensus, repeatedly corroborated by independent case studies" — UNVERIFIED as a numeric effect size, VERIFIED as a durable descriptive finding about where students struggle.

**Bearing on mechanic:** Names exactly where productive conflict is most likely to pay off for this learner: the gap between procedural fluency (row reduction, determinants) and structural/conceptual understanding (span, basis, independence, subspace, linear transformation as a single object) is precisely where a half-remembered first course leaves false confidence — predictions about these structural concepts are the highest-value targets to break, and the habits-of-mind framing argues the *repair* should reinforce transferable mathematical habits (e.g., "always check a conjecture against a low-dimensional counterexample"), not just the specific fact corrected.

Sources: [Cuoco, Goldenberg & Mark 1996, nrich PDF](https://nrich.maths.org/content/id/12640/Cuoco.HabitsOfMind.pdf), [CME Project habits-of-mind summary](https://cmeproject.edc.org/sites/default/files/CME_Habits%20of%20Mind.pdf), [Dorier & Sierpinska research synthesis](https://www.researchgate.net/publication/226963684_Research_into_the_Teaching_and_Learning_of_Linear_Algebra), [student difficulties with basis/span/independence](https://www.researchgate.net/publication/233261892_Student_learning_of_basis_span_and_linear_independence_in_linear_algebra)

---

## Confirmed anchors (solid enough to design on)

1. **Hypercorrection effect (Butterfield & Metcalfe 2001)** — strongly, independently replicated across decades/populations; the most direct evidence that confident commitment + corrective break drives durable correction. Requires a *genuine* confidence judgment before the break.
2. **Testing effect / retrieval practice (Roediger & Karpicke 2006) and pretesting/errorful generation (Kornell/Hays/Bjork 2009; Richland/Kornell/Kao 2009)** — robust, feedback-contingent: failed retrieval attempts followed by clear correction beat passive study. This is the mechanistic engine under commit→break→repair.
3. **Generation effect (Slamecka & Graf 1978)** — one of the most reliable findings in memory research for self-generated vs. presented content, supporting "commit" over "observe."
4. **Spacing (Cepeda et al. 2006) and interleaving (Rohrer & Taylor 2007)** — well-replicated, with the actionable, non-obvious finding that optimal gap scales with desired retention length (favorable to irregular, learner-paced sessions) and that interleaving costs practice-session performance while helping retention.
5. **Expertise reversal effect (Kalyuga et al. 2003)** — well-replicated; critical for a relearner who "quits when slow" because it predicts scaffolding miscalibrated to a given concept's prior-knowledge fragment will actively harm engagement.
6. **Assistance dilemma (Koedinger & Aleven 2007) / impasse-driven learning (VanLehn et al. 2003)** — foundational, repeatedly corroborated in ITS research; gives the direct dosage principle (break until genuine self-detected impasse, then minimal adaptive help).
7. **Self-explanation effect (Chi et al. 1989, 1994)** — long-replicated; the repair step should demand explanation of *why* the prediction failed, not just present the correct answer.
8. **VanLehn 2011's corrected tutoring effect sizes and granularity finding** — the standard, uncontested corrective to Bloom's 2-sigma; step-level engagement (not answer-checking) is what closes the human-tutor gap.

## Weak or contested (should not be leaned on)

1. **Productive failure's superiority over instruction-first sequencing** — Sinha & Kapur's d = 0.36 is real but modest, and there is a live, unresolved theoretical dispute with cognitive-load-theory/expertise-reversal researchers (Kalyuga, Likourezos, Sweller) who report mediational evidence for the opposite sequencing in some conditions. Treat the PF design principles as a strong template, not as proof that "struggle-first" dominates "explain-first" in general — the right sequence likely depends on the learner's prior-knowledge fragment for that specific concept (per expertise reversal).
2. **Cognitive conflict as sufficient for conceptual change** — Posner et al.'s model is widely used but Limón (2001) and the subsequent conceptual-change literature treat "conflict alone works" as essentially debunked; breaking a prediction without making the replacement concept intelligible/plausible/fruitful will often fail to produce restructuring (learner explains away the anomaly instead).
3. **Bloom's original 2-sigma effect size** — now understood as an overstated, small-sample figure; do not cite "2 sigma" as an achievable or even well-estimated target. VanLehn's ~0.76–0.79 range is the credible figure.
4. **Desirable difficulties as a general-purpose design license** — the umbrella term is often invoked loosely; several of its component manipulations (notably interleaving and heavy self-regulation demands) have documented null or negative results for low-prior-knowledge or low-motivation learners in applied/online settings. The framework's own stated boundary condition (sufficient prior resources to engage productively) is the exact condition most at risk for an irregular, "quits when slow," half-forgotten-prior-course learner.
5. **Generation effect's extension beyond simple verbal items to complex conceptual/procedural generation** — the original and best-replicated evidence is for single-item word generation; boundary-condition work (negative generation effect for source/context memory, constraint-dependent reversals) means its extrapolation to "generate a mathematical prediction" is plausible but not itself directly tested at that grain.
6. **A single formal large-scale Registered Replication Report for hypercorrection** — UNVERIFIED; the effect is replicated many times independently, but I could not confirm a coordinated multi-lab RRR exists specifically for it (distinguish "many replications" from "a Many-Labs-style RRR," which is a higher evidentiary bar this search did not locate).
7. **Mathematical maturity / habits-of-mind framework and linear-algebra misconception literature** — valuable and durable as descriptive/curricular consensus, but neither offers a quantified effect size or causal experiment; they identify *where* conflict is likely productive (basis/span/independence, formalism obstacle) without quantifying *how much* designed conflict helps there.
