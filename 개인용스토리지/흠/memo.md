# memo

1. llptr.md
2. study

## 1. llptr.md

````markdown
# llptr.md

Low Level ptr관리를 간단하게 해주는 해더좀 기획해봄.

## llptr.h

```c
#pragma once

#ifndef _LLPTR_H
# define _LLPTR_H

#include <stddef.h>
#include <stdint.h>

/* NORMAL VERSION STARTED. PLZ SEE BELLOW TO SEE WHEN IT END */

#define _Try_force_inline \
        static inline __attribute__((always_inline, hot, flatten))

#define STUN_CASTING_FORM(T, V) \
        (T)V
#define CASTING_FORM(T, V)\
        STUN_CASTING_FORM(T, (V))

#define ModelicInlineFunctionDefer(type, var, func, macro) \
        _Try_force_inline type func(type var) \
        { \
                var = macro(var); /* this code is elimitate to optimize, when O1~O3... static inline flatten hot typecasting pure identity function is make compile it inline and make optimize as copy propagation and constant folding path  */ \
                return var; /* will Copy Elision */ \
        }

typedef void* ptr_t;

typedef union {
        /* si non optimization, ergo Temporary Materialization the Automatic Object */
        ptr_t ptr_v;
        uintptr_t uintptr_v;
        size_t size_v;
        //tip : sizeof(uintptr_t) == sizeof(size_t) == sizeof(ptr_t) est. ergo, sizeof(addr_t) == sizeof(ptr_t) (quia, union deterministic est.)
} addr_t;

#define addr_macro_typechecker(addr_v) \
        _Generic( \
                (addr_v), \
                addr_t: (addr_v) \
        )

#define ptr_macro_typechecker(ptr_v) \
        _Generic( \
                (ptr_v), \
                ptr_t: (ptr_v) \
        )
#define uintptr_macro_typechecker(uintptr_v) \
        _Generic( \
                (uintptr_v), \
                uintptr_t: (uintptr_v) \
        )
#define size_macro_typechecker(size_v) \
        _Generic( \
                (size_v), \
                size_t: (size_v) \
        )

#define addr_inline_defer(func_name, macro_name) \
        ModelicInlineFunctionDefer(addr_t, addr_v, func_name, macro_name)

/* in Compound Literal : Temporary Materialization the Automatic Object if static-inline-flatten-hot-typecasting-pure-identity-function fails to make compile it inline and make optimize as copy propagation and constant folding path because non optimization */
/* when CASTING_FORM : Type Punning non Value Conversion */
/* when acess size_v : Type Punning non Value Conversion */
#define addr_macro_size2uintptr(addr_v) \
        addr_macro_typechecker( \
                STUN_CASTING_FORM( \
                        addr_t, \
                        { \
                                .uintptr_v = CASTING_FORM( \
                                        uintptr_t, \
                                        addr_macro_typechecker(addr_v).size_v \
                                ) \
                        } \
                ) \
        )
/* in Compound Literal : Temporary Materialization the Automatic Object if static-inline-flatten-hot-typecasting-pure-identity-function fails to make compile it inline and make optimize as copy propagation and constant folding path because non optimization */
/* when CASTING_FORM : Type Punning non Value Conversion */
/* when acess uintptr_v : Type Punning non Value Conversion */
#define addr_macro_uintptr2size(addr_v) \
        addr_macro_typechecker( \
                STUN_CASTING_FORM( \
                        addr_t, \
                        { \
                                .size_v = CASTING_FORM( \
                                        size_t, \
                                        addr_macro_typechecker(addr_v).uintptr_v \
                                ) \
                        } \
                ) \
        )
/* in Compound Literal : Temporary Materialization the Automatic Object if static-inline-flatten-hot-typecasting-pure-identity-function fails to make compile it inline and make optimize as copy propagation and constant folding path because non optimization */
/* when CASTING_FORM : Type Punning non Value Conversion */
/* when acess ptr_v : Type Punning non Value Conversion */
#define addr_macro_ptr2uintptr(addr_v) \
        addr_macro_typechecker( \
                STUN_CASTING_FORM( \
                        addr_t, \
                        { \
                                .uintptr_v = CASTING_FORM( \
                                        uintptr_t, \
                                        addr_macro_typechecker(addr_v).ptr_v \
                                ) \
                        } \
                ) \
        )
/* in Compound Literal : Temporary Materialization the Automatic Object if static-inline-flatten-hot-typecasting-pure-identity-function fails to make compile it inline and make optimize as copy propagation and constant folding path because non optimization */
/* when CASTING_FORM : Type Punning non Value Conversion */
/* when acess uintptr_v : Type Punning non Value Conversion */
#define addr_macro_uintptr2ptr(addr_v) \
        addr_macro_typechecker( \
                STUN_CASTING_FORM( \
                        addr_t, \
                        { \
                                .ptr_v = CASTING_FORM( \
                                        ptr_t, \
                                        addr_macro_typechecker(addr_v).uintptr_v \
                                ) \
                        } \
                ) \
        )

#define addr_macro_size2ptr(addr_v) \
        addr_macro_uintptr2ptr( \
        addr_macro_size2uintptr( \
                addr_v \
        ) \
        )
#define addr_macro_ptr2size(addr_v) \
        addr_macro_uintptr2size( \
        addr_macro_ptr2uintptr( \
                addr_v \
        ) \
        )

addr_inline_defer(
        addr_typechecker,
        addr_macro_typechecker
)

ModelicInlineFunctionDefer(ptr_t, ptr_v, ptr_typechecker, ptr_macro_typechecker)
ModelicInlineFunctionDefer(uintptr_t, uintptr_v, uintptr_typechecker, uintptr_macro_typechecker)
ModelicInlineFunctionDefer(size_t, size_v, size_typechecker, size_macro_typechecker)

/* Punning feature of addr_size2uintptr not supported in debug(O0) without opmimization. if not debug, Temporaray Materialization is blocked to optimized. */
addr_inline_defer(
        addr_size2uintptr,
        addr_macro_size2uintptr
)
/* Punning feature of addr_uintptr2size not supported in debug(O0) without opmimization. if not debug, Temporaray Materialization is blocked to optimized. */
addr_inline_defer(
        addr_uintptr2size,
        addr_macro_uintptr2size
)
/* Punning feature of addr_ptr2uintptr not supported in debug(O0) without opmimization. if not debug, Temporaray Materialization is blocked to optimized. */
addr_inline_defer(
        addr_ptr2uintptr,
        addr_macro_ptr2uintptr
)
/* Punning feature of addr_uintptr2ptr not supported in debug(O0) without opmimization. if not debug, Temporaray Materialization is blocked to optimized. */
addr_inline_defer(
        addr_uintptr2ptr,
        addr_macro_uintptr2ptr
)

/* Punning feature of addr_size2ptr not supported in debug(O0) without opmimization. if not debug, Temporaray Materialization is blocked to optimized. */
addr_inline_defer(
        addr_size2ptr,
        addr_macro_size2ptr
)
/* Punning feature of addr_ptr2size not supported in debug(O0) without opmimization. if not debug, Temporaray Materialization is blocked to optimized. */
addr_inline_defer(
        addr_ptr2size,
        addr_macro_ptr2size
)

#define inline_cast_defer(from_t, to_t, func_name, macro_name) \
        _Try_force_inline to_t func_name(from_t v) \
        { \
                return macro_name(v); /* will Copy Elision, so... flatten aren't actually need. it's actually almost high flatten-like */ \
        }

/* in Compound Literal : Temporary Materialization the Automatic Object if static-inline-flatten-hot-typecasting-pure-identity-function fails to make compile it inline and make optimize as copy propagation and constant folding path because non optimization */
#define macro_ptr2addr(ptr) \
        addr_macro_typechecker( \
                STUN_CASTING_FORM( \
                        addr_t, \
                        { .ptr_v = ptr_macro_typechecker(ptr) } \
                ) \
        )
/* when acess ptr_v : Type Punning non Value Conversion */
#define macro_addr2ptr(addr_v) \
        ptr_macro_typechecker( \
                addr_macro_typechecker(addr_v).ptr_v \
        )
/* in Compound Literal : Temporary Materialization the Automatic Object if static-inline-flatten-hot-typecasting-pure-identity-function fails to make compile it inline and make optimize as copy propagation and constant folding path because non optimization */
#define macro_uintptr2addr(uintptr) \
        addr_macro_typechecker( \
                STUN_CASTING_FORM( \
                        addr_t, \
                        { .uintptr_v = uintptr_macro_typechecker(uintptr) } \
                ) \
        )
/* when acess uintptr_v : Type Punning non Value Conversion */
#define macro_addr2uintptr(addr_v) \
        uintptr_macro_typechecker( \
                addr_macro_typechecker(addr_v).uintptr_v \
        )
/* in Compound Literal : Temporary Materialization the Automatic Object if static-inline-flatten-hot-typecasting-pure-identity-function fails to make compile it inline and make optimize as copy propagation and constant folding path because non optimization */
#define macro_size2addr(size) \
        addr_macro_typechecker( \
                STUN_CASTING_FORM( \
                        addr_t, \
                        { .size_v = size_macro_typechecker(size) } \
                ) \
        )
/* when acess size_v : Type Punning non Value Conversion */
#define macro_addr2size(addr_v) \
        size_macro_typechecker( \
                addr_macro_typechecker(addr_v).size_v \
        )

/* Punning feature of ptr2addr not supported in debug(O0) without opmimization. if not debug, Temporaray Materialization is blocked to optimized. */
inline_cast_defer(ptr_t, addr_t, ptr2addr, macro_ptr2addr)
inline_cast_defer(addr_t, ptr_t, addr2ptr, macro_addr2ptr)
/* Punning feature of uintptr2addr not supported in debug(O0) without opmimization. if not debug, Temporaray Materialization is blocked to optimized. */
inline_cast_defer(uintptr_t, addr_t, uintptr2addr, macro_uintptr2addr)
inline_cast_defer(addr_t, uintptr_t, addr2uintptr, macro_addr2uintptr)
/* Punning feature of size2addr not supported in debug(O0) without opmimization. if not debug, Temporaray Materialization is blocked to optimized. */
inline_cast_defer(size_t, addr_t, size2addr, macro_size2addr)
inline_cast_defer(addr_t, size_t, addr2size, macro_addr2size)

#define macro_ptr2uintptr(ptr_v) \
        macro_addr2uintptr( \
        addr_macro_ptr2uintptr( \
        macro_ptr2addr( \
                ptr_v \
        ) \
        ) \
        )
#define macro_uintptr2ptr(uintptr_v) \
        macro_addr2ptr( \
        addr_macro_uintptr2ptr( \
        macro_uintptr2addr( \
                uintptr_v \
        ) \
        ) \
        )
#define macro_size2uintptr(size_v) \
        macro_addr2uintptr( \
        addr_macro_size2uintptr( \
        macro_size2addr( \
                size_v \
        ) \
        ) \
        )
#define macro_uintptr2size(size_v) \
        macro_addr2size( \
        addr_macro_uintptr2size( \
        macro_uintptr2addr( \
                size_v \
        ) \
        ) \
        )
#define macro_ptr2size(ptr_v) \
        macro_addr2size( \
        addr_macro_ptr2size( \
        macro_ptr2addr( \
                ptr_v \
        ) \
        ) \
        )
#define macro_size2ptr(size_v) \
        macro_addr2ptr( \
        addr_macro_size2ptr( \
        macro_size2addr( \
                size_v \
        ) \
        ) \
        )

/* Punning feature of ptr2uintptr not supported in debug(O0) without opmimization. if not debug, Temporaray Materialization is blocked to optimized. */
inline_cast_defer(ptr_t, uintptr_t, ptr2uintptr, macro_ptr2uintptr)
/* Punning feature of uintptr2ptr not supported in debug(O0) without opmimization. if not debug, Temporaray Materialization is blocked to optimized. */
inline_cast_defer(uintptr_t, ptr_t, uintptr2ptr, macro_uintptr2ptr)
/* Punning feature of size2uintptr not supported in debug(O0) without opmimization. if not debug, Temporaray Materialization is blocked to optimized. */
inline_cast_defer(size_t, uintptr_t, size2uintptr, macro_size2uintptr)
/* Punning feature of uintptr2size not supported in debug(O0) without opmimization. if not debug, Temporaray Materialization is blocked to optimized. */
inline_cast_defer(uintptr_t, size_t, uintptr2size, macro_uintptr2size)
/* Punning feature of ptr2size not supported in debug(O0) without opmimization. if not debug, Temporaray Materialization is blocked to optimized. */
inline_cast_defer(ptr_t, size_t, ptr2size, macro_ptr2size)
/* Punning feature of size2ptr not supported in debug(O0) without opmimization. if not debug, Temporaray Materialization is blocked to optimized. */
inline_cast_defer(size_t, ptr_t, size2ptr, macro_size2ptr)

/* NORMAL VER IS END, PLZ SEE BELLOW */

/* BELLOW CODE IS HAND PUNNING OPTIMIZED FUNCTIONS. VERY CLEAR, TRIVIAL. but if you optimized with optimized compiler which like-clang, this is not need. because normal version is be punning optimized */

#define hand_optimized_macro_ptr2uintptr(ptr_v) \
        uintptr_macro_typechekcer( \
                CASTING_FORM( \
                        uintptr_t, \
                        ptr_macro_typechecker(ptr_v) \
                ) \
        )
#define hand_optmized_macro_uintptr2ptr(uintptr_v) \
        ptr_macro_typechecker( \
                CASTING_FORM( \
                        ptr_t, \
                        uintptr_macro_typechecker(uintptr_v) \
                ) \
        )
#define hand_optimized_macro_size2uintptr(size_v) \
        uintptr_macro_typechecker( \
                CASTING_FORM( \
                        uintptr_t \
                        size_macro_typechecker(size_v) \
                ) \
        )
#define hand_optimized_macro_uintptr2size(uintptr_v) \
        size_macro_typechecker( \
                CASTING_FORM( \
                        uintptr_v, \
                        uintptr_macro_typechecker(uintptr_v) \
                ) \
        )

#define hand_optimized_macro_ptr2size(ptr_v) \
        hand_optimized_macro_uintptr2size( \
        hand_optimized_macro_ptr2uintptr( \
                ptr_v \
        ) \
        )
#define hand_optimized_macro_size2ptr(size_v) \
        hand_optimized_macro_uintptr2ptr( \
        hand_optimized_macro_size2uintptr( \
                ptr_v \
        ) \
        )

inline_cast_defer(ptr_t, uintptr_t, hand_optimized_ptr2uintptr, hand_optimized_macro_ptr2uintptr)
inline_cast_defer(uintptr_t, ptr_t, hand_optimized_uintptr2ptr, hand_optimized_macro_uintptr2ptr)
inline_cast_defer(size_t, uintptr_t, hand_optimized_size2uintptr, hand_optimized_macro_size2uintptr)
inline_cast_defer(uintptr_t, size_t, hand_optimized_uintptr2size, hand_optimized_macro_uintptr2size)
inline_cast_defer(ptr_t, size_t, hand_optimized_ptr2size, hand_optimized_macro_ptr2size)
inline_cast_defer(size_t, ptr_t, hand_optimized_size2ptr, hand_optimized_macro_size2ptr)

#define hand_optimized_macro_addr2ptr macro_addr2ptr
#define hand_optimized_macro_addr2uintptr macro_addr2uintptr
#define hand_optimized_macro_addr2size macro_addr2size

// the three RVO optimized functions
#define hand_optimized_addr2ptr addr2ptr
#define hand_optimized_addr2uintptr addr2uintptr
#define hand_optimized_addr2size addr2size

// the four RVO optimized functions (typechekcers)
#define hand_optimized_addr_macro_typechecker addr_macro_typechecker
#define hand_optimized_ptr_macro_typechecker ptr_macro_typechecker
#define hand_optimized_uintptr_macro_typechecker uintptr_macro_typechecker
#define hand_optimized_size_macro_typechecker size_macro_typechecker

#define hand_optimized_addr_typechecker addr_typechecker
#define hand_optimized_ptr_typechecker ptr_typechecker
#define hand_optimized_uintptr_typechecker uintptr_typechecker
#define hand_optimized_size_typechecker size_typechecker

// other optimizible functions

#define hand_optimized_macro_addr_ptr2uintptr_then_addr2uintptr(v) \
	macro_addr2ptr( \
	hand_optimized_macro_ptr2uintptr( \
		v \
	) \
	)
#define hand_optimized_macro_addr_uintptr2ptr_then_addr2uintptr(v) \
	macro_addr2uintptr( \
	hand_optimized_macro_uintptr2ptr( \
		v \
	) \
	)
#define hand_optimized_macro_addr_size2uintptr_then_addr2uintptr(v) \
	macro_addr2size( \
	hand_optimized_macro_size2uintptr( \
		v \
	) \
	)
#define hand_optimized_macro_addr_uintptr2size_then_addr2size(v) \
	macro_addr2uintptr( \
	hand_optimized_macro_uintptr2size( \
		v \
	) \
	)
#define hand_optimized_macro_addr_ptr2size_then_addr2size(v) \
	macro_addr2ptr( \
	hand_optimized_macro_ptr2size( \
		v \
	) \
	)
#define hand_optimized_macro_addr_size2ptr_then_addr2ptr(v) \
	macro_addr2size( \
	hand_optimized_macro_size2ptr( \
		v \
	) \
	)

#endif
```

