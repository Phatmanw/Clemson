whatis([],0).
whatis([_|T],N) :- whatis(T,N1), N is N1 + 1.

lpredicate([],0).
lpredicate([H|T],N) :- lpredicate(T,N1), N is N1 + H.
