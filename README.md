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
$ unicode r 41-5A
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
```
