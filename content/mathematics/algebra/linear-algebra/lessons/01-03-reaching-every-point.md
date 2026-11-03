# Reaching every point

## Commit

Let v = (2, 1) and w = (1, 1). Neither is horizontal or vertical, and they are not perpendicular to each other; they lean toward the same side.

1. Using any amounts a and b, positive, negative, or fractional, can you reach the point (0, 5) as a·v + b·w? If yes, give a and b.
2. Can you reach every point in the plane with v and w alone?

Answer both and give a confidence from 1 to 4.

## Truth

1. Yes: a = −5, b = 10. Check: −5·(2, 1) + 10·(1, 1) = (−10 + 10, −5 + 10) = (0, 5).
2. Yes, every point. To reach a target (x, y) you need 2a + b = x and a + b = y, and these always have a solution: a = x − y, b = 2y − x. No target is excluded.

The picture: v and w lay down a skewed grid instead of a square one. Walk any distance along v's line, then any distance along w's line. A skewed grid still covers the whole plane. Perpendicularity made the square grid easy to read; it was never what made the grid complete.

## Repair

(0, 5) looked out of reach because both arrows lean right and up. But a = −5 walks backward along v and b = 10 walks far along w: the sideways steps cancel (−10 + 10 = 0) and the upward steps leave 5. Leaning the same way never mattered, and neither did being perpendicular. Lying on one line would have.

## Artifact

If you can build an interactive: arrows v and w from the origin, a target the learner places, sliders for a and b, and a locked yes/no guess before the sliders unlock. On reveal, draw the skewed grid that v and w generate.

## Exercises

1. Reach (7, 2) with v = (2, 1) and w = (1, 1). Give a and b and check.
2. Find a and b for the targets (1, 0) and (0, 1). What does being able to hit these two points tell you about hitting everything else?
3. In your own words: state the real condition two arrows must satisfy to reach the plane, and say why "perpendicular" was the wrong thing to fixate on.

## Twist

Add a third arrow u = (3, 0). Find two different triples (a, b, c) with a·v + b·w + c·u = (0, 5). What does the existence of two answers say about the third arrow?