## test.c

```c
#include <stdio.h>
#include "llptr.h"

#define pass ((void)0)

typedef const char const_char;
typedef const_char* immutable_str_t;
typedef immutable_str_t imm_str_t;

const_char test[] = "rikaidekinaina\nsono hisuterikuna jouchou dobutsumitaide\nmada ugokenaina\nhiyorimino messgage baketa meirono sue";

int main(void)
{
        imm_str_t seijinkunshidearitai = (imm_str_t) &test;
        uintptr_t num = ptr2uintptr(CASTING_FORM(void*, seijinkunshidearitai));
        printf("%lu\n", num);
        return 0;
}
```

## test.s

### when O0

```x86asm
        .file        "test.c"
        .text
        .globl        main                            # -- Begin function main
        .p2align        4
        .type        main,@function
main:                                   # @main
# %bb.0:
        pushq        %rbp
        movq        %rsp, %rbp
        subq        $48, %rsp
        movl        $0, -28(%rbp)
        leaq        test(%rip), %rax
        movq        %rax, -40(%rbp)
        movq        -40(%rbp), %rax
        movq        %rax, -8(%rbp)
        movq        -8(%rbp), %rax
        movq        %rax, -24(%rbp)
        movq        -24(%rbp), %rax
        movq        %rax, -16(%rbp)
        movq        -16(%rbp), %rax
        movq        %rax, -48(%rbp)
        movq        -48(%rbp), %rsi
        leaq        .L.str(%rip), %rdi
        movb        $0, %al
        callq        printf@PLT
        xorl        %eax, %eax
        addq        $48, %rsp
        popq        %rbp
        retq
.Lfunc_end0:
        .size        main, .Lfunc_end0-main
                                        # -- End function
        .type        test,@object                    # @test
        .section        .rodata,"a",@progbits
        .globl        test
        .p2align        4, 0x0
test:
        .asciz        "rikaidekinaina\nsono hisuterikuna jouchou dobutsumitaide\nmada ugokenaina\nhiyorimino messgage baketa meirono sue"
        .size        test, 111

        .type        .L.str,@object                  # @.str
        .section        .rodata.str1.1,"aMS",@progbits,1
.L.str:
        .asciz        "%lu\n"
        .size        .L.str, 5

        .ident        "Ubuntu clang version 21.1.8 (6ubuntu1)"
        .section        ".note.GNU-stack","",@progbits
        .addrsig
        .addrsig_sym printf
        .addrsig_sym test
```

