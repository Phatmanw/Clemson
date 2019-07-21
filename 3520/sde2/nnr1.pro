

/* prototype: theClass(+Avect, -C) */

theClass([A],A).

theClass([_|TA],Class) :- theClass(TA, Class).

/* prototype: distanceR2(+V1, +V2, -DistSq) */

distanceR2([X],[Y],((X-Y)*(X-Y))).  

distanceR2([HA|TA],[HB|TB],Sum) :- 
	distanceR2([HA],[HB],I), 
	distanceR2(TA,TB,J),
	Sum is I+J.
