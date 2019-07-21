
/* work describing a row of image 2 - image1  */

diff([],[],[]).

diff([H1|T1],[H2|T2],[D1|D2]) :- D1 is (H2-H1), diff(T1,T2,D2).
