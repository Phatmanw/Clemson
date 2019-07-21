/* rough solution to add 2 lists */
/* prototype: addMe(+A,+B,-C)  */

addMe([],[],[]).  /* note order ! */

addMe([HA|TA],[HB|TB],[HC|TC]) :- HC is HA+HB, addMe(TA,TB,TC).


