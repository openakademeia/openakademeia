Fourteen chapters and an epilogue, taught geometry first: arrows and the machines that move them come before systems of equations, the way 3Blue1Brown does it and the opposite of most textbooks. Each chapter is three to five rungs, short enough to finish in one sitting, and each is built around something you probably believe about arrows or matrices that turns out to be wrong. The concept is what fixes it.

## What you need

School algebra and the coordinate plane. You should be able to solve 2x + 3 = 7, multiply out brackets, handle fractions and negatives, plot a point from two numbers, and read the numbers back off a plot. No other prior knowledge is required. Pythagoras comes up in chapter 9, and the rung that needs it reminds you how it goes.

The first two rungs double as the check. Beyond that, the one thing the course asks of you is to commit to an answer before you see the right one. Mentor holds you to that.

## Chapters

### Part I. The objects

1. **Arrows and columns.** A vector is anything you can add and scale. An arrow and a column of numbers are two views of the same thing, and combining arrows is the move the whole subject is built on. You probably think you need perpendicular directions to reach every point. You don't.
2. **Reach and redundancy.** Which points a set of arrows can reach, when an extra arrow adds nothing, and how to count the directions that matter: span, independence, basis, dimension. Three arrows in space do not always reach all of space.
3. **A matrix is a machine.** A matrix moves every arrow at once, and where it sends the unit arrows, its columns, determines everything. Linear means lines stay lines and the origin stays put. Not every map that fixes the origin is linear.
4. **Composition is multiplication.** Multiplying matrices is running one machine after another. The row-times-column rule is the only rule consistent with that, and the order matters: AB and BA are usually different.

### Part II. Solving

5. **The reach question, answered.** A system of equations asks which input lands on a target. Elimination answers it, and the only possible outcomes are no solution, one, or infinitely many, for a reason you can see. n equations in n unknowns do not guarantee exactly one solution.
6. **What it reaches and what it crushes.** Column space is what the machine can produce, null space is what it flattens to zero. Rank-nullity is a conservation law: the dimensions you put in equal the dimensions reached plus the dimensions crushed. A 3 by 3 matrix does not always produce three-dimensional output.
7. **Undoing.** A matrix is reversible exactly when it crushes nothing, exactly when its columns are independent, exactly when its rank is full. That web of equivalences is the first taste of mathematical structure. The inverse of AB is not A-inverse times B-inverse.
8. **The determinant is a stretch factor.** The signed factor by which area or volume scales: zero means collapse, negative means a flip. The product rule is obvious from the picture and horrible from the formula. The determinant of a sum is not the sum of the determinants.

### Part III. Geometry

9. **Length, angle, perpendicular.** The dot product measures how much of one arrow lies along another. Pythagoras gives length, zero means perpendicular, and the transpose shows up as its natural partner. The arrows perpendicular to a plane in space do not form a plane.
10. **The closest answer.** When no input lands on the target, find the nearest reachable point: projection onto a subspace, the normal equations, the line of best fit. "No solution" is not the end of the conversation.

### Part IV. Structure

11. **Coordinates are a choice.** The same arrow has different numbers in different bases, so the matrix of a machine depends on the basis you picked. Similar matrices are the same machine in different coordinates. (1, 2) is not the vector. It is a description of the vector relative to a basis.
12. **Directions the machine does not turn.** Eigenvectors are the lines a matrix leaves in place, eigenvalues the stretch along them, and the characteristic equation is chapter 8 paying off. Diagonalizing is choosing the basis in which the machine is pure scaling. Not every matrix has a real eigenvector.
13. **The long run.** Powers of a matrix through the eigenbasis, why the largest eigenvalue wins, steady states of Markov chains, PageRank, Fibonacci as a matrix power. Repeated application does not always blow up or die out.
14. **Every matrix is rotate, stretch, rotate.** Symmetric matrices have perpendicular eigenvectors, and the SVD extends that to any matrix. PCA and image compression fall out as "keep the biggest stretches." Matrices that aren't square decompose too.

### Epilogue

**It was never about arrows.** Polynomials, sequences, and functions can be added and scaled, so everything above applies to them, and the derivative is a matrix.
