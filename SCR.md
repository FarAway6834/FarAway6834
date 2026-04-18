# Shitting and CastedRealloc Type System

Introduce : 나도 내가 도데체 뭔 똥을 배설한건지 모르겠다 ㅠ ㅋ...

용어 정의 : first랑 last는 각각 first(x, y) = x및 last(x, y) = y임.

본론)

isSCR(M) : M = <dom Typing, Typing, Shitting, CastedRealloc, Shit, nonShit>

Typing : dom Typing ↦ dom Typing
Typing(id, x) = (id, x)

Shitting : dom Typing ↦ Typing
Shitting(x) = Typing(first(x), first(x))

Shit(x) : x ∈ dom Typing ∧ first(x) = last(y)

nonShit(x) : x ∈ dom Typing ∧ first(x) ≠ last(y)

CastedRealloc : (dom Typing)² ↦ dom Typing
CastedRealloc(x, y) = Typing(first(x), last(y))

마치며)

ㅅㅂ ㅋㅋㅋㅋ ㅠ ㅈㄴ 현타오네 ㅋㅋㅋ