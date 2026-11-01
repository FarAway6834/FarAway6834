# InlineLimiterButLibible Coding

만드는 중...

## impl_macroper.h

```c
#pragma once

#ifndef _IMPL_MACROPER_H
# define _IMPL_MACROPER_H
    
    #ifdef MACRO_BRANCH_CORE
    # error "MACRO_BRANCH_CORE must defined by impl_macroper.h not before including it."
    #else
    # define MACRO_BRANCH_CORE(DUMMY, MACRO, ...) MACRO
    #endif
    #ifdef MACRO_BRANCH
    # error "MACRO_BRANCH must defined by impl_macroper.h not before including it."
    #else
    # define MACRO_BRANCH(THEN, ELSE, ...) MACRO_BRANCH_CORE(__VA_OPT__(~, ) ELSE, THEN)
    #endif
    
    #ifdef STRINGIFY_IMPL
    # error "STRINGIFY_IMPL must defined by impl_macroper.h not before including it."
    #else
    # define STRINGIFY_IMPL(X) #X
    #endif
    #ifdef 
    # error "STRINGIFY must defined by impl_macroper.h not before including it."
    #else
    # define STRINGIFY(X) STRINGIFY_IMPL(X)
    #endif
    #ifdef CONCAT_IMPL
    # error "CONCAT_IMPL must defined by impl_macroper.h not before including it."
    #else
    # define CONCAT_IMPL(X, Y) X ## Y
    #endif
    #ifdef CONCAT
    # error "CONCAT must defined by impl_macroper.h not before including it."
    #else
    # define CONCAT(X, Y) CONCAT_IMPL(X, Y)
    #endif

#endif
```

## impl.h

```c
#pragma once

#ifndef _ILBL_H
# define _ILBL_H
    
    #include "impl_macroper.h"
    
    #ifdef _Try_force_inline
    # error "_Try_force_inline must defined by InlineLimiterButLibible not before including ilbl.h"
    #elifdef _MSC_VER
        #ifdef _ILBL_INLINE_DEPTH_SET_CORE_OF_CORE
        # error "_ILBL_INLINE_DEPTH_SET_CORE_OF_CORE must defined by InlineLimiterButLibible not before including ilbl.h"
        #else
        # define _ILBL_INLINE_DEPTH_SET_CORE_OF_CORE(X) _Pragma(STRINGIFY(inline_depth(X)))
        #endif
        
        #define INLINE_RECURSION(X) _Pragma(STRINGIFY(inline_recursion(X)))
        #define _Try_force_inline static __forceinline
    #elif define(__GNUC__) || define(__clang__)
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