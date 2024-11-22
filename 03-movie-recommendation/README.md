# Movie recommendation engine based using clustering algorithm

Authors: Antoni Kania, Rafał Sojecki

Application solve problem of making recomendations based on previously rated movies by different users. It uses clustering algorithm (k-means) with different, user selected metric to achive this goal

## Usage

1. Install the dependencies listed in the `requirements.txt` file (in root folder of repository):
    ```bash
    pip install -r requirements.txt
    ```
2. Generate .env file based on template.env (`cp template.env .env`) and fill it up with your themoviedb API KEY (avoiding storing api in repository)
3. Run application
   ```bash
    python index.py
    ```
    and type id of user for with you want to make recomendation. Id is a row numer - 2 in csv file located in resources/questionary_list.csv
4. [Use non-default metric](#usage-of-set-of-metrics-in-recomendation-engine)
## Features

#### Making recomendation and anti-recomendation based on data stored in "database"

For each user application predict 5 movies that are recommended with extra data and 5 that aren't.

#### Displaying description an genres of recommended movies (connection to themoviedb API)

```
1670
Gatunki: Komedia
Opis: Jest rok 1670. Jan, głowa szlacheckiej rodziny i właściciel (mniejszej) połowy wsi Adamczycha,
marzy o zapisaniu się na kartach historii Polski. Jego życie to pasmo sukcesów. Wszystko, co ma,
odziedziczył sam, a całą resztę osiągnął ciężką pracą własnych chłopów. Jego ambitne plany zakłóca
niełatwa codzienność właściciela ziemskiego: na sejmiku znów trzeba zawetować pomysł podniesienia
podatków, zdemotywowani chłopi, córka sprzeciwia się wydaniu za syna magnata a w dodatku Rzeczpospolita
szlachecka złośliwie akurat teraz chyli się ku upadkowi...
```

#### Usage of set of metrics in recomendation engine
- l2
- hamming
- jaccard
- euclidean
- chebyshev
- manhattan
- wminkowski
- sokalsneath
- precomputed
- rogerstanimoto
- l1
- nan_euclidean
- sokalmichener
- cityblock
- canberra
- yule
- seuclidean
- mahalanobis
- cosine
- haversine
- braycurtis
- minkowski
- russellrao
- matching
- dice
- sqeuclidean
- correlation

With you can use it by passing it as argv argument in comand line on app startup like this:

`python3 index.py cosine`


Example of recommendation for user with ID 4 using selection of metrics:

| l1         | manhattan  | cosine                | euclidean             |
| ---------- | ---------- | --------------------- | --------------------- |
| WALL·E     | WALL·E     | American Horror Story | 1670                  |
| Rancho     | Rancho     | Breaking Bad          | 365 dni               |
| Teściowie  | Teściowie  | The Digital Circus    | Ahsoka                |
| Grawitacja | Grawitacja | Piła                  | American Horror Story |
| Bridgerton | Bridgerton | Queen's Gambit        | American Pie          |

Anti - recomendation for user with ID 4 using selection of metrics:

| l1                    | manhattan             | cosine          | euclidean             |
| --------------------- | --------------------- | --------------- | --------------------- |
| 1670                  | 1670                  | 1670            | 1670                  |
| 365 dni               | 365 dni               | Ahsoka          | 365 dni               |
| Ahsoka                | Ahsoka                | Anioły i Demony | Ahsoka                |
| American Horror Story | American Horror Story | American Pie    | American Horror Story |
| American Pie          | American Pie          | Arcane          | American Pie          |
 

## Example usage 
[cosine](/media/cosine_1.mov)
[euklides](/media/euklides_1.mov)
[manhattan](/media/manhattan_1.mov)