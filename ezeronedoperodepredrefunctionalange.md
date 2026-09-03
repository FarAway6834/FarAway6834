# ezeronedoperodepredrefunctionalang

목차
1. Shitting and CastedRealloc Type System (10 line ~ 64 line)
2. zerone system (65 line ~ 105 line)
3. ezerone (106 line)
4. OperodepredrofunctionalLang (232 line ~ 357line)
5. ezeronedoperodepredrefunctionalange (358 line ~ )

## 1. Shitting and CastedRealloc Type System

Introduce : 만들때만 해도 똥 배설했다며 현타왔었는데, 지금보니 인용할만큼 잘만들었다.

용어 정의 : first랑 last는 각각 first(x, y) = x및 last(x, y) = y임.

본론)

```
isSCR(M) : M = <dom Typing, Typing, Shitting, CastedRealloc, Shit, nonShit>

tip : 이후로 이 글은 isSCR술어가 언질하는 모델 M의 심볼 Typing, Shitting, CastedRealloc, Shit, nonShit을 정의할 뿐이다. 아무튼 저 심볼들을 마저 정의하겠다.

Typing : dom Typing ↦ dom Typing
Typing(id, x) = (id, x)

fact 1. Typing(id, x)는 X = first[domTyping]일시, `typedef Typing struct {X id; X x; inline Typing(X id, X x) : id(id), x(x) {}} Typing;`인 타입 Typing처럼 작동하는 함수다. 정확히는, 그 직관을 가져다가 쓴거다. 동적 타입 번호를 지정하는 C++의 직관.
fact 2. dom Typing내에선, Typing(x) = x식의 항등함수다.
fact 3. 나는 이걸 C++직관마냥 쓰지만, 펙트는 그렇게 쓸 이유가 없다는 점을 명시하라. 형식만 맞으면 된다. 내가 이 타입을 보는 직관은, 이 형식에 본질의 극히 일부에 지나지 않는다. 아무튼, 내 직관에 근거한 의미 해석 방식을 FCS(Fucking Coding Semmentics)라 하겠다.

Shitting : dom Typing ↦ dom Typing
Shitting(x) = Typing(first(x), first(x))

fact 1. FCS적 입장으로 보자면, Shitting는 타입이름을 값으로 꺼내오는 함수다. 사실은, CastedRealloc이랑 같이 쓰면 기본값처럼 쓸수 있지만. 흠.... first(x)말고 last(x)만 꺼낼 생각인데 nonShit 이면 first를 꺼낼수 없다, 그러므로, last(Shit(x))로 꺼내면 된다.
fact 2. Shitting은 dom Typing을 Shit으로 대응시키는 전사사상이다.

Shit(x) : x ∈ dom Typing ∧ first(x) = last(y)
nonShit(x) : x ∈ dom Typing ∧ first(x) ≠ last(y)

fact) 참고로 Shit은 Shitting된 dom Typing이다. (참고 1)

CastedRealloc : (dom Typing)² ↦ dom Typing
CastedRealloc(x, y) = Typing(first(x), last(y))

fact 1. FCS적 입장으로 보자면, CastedRealloc는 y의 타입명을 x의 타입병으로 바꾸는 타입케스팅이자, 완전히 새로 할당한다는 점에서, 재할당이다.
fact 2. CastedRealloc은, 어쨌거나, CastedRealloc((a, b), (c, d)) = (a, d)라는 튜플간 연산일 뿐이다.

참고사항)

참고 1
th. ran Shitting = Shit
pf. DICO QUOD ERAT
1. ran Shitting = Shitting[dom Typing] = {y = (first(x), first(x)) | x ∈ dom Typing}
2. ∀X ⊆ dom Typing, X ∖ {z  ∈ X | first(x) = first(z)} = {z  ∈ X | first(x) ≠ first(z)}
3. ran Shitting ∖ {z  ∈ ran Shitting | first(x) = first(z)} = {z  ∈ ran Shitting | first(x) ≠ first(z)}
4. ∀y ∈ dom Typing, {x ∈ ran Shitting | first(x) = first(y)} ∖ {Shit(x) | first(x) = first(y)} = ∅
5. ran Shitting = Shit

tip : Typing, Shitting, CastedRealloc, Shit, nonShit은 FCS적 의미로 해석할수 있을 뿐이지, 실제론 항등함수 Typing와, 단항/이항연산 Shitting, CastedRealloc및 단항술어 Shit, nonShit인 SCR대수의 심볼들일 뿐이다. 에초에, 이건 글이 아니라, 그냥 수학식을 선언하고, 관련된 명제 몇게 적은것이다.

fun fact) first(y) = last(x) s.t. x = CastedRealloc(x, y) = CastedRealloc(x, Shitting(y))이다. 이걸 이용하여 y = f(x)인 f를 얻으면, f(a, b) = (b, b)를 할수 있다. (궁금하면 집적 즐겁게 증명해보길 바란다, 재미도 있고 실력도 늘어난다.)
```

