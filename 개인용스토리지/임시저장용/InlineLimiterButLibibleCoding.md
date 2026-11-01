# InlineLimiterButLibible Coding

만드는 중...

## impl_macroper.h

```c
#pragma once

#ifndef _IMPL_MACROPER_H
# define _IMPL_MACROPER_H
    
    #ifdef MACRO_BRANCH_CORE //begin-if
    # error "MACRO_BRANCH_CORE must defined by impl_macroper.h not before including it."
    #else //pov : I am impl_macroper.h and the macro isn't defined yet.
    # define MACRO_BRANCH_CORE(DUMMY, MACRO, ...) MACRO
    #endif //end-if
    #ifdef MACRO_BRANCH //begin-if
    # error "MACRO_BRANCH must defined by impl_macroper.h not before including it."
    #else //pov : I am impl_macroper.h and the macro isn't defined yet.
    # define MACRO_BRANCH(THEN, ELSE, ...) MACRO_BRANCH_CORE(__VA_OPT__(~, ) ELSE, THEN)
    #endif //end-if
    
    #ifdef STRINGIFY_IMPL //end-if
    # error "STRINGIFY_IMPL must defined by impl_macroper.h not before including it."
    #else //pov : I am impl_macroper.h and the macro isn't defined yet.
    # define STRINGIFY_IMPL(X) #X
    #endif //end-if
    #ifdef  //begin-if
    # error "STRINGIFY must defined by impl_macroper.h not before including it."
    #else //pov : I am impl_macroper.h and the macro isn't defined yet.
    # define STRINGIFY(X) STRINGIFY_IMPL(X)
    #endif //end-if
    #ifdef CONCAT_IMPL //begin-if
    # error "CONCAT_IMPL must defined by impl_macroper.h not before including it."
    #else //pov : I am impl_macroper.h and the macro isn't defined yet.
    # define CONCAT_IMPL(X, Y) X ## Y
    #endif //end-if
    #ifdef CONCAT //begin-if
    # error "CONCAT must defined by impl_macroper.h not before including it."
    #else //pov : I am impl_macroper.h and the macro isn't defined yet.
    # define CONCAT(X, Y) CONCAT_IMPL(X, Y)
    #endif //end-if

#endif
```

## impl.h

```c
#pragma once

#ifndef _ILBL_H
# define _ILBL_H
    
    #include "impl_macroper.h"
    
    #if defined(_Try_force_inline) || define(_compiler_specific_core_force_inliner)
    # error "_Try_force_inline and _compiler_specific_core_force_inliner must defined by InlineLimiterButLibible not before including ilbl.h but _Try_force_inline or _compiler_specific_core_force_inliner was not."
    #elifdef _MSC_VER
         /* INLINE_RECURSION SYSTEM : which only in MSVC pragma */
        #define INLINE_RECURSION(X) _Pragma(STRINGIFY(inline_recursion(X)))
        #define _Try_force_inline static __forceinline
    #elif defined(__GNUC__) || defined(__clang__)
        #define _Try_force_inline static inline __attribute__((always_inline, hot, flatten))
    #else
        #warning "compiler isn't the supported to try inline-forcing compiler — MSVC, GCC, clang"
        #define _Try_force_inline static inline
    #endif
    
    #if defined(_ILBL_INLINE_DEPTH) && defined(_ILBL_INLINE_DEPTH_SET_CORE)
    # error "_ILBL_INLINE_DEPTH_SET_CORE must defined by InlineLimiterButLibible not before including ilbl.h"
    #elifdef _ILBL_INLINE_DEPTH
    # define _ILBL_INLINE_DEPTH_SET_CORE() _ILBL_INLINE_DEPTH_SET_CORE_OF_CORE(_ILBL_INLINE_DEPTH_VALUE)
    #else
    #
    #endif
    
    #ifdef _ILBL_INLINE_DEPTH_SET_CORE_OF_CORE
    # error "_ILBL_INLINE_DEPTH_SET_CORE_OF_CORE must defined by InlineLimiterButLibible not before including ilbl.h"
    #elifdef __GNUC__
    # define _ILBL_INLINE_DEPTH_SET_CORE_OF_CORE(X) _Pragma(STRINGIFY(GCC params (STRINGIFY(CONCAT(max-inline-recuresive-depth=, X))))))
    #elifdef _MSC_VER
    # define _ILBL_INLINE_DEPTH_SET_CORE_OF_CORE(X) _Pragma(STRINGIFY(inline_depth(X)))
    #else
    #
    #endif
    
    #if (defined(__GNUC__) || defined(_MSC_VER)) & defined(_ILBL_INLINE_DEPTH_SET)
    # error "_ILBL_INLINE_DEPTH_SET must defined by InlineLimiterButLibible not before including ilbl.h"
    #elifndef _ILBL_INLINE_DEPTH_SET
    # define _ILBL_INLINE_DEPTH_SET(...) MACRO_BRANCH(_ILBL_INLINE_DEPTH_SET_CORE_OF_CORE, _ILBL_INLINE_DEPTH_SET_CORE __VA_OPT__(, __VA_ARGS__))(__VA_ARGS__)
    #endif
    
    /* 일단은 여기까지 작성함. */
#endif
```