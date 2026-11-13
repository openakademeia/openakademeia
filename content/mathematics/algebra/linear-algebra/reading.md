# Linear Algebra

The reading for the course: one concept per lesson, in course order, each explained with why it holds. Lessons ask you to predict before you read; reading ahead is allowed, but you will miss the surprise.

## 1. Arrows and columns

### Vectors are displacements {#vectors-are-displacements}

A vector is a trip: so far across, so far up. Written as a column, (2, −3) means 2 steps right and 3 steps down. Drawn as an arrow, it is that trip, and the arrow can start anywhere. A vector records a displacement, not a location.

To find the vector of an arrow, subtract where it starts from where it ends, entry by entry. The arrow from (5, 1) to (7, −2) is (7 − 5, −2 − 1) = (2, −3). Subtracting removes the starting point and leaves only the trip, which is why two arrows in different places can be the same vector: equal length, same direction, different start.

Drawing every arrow from the origin is a convention, not a rule. It is useful because the tip then sits at the point whose coordinates are the column's entries, so a column, an arrow from the origin, and a point all carry the same two numbers. Keep in mind which one you mean: a point is a place, a vector is a move.

Nothing here depends on there being two entries. A column of three numbers is a trip in space, and a column of twelve monthly figures is a single object you can shift and compare as a whole.

### Adding and scaling {#adding-and-scaling}

Vectors allow two operations, and the rest of the course is built from them.

**Adding** is doing one trip and then the other. Place the second arrow's tail on the first arrow's tip; the sum runs from the first tail to the second tip. In columns, add entry by entry: (1, 4) + (3, −1) = (4, 3). Order does not matter. Doing v then w, or w then v, traces the two routes around a parallelogram and ends at the same far corner. In columns this is just the fact that horizontal steps add among themselves, vertical steps among themselves, and ordinary numbers add in either order.

**Scaling** by a number c multiplies every entry by c: 3·(1, 4) = (3, 12). Geometrically the arrow stretches along its own line. A negative c turns it around, c = 0 shrinks it to the zero vector, and a fraction shortens it. As c runs over all numbers, the multiples c·v fill the whole line through the origin in v's direction, and nothing off it.

These two operations describe a plane's velocity in a crosswind, the forces meeting at a bridge joint, and money moving between accounts. From chapter 3 on, they are the only two things a matrix is required to respect.

### Linear combinations and reach {#linear-combinations-and-reach}

A **linear combination** of v and w is any vector a·v + b·w, where a and b are any numbers: positive, negative, zero, or fractional. The **reach** of v and w (textbooks call it their span) is the set of every point some combination lands on.

Think of a and b as distances walked along two lines: a along v's line, then b along w's. As a and b vary, the combinations lay down a grid. For v = (1, 0) and w = (0, 1) it is the usual square grid. For two arrows that lean, it is a slanted grid of parallelograms, and a slanted grid covers the plane just as completely as a square one.

So two arrows in the plane reach every point exactly when they do not lie on one line. Perpendicular arrows are the tidy special case, where the grid is easy to read; they are not what makes the grid complete. What matters is that the second arrow supplies a direction the first cannot. Negative and fractional amounts are essential: they let you walk backward along one arrow and far along the other, reaching points neither arrow leans toward.

Finding the actual amounts for a given target means solving two equations, one per coordinate; section 1.5 shows that this is exactly what school algebra was doing. Isometric game maps and crystal lattices use slanted grids that still address every location for the same reason. In chapter 2, the question becomes how many genuinely different directions a set of arrows in space supplies.

### Redundant arrows {#redundant-arrows}

The condition for reaching the plane works in both directions. If w is a multiple of v, say w = c·v, then every combination collapses: a·v + b·w = (a + bc)·v, a single multiple of v. Walking tip to tail along one line never leaves it, so the reach is that line and nothing off it. The second arrow offers more ways to reach the same points but no new direction. It is **redundant**.

That leaves exactly three possibilities for two arrows in the plane: the reach is the whole plane (they point in different directions), a line through the origin (one is a multiple of the other, and not both are zero), or the origin alone (both are zero). There is no reach that is half the plane, or a strip, or a line plus a point.

To check for redundancy, ask whether one column is a multiple of the other: (3, −1) and (−6, 2) are, since the second is −2 times the first. The same all-or-collapse pattern returns as rank in chapter 6 and as a zero determinant in chapter 8. Outside geometry, two sensors that measure the same quantity in different units give one number's worth of information, however many readings they report.

### Systems are combinations {#systems-are-combinations}

A linear combination of columns and a system of linear equations are one idea in two notations. Asking for a and b with

a·(2, 3) + b·(1, −1) = (4, 1)

is the same as solving

2a + b = 4
3a − b = 1

Each equation is one coordinate of the walk: the horizontal steps must total 4 and the vertical steps must total 1. Here a = 1 and b = 2. The columns of coefficients are the arrows, the unknowns are how far to walk along each, and the right-hand side is the destination. Elimination is a procedure for walking the slanted grid. A system has no solution exactly when its destination lies outside the reach of its columns, which for two columns can only happen when they lie on one line.

This also explains the word **vector**. It was never about arrows: a vector is anything you can add and scale by numbers, with the usual rules holding. Columns of two numbers were the first example. Columns of n numbers, audio samples, recipes (double one, add two together), and, by the end of this course, functions all qualify, and everything proved about arrows applies to them.

---

Further reading: David Austin, *Understanding Linear Algebra* (CC BY 4.0), sections 2.1, 2.3 and 2.4 cover this chapter in equations-first order.