오늘의 추천곡 : [유령 체험](youtu.be/hbGFPAF9-_Q), 이게 JPOP이지 소리가 자동으로 나온다.

## 2. zerone system

Introduce : SCR로 구축한 일급타입시스템이다. 막 만들었을때만 해도, 할말이 없고 스스로 센스없고, 어짜피 유용하게 쓰이지 않을거라 자조했지만, 지금보니 인용할만큼 잘만들었다.

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

SCR은 zerone와 E-zerone의 기반으로 유용하게 써먹을거라, 지금 zerone랑 SCR을 단번에 채득하길 빌겠다.

저번엔 SCR을 만들었고, 이번에 zerone를 만들었다면, 다음에는 E-zerone를 만들거다.

오늘의 추천곡 : [NEURODIVERSE](youtu.be/DCyRVr9lcZI) - (정말이지, GUMI가 이렇게나 내 취향의 노래를 부를수 있을줄이야... 상상도 못했다.)

## 3. ezerone (n.b. 아직 편집중이다. 초안이 읽기 구리니까, 편집을 좀 할거다.)

ETSed ZERONE

operodepredrefunctionalang을 객체지향적으로 바라보기 위한 첫번재 축이다.

### 용어 정의

뭐... "Endofunctor Type System"이랑, "SCR"이랑 "zerone"를 읽고 오면 걍 거의다 이해될거다....

그리고, zerone에서 사용하기 위한 용도로, EndofunctorTyper라는 함수가 제공되긴 한다... 음... 그냥 그렇다고.

그래서, Endofunctor Type에 대한 배경지식이 있다 가정하고, EndofunctorTyping함수를 정의해보겠다.

뭐... 사실 그 정의가 zerone에 의존하고, 타입 시스템으로써의 성질은 Endofunctor Type System문서에서 정의한 바를 가져와야, 타입시스템으로써 성질을 가지긴 한다만...

뭐.... 그렇다고.

first, last, isSCR, Typing, Typing, Shitting, CastedRealloc, Shit, nonShit같은건 "Shitting and CastedRealloc Type System"를, zerok, onek, bezero, beone, iszero, isone, iszerone는 "zerone"를 참고하도록 하라.

Edit : ㅅㄲ왜이렇게 지침?;;

### 본론

isezeroneby(M₁, M₂) : (M₁, M₂) = (M₁, (<iszero ∪ isone, zerok, onek, bezero, beone, Typing, Typing, Shitting, CastedRealloc, Shit, nonShit, iszero, isone>, <isEndofunctorTyper ∪ definedOnEndofunctorTyper, EndofunctorTyperCore, isEndofunctorTyper, isntEndofunctorTyper, undefinedOnEndofunctorTyperCore, definedOnEndofunctorTyperCore>) ∧ isEndofunctorTyperModelOn(<iszero ∪ isone, iszero, isone>, <isEndofunctorTyper ∪ definedOnEndofunctorTyper, EndofunctorTyperCore, isEndofunctorTyper, isntEndofunctorTyper, undefinedOnEndofunctorTyperCore, definedOnEndofunctorTyperCore>))

