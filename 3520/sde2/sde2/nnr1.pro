/* prototype: printList(+H) 												*/

printList([]).

printList([HD|TL]) :- write(HD), nl, printList(TL).


/* prototype: theClass(+Avect, -C) 										*/

theClass([A], A).

theClass([_|TA], Class) :- theClass(TA, Class).

/* prototype: distanceR2(+V1, +V2, -DistSq) 							*/

distanceR2([_], [_], 0.0).

distanceR2([HA|TA], [HB|TB], Sum) :- 
	I is (HA-HB)*(HA-HB),
	distanceR2(TA, TB, J),
	Sum is I+J.

/* prototype: distanceAllVectors2(+V, +Vset, -Dlist) 				*/

distanceAllVectors2(_, [], []). 									   	

distanceAllVectors2(A, [HB|HT], Dlist) :- 
	distanceR2(A, HB, I),
	distanceAllVectors2(A, HT, J),
	append([I], J, Dlist).

/* prototype: nnr1(+Test, +H, -Class)									*/

nnr1(Test, [H|T], Class) :- 
	distanceR2(Test, H, I),
	append([H], T, B),
	distanceAllVectors2(Test, B, J),
	(min_member(I, J) -> theClass(H, Class));
	nnr1(Test, T, Class).
