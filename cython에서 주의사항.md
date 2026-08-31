# cython에서 주의사항

1. 이건 그럭저럭 빠르다.
```cython
cdef inline bint whitespaceFingerprint(char x):
    return <bint> ((((x^8)&2)>>1)^((x^8)&1)) ^ 1 == 0 == (((3^x)|x) ^ 11)
```
2. 이게 더 빠르고, 이건 개행까지 감지한다
```cython
from libc.ctype cimport isspace
```