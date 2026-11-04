# Colour palette

openacademy's main palette. Every colour on the site is one of these five or a role derived from them in `:root` of `src/static/style.css`; add new colours there, not inline.

| Name | Hex | Used for |
|---|---|---|
| Olive leaf | `#606c38` | Secondary text (`--ink-soft`) |
| Black forest | `#283618` | Body text (`--ink`), top bar, footer, code and chat panels (`--night`) |
| Cornsilk | `#fefae0` | Page ground, text on dark surfaces |
| Sunlit clay | `#dda15e` | Accent field on the home page, highlight rules on dark (`--accent-soft`) |
| Copperwood | `#bc6c25` | Accent: focus ring, text selection (`--accent`) |

## Derived roles

Copperwood behind 18px cornsilk text is 3.8:1, below the 4.5:1 WCAG AA minimum, so buttons use a deeper shade mixed toward Black forest. The other derived values are tints for surfaces the five colours can't separate on their own.

| Role | Hex | Derivation |
|---|---|---|
| `--accent-button` | `#9e6122` | Copperwood + 20% Black forest; 4.8:1 with Cornsilk |
| `--accent-press` | `#905c21` | Copperwood + 30% Black forest |
| `--paper` | `#f9edcc` | Cornsilk + 15% Sunlit clay; panels on the ground |
| `--paper-deep` | `#f6e4c0` | Cornsilk + 25% Sunlit clay; hover on paper |
| `--night-2` | `#364420` | Black forest + 25% Olive leaf; chat bubbles |
| `--on-night-soft` | `#bebfa4` | Cornsilk + 30% Black forest; muted text on dark |

## Contrast pairs in use

| Text on background | Ratio |
|---|---|
| Black forest on Cornsilk | 12.2:1 |
| Olive leaf on Cornsilk | 5.4:1 |
| Olive leaf on `--paper` | 4.9:1 |
| Black forest on Sunlit clay | 5.7:1 |
| Cornsilk on `--accent-button` | 4.8:1 |
| `--on-night-soft` on Black forest | 6.9:1 |
