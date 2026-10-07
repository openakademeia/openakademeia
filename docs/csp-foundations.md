# Cognitive Sparring Partner: Foundations

Distilled from a Gemini conversation (Sept 2, 2026, https://share.gemini.google/AJ1K0QZlaIva) that started as a search for open linear algebra textbooks and ended with a draft rulebook for an agent that teaches anything. This document keeps what was load-bearing, sharpens it, names what was left undefined, and lists the decisions that gate a build.

## 1. Thesis

When every learner has an LLM, delivering knowledge is worth nothing and executing procedures is worth little. What stays scarce is judgment: knowing which question to ask, holding a mental model that predicts behavior, and catching a machine when it is confidently wrong. A teaching agent must therefore not be a better textbook or a patient Q&A oracle. It must be a sparring partner that manufactures cognitive friction and refuses to resolve it on the learner's behalf.

Linear algebra makes the stakes concrete. Transformers, embeddings, retrieval, and PCA are all linear algebra, and the person debugging them has to see the rank drop or the dimensional mismatch that the model itself cannot see.

## 2. The load-bearing mechanic: commit, break, repair

Every technique in the conversation reduces to one move. The learner commits to a prediction before seeing the answer. The prediction meets a simulation or a puzzle and, ideally, breaks. The concept then arrives as the repair for a gap the learner already feels. Reading the definition first short-circuits this, so the definition must come after the break. Everything else is scaffolding around this move.

## 3. The pipeline

Your ordering from the final prompt, with Gemini's refinements folded in.

| Stage | Agent does | Learner produces |
|---|---|---|
| 1. Foundation | One micro-concept from source material, grounded in a concrete situation. Under 150 words. | Reads. |
| 2. Simulation | A sandbox the learner manipulates before the formal rule appears. | Observations, a first hypothesis. |
| 3. Friction puzzle | A counterintuitive scenario where the naive model fails. | A committed prediction, then a broken one. |
| 4. Human-answer questions | Explain the mechanism in your own words; defend a choice. | Structural reasoning, judged on structure, not keywords. |
| 5. Multi-model synthesis | The same concept through at least two lenses (algebraic, geometric, computational). | Translation between representations. |
| 6. Adversarial verification, dosed | Hallucination audit, constraint shift, refusal of plug-and-chug. | Diagnosis of a planted flaw; reasoning at the rule's boundary. |

Gemini merged stages 4 and 6 into a single final "human-only verification". Splitting them is deliberate: stage 4 checks the happy path, stage 6 checks the boundary, and they cost the learner very different amounts of patience.

## 4. Behavioral rules worth keeping verbatim

- Never lecture. Under 150 words of instruction before pivoting to a question or a sandbox.
- Scaffold down, never give away. On a stuck learner, remove a dimension or drop to a simpler simulation. Do not reveal.
- Honor the human loop. Never advance without a real reply; never simulate the learner's side.
- Refuse plug-and-chug. Redirect "compute this" to "why is this approach structurally sound."
- Dose adversarial testing. Hallucination audit at most once per module; constraint shift occasionally. Over-testing produces impatience, not learning.

## 5. Grounding in learning science (added here, to verify before relying on)

The conversation rediscovered results that already have names and calibration data:

- Predict-observe-explain and cognitive conflict (conceptual-change literature) back stage 3.
- Desirable difficulties (Bjork) and the generation effect back stage 4: retrieval and self-explanation beat re-reading.
- Productive failure (Kapur) backs the commit-break-repair ordering: struggle before instruction improves transfer.
- Multiple external representations (Ainsworth) back stage 5.

Each also has a documented failure mode, too much difficulty causing disengagement, which is the dosage problem in section 4.

## 6. What the conversation left undefined

The gaps a build hits first, roughly in order.

1. Unit of learning. "Module" and "micro-concept" are used but never defined: granularity, prerequisites, how a textbook chapter becomes a sequence of modules.
2. Advancement criteria. "Evaluate on structural reasoning" is a goal, not a rubric. What signal moves a learner between stages, or to the next module?
3. Simulation provenance. Generated on the fly by the agent, drawn from a curated per-domain library, or both. On-the-fly scales to any domain but is unreliable; curated is reliable but must be authored.
4. Trap and audit libraries. Good counterintuitive puzzles and plausible-but-wrong proofs are hard to write. Same provenance question.
5. Learner state. What persists across sessions: mastered concepts, models the learner currently holds, patience budget consumed.
6. Dosage model. "One per module" and "occasional" need to become a budget tied to observable learner signals.
7. "Human-only" is unenforceable. The premise is that the learner has an LLM, so any question answerable by pasting into one will be. Design around it: ask for the learner's own prior prediction, follow up live on their specific wording, ask about sandbox state only they saw.
8. Generic versus domain-specific. The rulebook is generic. Simulations, traps, audits, and concept graphs are not. This implies two layers: a teaching protocol plus domain packs.

## 7. Linear algebra as the first domain pack

Assets already named in the conversation:

- Source material: MIT 18.06 / 18.06SC (Strang). Alternatives: Hefferon, Austin, Beezer, Siefken.
- Friction puzzle: predict how a shape's area changes under a matrix, before determinants are introduced.
- Simulation: grab vectors and warp a grid; watch a matrix drop rank.
- Hallucination audits: a proof that inverts a non-square matrix; an explanation that misreads an eigenvector geometrically.
- Debugging exercise: a coordinate-transform pipeline or toy recommender with a change-of-basis bug.
- Synthesis: PageRank on a learner-chosen graph; PCA on a learner-chosen dataset.
- Lenses: algebraic, geometric, computational.

## 8. Decisions that gate the build

In order of how much each shapes everything downstream.

1. Form factor. A protocol or skill for an existing agent, a purpose-built agent with a code sandbox, or a web app with a learner UI.
2. First learner. You in self-study, or other people from day one. Decides how much UI and state management matter.
3. Simulation medium for v1. Text-only thought experiments, Python in a sandbox, or browser visualizations.
4. First module. One concept end to end, run on a real learner before generalizing. Determinants-as-area is the obvious candidate.
5. Success criterion. Transfer to a novel problem, a hallucination audit passed, or the learner's own report.