isEndofunctorTyperModelOn(M₁, M₂) : (M₂, M₁) = (<iszero ∪ isone, iszero, isone>, <isEndofunctorTyper ∪ definedOnEndofunctorTyper, EndofunctorTyperCore, isEndofunctorTyper, isntEndofunctorTyper, undefinedOnEndofunctorTyperCore, definedOnEndofunctorTyperCore>)

$EndofunctorTyperCore(x) = \begin{cases} EndofunctorTyper(x), &(definedOnEndofunctorTyper(x)), \ x, &(undefinedOnEndofunctorTyper(x)) \end{cases}$

isEndofunctorTyper(x) : x ∈ codom EndofunctorTyper

definedOnEndofunctorTyper(x) : x ∈ dom EndofunctorTyper

isntEndofunctorTyper(x) : x ∈ isEndofunctorTyper ∪ definedOnEndofunctorTyper ∧ ¬isEndofunctorTyper(x)

definedOnEndofunctorTyper(x) : x ∈ isEndofunctorTyper ∪ definedOnEndofunctorTyper ∧ ¬undefinedOnEndofunctorTyper(x)

EndofunctorTyper = EndofunctorTyperCore|_{dom EndofunctorTyper}

inEndofunctorTyperModelDomain(x) : x ∈ isEndofunctorTyper ∪ definedOnEndofunctorTyper

inZeroneModelDomain(x) : x ∈ iszero ∪ isone
isEndofunctorTyped(x) : ∃f ∈ definedOnEndofunctorTyper, x ∈ codom f

ExtendedShit(x) : x ∈ dom ExtendedTyping ∧ first(x) = last(y)
ExtendednonShit(x) : x ∈ dom ExtendedTyping ∧ first(x) ≠ last(y)
Extendediszero(x) : x ∈ dom ExtendedTyping ∧ first(x) = 0
Extendedisone(x) : x ∈ dom ExtendedTyping ∧ first(x) = 1

ExtendedTyping : dom ExtendedTyping ↦ dom ExtendedTyping
ExtendedTyping(id, x) = (id, x)

ExtendedShitting : dom ExtendedTyping ↦ dom ExtendedTyping
ExtendedShitting(x) = ExtendedTyping(first(x), first(x))

ExtendedCastedRealloc : (dom ExtendedTyping)² ↦ dom ExtendedTyping
ExtendedCastedRealloc(x, y) = ExtendedTyping(first(x), last(y))

Extendedbezero : dom ExtendedTyping ↦ dom ExtendedTyping
Extendedbezero(x) =  ExtendedCastedRealloc(zerok, x)
Extendedbeone : dom ExtendedTyping ↦ dom ExtendedTyping
Extendedbeone(x) =  ExtendedCastedRealloc(onek, x)

$ExtendedEndofunctorTyperCore(x) = \begin{cases} EndofunctorTyperCore(x), &(inEndofunctorTyperModelDomain(x)), \ x, &(¬inEndofunctorTyperModelDomain(x)) \end{cases}$

M = <dom ExtendedTyping, zerok, onek, ExtendedTyping, ExtendedShitting, ExtendedCastedRealloc, Extendedbezero, Extendedbeone, ExtendedEndofunctorTyperCore, isEndofunctorTyper, isntEndofunctorTyper, undefinedOnEndofunctorTyperCore, definedOnEndofunctorTyperCore, ExtendedShit, ExtendednonShit, Extendediszero, Extendedisone, inEndofunctorTyperModelDomain, inZeroneModelDomain, isEndofunctorTyped> ∧ dom ExtendedTyping = isEndofunctorTyped ∪ inZeroneModelDomain ∪ inEndofunctorTyperModelDomain ∧ iszerone(<dom ExtendedTyping, zerok, onek, ExtendedTyping, ExtendedShitting, ExtendedCastedRealloc, Extendedbezero, Extendedbeone, ExtendedShit, ExtendednonShit, Extendediszero, Extendedisone>)

