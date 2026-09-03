# zerone system

할말이 없어 ㅋ ㅠ ...

Introduce : SCR로 구축한 일급타입시스템인데 ... 걍, 센스가 제로네(zerone)... 작명도, 유머도...

용어 정의 : 정규직교기저 x̂, ŷ가 중간에 들어가서 당황할까봐, 용어를 명확히 하자면, 정규직교기저 x̂, ŷ는 각각 x̂ = (1, 0), ŷ = (0, 1)임이 ZFC상에서 자명하다. 그리고, first, last, isSCR, dom Typing, Typing, Shitting, CastedRealloc, Shit, nonShit같은건 "Shitting and CastedRealloc Type System"를 참고하도록 하라.

본론)

```
iszerone(M) : M = <iszero ∪ isone, zerok, onek, bezero, beone, Typing, Shitting, CastedRealloc, Shit, nonShit, iszero, isone> ∧ {last(x) | iszero(x)} = {last(x) | isone(x)} ∧ isSCR(<iszero ∪ isone, Typing, Typing, Shitting, CastedRealloc, Shit, nonShit>)

fact) M = <iszero ∪ isone, zerok, onek, bezero, beone, Typing, Shitting, CastedRealloc, Shit, nonShit, iszero, isone> ∧ isSCR(<iszero ∪ isone, Typing, Typing, Shitting, CastedRealloc, Shit, nonShit>) ↔ iszerone(M)다. (궁금하면 집적 즐겁게 증명해보길 바란다, 재미도 있고 실력도 늘어난다.)

zerok = Shitting(ŷ)
fact) Shitting(ŷ) = (0, 0)이다. (궁금하면 집적 즐겁게 계산해보길 바란다, 재미도 있고 실력도 늘어난다.)
onek = Shitting(x̂)
fact) Shitting(x̂) = (0, 0)이다. (궁금하면 집적 즐겁게 계산해보길 바란다, 재미도 있고 실력도 늘어난다.)

bezero : dom Typing ↦ dom Typing
bezero(x) = CastedRealloc(zerok, x)
fact) bezero(x) = Typing(0, last(x))이다. (궁금하면 집적 즐겁게 계산... 아니 증명해보길 바란다, 재미도 있고 실력도 늘어난다. 벌써 힌트를 줘버렸네, 등호를 쓰면 계산이 곧 증명이라는걸...)

beone : dom Typing ↦ dom Typing
beone(x) = CastedRealloc(onek, x)
bezero(x) = CastedRealloc(zerok, x)
fact) beone(x) = Typing(1, last(x))이다. (궁금하면 집적 즐겁게 계산... 아니 증명해보길 바란다, 재미도 있고 실력도 늘어난다. 벌써 힌트를 줘버렸네, 등호를 쓰면 계산이 곧 증명이라는걸...)

isone(x) : x ∈ dom Typing, first(x) = 1
iszero(x) : x ∈ dom Typing, first(x) = 0

fact) 저번 SCR의 shitting처럼, 이번 bezero, beone도, ran값이 iszero, isone이다.
```

마치며)

SCR도 zerone도 유용하게 쓰이는 경우는 딱 하나밖에 못본것같다.
각각 zerone와 E-zerone.

저번엔 SCR을 만들었고, 이번에 zerone를 만들었다면, 다음에는 E-zerone를 만들거다.