### when O1

```x86asm
        .file        "test.c"
        .text
        .globl        main                            # -- Begin function main
        .p2align        4
        .type        main,@function
main:                                   # @main
# %bb.0:
        pushq        %rax
        leaq        .L.str(%rip), %rdi
        leaq        test(%rip), %rsi
        xorl        %eax, %eax
        callq        printf@PLT
        xorl        %eax, %eax
        popq        %rcx
        retq
.Lfunc_end0:
        .size        main, .Lfunc_end0-main
                                        # -- End function
        .type        test,@object                    # @test
        .section        .rodata,"a",@progbits
        .globl        test
        .p2align        4, 0x0
test:
        .asciz        "rikaidekinaina\nsono hisuterikuna jouchou dobutsumitaide\nmada ugokenaina\nhiyorimino messgage baketa meirono sue"
        .size        test, 111

        .type        .L.str,@object                  # @.str
        .section        .rodata.str1.1,"aMS",@progbits,1
.L.str:
        .asciz        "%lu\n"
        .size        .L.str, 5

        .ident        "Ubuntu clang version 21.1.8 (6ubuntu1)"
        .section        ".note.GNU-stack","",@progbits
        .addrsig
        .addrsig_sym test
```

### when O2

```x86asm
        .file        "test.c"
        .text
        .globl        main                            # -- Begin function main
        .p2align        4
        .type        main,@function
main:                                   # @main
# %bb.0:
        pushq        %rax
        leaq        .L.str(%rip), %rdi
        leaq        test(%rip), %rsi
        xorl        %eax, %eax
        callq        printf@PLT
        xorl        %eax, %eax
        popq        %rcx
        retq
.Lfunc_end0:
        .size        main, .Lfunc_end0-main
                                        # -- End function
        .type        test,@object                    # @test
        .section        .rodata,"a",@progbits
        .globl        test
        .p2align        4, 0x0
test:
        .asciz        "rikaidekinaina\nsono hisuterikuna jouchou dobutsumitaide\nmada ugokenaina\nhiyorimino messgage baketa meirono sue"
        .size        test, 111

        .type        .L.str,@object                  # @.str
        .section        .rodata.str1.1,"aMS",@progbits,1
.L.str:
        .asciz        "%lu\n"
        .size        .L.str, 5

        .ident        "Ubuntu clang version 21.1.8 (6ubuntu1)"
        .section        ".note.GNU-stack","",@progbits
        .addrsig
        .addrsig_sym test
```