#### [Endofunctor Type](xunr3.github.io/e)

EndofunctorTyper : {S | S ⊆ {last(x) | iszero(x)}} ↦ ran EndofunctorTyper

EndofunctorTyper(S) : S ↦ ran EndofunctorTyper(S)

EndofunctorTyper(S)(x) = (S⁰, S, S⁰ × {x})

이러면 S⁰ = {ε}이고 ε = ()인 공튜플이니,

dom EndofunctorTyper(S)(x) = {ε}이기에, 
graph EndofunctorTyper(S)(x) = {ε} × {x} = {(ε, x)}이므로,
EndofunctorTyper(S)(x)는 오직 무인자에서만 정의되는 다변수함수(ZFC의 표준 정의를 따르자면 그렇다.)로
EndofunctorTyper(S)(x)() = x임이 자명하다.

뭐... 증명하라고 하면, 다변수함수가 사실 튜플을 정의역으로 하는 단변수함수라는거나, 튜플이 사실 제귀적으로 정의되니까 사실상 전부 순서쌍일 뿐이라는 기초론적인 내용까지 가야한다.
내가 설명 안해도 쉽게 보일수 있다.
그리고 너무 당연해서, 직관적으로 논리적 증명이 보인다.
뭐.... 에초에 정의역과 치역, 공역을 저걸로 구해본 후에, 정의역이 유한하므로, 오른쪽 유일성을 가지는 graph자체도 유한하니, 모는 경우를 단순히 조사해서 증명된다... 는게 직관적으로 보이지 않는가?
한마디로 너무 자명해서 위 내용에 대한 상세증명은 다루지 않는다.

codom EndofunctorTyper(S)(x) = S이다.
즉, Endofunctor Type은 codom을 통해서 그 타입을 구할수 있다.

음... 뭐... 이것도 너무 당연하고...

...물론, Endofunctor Type은 타입의 관점에서 접근할 필연성이 없다. 님들도 시그마 쓸때, 꼭 수열에서만 쓰는거 아니잖음?....

그러니까, codom이 타입이라는 말은 걍, 여기서 정의한 타입에 대한 관계에서 그렇다는 말이다.

뭐.... 그냥 그렇다고.

isEndofunctorTyperModelOn(M₁, M₂) : (M₂, M₁) = (<iszero ∪ isone, iszero, isone>, <isEndofunctorTyper ∪ definedOnEndofunctorTyper, EndofunctorTyperCore, isEndofunctorTyper, isntEndofunctorTyper, undefinedOnEndofunctorTyperCore, definedOnEndofunctorTyperCore>)

$EndofunctorTyperCore(x) = \begin{cases} EndofunctorTyper(x), &(definedOnEndofunctorTyper(x)), \ x, &(undefinedOnEndofunctorTyper(x)) \end{cases}$

((엄청 할말 많지만) tip : EndofunctorTyper는 iszero가 어떻게 선언되었는지에 따라 그 값(함수는 튜플이고, 튜플은 값이니)이 다름이 자명하다.)

isEndofunctorTyper(x) : x ∈ codom EndofunctorTyper

((엄청 할말 많지만) tip : isEndofunctorTyper(Kₛ)인 Kₛ에 대하여, Kₛ는 operdepredrel의 그 Kₛ다.)

definedOnEndofunctorTyper(x) : x ∈ dom EndofunctorTyper

((엄청 할말 많지만) tip : Kₛ를 구할수 있는 s)

