from functools import reduce

"""
# kanatoggle.py

1. about it
2. docs

## about it

simple hiragana-katagana toggle tool

...writing...

## docs

1. imported obj, from another toolkit
2. imported obj, from same toolkit
3. imported for export builtin or non-imported builtin-scope obj
4. non-imported global-scope obj
5. imported in only local-scope or non-imported local-scope obj

### === # imported obj, from another toolkit # === ###

 - reduce from functools
 - functools.partial (local scope only)

### === # imported obj, from same toolkit # === ###

no imported obj, from same toolkit

### === # imported for export builtin or non-imported builtin-scope obj # === ###

no imported for export builtin or non-imported builtin-scope obj

### === # non-imported global-scope obj # === ###

DOCUMENTED_OBJ
 - iterjoin
 - iterize
NONDOCUMENTED_OBJ
 - lambda `optional_flagging(f)` : make f as function which output `__import__("functools").partial(f, *argv, **kargv)` from `(*argv, **kargv)` (here are where functools.partial is used)
 - lambda `ifelifelse_selecter(p, a, q, b, c)` : which actually work as `p?a:q?b:c`
 - lambda `escaping_processes(target, escape, work)` : escaping input of work to make escaping processed work. by replacing input's target to escape, work cannot detect non-escaping target. and also, by unescaping in output, every escaped-target is be target again.
 - lambda `optional_process(f)(p)(x)` : applying f optionally to process to return x. (option by p)
 - lambda `hirakanatoggle(char, *, kanaonly = True)` : toggle what gana is not hirakana. switch hiragana to katagana. but also undo is included. i.e. means, hiraganatoggle is make gatagana which toggle from hiragana to hiragana.
   + kanaonly = False : toggles including ryakuji (abbreviation). that means 'ゕゖヵヶ' is also included.
   + input : 1 char
   + output : 1 char, if input is not toggle target, just return the input.
 - lambda `katakanatoggle_without_hirakanatoggle_corework(f, g)(x, t)` : ...writing...
 - 
 - ...writing...
 - dictionarry kataganatoggle_table : not for you. (read the sucks code as document if you want to use it)

...writing...

### === # imported in only local-scope or non-imported local-scope obj # === ###

 - (imported) functools.partial (on optional_flagging's parameter default value)

...writing...
"""

def iterjoin(*iters):
    """
    # yield-generator `iterjoin(*iters)`
    
    iterjoin(*iters) is actaully work as iterize(*(elem for iter in iters for elem in iter))
    """
    for iter in iters: yield from iter

def iterize(*args):
    """
    # yield-generator `iterize(*args)`
    
    Q. why name is iterize?
    A. iterible obj args is iterized in this yield-generter
    """
    yield from args

optional_flagging = (lambda partialer = __import__("functools").partial: lambda f : partialer(partialer, f))() # block the mistake default overriding. it's not unfree. you can hake closure variable field freely >ω<. so it's not unfree

ifelifelse_selecter = lambda p, a, q, b, c: a if p else b if q else c
escaping_processes = lambda target, escape, work : lambda string : work(
    string.replace(target, escape)
    ).replace(escape, target)
optional_process = lambda f : lambda p : lambda x : f(x) if p else x

hirakanatoggle = lambda char, *, kanaonly = True : (
    lambda CodePoint : ifelifelse_selecter(
        0x3040 < CodePoint < (0x3095 if kanaonly else 0x3097),
        chr(CodePoint + 0x60),
        30A0 < CodePoint < (0x30F5 if kanaonly else 0x30F7),
        chr(CodePoint - 0x60),
        char
)
)(chr(char))
kataganatoggle_table = {
    "\u30F7" : "\u308F\u3099",
    "\u30F8" : "\u3090\u3099",
    "\u30F9" : "\u3091\u3099",
    "\u30FA" : "\u3092\u3099"
}

katakanatoggle_without_hirakanatoggle_corework = lambda f, g : lambda x, t : escaping_processes(
    "\u3099",
    "\\\u3099",
    lambda string : string.replace(
        t[0], f(t[1])
    ).replace(
        g, t[0]
    )
)(x)
katakanatoggle_without_hirakanatoggle = lambda char, *, katagana_decompose_force = False : reduce(
    katakanatoggle_without_hirakanatoggle_corework(
        optional_process(hirakanatoggle)(katagana_decompose_force), "{}\\{}".format(*t[1])
    ),
    iterjoin(
        iterize(char),
        kataganatoggle_table.items()
    )
)

katakanatoggle_with = lambda char, *, kanaonly = True, func = hirakanatoggle, katagana_decompose_force = True : optional_flagging(func)(
    kanaonly = kanaonly
)(
    optional_flagging(katakanatoggle_wihtout_hirakanatoggle)(
        katagana_decompose_force = katagana_decompose_force
    )(
        char
    )
)
katakanatoggle = lambda char, *, kanaonly = True, katagana_decompose_force = True : func(kataganatoggle)(
    kanaonly = kanaonly,
    katagana_decompose_force = katagana_decompose_force
)(
    char
) #it just using katakanatoggle_with.

strjoin = "".join

customizible_kanahint = lambda text, *, toggler = kataganatoggle, kanaonly = True, hintsym = "°", hintsym_escapes = "⁰" : strjoin(
    (
        (
            f"{x}（{toggler(x, kanaonly = kanaonly)}）" if i % 2 else x
        ).replace(
hintsym_escapes * 2, hintsym
        ).replace(
f"\\{hintsym_escapes}", hintsym_escapes
        )
        for i, x in enumerate(
            text.replace(
hintsym_escapes, f"\\{hintsym_escapes}"
            ).replace(
f"\\{hintsym}", hintsym_escapes * 2
            ).split(hintsym)
        )
    )
)

kanahint = lambda text : customizible_kanahint(
    customizible_kanahint(
        customizible_kanahint(
            customizible_kanahint(
                text, kanaonly = False, hintsym = "°°°°"
            ),
            toggler = hirakanatoggle, kanaonly = False, hintsym = "°°°"
        ),
        hintsym = "°°"
    ),
    toggler = hirakanatoggle
) #it just using customizible_kanahint.