### when O3

```x86asm
        .file        "test.c"
        .text
        .globl        main                            # -- Begin function main
        .p2align        4
        .type        main,@function
main:                                   # @main
# %bb.0:
        pushq        %rax
        leaq        .L.str(%rip), %rdi
        leaq        test(%rip), %rsi
        xorl        %eax, %eax
        callq        printf@PLT
        xorl        %eax, %eax
        popq        %rcx
        retq
.Lfunc_end0:
        .size        main, .Lfunc_end0-main
                                        # -- End function
        .type        test,@object                    # @test
        .section        .rodata,"a",@progbits
        .globl        test
        .p2align        4, 0x0
test:
        .asciz        "rikaidekinaina\nsono hisuterikuna jouchou dobutsumitaide\nmada ugokenaina\nhiyorimino messgage baketa meirono sue"
        .size        test, 111

        .type        .L.str,@object                  # @.str
        .section        .rodata.str1.1,"aMS",@progbits,1
.L.str:
        .asciz        "%lu\n"
        .size        .L.str, 5

        .ident        "Ubuntu clang version 21.1.8 (6ubuntu1)"
        .section        ".note.GNU-stack","",@progbits
        .addrsig
        .addrsig_sym test
```
````

## 2. study

````markdown
# clang _Try_force_inline만들고 알아보기 ft. llptr.h (n.b. 지극히 개인용 노트고, 내 기억을 잊어버리면 나도 못읽는, 미래신경안쓴 연습장식 디지털 포스트잇이다.)

