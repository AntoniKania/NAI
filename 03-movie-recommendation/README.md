scikit-learn
request
pandas
python-dotenv





{'l2', 'hamming', 'jaccard', 'euclidean', 'chebyshev', 'manhattan', 'wminkowski', 'sokalsneath', 'precomputed', 'rogerstanimoto', 'l1', 'nan_euclidean', 'sokalmichener', 'cityblock', 'canberra', 'yule', 'seuclidean', 'mahalanobis', 'cosine', 'haversine', 'braycurtis', 'minkowski', 'russellrao', 'matching', 'dice', 'sqeuclidean', 'correlation'}

Recommendation for user ID 4 using selection of metrics:

| l1 | manhattan | cosine | euclidean |
|---|---|---|---|
| WALL·E | WALL·E  | American Horror Story  |  1670 |
| Rancho |  Rancho | Breaking Bad  |  365 dni |
| Teściowie | Teściowie  | The Digital Circus  |  Ahsoka |
| Grawitacja | Grawitacja  | Piła  |  American Horror Story |
| Bridgerton | Bridgerton  | Queen's Gambit  | American Pie  |
|---|---|---|---|---|
|  1670 | 1670  | 1670  | 1670  | 
|  365 dni | 365 dni  |  Ahsoka |  365 dni | 
|  Ahsoka |Ahsoka   |  Anioły i Demony |  Ahsoka | 
|  American Horror Story |American Horror Story   | American Pie  | American Horror Story  |
| American Pie  | American Pie  | Arcane  |  American Pie |


rafal@MacBook-Pro-rafal 03-movie-recommendation % python3 index.py euclidean
Podaj swoje id w bazie obejrzanych filmów: 4
Using: euclidean metric
Filmy rekomendowane: 

1670
Gatunki: Komedia
Opis: Jest rok 1670. Jan, głowa szlacheckiej rodziny i właściciel (mniejszej) połowy wsi Adamczycha, marzy o zapisaniu się na kartach historii Polski. Jego życie to pasmo sukcesów. Wszystko, co ma, odziedziczył sam, a całą resztę osiągnął ciężką pracą własnych chłopów. Jego ambitne plany zakłóca niełatwa codzienność właściciela ziemskiego: na sejmiku znów trzeba zawetować pomysł podniesienia podatków, zdemotywowani chłopi, córka sprzeciwia się wydaniu za syna magnata a w dodatku Rzeczpospolita szlachecka złośliwie akurat teraz chyli się ku upadkowi...

365 dni
Gatunki: Romans,Dramat
Opis: Laura i Massimo znów są razem i jeszcze bardziej między nimi iskrzy. Jednak nowy początek nie będzie dla nich prosty z powodu powiązań rodzinnych Massimo i tajemniczego mężczyzny, który wkracza w życie Laury, by za wszelką cenę zdobyć jej serce i zaufanie. W drugiej części filmowego tryptyku bohaterka Anny-Marii Siekluckiej przejdzie transformację, która przyniesie znaczące zmiany w jej dotychczasowym życiu i związku z Massimo. Na ekran powrócą ulubieńcy - najlepsza przyjaciółka i powierniczka Laury, Olga oraz zaufany pomocnik Don Massima, Domenico - a wraz z nimi nowa postać, zabójczo przystojny i tajemniczy Nacho, na widok którego serca zabiją mocniej. Nie zabraknie także zapierających dech w piersiach włoskich krajobrazów, olśniewających kreacji i eleganckich sportowych samochodów.

Ahsoka
Gatunki: Sci-Fi & Fantasy,Akcja i Przygoda
Opis: Imperium upadło. Dawna Jedi, Ahsoka Tano, próbuje odkryć źródło zła zagrażającego wyniszczonej wojną galaktyce.

American Horror Story
Gatunki: Dramat,Tajemnica,Sci-Fi & Fantasy
Opis: Antologia mrożących krew w żyłach opowiadań, których wspólnym mianownikiem są nawiedzone miejsca.

American Pie
Gatunki: Komedia,Romans
Opis: "American Pie" to zwariowana komedia o wkraczaniu w dorosłość. Grupa przyjaciół zdenerwowanych faktem, że nie mogą się pozbyć znienawidzonego dziewictwa, postanawia podjąć zdecydowane kroki. Jednak, aby zamknąć niechlubny dziewiczy rozdział w swoim życiu trzeba się nieźle namęczyć: zaliczyć parę trudnych lekcji miłości i seksu, doświadczyć poniżenia i rozczarowania i ćwiczyć cierpliwość.

Filmy odradzane: 

1670, 365 dni, Ahsoka, American Horror Story, American Pie
rafal@MacBook-Pro-rafal 03-movie-recommendation % 