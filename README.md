# unicodes
Unicode information

usage: unicode TYPE INPUT

types: s (string), d (decimal), h (hex) or r (range)

example:

```
$ unicode s 'יְהוָ֖ה'
Unicode 1497 [hex: 0x5d9 ] is: י (Other Letter › HEBREW LETTER YOD)
Unicode 1456 [hex: 0x5b0 ] is: ְ (Nonspacing Mark › HEBREW POINT SHEVA)
Unicode 1492 [hex: 0x5d4 ] is: ה (Other Letter › HEBREW LETTER HE)
Unicode 1493 [hex: 0x5d5 ] is: ו (Other Letter › HEBREW LETTER VAV)
Unicode 1464 [hex: 0x5b8 ] is: ָ (Nonspacing Mark › HEBREW POINT QAMATS)
Unicode 1430 [hex: 0x596 ] is: ֖ (Nonspacing Mark › HEBREW ACCENT TIPEHA)
Unicode 1492 [hex: 0x5d4 ] is: ה (Other Letter › HEBREW LETTER HE)
```
```
$ unicode r 03b1-03c9
α β γ δ ε ζ η θ ι κ λ μ ν ξ ο π ρ ς σ τ υ φ χ ψ ω

$ unicode r 010840-010855
𐡀 𐡁 𐡂 𐡃 𐡄 𐡅 𐡆 𐡇 𐡈 𐡉 𐡊 𐡋 𐡌 𐡍 𐡎 𐡏 𐡐 𐡑 𐡒 𐡓 𐡔 𐡕 
```