always_inline
 - O0 : 원칙적으로 always inline를 추가 최적화 데드 코드 제거, 상수 폴딩 등) 없이 함. 이로인해 더 느려질수 있다. 가변인자, 간접호출, 제귀호출시 경고나 에러로 인라인화 실패가 일어난다.
 - O1 : 코드 크기가 크게 늘지 않는 선에서 static inline이 부분적 허용되고 always_inline이 잇어야 인라이닝이 수행된다 할수 있다. 불필요한 임시 변수가 제가되고 가벼운 최적화가 덧붙혀진다.  가변인자, 간접호출, 제귀호출시 경고나 에러로 인라인화 실패가 일어난다. TCO(Tail Call Optimization) 이 기본 활성화되나, `-O2`부터 본격적인 분석 적용되는 경우가 많다. call대신 단순 jmp를 쓰게 하는 경우가 많다. 만약 디버깅모드에서 강제 TCO를 원하면 `[[clang::musttail]] return 함수();`문법을 사용해 컴파일러에게 강제할수 있다.
 - O2 : 컴파일러가 표준 인라인 패스(Heuristic)를 적극적으로 활용하며, 루프 invariant 제거 등 강력한 최적화 패스들이 연쇄적으로 적용된다. 가변인자, 간접호출, 제귀호출시 경고나 에러로 인라인화 실패가 일어나거나, '간접 호출 승격(Indirect Call Promotion)' 및 '탈가상화(Devirtualization)' 최적화로, 정적 분석이나 PGO(프로필 기반 최적화)를 통해 타겟 함수가 명확해지면 인라인을 포함한 모든 최적화가 연쇄 적용될수도, 아니면 인라이닝을 포기할수도 있다. 제귀 호출부는, 1~2번만 풀리고 그 이후 깊이의 제귀 호출부에선 인라인화에 실패할수 있다. TCO(Tail Call Optimization) 이 기본 활성화되었으며 보통 이정도 레벨이면 본격적인 분석 역시 적용되어있다. call대신 단순 jmp를 쓰게 하는 경우가 많다. 만약 디버깅모드에서 강제 TCO를 원하면 `[[clang::musttail]] return 함수();`문법을 사용해 컴파일러에게 강제할수 있다. Recursion-to-Loop최적화가 활성화되며, 임시 변수 레지스터 등 원래는 TCO가 불가능한 코드를 임시 변수(Accumulator)를 레지스터에 할당하는 방식의 반복문 루프로 재조립한다. 조금만 복잡해져도 포기하는경우가 많다. 이는 `O3`에서도 그렇다.
 - O3 : `-O2`보다 더 공격적인 인라인화와 자동 벡터화(SIMD) 등이 결합된다. 최고 수준인 `-O3`에서도 무조건 작동하는것이 원칙이지만, 하드웨어적 제약이나 언어 규격상의 한계로, 인라인화가 절대 불가능한 실패 경우들이 존재한다. 간접호출이고 타깃도 불확실하고, 정적 분석을 이용해 타겟을 단 하나로 좁힌다는 전제를 실패했거나 간접호출승격되지 않았거나 하거나 패스가 그걸 구출해 인라인화하는것에 실패했거나, 하는 등, 컴파일에 코드를 넣는게 불가능한 상황에선, 실패할수 있고, 가변 함수 인자는, ABI수준이라 안전을 위해, 위험성이 원천 차단되었고, 인라인 어셈블리에 의해 특정 하드웨어 레지스터가 고정적으로 사용되기에, 라벨 중복 오류나 레지스터 할당 충돌이 일어나는걸 안전하게 재배치 불가능하면 인라인화에 실패하고, 심드셋 명시에서 `__attribute__((target("avx512f")))`로 하는것이 대표적인 예시인, 하드웨어 타겟 불일치가 일어나도 인라인화 실패하고, 제귀함수가 max-recursive-inline-depth에 걸리면, 최대한 인라이닝하되, 그 이후론 call을 쓴다. 에러까지도 날수 있다. clang에서는 말이다. 참고로... "static inline에서 과도한 인라이닝으로 인해 명령어 캐시(I-Cache) 미스가 발생하여 오히려 `-O2`보다 속도가 느려지는 역효과가 날 가능성도 있다".... 여기서도 그렇다.

