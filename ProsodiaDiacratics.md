# 프로소디아 다이어크라틱 (προσωδία διακριτικός) 결합용 문자 (Combinational)

먼저 `◌`의 코드 포인트를 밝히겠다. U+25CC다. 치환할때 활용하기 위해 밝히었다.

1. 프네우마 (πνεῦμα)
   - U+0314 spiritus asper, δᾀσεῖα ◌̔
   - U+0313 ψιλή ◌̓
2. 토노스 (τόνος)
   - U+0301 ὀξεῖα (monotonic에서 τόνος에 해당) ◌́
   - U+0300 βαρεῖα ◌̀
   - U+0342 περισπωμένη ◌͂
3. 이오타 서브스크립툼 Iota Subscripum, 이포예그람메니 (ὕπογεγραμμένῃ)
   - U+0345 ◌ͅ
4. 디아레시스 (διαλυτικά)
   - U+0308 ◌̈ (monotinic에서 διαλυτικά에 해당)

코드 `from toolz import partial, comp`및 `with open("temptxt.txt", "w") as fp: fp.write(comp("\n\n".join, partial(map, comp("```\n{}\n```".format, chr, (0x0300).__add__)))(b"\x13\x14\x01\x00\x42\x45\x08"))`를 통해 코드 블럭으로 표시해줘보자면

```
̓
```

```
̔
```

```
́
```

```
̀
```

```
͂
```

```
ͅ
```

```
̈
```

typing tips : 어케 타이핑할지는 다음 절차 순으로 생각해보셈
1. 당신이 그리스어 키보드를 쓰는 중이며
2. 키보드 문구추천 단축어로 저 문자들을 쓰고싶다면
3. 단축어 이름에 대한 다음 추천사항이 만족스럽다면, 단축어 추천사항으로 지정할것

 - δασεῖα

```
̓
```

   + 본 단축어명에 쓰이는 다이어크라틱
     * 결합문자를 통한 다이어크라틱 : περισπωμένη
     * monotonic keyboard을 통한 완성형 문자로 작성된 다이어크라틱 : 없음

 - ψιλή

```
̔
```

   + 본 단축어명에 쓰이는 다이어크라틱
     * 결합문자를 통한 다이어크라틱 : 없음
     * monotonic keyboard을 통한 완성형 문자로 작성된 다이어크라틱 : ὀξεῖα (monotonic τόνος)

 - βαρεῖα

```
̀
```

   + 본 단축어명에 쓰이는 다이어크라틱
     * 결합문자를 통한 다이어크라틱 : περισπωμένη
     * monotonic keyboard을 통한 완성형 문자로 작성된 다이어크라틱 : 없음

 - περισπωμένη

```
͂
```

   + 본 단축어명에 쓰이는 다이어크라틱
     * 결합문자를 통한 다이어크라틱 : 없음
     * monotonic keyboard을 통한 완성형 문자로 작성된 다이어크라틱 : ὀξεῖα (monotonic τόνος)

 - ὑπογεγραμμένη

```
ͅ
```
   + 본 단축어명에 쓰이는 다이어크라틱
     * 결합문자를 통한 다이어크라틱 : περισπωμένη
     * monotonic keyboard을 통한 완성형 문자로 작성된 다이어크라틱 : ὀξεῖα (monotonic τόνος)

 - διαλυτικά

```
̈
```

   + 본 단축어명에 쓰이는 다이어크라틱
     * 결합문자를 통한 다이어크라틱 : 없음
     * monotonic keyboard을 통한 완성형 문자로 작성된 다이어크라틱 : ὀξεῖα (monotonic τόνος)

 - 부가 옵션
   + προσωδία
```
PHS(προσωδία hint system) diacratics typing dependency map
1. monotonic keyboard ´ input : plz check your keyboard manual. (if you have no manual. then sorry I've no idea)
2. monotonic keyboard ´ input → ψιλή (ψιλή requires monotonic greek keyboard)
3. monotonic keyboard ´ input → διαλυτικά (διαλυτικά requires monotonic greek keyboard)
4. monotonic keyboard ´ input → περισπωμένη (περισπωμένη requires monotonic greek keyboard)
5. περισπωμένη⁴ → δασεῖα (δασεῖα requires περισπωμένη)
6. περισπωμένη⁴ → βαρεῖα (βαρεῖα requires περισπωμένη)
7. δασεῖα⁵ & monotonic keyboard ´ input → ὑπογεγραμμένη (ὑπογεγραμμένη requires δασεῖα and monotonic greek keyboard)
```
