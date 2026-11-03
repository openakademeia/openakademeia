# Tip to tail

## Commit

Let v = (2, 1) and w = (1, 3).

1. Predict v + w as a column, and where its tip lands when drawn from the origin.
2. Predict 2v, −v, and ½w.
3. Walk v then w, tip to tail. Separately, walk w then v. Do the two trips end at the same point?

Give your answers and a confidence from 1 to 4.

## Truth

1. v + w = (3, 4), tip at the point (3, 4).
2. 2v = (4, 2), −v = (−2, −1), ½w = (½, 3⁄2).
3. The same point. Draw it: v then w and w then v trace the two routes around a parallelogram and meet at the far corner.

The reason is that the entries are handled independently. Horizontal steps add among themselves, vertical steps add among themselves, and ordinary numbers add in either order. Scaling by 2 doubles each step, so the arrow doubles in length and keeps its direction. Scaling by −1 reverses each step, so the arrow turns around. Every multiple of v, positive, negative, or fractional, lies on the one line through the origin in v's direction.

## Repair

Both orders end at (3, 4) because the horizontal steps, 2 and 1, total 3 in either order, and the vertical steps, 1 and 3, total 4 in either order. The parallelogram is that bookkeeping drawn as a picture. 2v and −v stay on v's line because scaling multiplies both steps by the same number, which keeps their ratio, and so the direction.

## Artifact

If you can build an interactive: two draggable arrows from the origin, a locked guess for where v + w lands, then an animation that slides w to the tip of v and reveals the parallelogram. A slider for the scalar on one arrow, including negatives.

## Exercises

1. With v = (2, 1) and w = (1, 3), compute 3v − w and describe where it points.
2. Find the number c such that c·(2, 1) = (−6, −3).
3. In your own words, using only the language of walking: explain to a friend why v + w must equal w + v, and why 2v − 2v has to be the arrow of length zero.

## Twist

Without computing any lengths: is the arrow (2, 1) + (1, 3) longer than, shorter than, or exactly as long as the two arrows' lengths added together? When would the two be equal?
