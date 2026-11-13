# Colour palette

openakademeia's main palette: warm black and white, with olive (the Academy's olive grove, the tree in the logo) as the only accent. Every colour on the site is a role in `:root` of `src/static/style.css`; add new colours there, not inline.

## Neutrals

| Role | Hex | Used for |
|---|---|---|
| `--ground` | `#e3e2de` | Page background, under an 18px dot grid (`--dot`, ink at 11%) |
| `--paper` | `#f4f4f2` | Panels, cards, plain buttons |
| `--ink` | `#111110` | Body text |
| `--ink-soft` | `#55534d` | Secondary text |
| `--night` | `#1c1b19` | Top bar, footer, code and chat panels |
| `--night-2` | `#262522` | Chat bubbles on night |
| `--on-night` | `#f1f1ef` | Text on night |
| `--on-night-soft` | `#a9a59b` | Muted text on night |

## Olive accent

| Role | Hex | Used for |
|---|---|---|
| `--accent` | `#7d8c45` | Accent field on the home page (ink text), text selection, highlight rule in the chat |
| `--accent-button` | `#606c38` | Primary buttons (white text), focus ring |
| `--accent-press` | `#4f5d2f` | Primary button hover |

`--accent` is light enough for ink text but too light to carry white text or to outline on the ground (2.8:1, under the 3:1 minimum for UI). So buttons and the focus ring use the deeper `--accent-button`.

## Contrast pairs in use

| Foreground on background | Ratio |
|---|---|
| Ink on ground | 14.6:1 |
| Ink-soft on ground | 5.9:1 |
| On-night-soft on night | 7.0:1 |
| Ink on `--accent` | 5.1:1 |
| White on `--accent-button` | 5.7:1 |
| `--accent-button` focus ring on ground | 4.4:1 |
| `--accent` rule on night | 4.7:1 |
