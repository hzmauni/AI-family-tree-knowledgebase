parent('Hasib' , 'Rakib'). parent('Rakib' , 'Sohel'). parent('Rakib' , 'Sara').  parent('Rakib' , 'Jamal').  parent('Rakib' , 'Rebeka'). parent('Rashid' , 'Hasib'). parent('Sara' , 'Mina').
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
male('Rakib'). male('Hasib'). male('Rashid'). male('Sohel'). male('Jamal').

brother(X,Y):-parent(Z,X), parent(Z,Y), male(Y), not(X=Y).
sister(X,Y):-parent(Z,X), parent(Z,Y),not( male(Y)), not(X=Y).
aunt(X,Y):- parent(Z,X), sister(Y, Z),not( male(Y)).
uncle(X,Y):- parent(Z,X), brother(Z,Y), male(Y).


findGc :- write(' Grandparent: '), read(X), write('Grandchildren: '),
		grandparent(X, Gc), write(Gc), tab(5), fail.
findGc.

findGp :- write(' Grandchild: '), read(X), write('Grandparent: '),
	grandparent(Gp, X), write(Gp), tab(5), fail.
findGp.

findBr :- write(' Name: '), read(X), write('Brother: '),
	brother(X, Br), write(Br), tab(5), fail.

findBr.

findSr :- write(' Name: '), read(X), write('Sister: '),
	sister(X, Sr), write(Sr), tab(5), fail.
findSr.
findAn :- write(' Name: '), read(X), write('Aunt: '),
	aunt(X, An), write(An), tab(5), fail.
findAn.
findUn :- write(' Name: '), read(X), write('Uncle: '),
	uncle(X, Un), write(Un), tab(5), fail.
findUn.

