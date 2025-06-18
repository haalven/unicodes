# unicodes
Unicode information

usage: unicode TYPE INPUT

types: s (string), d (decimal), h (hex) or r (hex-range)

example:

```
$ unicode s 'hebr.: יהוה'
Unicode U+68 (104) [68] is: h (Lowercase Letter › LATIN SMALL LETTER H)
Unicode U+65 (101) [65] is: e (Lowercase Letter › LATIN SMALL LETTER E)
Unicode U+62 (98) [62] is: b (Lowercase Letter › LATIN SMALL LETTER B)
Unicode U+72 (114) [72] is: r (Lowercase Letter › LATIN SMALL LETTER R)
Unicode U+2e (46) [2e] is: . (Other Punctuation › FULL STOP)
Unicode U+3a (58) [3a] is: : (Other Punctuation › COLON)
Unicode U+20 (32) [20] is:   (Space Separator › SPACE)
Unicode U+5d9 (1497) [d7 99] is: י (Other Letter › HEBREW LETTER YOD)
Unicode U+5d4 (1492) [d7 94] is: ה (Other Letter › HEBREW LETTER HE)
Unicode U+5d5 (1493) [d7 95] is: ו (Other Letter › HEBREW LETTER VAV)
Unicode U+5d4 (1492) [d7 94] is: ה (Other Letter › HEBREW LETTER HE)
```
```
$ unicode r 03b1-03c9
α β γ δ ε ζ η θ ι κ λ μ ν ξ ο π ρ ς σ τ υ φ χ ψ ω

$ unicode r 010840-010855
𐡀 𐡁 𐡂 𐡃 𐡄 𐡅 𐡆 𐡇 𐡈 𐡉 𐡊 𐡋 𐡌 𐡍 𐡎 𐡏 𐡐 𐡑 𐡒 𐡓 𐡔 𐡕 
```