hot inline
 - O0 : 무시된다
 - O1 : 기본 최적화만 적용되고, 섹션 분리는 거의 일어나지 않는다. 인라이닝 기준 (인라이닝 비용 계산시 가산점을 받는다. Threshold에서 약간의 이점)은 약간 완화되는 정도의 영향이다.
 - O2 : `.text.hot` 전용 섹션으로 이동하고, 케시 적중률이 극대화된다. 그리고 인라이닝 우선순위가 급상승된다. 다시말해, 꽤 반영되는거다. (이 등급부터(i.e. `-O3`도)는 Threshold(비용한도)를 대폭 높여주고, 크기가 커서 거절당했을만한 static inline이 강제로 펼쳐지듯 인라이닝된다. `-O1`이 드라마틱한 변화가 없었던것과 대조적이다) 실패해도 hot공간에서 적중률을 극대화하고 실행속도를 빠르게 하는 등의 빌드를 해준다.
 - O3 : `.text.hot` 전용 섹션으로 이동하고, 루프 풀기 등 공격적 최적화가 이루어지며, 무조건 인라이닝에 가깝게 작동한다. 실패해도 hot공간에서 적중률을 극대화하고 실행속도를 빠르게 하는 등의 빌드를 해준다.

flatten : 가장 빠르게 실행되야 하는 핵심 진입점처럼 평탄한 바이너리처럼 된다. 그리고 간접 호출이나 제귀함수로는 평탄화를 못해서 컴파일러가 일정 단계에서 중단한다. 근데 너무 코드가 큰 함수를 호출하면 Code Bloat이 일어날 우려가 있다.
 - O0 : 무시된다
 - O1 : 제한적 활성화로, flatten이 지정된 함수 내부의 호출만 예외적으로 적극 인라이닝한다. 인라이닝 강제성 측면에선 비용 검사가 완화된다.
 - O2 : 강력 활성화로, 비용 검사를 거의 무시하는듯 행동한다. 크기 제약을 거의 무시하고, 냅 호출을 전부 풀어헤친다.
 - O3 : 최대 활성화로, 무조건 수행 수준이다. 간접 호출이나 특수 상황을 제외하고, 완벽하게 평탄화된다.

