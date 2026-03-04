# C+9kw라는 esolang

원칙 : "문법은 커스터마이징 가능하다면 많아도 좋다. 그러나 실행은 C스러워야하고, C다운 방식이여야 하고, 근본 C/Asaambly식 사고여야한다. 원리는 간단하다. 마이너스 추상화를 통해서 C스러운 최적화된 코드로 표현 가능한 개념만 수용한다. 나머지는 getout."
참고 : 슈퍼컴파일러가 아님. LLVM/clang을 C컴파일러로 쓸것은 권장사항일 뿐. 어디에도 슈퍼컴파일이라 할만한건 없음.

9kw = [constexpr, consteval, template, using, concept, requires, namespace, enum, enum class]
임.

C+9kwc : C+9kw compiler

C+9kwc가 하는 일 : C+9kw코드를 C로 컴파일함.

C+9kw코드 : 9kw에 해당하는 키워드를 지원하는 C

C+9kwc 기본옵션 : `--preprocess`가 기본이고 `--no-preprocess`는 기본리 아니다. 기본적으로 C+9kwp를 쓰는것.

C+9kwc의 특징 : C+9kwp가 존재하는 디렉토리에 conf.json에 C컴파일러를 명시해줘야한다. pch를 사용하기 때문. 또한 C+9kwp가 존재하는 디렉토리에 C+9kwc도 존재함.

C+9kwic : C+9kw initial compiler
C+9kwic와 C+9kwc의 차이점 : 작성 언어 빼고 없음.

주의사항 : asmlib는 C+9kwc의 기능이지 C+9kwp의 기능이 아님.

C+9kwc 작성 언어 : pure C+9kw
C+9kwic 작성 언어 : pure C

C+9kw 컴파일 결과물 : pure C

C+9kw 런타임 = C런타임

요약 : 9kw에 해당하는걸 C로 컴파일해주는 유사 슈퍼컴파일러

bitwisePCRE : 0x00 (0b00000000) ~ 0xFF (0b11111111)에서, 비트마저 다룰수 있는 PCRE. 다른 PCRE regex를 서브루틴으로 쓰려면 ${「해당 regex」}식으로 써야... 예를들어 해당 regex가 match용이면, match서브루틴으로 쓰이고, substitute용이면, substitute결과를 캡쳐한 함수로 쓰임.

bitwisePCRE 작동 원리 : C의 PCRE2.h를 사용하는 소스코드 + Callout을 이용하여, bitwise조작의 경우 PCRE2.h를 사용하는 소스코드 + Callout으로 C위탁 방식이고, regex끼리의 호출도 callout. 참고로 app이라는 PCRE substituate를 하는 서브루틴이 최상위 함수고, bitwisePCRE실행시 사용됨. 그러나 bitwisePCRE는 컴파일 타임에만 애용된다는게 함정.

C+9kwp : C+9kw preprosessor (DSL은 C+9kwp의 기능이지, C+9kwc와는 무관한 기능이다. DSL은 컴파일 타임에 처리가 끝난다.)
1. `#DomainSpecificLanguage(load, 「DSL0 ~ DSL7」, 「bitwisePCRE 파일명 (파일경로일수 있음)」)`나 `#DomainSpecificLanguage(set, 「DSL0 ~ DSL7」, 「bitwisePCRE 소스코드」)`는 bitwisePCRE 소스코드를 DSL0 ~ DSL7중 하나의 변수인 「DSL0 ~ DSL7」에 넣고
2. `#DomainSpecificLanguage(move, 「DSL0 ~ DSL7」, 「DSL0 ~ DSL7」)`는 변수간 swap
3. `#DomainSpecificLanguage(「push / pop」, 「left / right」, 「DSL0 ~ DSL7」)`로 lstack / rstack에 push / pop도 되고
4. `#DomainSpecificLanguage(「use / unuse」, 「DSL0 ~ DSL7」, 「lv」)`로 DSL변수로 설정된 DSL사용을 설정 / 해제 가능함. (참고로 「lv」은 숫자로, 「lv」 = n이면, n < m인 m레벨인 DomainSpecificLanguage의 경우 설정 / 해제를 dsl내에서 지시할수 있다. 그치만, 동일한 n레벨은 지시가 안된다. unuse로 쉽게 해제하기 위함)
5. `#C+9kwdefine`, `#C+9kwifndef`, `#C+9kwifdef`, `#C+9kwif`, `#C+9kwelif`, `#C+9kwelse`, `#C+9kwendif`, `#C+9kwinclude`, `#C+9kwpragma`가 따로 있다. 기본 전처리문은 C로 컴파일될시 C의 전처리를 사용하기 때문에, C+9kw에서 전처리를 쓰고싶으면, 저 구문을 써야함.