isntEndofunctorTyper(x) : x ∈ inEndofunctorTyperModelDomain∧ ¬isEndofunctorTyper(x)

undefinedOnEndofunctorTyper(x) : x ∈ inEndofunctorTyperModelDomain ∧ ¬definedOnEndofunctorTyper(x)

에초에, inEndofunctorTyperModelDomain밖에 있는것에 대해서도 ¬isEndofunctorTyper나 ¬definedOnEndofunctorTyper가 먹히기에, 도메인 제한을 하는식으로 선언을 해야한다.

EndofunctorTyper = EndofunctorTyperCore|_{dom EndofunctorTyper}

아까전에 말했듯, dom EndofunctorTyper는 이미 정의되어있다. 집합 s를 입력으로, Kₛ를 출력으로 하는 놈이니까.

오늘의 추천곡 : [갈채](youtu.be/qsA0eThr-6A), 말이 필요없다.

## 4. OperodepredrofunctionalLang (n.b. 아직 편집중이다. 초안이 읽기 구리니까, 편집을 좀 할거다.)

operodepredrofunctional lang의 정의와 operodepredrodel에 대해 다루겠다.

### operodepredrodel

WellOrdering(S, ≤) : (∀x, y, z ∈ S, (x ≤ y ∨ y ≤ x) ∧ ((x ≤ y ∧ y ≤ x) → x = y) ∧ ((x ≤ y ∧ y ≤ z) → x ≤ z) ∧ (∃!m ∈ S s.t. m ≤ x)) ∧ S ≠ ∅

Predrel(S) ≜ S ∪ 𝔹

first(x, y) ≜ x
last(x, y) ≜ y
x concat y = \begin{cases} (x, y), &(x ∉ dom first ∧ y ≠ ε ≠ x), \ first(x) concat (last(x) concat y), &(x ∈ first ∧ y ≠ ε ≠ x), \ x, &(y = ε), \ y, &(x = ε) \end{cases}

