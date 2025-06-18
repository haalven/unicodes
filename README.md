# unicodes
Unicode information

usage: unicode TYPE INPUT

types: s (string), d (decimal), h (hex) or r (hex-range)

example:

```
$ unicode s 'יְהוָ֖ה'
Unicode U+5d9 (1497) [d7 99] is: י (Other Letter › HEBREW LETTER YOD)
Unicode U+5b0 (1456) [d6 b0] is: ְ (Nonspacing Mark › HEBREW POINT SHEVA)
Unicode U+5d4 (1492) [d7 94] is: ה (Other Letter › HEBREW LETTER HE)
Unicode U+5d5 (1493) [d7 95] is: ו (Other Letter › HEBREW LETTER VAV)
Unicode U+5b8 (1464) [d6 b8] is: ָ (Nonspacing Mark › HEBREW POINT QAMATS)
Unicode U+596 (1430) [d6 96] is: ֖ (Nonspacing Mark › HEBREW ACCENT TIPEHA)
Unicode U+5d4 (1492) [d7 94] is: ה (Other Letter › HEBREW LETTER HE)
```
```
$ unicode r 03b1-03c9
α β γ δ ε ζ η θ ι κ λ μ ν ξ ο π ρ ς σ τ υ φ χ ψ ω

$ unicode r 010840-010855
𐡀 𐡁 𐡂 𐡃 𐡄 𐡅 𐡆 𐡇 𐡈 𐡉 𐡊 𐡋 𐡌 𐡍 𐡎 𐡏 𐡐 𐡑 𐡒 𐡓 𐡔 𐡕 
```
