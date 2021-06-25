# NSE-Analyses

Data analyses uitgevoerd voor de Nationale Studenten Enquête

1.  Significantie analyses
2.  Prioriteitenmatrix

Belangrijke notities bij het gebruik van NSE respondent data

## NSE respondenten data: Weegfactor & normalisatie

In de NSE vragenlijst corrigeert de weegfactor voor verschillen in
responspercentages. Naast het gebruik van een weegfactor is ook de
normalisatie hiervan zeer belangrijk. Dit werkt als volgt:

> Stel je voor dat er twee opleidingen zijn, opleiding A en opleiding B,
> beiden met 100 studenten. Zo kan het zijn dat studenten van opleiding
> A alle 100 de vragenlijst invullen (d.w.z. 100%) terwijl voor
> opleiding B maar een respons van 10% gehaald wordt, d.w.z. 10
> studenten vullen de vragenlijst in. Als je nu wilt weten hoe tevreden
> studenten van opleiding A én B samen gemiddeld zijn, kun je eenvoudig
> het gemiddelde van de 110 studenten nemen (100 van opleiding A, en 10
> van opleiding B), maar hiermee gaat het gemiddelde vooral weergeven
> wat de mening is van de studenten van opleiding A, ondanks dat
> opleiding A en B evenveel studenten hebben. Stiekem meet je hiermee
> niet netjes het gemiddelde van de twee opleidingen, maar meer de
> bereidheid van studenten om de vragenlijst in te vullen.

Om hiervoor te corrigeren kun je een weegfactor gebruiken. Meerdere
methoden zijn mogelijk, maar in het geval van NSE wordt raking gebruikt.
Uit bovenstaand voorbeeld is duidelijk dat de weegfactor voor
studentresponses uit opleiding B 10x zo hoog moet zijn dan de weegfactor
voor studentresponses uit opleiding A.

> Stel je voor dat we een weegfactor van 1 voor elke student uit
> opleiding A kiezen. De weegfactor voor opleiding B is dan 10x zo hoog
> en dus10 voor elke student uit opleiding B. Impliciet betekent dit dat
> we doen alsof elke student uit opleiding B die de vragenlijst invult
> staat voor 10 studenten, en elke student uit opleiding A staat voor 1
> student. Totaal hebben we nu dan 100 x 1 + 10 x 10 = 200 studenten in
> ons gewogen sample. Dit, terwijl ons oorspronkelijke (ongewogen)
> sample 110 studenten bevatte. Het lijkt nu dus alsof meer studenten de
> vragenlijst hebben ingevuld dan daadwerkelijk het geval was.

Voor het berekenen van beschrijvende statistiek (bijv. gemiddelden) is
dit geen probleem, echter als je een vergelijkende statistiek gebruikt
(bijv. t-Toetsing, regressie) leidt kunstmatig aanpassen van de N tot
problemen: je zult gemakkelijker significante verschillen vinden vanwege
de grotere N hoewel deze verschillen wellicht niet bestaan (false
positives). Om het totaal aantal studenten (de sample N) niet te
veranderen is normalisatie zeer belangrijk.

Normalisatie van weegfactoren vindt plaats door de oorspronkelijke
ongewogen sample size (N) in beschouwing te nemen. In bovenstaand
voorbeeld is de ongewogen N = 110. De gewogen N wordt berekend door alle
gewichten bij elkaar op te tellen zodat deze ook gelijk is aan de
ongewogen N.

> Stel nu dat we al onze gewichten aanpassen met een factor 110/200. Zo
> zul je elke student van opleiding A een weegfactor van 0.55 geven, en
> elke student van opleiding B een weegfactor van 5.5. Impliciet
> betekent dit dat we doen alsof elke student uit opleiding B die de
> vragenlijst invult staat voor vijf-en-een-halve student, en omgekeerd
> staat elke student uit opleiding A voor een halve student ongeveer.
> Bekeken vanuit deze weegfactor hebben we nu dus 5.5 x 10 + 0.55 x 100
> = 110 studenten; hetzelfde aantal dat we voorheen in de situatie
> zonder weegfactor óók hadden. Alleen tellen de antwoorden van
> studenten uit opleiding B nu een stuk zwaarder mee dan opleiding A,
> waardoor voor het verschil in responspercentage (10% t.o.v. 100%)
> gecorrigeerd wordt.

Uit dit voorbeeld blijkt dat zowel de weegfactor zelf als normalisering
hiervan binnen elke groep erg belangrijk is: in de ongewogen situatie
hebben we 110 responses (d.w.z. het aantal studenten uit alle groepen
met een respons), en in de gewogen situatie hebben we ook 110 responses
(d.w.z. de som van alle weegfactoren).

NB: deze methode werkt niet of slecht in extreme/rand-gevallen (respons
van een groep is 0% of rond nul).
