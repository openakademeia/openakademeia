# Linear Algebra: syllabus

Status: approved on 2026-11-02 (proposed 2026-10-07). Each chapter is one flight in `course.yaml` next to this file; chapter 1 is written, the rest are listed as planned flights with no rungs yet.

## Sources

Two open textbooks in `~/Downloads`:

- Jim Hefferon, *Linear Algebra*, 4th ed. (`linalgebra.pdf`, 525 pp). Proof-first, abstract vector spaces in chapter 2, Jordan form in chapter 5, assumes a semester of calculus. Best source for proofs and for puzzle exercises (marked `?`). License is on his website, not in the PDF; recalled as share-alike, to verify before adapting his material.
- David Austin, *Understanding Linear Algebra* (`Understanding Linear Algebra.pdf`, 519 pp). No calculus assumed, stays in R^n, ends at SVD and PCA. CC BY 4.0 (verified, page 2). Primary source for the arc and for applied examples.

Recommended spine: Austin's arc, reordered geometry-first (vectors and transformations before systems of equations, as 3Blue1Brown does), with Hefferon's "every claim gets a reason" standard reserved for the unify rungs and the epilogue.

## Prerequisites

Almost nothing. The first two rungs of chapter 1 double as the check.

- School algebra: solve `2x + 3 = 7`, multiply out brackets, fractions and negatives.
- The coordinate plane: plot a point from two numbers and read them back.
- Pythagoras, first needed in chapter 9; the rung that needs it reminds the learner.

Not assumed: calculus, trigonometry, complex numbers, proof experience, programming. Quarter-turn rotation needs no trigonometry; the one rung with a general rotation carries a one-paragraph reminder that cosine and sine are coordinates on the unit circle. Real numbers throughout, so "a rotation has no real eigenvector" is a break rung, not a gap. Proof skill is an output of the course, not an input. The real prerequisite is the disposition to commit to an answer before seeing the right one, which the addon enforces.

## Chapters

Each chapter is one flight of 3 to 5 rungs, small enough that one sitting finishes it. Each is built around a belief the returning learner holds confidently and wrongly; the concept is the repair. "Breaks:" names that belief.

### Part I. The objects

1. **Arrows and columns.** A vector is anything you can add and scale. The arrow and the column of numbers are two views of one thing; combining arrows is the central move of the subject. Breaks: "you need perpendicular directions to reach every point."
2. **Reach and redundancy.** Which points a set of arrows can reach, when an extra arrow adds nothing, how to count the directions that matter. Span, independence, basis, dimension. Breaks: "three arrows in space always reach all of space."
3. **A matrix is a machine.** A matrix moves every arrow at once and is determined by where it sends the unit arrows, which are its columns. Linearity: lines stay lines, the origin stays put. Breaks: "any map that fixes the origin is linear."
4. **Composition is multiplication.** Multiplying matrices is running one machine after another; the row-times-column rule is the only rule consistent with that; order matters. Breaks: "AB equals BA."

### Part II. Solving

5. **The reach question, answered.** A system of equations asks which input lands on a target. Elimination answers it; the only outcomes are none, one, or infinitely many, for a visible reason. Breaks: "n equations in n unknowns have exactly one solution."
6. **What it reaches and what it crushes.** Column space is what the machine can produce, null space is what it flattens to zero, rank-nullity is a conservation law: dimensions in equal dimensions reached plus dimensions crushed. Breaks: "a 3 by 3 matrix always produces three-dimensional output."
7. **Undoing.** Reversible exactly when nothing is crushed, exactly when the columns are independent, exactly when rank is full. The web of equivalences is the first taste of mathematical structure. Breaks: "the inverse of AB is A-inverse times B-inverse."
8. **The determinant is a stretch factor.** The signed factor by which area or volume scales. Zero means collapse, negative means a flip; the product rule is obvious from the picture and horrible from the formula. Breaks: "det of a sum is the sum of dets."

### Part III. Geometry

9. **Length, angle, perpendicular.** The dot product measures how much of one arrow lies along another. Pythagoras gives length, zero gives perpendicular, the transpose appears as the natural partner. Breaks: "the arrows perpendicular to a plane in space form a plane."
10. **The closest answer.** When no input lands on the target, find the nearest reachable point. Projection onto a subspace, the normal equations, the line of best fit. Breaks: "no solution means there is nothing to say."

### Part IV. Structure

11. **Coordinates are a choice.** The same arrow has different numbers in different bases, so the matrix of a machine depends on the basis. Similar matrices are the same machine in different coordinates. Breaks: "`(1, 2)` is the vector," when it is a description relative to a basis.
12. **Directions the machine does not turn.** Eigenvectors are the lines a matrix leaves in place, eigenvalues the stretch along them, the characteristic equation is chapter 8 paying off. Diagonalization is choosing the basis where the machine is pure scaling. Breaks: "every matrix has a real eigenvector."
13. **The long run.** Powers of a matrix through the eigenbasis, why the largest eigenvalue wins, steady states of Markov chains, PageRank, Fibonacci as a matrix power. Breaks: "repeated application always blows up or dies out."
14. **Every matrix is rotate, stretch, rotate.** Symmetric matrices have perpendicular eigenvectors; the SVD extends that to any matrix; PCA and image compression fall out as "keep the biggest stretches." Breaks: "only square matrices decompose."

### Epilogue

**It was never about arrows.** Polynomials, sequences, and functions can be added and scaled, so everything above applies to them, and the derivative is a matrix. This is the maturity payoff and where Hefferon's abstraction earns its place. Breaks: "the derivative has nothing to do with matrices."

## Notes

- Interactive artifacts matter most in chapters 3, 4, 8, 12, and 14, where the claim is about a picture.
- Rung mix per flight follows `plugins/mentor/SKILL.md`: confirm, break, unify kinds, about 1 in 4 rungs a trap, at least one human-only exercise per rung.

## Decisions

1. All 14 chapters and the epilogue kept, in this order (approved 2026-11-02). Merging 9 with 10 or 13 into 12 stays an option if the middle drags.
2. Geometry-first order, not the equations-first order both books use.
3. Hefferon's license is still unverified; nothing of his is adapted yet. Verify before borrowing any exercise.

Next: run chapter 1 through the rung loop with a real learner, fix what drags, then write chapter 2.
