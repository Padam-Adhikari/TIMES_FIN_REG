# Industry keys (EU ETS free allocation)

Built by `tools/industry_keys.py` from `data/sources/eutl_FI_industry.csv` (`tools/industry_register.py`: EUTL via the open EUETS.INFO API, sites placed by coordinates in the official maakunta polygons, three geocoding errors corrected by hand with reasons in the tool).

Key value = free allocation of the installation summed over the period (phase 3 2013-2020 = EU product benchmark x historical production). Each key: 19 shares >= 0 summing to exactly 1 (rational arithmetic).

## ind_ipp (2013-2020): pulp and paper (all IPP processes, IPP heat plant, black-liquor CHP)

- File `data/keys/ind_ipp_2013-2020.csv`; 49 installations; total 29,091,613 allowances; sum of shares = 1 (exact)

| Region | Share | Installations (allocation) |
|---|---|---|
| FI1C5 Etelä-Karjala | 15.9455% | Imatran tehtaat (1,979,757); Kaukaan tehtaat (1,520,402); Metsä Board Joutseno BCTMP (388,325); Joutsenon tehdas (237,638); Simpeleen tehdas (512,693) |
| FI1C7 Kymenlaakso | 15.8116% | Karhulan Kartonkitehdas (120,444); Kotkan tehtaat (1,001,196); Kymin tehtaat (1,956,118); Sunila (0); Sunila (135,918); Anjalan tehtaat (1,386,173); Summan tehtaat (0); Voikkaan paperitehdas (0) |
| FI196 Satakunta | 10.1447% | Ahlstrom Tampere Oy Kauttuan tehdas (12,651); Porin kartonkitehdas (266,496); Rauman tehtaat (2,200,720); Rauman tehdas (221,135); Kauttuan tehtaat (0); Kauttuan tehdas (250,248) |
| FI1D7 Lappi | 8.8312% | Veitsiluodon tehtaat (1,746,221); Kemijärven tehtaat (0); Kemin tehdas (189,639); Kemin tehtaat (633,289) |
| FI1D9 Pohjois-Pohjanmaa | 8.4924% | Oulun tehdas (2,470,563) |
| FI19B Pirkanmaa | 8.4246% | Tervasaaren tehtaat (1,097,183); Lielahden tehtaat (0); Nokian tehdas (193,622); Mäntän tehdas (334,465); M-real Kyro (0); Takon tehtaat (413,109); Kyröskosken voimalaitos (412,468) |
| FI198 Keski-Suomi | 8.2331% | Äänekosken tehtaat (502,235); M-real Oyj, M-real Kangas (0); Äänekoski Board (396,500); Äänekoski Paper (0); Jämsänkoski (0); Kaipolan paperitehdas (1,496,400) |
| FI19A Pohjanmaa | 7.4376% | Pietarsaaren tehtaat, Wisaforest (1,627,731); Metsä Board Kaskinen BCTMP (535,990) |
| FI1B1 Uusimaa | 5.7234% | Lohjan tehdas (143,564); Kirkniemen tehtaat (1,521,455) |
| FI1DB Pohjois-Savo | 5.1336% | Varkauden tehtaat (743,950); Kuopion tehdas (727,073); Juankosken kartonkitehdas (22,419) |
| FI1C6 Päijät-Häme | 2.0948% | Heinolan Flutingtehdas (609,416) |
| FI1DC Pohjois-Karjala | 1.8927% | Enocell Oy Uimaharjun tehtaat (385,486); Pankakosken tehtaat (165,130) |
| FI1C2 Kanta-Häme | 1.8349% | Tervakosken tehtaat (533,791) |

## ind_iis (2013-2020): iron and steel sites (finishing IISFINPRO00)

- File `data/keys/ind_iis_2013-2020.csv`; 5 installations; total 34,964,571 allowances; sum of shares = 1 (exact)

| Region | Share | Installations (allocation) |
|---|---|---|
| FI1D9 Pohjois-Pohjanmaa | 79.8521% | Raahen terästehdas (27,919,945) |
| FI1D7 Lappi | 16.9269% | Tornion tehtaat (5,918,422) |
| FI1C2 Kanta-Häme | 2.0504% | Hämeenlinnan tehtaat (716,928) |
| FI1C5 Etelä-Karjala | 1.1705% | Imatran terästehdas (409,276) |

## ind_iis_eaf (2013-2020): electric-arc furnaces: Outokumpu Tornio and Ovako Imatra

- File `data/keys/ind_iis_eaf_2013-2020.csv`; 2 installations; total 6,327,698 allowances; sum of shares = 1 (exact)

| Region | Share | Installations (allocation) |
|---|---|---|
| FI1D7 Lappi | 93.5320% | Tornion tehtaat (5,918,422) |
| FI1C5 Etelä-Karjala | 6.4680% | Imatran terästehdas (409,276) |

## ind_ilm (2013-2020): lime kilns

- File `data/keys/ind_ilm_2013-2020.csv`; 6 installations; total 4,764,141 allowances; sum of shares = 1 (exact)

