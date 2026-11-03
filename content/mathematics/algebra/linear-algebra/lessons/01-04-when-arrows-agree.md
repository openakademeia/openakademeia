# When arrows agree

## Commit

Let v = (2, 1) and u = (4, 2).

1. Can you reach (0, 5) as a·v + b·u?
2. Can you reach (6, 3)?
3. Describe the complete set of points you can reach with v and u together.

Give a confidence from 1 to 4.

## Truth

u is 2v, so every combination a·v + b·u equals (a + 2b)·v: a single multiple of v.

1. No. You would need 2(a + 2b) = 0 and (a + 2b) = 5 at once, which is impossible.
2. Yes: (6, 3) = 3v, for instance a = 3, b = 0, or a = 1, b = 1.
3. The line through the origin in the direction (2, 1), and nothing off it.

The picture: both arrows lie on one line, and tip-to-tail walking along a line never leaves it. The second arrow adds length options but no new direction.

## Repair

u is 2v, so every walk that uses both is a walk along v alone: a·v + b·u = (a + 2b)·v. (6, 3) is 3v, on v's line, so it is reachable in many ways. (0, 5) is off the line, and no amount of u can help, because u offers no direction that v lacks.

## Artifact

If you can build an interactive: the same slider setup as the previous lesson, but with u = 2v, so the learner watches the reachable set stay pinned to one line while the sliders move.

## Exercises

1. Are (3, −6) and (−1, 2) on the same line? What set do they reach?
2. Choose any w so that v = (2, 1) and w reach the plane, and any w′ so that they do not. What is the quickest arithmetic test that decides?
3. In your own words: how can two arrows supply only one direction's worth of reach?

## Twist

In three dimensions, take v = (1, 0, 0) and w = (0, 1, 0). They are not on one line. Do they reach every point in space? Describe exactly what they reach.
