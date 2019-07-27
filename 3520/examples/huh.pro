huh(A,B) :- huhA(A,B),huhB(A,B),!.

huhA([HA|TA],B) :- member(HA,B), huhA(TA,B).
huhA([],_).

huhB(A,[HB|TB]) :- member(HB,A), huhB(A,TB).
huhB(_,[]).