| Region | Share | Installations (allocation) |
|---|---|---|
| FI1D9 Pohjois-Pohjanmaa | 35.1700% | Raahen kalkkitehdas (1,675,550) |
| FI1D7 Lappi | 34.0367% | Röyttän kalkkitehdas (1,621,556) |
| FI1B1 Uusimaa | 13.4810% | Tytyrin kalkkitehdas (642,253) |
| FI1C1 Varsinais-Suomi | 9.8225% | Paraisten kalkkitehdas (467,956) |
| FI1DA Etelä-Savo | 5.1020% | Louhin kalkkitehdas (243,065) |
| FI1C5 Etelä-Karjala | 2.3879% | Lappeenrannan kalkkitehdas (113,761) |

## ind_icm (2013-2020): cement clinker (generic cement processes; site processes go to their plant)

- File `data/keys/ind_icm_2013-2020.csv`; 2 installations; total 6,900,648 allowances; sum of shares = 1 (exact)

| Region | Share | Installations (allocation) |
|---|---|---|
| FI1C1 Varsinais-Suomi | 57.8926% | Paraisten sementtitehdas (3,994,963) |
| FI1C5 Etelä-Karjala | 42.1074% | Lappeenrannan sementtitehdas (2,905,685) |

## ind_ich (2013-2020): chemicals (bulk/organic/inorganic, excl. fertiliser and hydrogen)

- File `data/keys/ind_ich_2013-2020.csv`; 5 installations; total 5,717,922 allowances; sum of shares = 1 (exact)

| Region | Share | Installations (allocation) |
|---|---|---|
| FI1B1 Uusimaa | 77.7005% | Borealis Polymers Oy:n tuotantolaitokset (4,442,852) |
| FI196 Satakunta | 19.6863% | Titaanidioksiditehdas (1,125,647) |
| FI1C5 Etelä-Karjala | 2.3716% | Taavetin tehdas (135,605) |
| FI1DC Pohjois-Karjala | 0.2417% | Puhoksen tehdas (13,818) |

## ind_iam (2013-2020): fertiliser / nitric acid (ammonia processes)

- File `data/keys/ind_iam_2013-2020.csv`; 2 installations; total 2,048,220 allowances; sum of shares = 1 (exact)

| Region | Share | Installations (allocation) |
|---|---|---|
| FI1C1 Varsinais-Suomi | 52.1503% | Uudenkaupungin tehdas (1,068,153) |
| FI1DB Pohjois-Savo | 47.8497% | Yara Suomi Oy Siilinjärvi (980,067) |

## ind_inm (2013-2020): other non-metallic minerals (glass fibre, mineral wool, bricks, gypsum, LECA)

- File `data/keys/ind_inm_2013-2020.csv`; 13 installations; total 950,174 allowances; sum of shares = 1 (exact)

| Region | Share | Installations (allocation) |
|---|---|---|
| FI1C7 Kymenlaakso | 27.5299% | Kuusankosken Leca-soratehdas (224,978); Karhulan tehdas (0); Korian tiilitehdas (36,604) |
| FI1B1 Uusimaa | 26.5736% | Saint-Gobain Finland Oy, Gyproc kipsilevy (166,004); Hyvinkään lasivillatehdas (86,491) |
| FI1C1 Varsinais-Suomi | 22.8296% | Kemiön tehdas (32,197); Paraisten Kivivillatehdas (184,724) |
| FI1D9 Pohjois-Pohjanmaa | 9.6911% | Oulun Kivivillatehdas (75,842); Ylivieskan tehdas (16,240) |
| FI1C5 Etelä-Karjala | 7.6778% | Lappeenrannan Kivivillatehdas (72,952) |
| FI1C2 Kanta-Häme | 4.2694% | Forssan lasivillatehdas (40,567) |
| FI1C6 Päijät-Häme | 1.4287% | Lappilan tiilitehdas (13,575) |

## ind_ioi (2013-2020): other industries in the ETS (food, wood products, ...)

- File `data/keys/ind_ioi_2013-2020.csv`; 14 installations; total 1,098,583 allowances; sum of shares = 1 (exact)

| Region | Share | Installations (allocation) |
|---|---|---|
| FI196 Satakunta | 22.0601% | Säkylän tehdas (65,016); Säkylän voimalaitos (177,332); Pihlavan höyrykeskus (0) |
| FI199 Etelä-Pohjanmaa | 20.1697% | Koskenkorvan tehdas (221,581) |
| FI1C6 Päijät-Häme | 19.1446% | Järvelän levyteollisuus (159,251); Järvelän sahateollisuus (51,068); Vierumäki (0) |
| FI1DC Pohjois-Karjala | 15.2901% | Vuonoksen tehdas (73,058); Joensuun vaneritehdas (94,916) |
| FI1D8 Kainuu | 14.8657% | Sotkamon tehdas (163,312) |
| FI1C5 Etelä-Karjala | 8.4699% | Honkalahden saha (93,049) |