응용
 + static inline + flatten : O1에서 원래 static inline은 크기가 작아야 인라이닝되지만, 내부는 꽤 적극적으로 펼쳐지며 (조건부 결합 느낌), O2~O3에선, 거의 제약을 무시하고 하나의 직렬화된 코드를 만들듯, 호출계층을 부수려는듯 하는 경향성을 만들어놓을수 있음. 그리고, execute_pipeline의 크기가 너무 커지면, 너무 커져서 static inline을 거절당할수도 있다. 변수가 ㅈㄴ 많아지니 변수 할당 최적화가 일어날 가능성이 생긴다. 다만 최적화가 되야지 의미가 있지만
 + static inline + hot :  호출하는 모든곳에 집어넣고, 혹은 덩치가 커서 다 못넣더라도 가장 빠른 특수 메모리 영역에 모아놓는 등의 행동인데, 코드를 flatten조합처럼 코드를 강제로 무너트리는 파괴적인 방식이 아니라, CPU캐시 효율과 컴파일러의 비용 모델을 완벽하게 활용해서 성능을 극한으로 끌어올리는 가장 안전하고 정석적인 고성능 조합. 근데 뭐... `O1`에서는, 메모리 섹션 분리까지는 안가고, 최적 inline은 커녕, 인라이닝 기준이 약간 느슨해지는 정도다. 루프전개나 자동 백터화 등으로 고속 레지스터로 돌리려 할것이다.
 + static inline + hot + flatten : hot을 시도하거나 flatten을 시도하는 등 탐욕적인 인라이닝 시도일 뿐, 그냥 뭐가 걸릴지 예측 안되므로, 두 기능중 하나가 필요 없을때 쓰면 도박인것이다. 근데, 어짜피 두개중 뭐가 반영되도 상관없을때 쓴다. 변수 할당등이, SSA(변수 통합 최적화)로 급한 순서대로 Register Spilling까지 동원해서, 존나 처리하려고 안달이 난다. 물론 불필요한 변수 제거에 있어선 DCE(Dead Code Elimintation)과 상수폴딩 등으로 임시변수들을 싹 죽이고 직통으로 연결시킨다 (O1). 그리고 CSE(Common Subexpr Elimination)과 상수 전파 등으로, 중복 개산식과 변수가 하나로 통일되며 코드 부피가 대폭 축약되고 (O2), 컴파일러가 더 축약 가능하다고 판단하면, 아예, 함수 내부 연산 자체를 수학적으로 재조립하여, 상수화 하는 등의 최적화를 한다. (O3)
 + static + inline + always inline + flatten : 평탄화 폭주
 + static + inline + always inline + hot : 뭐.... static + inline + always inline도 100%니까 120%응원이려나
 + static + inline + always inline + hot + flatten : 인라인이 뭔 메크로냐 ㅅㅂ

## 공부로 얻은 내용

