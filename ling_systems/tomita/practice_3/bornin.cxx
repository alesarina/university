#encoding "utf-8"
Born -> Verb<kwtype=born>;
City -> Noun<kwtype=city>;
Person -> AnyWord<gram="persn"> AnyWord<gram="famn"> | AnyWord<gram="persn">;
Date -> Word<wff=/\d{1,2}/> Noun<kwtype=month> Word<wfl=/\d{4}/>;
S -> Person interp(BornFact.Person) Born "в" City interp(BornFact.Place);
S -> Born Person interp(BornFact.Person) Date interp(BornFact.Date) AnyWord+ City interp(BornFact.Place);
