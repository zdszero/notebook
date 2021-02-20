## quote

quote disable evaluation when referencing the symbol

## list

```racket
; list operation

; element reference

(list-ref (list 1 2 3) 2)
(car (list 1 2 3))
(cdr (list 1 2 3))
(list-tail (list 1 2 3 4 5) 1) ; get sublist after the first element

; operation

(append lst1 lst2 ...)
(reverse lst)

; iteration

(map proc lst) => list
(andmap proc lst) => boolean
(ormap proc lst) => boolean
(for-each proc lst) => void
(foldl proc init lst) => void
(foldr proc init lst) => void

; filter

(filter proc lst) ; filter all elements that don't conform to proc
(remove v lst)
(remove* v-lst lst)
(sort lst less-than?)

; searching
(member v lst) => list or #f
(memf proc lst) => list or #f
(findf proc lst) => any
(assoc v lst) => list or #f
```

## number

```racket
(modulo 10 3)
(quotient/remainder 10 3)
```