추가기능 enable / disable
1. asmlib "filename.pch" extern 「함수 시그니쳐」 { 「어셈블리 소스코드」 } 문 : C컴파일러에서, extern된 함수를 "filename.pch"이라고 해서, 같이 링킹될 C용 라이브러리로 어셈블리 코드를, 별도파일로 컴파일 (이걸 쓰면 pure C가 아닌, assambly포함인 셈. filename.pch는 filename.lib라는 정적 라이브러리를 링킹하는것.) (참고 : standardsl가 아닌 C+9kw의 열번째 정규 구문임에도 `#enable asmlib`나 `#disable asmlib`를 써야하는 괴상한 놈이다.)
2. `#enable TROasm(lv)`를 통해서만 사용 가능한 standardsl에서 제공하는 구문인「wrapper함수 시그니쳐」{ asm "jump함수명"; 「소스코드」} 문 : asmlib "filename.pch" extern 「함수 시그니쳐」 { 「어셈블리 소스코드」 } 문을 마개조한거임. wrapper용도의 인라인/비인라인 함수 내에서 선언해줘야함. (Tail-Call Jumps를 응용하여, wrapper함수가 단지 jump함수를 호출해서 인자를 넘겨주자마자 반환하도록 만들어서 pch에서 컴파일하고, jump함수는 asmlib "filename.pch" extern 「함수 시그니쳐」 { 「어셈블리 소스코드」 } 문을 통해서 구현되어있고, target이라는 함수의 begin이라는 줄로 jump하고, target은 end라는 줄에소, 다시 jump함수로 점프하는 nonlocal jump를 저지름) (그러나 이건 `#enable TROasm(lv)`를 통해서만 사용 가능한 standardsl일 뿐. standardsl은 C+9kw에 내장된 DSL임. 즉, 내장 bitwisePCRE파일을 이용함.) (참고 : 이를 통해서, C compiler's jump (also inlineible) -> nonlocal jump (to assambly) -> assambly -> nonlocal jump (to back) -> jump (return) 인 흐름을 만들고, 저기에 쓰이는 불필요한 jump는 컴파일러가 똑똑하다면 사라질것임. 하지만, 그런 평탄화를 하면 바이너리가 C의 바이너리 느낌이 사라지기에, 실제로는 평탄화 안된 바이너리가 디버깅은 더 용이할것임. 나같으면 똑똑한 컴파일러를 쓰겠지만. 암튼간에, 이걸 하는 이유는 인라인 어셈블리라는 기능을 제공하기 위해서였을 뿐.)
3. gcc/clang의 jump table지원 : 내부적으로 asm문으로 컴파일됨. (그러나 이건 `#enable JumpTable(lv)`를 통해서만 사용 가능한 standardsl일 뿐. standardsl은 C+9kw에 내장된 DSL임. 즉, 내장 bitwisePCRE파일을 이용함.)
4. `#enable EBNF(lv)` : EBNF용 DSL(EBNF의 non terminal symbol을 bitwisePCRE용 서브루틴으로 컴파일)활성화로 내부적으로 컴파일됨. (`#disable`도 존재. 이렇게 껏다 켰다 할수있는 DSL을 standardsl이라 부름. standardsl은 C+9kw에 내장된 DSL임. 즉, 내장 bitwisePCRE파일을 이용함.)
6. `#enable CLASS(lv)` : 구조체 struxt x { 「code」 }에 대해 struct y : x { 「code2」}로 선언된(상속) 구조체를, struct y { 「code」 「code2」 }로 컴파일해주는 DSL 활성화 (`#disable`도 존재. 이렇게 껏다 켰다 할수있는 DSL을 standardsl이라 부름. standardsl은 C+9kw에 내장된 DSL임. 즉, 내장 bitwisePCRE파일을 이용함.)
7. `#enable method(lv)` : method라고 쓰면 struct에 함수를 만들수 있음. 사실은 struct x에 대해, namespace method_x에다가 처박는거 뿐이지만... (참고 : C+9kw는 template namespace라는 키워드를 사용하면, 해당 네임스페이스는 템플릿을 달수 있다. 대신에 template namespace는 일반 namespace나 템플릿 struct에서 템플릿 인자를 주어서 사용하지 않으면 런타임엔 사용 못한다.) 그렇게 모든 method는 static인 method만 허용됨. deducing this로 self를 쓰는 method키워드나, static method 키워드로, static함수를 struct안에 선언 가능하다. (`#disable`도 존재. 이렇게 껏다 켰다 할수있는 DSL을 standardsl이라 부름. standardsl은 C+9kw에 내장된 DSL임. 즉, 내장 bitwisePCRE파일을 이용함.)
8. `#enable ABC(lv)` : abstract라는 키워드로 선언한 함수는 상속시에 꼭 구현해야함. 상속 전에 struct에 있다면 해당 struct는 abstract struct임. abstract struct는 런타임에 존재하지 않음. abstract struct끼리의 상속에는, abstract함수의 구현이 필수가 아님. abstract struct를 struct가 상속하면, 해당 struct에서 abstract 함수의 구현 여부를 체크함. 이를 통해서 C++의 virtual보다 나은 abstract를 사용 가능. 문제점이 있다면, virtual특유의 다형성을 쓸수 없음. (`#disable`도 존재. 이렇게 껏다 켰다 할수있는 DSL을 standardsl이라 부름. standardsl은 C+9kw에 내장된 DSL임. 즉, 내장 bitwisePCRE파일을 이용함.)
9. `#enable operator(lv)` : 객체에 연산을 하면, operator method가 대신 실행되도록 컴파일. 내임 맹글링으로 operator method가 정의되도록 하고, 객체간 연산은, operator method의 호출로 내부적으로 컴파일됨 (`#disable`도 존재. 이렇게 껏다 켰다 할수있는 DSL을 standardsl이라 부름. standardsl은 C+9kw에 내장된 DSL임. 즉, 내장 bitwisePCRE파일을 이용함.)
10. `#enable standardsl`을 통해서, standardsl라는 추가기능의 사용 여부를 결정 가능. (이건 standardsl이 아닌, standardsl라는 기능을 사용할지 말지를 결정하는거임. 비슷하게 standardsl이 아닌데도 enable/disable이 있는것의 예시로는 asmlib문의 활성화 / 비활성화가 있음)
11. standardsl인 Uintptr_tUnion : uintptr_t union이라고 하는 구문이며, 유일한 uintptr_t인 맴버변수 x와 다른 임의의 맴버변수 y에 대해, y의 타입이 T일때, *.y인 접근은, (T) *.x로 컴파일되는 DSL
12. standardsl인 ForseInline : 말이 좋아서 forse inline이지, inline형태로 작성한 함수를 메크로로 바꿔주는것 뿐이다. 그렇기에 실제 사용시 컴파일타임 타입체크밖에 안되니, forse를 쓰는건 역시 위험하다.
13. standardsl인 AllignedStruct : 말이 좋아서 alligned struct지 실상은 `#pragma pack(push, 1)`과 `#pragma pack(pop)`를 이용한것.
14. standardsl인 ForseBitfieldStruct : 걷으로 보기엔 forse bitfield struct라고 구조체를 선언하고 쓰는걸로 보이지만, 실상은 enum class를 이용하여서, 비트필드용 마스크를 만들고, 그걸 가지고, 비트 인자를 플립 • enable • disable하는 등등의 작업을 한것 뿐이다. 진짜 개무식한 마스킹 접근일 뿐.
15. standardsl인 FunctionOverloadingDsl( function overloading dsl) : 주의사항으로는 "존나 느리다."이거는 standardsl인 주제에, lpush • rpush같은 컴파일 타임 코드용 스택을 저장용량삼는 regex며, regex를 서브루틴으로 쓰는 정신나간 함수 프로그래밍을 쓰기 때문이다. (실제 구현 권장사항은, 15번 추가기능인 이것에만 한정해서, 컴파일러의 최적화를 추가적으로 할 필요가 있다는것. 컴파일 결과의 속도에는 영향이 없지만, regex로 프로그래밍을 하면 느리다. 그니까 컴파일러가 왕창 느려질수 있다.)

C+9kwp의 특징 : C+9kwc가 존재하는 디렉토리에 conf.json에 C컴파일러를 명시해줘야한다. pch를 사용하기 때문. 또한 C+9kwc가 존재하는 디렉토리에 C+9kwp도 존재함.

주의사항 : conf.json은 C+9kwp가 존재하는 디렉토리에 있는거지 프로젝트 디렉토리에 있는게 아님. pch의 내부 설정에 따라, 정적 라이브러리를 pch가 링크하도록 설정되어있어서, 실제 빌드시엔, C컴파일러의 컴파일 옵션은 없고, include에 따라 pch가 불러와지면, pch에 기록되어있는 lib가 불러와지는것 뿐.

## 여담

다른사람이 보면, "C+9kw는 C에다 문자열 치환을 통한 컴파일을 몇게 더한 조악한 언어일 뿐"이라고 싫어할수도 있겠지만... 난 문자열 치환 좋아함.
컴파일러는 PCRE2.h에 의존하지만, 런타임은 아님. 예를들어서, "C++마냥 template meta programming에 쓰이는 include를 사용"하는 미친코드를 적으면, C+9kwc는 그걸 include로 취급하지 않고, 일게 텍스트 덩어리로 취급하기에, 실제로 사용되는 template meta programming의 기능을 C로 컴파일 해주는것만 함. 그렇기에, TMP(template meta programming)을 사용함에도 컴파일 결과물은, 부가적인 include를 안함. ) (C++의 include랑은 딴판.)

실제 개발시 C & C+9kw로 프로그래밍 가능. 두가지는 같은 환경이기 때문. C+9kw는 C로 컴파일되기에, C런타임으로, C의 라이브러리 환경을 죄다 사용 가능. 반대로 C에서 C+9kw로 작성된 함수를 사용 가능. 근데 그과정에서 C+9kw의 함수를 C가 불러올때는, C+9kw의 경우, 템플릿이 붙거나 하는 특수한 경우엔 맹글링되기에, 그런 경우를 빼고는, 그냥 C에서 include후 다이렉트로 사용 가능.

C에다가 기능 확장을 존나 한거라 범용성에서 밀린다고 생각하지 않는다고 자부함. (사실 그건 C의 확장이라 범용성이 좋고, 9kw등의 표준 기능이 범용성이 좋아서 그렇다는게 펙트지만)

환경설정에 대한 공포 해소 : 그거 개발 환경에서만 환경설정이 필요한거지, 실행 환경은 환경설정과 무관히 걍 C임.

요약 : 런타임 = 최고, 컴파일러 = pcre땜에 무거움 (에초에 pcre가 C+9kw같은 고속 언어랑은 달리 무거운 라이브러리라)