minf ≜ ϝ(S, ≤) : WellOrdering. (ϝx : P(S). εm (∀x ∈ S, m ≤ x) : S) : {𝔉(P(S), S) | S = first(x) ∧ x ∈ WellOrdering}
SetTuplize(S, ≤) ≜ \begin{cases} minf(S, ≤)(S) concat SetTuplize(S ∖ {minf(S, ≤)(S)}, ≤), &(S ≠ ∅, \ ε,  &(S = ∅) \end{cases}

뭐... SetTuplize는 알아서 잘 튜플을 만들겠지 뭐... 비가산길이에서 튜플이 작동하는지는 잘 모르겠지만...

참고로, 저 정의를 보면 dom minf과 dom SetTuplize가 같다는 개똥직관을 느낄수 있지만, 실제론, dom SetTuplize = dom minf ∪ {(∅, x) | x ∈ dom first}다. 에초에 S = ∅인 경우에 대해서 정의되어야 정의되는, 너무 당연한 소리지만.

oper(S) ≜ lim_{n ⟶ ∞} ∪ᵢ₌₀ⁿ 𝔉(Sⁱ, S)
pred(S) ≜ lim_{n ⟶ ∞} ∪ᵢ₌₀ⁿ P(Sⁱ)

oper는 모델의 도메인이 S일때, n=0~∞항연산자의 집합을, pred는 모델의 도메인이 S일떼, n=0~∞항 술어임이 너무 자명하므로, 전혀 탐구할 가치가 없다고 느낀다.

FullSpecifiedModel(S, ≤) = S concat SetTuplize(S, ≤) concar SetTuplize(oper(S), ≤) concat SetTuplize(pred(S), ≤)

이 (여기도 개똥직관으로 ≤가 S²의 부분집합이라고 착각하는 놈들이 있을까봐 말하는데, 여기서 ≤는 (S ∪ oper(S) ∪ pred(S))²의 부분집합이여야만 정의된다.) FullSpecifiedModel은 무엇인가 하면,
FullSpecifiedModel(S, ≤)는 상수기호들의 튜플 SetTuplize(S, ≤), 함수•연산자기호들의 튜플 SetTuplize(oper(S), ≤), 술어•관계•논리연결사기호들의 튜플 SetTuplize(pred(S), ≤)를 concat해서 만든 모델로, S위에서의 모든 원소를 상수로 다 선언하고, 모든 함수를 다 선언하고, 모든 술어를 다 선언한 상태라 보면 된다.

그냥 그걸 표기하는 용도다. 그러려고 만든거임.

operodel(S) ≜ oper(S) ∪ S

이러한 operodel(S)은 어떤 특별한 모델의 도메인이다. 조금 이따가 알아보자.

Kₛ|ₛ ≜ ϝx:s. (s⁰, s, s⁰ × {x}):oper(s)
Kₛ|ₒₚₑᵣ₍ₛ₎ ≜ ϝx:oper(s). x:oper(s)

이렇게 Kₛ가 정의된다.

이때, <operodel(s), Kₛ>는 닫힌 연산을 이룬다.

pf.

x ∈ operodel(s) ↔ (x ∈ oper(s) ∨ x ∈ s)이니,

x ∈ s → Kₛ(x) = Kₛ|ₛ(x), x ∈ oper(s) → Kₛ(x) = Kₛ|ₒₚₑᵣ₍ₛ₎(x)로,

$Kₛ(x) = \begin{cases} Kₛ|ₛ, & (x ∈ s), \ Kₛ|ₒₚₑᵣ₍ₛ₎(x), & (x ∈ oper(S)) \end{cases}$다.

즉, Kₛ : operodel(s) ↦ operodel(s)로 operodel(s)에 대해 닫혀있다.

Q.E.D.

t₀ = SetTuplize(S, ≤)
t₁ = SetTuplize(oper(S), ≤)
t₂ = SetTuplize(oper²(S), ≤)
t₃ = SetTuplize(pred(S), ≤),
t₄ = SetTuplize(pred(oper(S)), ≤)
t₅ = t₀ concat t₁
t₆ = t₁ concat t₂
t₇ = t₀ concat t₁ concat t₆
t₈ = t₃ concat t₄
s₀ = S
s₁ = oper(S)
s₂ = oper(operodel(S)) ∖ operodel(oper(S))
s₃ = pred(operodel(S)) \ (pred(S) ∪ pred(oper(S)))

FullSpecifiedModel(operodel(S), ≤) = operodel(S) concat t₇ concat SetTuplize(s₂ , ≤) concat t₈ concat SetTuplize(s₃ , ≤)다.

FullSpecifiedModel(S, ≤) = s₀ concat t₅ concat t₃
FullSpecifiedModel(oper(S), ≤) = s₁ concat t₆ concat t₄
으로, FullSpecifiedModel(S, ≤)와 FullSpecifiedModel(oper(S), ≤)의 구성 요소를 FullSpecifiedModel(operodel(S), ≤)가 그대로 가지고 있음을 알수 있고,

두 모델 FullSpecifiedModel(S, ≤), FullSpecifiedModel(oper(S), ≤)이 Kₛ ∈ SetTuplize(s₂ , ≤)를 통해 준동형임을 알 수 있다.

이러한 준동형성의 증명은, 모델 FullSpecifiedModel(operodel(S), ≤)에서 귀결이며, 이러한 특별한 모델의 도메인이 바로 operodel(S)인것이다.

operodel^∞(S) ≜ lim_{n ⟶ ∞} ∪ᵢ₌₀ⁿ operodelⁱ(S)

뭐... operodel을 k번 적용시 (k-1)번 적용한것을 포함하므로, 무한번째에도 대강 저렇게 되는걸 알수 있으니, 걍 넘어가라. 그냥 operodel^∞을 정의하기 위해서 저랬을 뿐이니.

Predel(S) ≜ P(S) ∪ S
x ∈ₛ y : (x, y) ∈ Predel(s)² ∧ x ∈ y
(∈ₛ y)(x) ≜ x ∈ₛ y

<Predel(S), ∈ₛ>는 멤버십을 서술하는 모델이다. 이 모델을 통해 맴버십을 서술할수 있다.

FullSpecifiedModel(Predel(S), ≤)에서, 튜플의 어느 인덱스에는 무조건 ∈ₛ가 존재한다.

Predrodel(S) ≜ Predel(Predrel(S))
smember : Predrodel(S)² ↦ Predrodel(S)
x smember y ≜ \begin{cases} T, &(y ∈ₛ x), \ F, &(y ∉ₛ x) \end{cases}

(tip : smember라는 명칭은 x's member라는 의미로 작한 명칭이다, 물론 명칭따위가 크게 중요하지 않고 beer로 바뀌더라도 무관하겠다만)

<Predrodel(S), smember>는 마그마를 이룬다만, 그 이상의 특별함점은 없다.

물론, 단순히 x ∉ₛ y : ¬(x ∈ₛ y)인지라, (x, y) ∈ S² ∪P(S)²에서 항상 x ∉ₛ y가 참이긴 하다. 뭐... 에초에 당연한거 아닌가? 그렇지 않을때 비교되지 않으라는 법은 인간의 착각이고, 똥멍청이나 하는 생각이다.

술어에선, 인자가 시스템 내에 있으면 항상 참이나 거짓으로 술어값이 정의되니까 (비결정적인 경우를 빼면), 당연히 술어에서 참 거짓으로 판단 대상이 아닌 경우 냅다 false를 뱉는게 당연한거다.

술어논리만 똑바로 쳐 알아도 그럼 바보같은 생각은 안하니 굳이 여기서 다룰 필욘 없지만.

참고로, ran smember = 𝔹 = {T, F}다. (너무 자명한 사실이긴 하지만, 에초에 아까전부터 자명한소리만 지껄이고 있었으니 뭐...)

operodepredrodel ≜ operodel ◦ predrodel
operodepredrodel^∞ ≜ operodel^∞ ◦ predrodel

뭐... 에초에 𝔹 ⊆ S면, operodepredrodelⁿ(S) = operodelⁿ(S)니, 굳이 설명 안해도, 똥멍청이가 아니면, operodepredrodel는, 𝔹 ⊆ S일시, S∖𝔹 ⊆ X ⊆ S 에서의, operodelⁿ(S) (=operodepredrodelⁿ(X))를 X에 대하여 표기할때 사용하는것이란걸 알것이라 보고 넘어가겠다.

### operodepredrofunctional lang

isFunctionalModelOf(M, S) : M = FullSpecifiedModel(oper(S), ≤)

 > ∀isFunctionalModelOf(M, S)에서, 표기"M " concat fn1 concat "(Mⁿ) " = " concat fn2은, fn1(x₁, ..., xₙ) = (Kₛ ◦ fn2)(Kₛ⁻¹(x₁), ..., Kₛ⁻¹(xₙ))
로 정의된다. 그리고, 이때 `fn1 :: M`는 참이다.

그렇다. operodepredrodel은 이러한 operodepredrofunctional lang을 규정하는데 사용된다.

이로써, `<type> <fname>(<type>ⁿ) : <type>`는 식의 형식언어체계로, 모델론을 더 쉽게 이해하는 언어인 operodepredrofunctional lang가 정의된다.

오늘의 추천곡 : [터미널](youtu.be/ZFxbl9Fm3c0) 혹은 [overdose](youtu.be/H08YWE4CIFQ) 혹은 [금목서](youtu.be/1pI242Hsi5U), (なとり의 전설적인 세 노래)

## 5. ezeronedoperodepredrefunctionalange

...아직 작성중...