`(union명){.필드명 = 값}`의 속도 (Compound Literal and Designated Initializer)

union typedef타입인 t타입의 변수 v에 대해, `v = (t){.필드명 = (동일 바이트 비동일 타입의 캐스팅)x.다른필드명};`의 속도

근데 그 작업이 단 하나의 깊이의 static inline always inline hot flatten 함수 내에서 `v = Generic((v), t: (t){.필드명 = (암튼 타입)v.다른필드명});` 라는 형태나, 혹은, 아예 변수 할당식은 하나 있었는데, 인수변수 v에 대하여, 그냥 단 한줄만에, 여러가지 캐스팅과, 복합리터럴 식으로, 유니언화->유니언편집->유니언값 순으로, Generic에 의해 한단계 한단계 격리하여, 각 과정당 타입에서 도망갈수 없게 만들었더니, O1~O3에선 변수가 증발하고, O0에선 그냥 변수를 돌리는 바보같은 구문이 나왔어.

Q. Generic에서 중간에 변수할당? 그렇단건 원래 r-value는 비최적화시, 임시변수로라도 할당될수밖에 없는거임?
A. yes. Temporary object는 메모리상에선 물리적으로 할당될수밖에 없음. 복합리터럴이나 케스팅 결과는, 해당 r-value계산식에선 수명을 보장해야할수밖에 없음.

Pruning과 C23반환값 최적화나, 비최적화 표준에서 r-value저장이 뭔소린지 모르겠음.
아, 가지치기구나.

C23표준에서, RVO(Return Value Optimization)를 통해서, 에초에 밖에 있는 최종 목적지 변수에 자동으로 적어버림.

Q. r-value저장을 부르는 전문용어 없음?
A. Temporary Materialization (임시 구체화  실체화)...

Temporary Materialization이라...

_Generic내부에 항등함수나 다름없는 casting과 union할당과 재할당(근데 사실 같은 유니온 타입인데, 사용된 유니온 필드만 바꾼것)을 하는 고장 길이 변수 관리 (근데 그 변수가 마침 주소 크기에 딱 맞음)구문만 있다면, 정확히는, typedef union {t1 v1; t2 v2;} t인 t타입(참고로, t1과 t2는 바이트는 같지만 동시사용은 안된다)의 v에 대하여 v = _Generic((v), t: (t){.v2 = (t1)v.v1});식으로 하는 코드는 Temporary Materialization이 몇번 일어나는겨?

아... Sub-expression이 컴파일 타임 선택기니까, 형식적 캐스팅은 구체화는 아니고, 복합 리터럴부터는 Automatic Object구나...

Temporary Materialization the Automatic Object

공용체에서 형식적으로 단순 값 읽기라서, 딱히 sizeof(void*)바이트만큼의 공용체(모든 맴버들의 크기가 그래서 그럼)의 맴버를 읽는것 & 값을 바꾸지 않는 형식적 케스팅 vs 몇 바이트단위로 CPU가 다루는데 문제없는 실질적으로 공용체가 필요한 공용체 값 접근 & 값을 바꾸는 내장 케스팅

이름을 바꾸는것과, 쪼개는것의 차이임.

전자(타입변경)과 후자(정보변경)을 구분하는 용어 있나? r-value를 말할때?

1. 전자 : Type Punning
2. 후자 : Value Conversion?

Type Punning non Value Conversion

"Temporary Materialization the Automatic Object if static-inline-flatten-hot-typecasting-pure-identity-function fails to make compile it inline and make optimize as copy propagation and constant folding path because non optimization" 이해가능한 문장인가?

"as C23 std RVO(Return Value Optimization) will adapt" vs "as C23 std RVO(Return Value Optimization) will adopt" vs "as C23 std RVO(Return Value Optimization) will adapted"

"as C23 std RVO(Return Value Optimization) will adapt" vs "as C23 std RVO(Return Value Optimization) will adopt" vs "as C23 std RVO(Return Value Optimization) will adapted"

아니 코드의 특정 위치에 RVO가 적용될거라 말하려면

"will Copy Elision"은?

O0에서 그저 공용체가 아니었던 8B값을 자신의 타입을 맴버로 가지는 8B공용체에 넣는거라, O1이었다면, 그냥 사라졌을수도 있는 놈이 안사라지는걸, 사라지도록 최적화하는법...같은게 있을리가.

우회적인것밖에 없군.

설마, 저기서 말한 optimization은 clang기준이엇는데, 알고보니 표준 C23에서는, O1~O3모드에 오직 "v = v만참조한 그냥 항등인 형식적 재할당; return v"나 "return 식"꼴은, RVO상 flatten과 다를바가 없는것과 O1~O3에서 컴파일러가 변수 Punning을 할것이 권장되는건가?

아 C23표준엔 최적화 개념이 없구나...
````