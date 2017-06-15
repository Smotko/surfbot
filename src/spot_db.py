"""Spot db

This is Surf Bot's spot database. It only includes spots in Portugal
for now and as this won't really scale needs to be moved into an actual db.
"""

from typing import Dict, Union, List

ALL_SPOTS: List[Dict[str, Union[str, float, int]]] = [
    {
        "forecast": "/Praia-da-Rocha-Surf-Report/127/",
        "guide": "/Praia-da-Rocha-Surf-Guide/127/",
        "id": 127,
        "lat": 37.1114,
        "lon": -8.5306,
        "name": "Praia da Rocha",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Sagres-Tonel-Surf-Report/128/",
        "guide": "/Sagres-Tonel-Surf-Guide/128/",
        "id": 128,
        "lat": 37.0054,
        "lon": -8.9493,
        "name": "Sagres (Tonel)",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Sines-Surf-Report/129/",
        "guide": "/Sines-Surf-Guide/129/",
        "id": 129,
        "lat": 37.97,
        "lon": -8.88,
        "name": "Sines",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Carrapateira-Surf-Report/130/",
        "guide": "/Carrapateira-Surf-Guide/130/",
        "id": 130,
        "lat": 37.1659,
        "lon": -8.9048,
        "name": "Carrapateira",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Afife-Surf-Report/187/",
        "guide": "/Afife-Surf-Guide/187/",
        "id": 187,
        "lat": 41.7754,
        "lon": -8.875,
        "name": "Afife",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Viana-do-Castelo-Surf-Report/188/",
        "guide": "/Viana-do-Castelo-Surf-Guide/188/",
        "id": 188,
        "lat": 41.6776,
        "lon": -8.8357,
        "name": "Viana do Castelo",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Agucadoura-Surf-Report/189/",
        "guide": "/Agucadoura-Surf-Guide/189/",
        "id": 189,
        "lat": 41.4291,
        "lon": -8.7868,
        "name": "Agu\u00e7adoura",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Leca-Surf-Report/190/",
        "guide": "/Leca-Surf-Guide/190/",
        "id": 190,
        "lat": 41.1896,
        "lon": -8.7089,
        "name": "Le\u00e7a",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Espinho-Surf-Report/191/",
        "guide": "/Espinho-Surf-Guide/191/",
        "id": 191,
        "lat": 41.0084,
        "lon": -8.6502,
        "name": "Espinho",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Praia-de-Mira-Surf-Report/192/",
        "guide": "/Praia-de-Mira-Surf-Guide/192/",
        "id": 192,
        "lat": 40.4561,
        "lon": -8.806,
        "name": "Praia de Mira",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Cabedelo-Surf-Report/193/",
        "guide": "/Cabedelo-Surf-Guide/193/",
        "id": 193,
        "lat": 40.14,
        "lon": -8.866,
        "name": "Cabedelo",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Nazare-Surf-Report/194/",
        "guide": "/Nazare-Surf-Guide/194/",
        "id": 194,
        "lat": 39.6103,
        "lon": -9.089,
        "name": "Nazar\u00e9",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Lagide-Surf-Report/195/",
        "guide": "/Lagide-Surf-Guide/195/",
        "id": 195,
        "lat": 39.3755,
        "lon": -9.336,
        "name": "Lagide",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Supertubos-Surf-Report/196/",
        "guide": "/Supertubos-Surf-Guide/196/",
        "id": 196,
        "lat": 39.3455,
        "lon": -9.365,
        "name": "Supertubos",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Ericeira-Surf-Report/198/",
        "guide": "/Ericeira-Surf-Guide/198/",
        "id": 198,
        "lat": 38.959,
        "lon": -9.417,
        "name": "Ericeira",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Praia-do-Guincho-Surf-Report/199/",
        "guide": "/Praia-do-Guincho-Surf-Guide/199/",
        "id": 199,
        "lat": 38.7348,
        "lon": -9.4754,
        "name": "Praia do Guincho",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Lisbon-Estoril-Surf-Report/200/",
        "guide": "/Lisbon-Estoril-Surf-Guide/200/",
        "id": 200,
        "lat": 38.7015,
        "lon": -9.4079,
        "name": "Lisbon/Estoril",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Malhao-Surf-Report/202/",
        "guide": "/Malhao-Surf-Guide/202/",
        "id": 202,
        "lat": 37.7833,
        "lon": -8.8048,
        "name": "Malh\u00e3o",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Arrifana-Surf-Report/836/",
        "guide": "/Arrifana-Surf-Guide/836/",
        "id": 836,
        "lat": 37.2942,
        "lon": -8.8721,
        "name": "Arrifana",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Costa-da-Caparica-Surf-Report/874/",
        "guide": "/Costa-da-Caparica-Surf-Guide/874/",
        "id": 874,
        "lat": 38.6546,
        "lon": -9.2529,
        "name": "Costa da Caparica",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Foz-do-Lizandro-Surf-Report/901/",
        "guide": "/Foz-do-Lizandro-Surf-Guide/901/",
        "id": 901,
        "lat": 38.9429,
        "lon": -9.4183,
        "name": "Foz do Lizandro",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Cortegaca-Surf-Report/906/",
        "guide": "/Cortegaca-Surf-Guide/906/",
        "id": 906,
        "lat": 40.9383,
        "lon": -8.66,
        "name": "Cortegaca",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Carcavelos-Surf-Report/912/",
        "guide": "/Carcavelos-Surf-Guide/912/",
        "id": 912,
        "lat": 38.6786,
        "lon": -9.3376,
        "name": "Carcavelos",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Vale-Figueiras-Surf-Report/936/",
        "guide": "/Vale-Figueiras-Surf-Guide/936/",
        "id": 936,
        "lat": 37.2489,
        "lon": -8.868,
        "name": "Vale Figueiras",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Matosinhos-Surf-Report/942/",
        "guide": "/Matosinhos-Surf-Guide/942/",
        "id": 942,
        "lat": 41.1754,
        "lon": -8.6907,
        "name": "Matosinhos",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Cantinho-Da-Baia-Surf-Report/994/",
        "guide": "/Cantinho-Da-Baia-Surf-Guide/994/",
        "id": 994,
        "lat": 39.3685,
        "lon": -9.3393,
        "name": "Cantinho Da Baia",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Buarcos-Surf-Report/1078/",
        "guide": "/Buarcos-Surf-Guide/1078/",
        "id": 1078,
        "lat": 40.1709,
        "lon": -8.8986,
        "name": "Buarcos",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Sagres-South-Surf-Report/1098/",
        "guide": "/Sagres-South-Surf-Guide/1098/",
        "id": 1098,
        "lat": 37.0047,
        "lon": -8.9401,
        "name": "Sagres (South)",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Lagos-Surf-Report/1128/",
        "guide": "/Lagos-Surf-Guide/1128/",
        "id": 1128,
        "lat": 37.1097,
        "lon": -8.6588,
        "name": "Lagos",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Esmoriz-Surf-Report/1228/",
        "guide": "/Esmoriz-Surf-Guide/1228/",
        "id": 1228,
        "lat": 40.9613,
        "lon": -8.6521,
        "name": "Esmoriz",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Odeceixe-Surf-Report/1255/",
        "guide": "/Odeceixe-Surf-Guide/1255/",
        "id": 1255,
        "lat": 37.4423,
        "lon": -8.8023,
        "name": "Odeceixe",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Falesia-Vilamoura-Surf-Report/1256/",
        "guide": "/Falesia-Vilamoura-Surf-Guide/1256/",
        "id": 1256,
        "lat": 37.0743,
        "lon": -8.1288,
        "name": "Falesia-Vilamoura",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Praia-Grande-Sintra-Surf-Report/1257/",
        "guide": "/Praia-Grande-Sintra-Surf-Guide/1257/",
        "id": 1257,
        "lat": 38.8161,
        "lon": -9.479,
        "name": "Praia Grande Sintra",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Praia-da-Barra-Surf-Report/1288/",
        "guide": "/Praia-da-Barra-Surf-Guide/1288/",
        "id": 1288,
        "lat": 40.6344,
        "lon": -8.751,
        "name": "Praia da Barra",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Santa-Cruz-Surf-Report/3763/",
        "guide": "/Santa-Cruz-Surf-Guide/3763/",
        "id": 3763,
        "lat": 39.135,
        "lon": -9.3849,
        "name": "Santa Cruz",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Praia-Da-Areia-Branca-Surf-Report/3784/",
        "guide": "/Praia-Da-Areia-Branca-Surf-Guide/3784/",
        "id": 3784,
        "lat": 39.2654,
        "lon": -9.337,
        "name": "Praia Da Areia Branca",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Praia-Azul-Surf-Report/3901/",
        "guide": "/Praia-Azul-Surf-Guide/3901/",
        "id": 3901,
        "lat": 39.1176,
        "lon": -9.3954,
        "name": "Praia Azul",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Beliche-Surf-Report/4323/",
        "guide": "/Beliche-Surf-Guide/4323/",
        "id": 4323,
        "lat": 37.0249,
        "lon": -8.9646,
        "name": "Beliche",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Zavial-Surf-Report/4324/",
        "guide": "/Zavial-Surf-Guide/4324/",
        "id": 4324,
        "lat": 37.0452,
        "lon": -8.873,
        "name": "Zavial",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Praia-da-Luz-Surf-Report/4325/",
        "guide": "/Praia-da-Luz-Surf-Guide/4325/",
        "id": 4325,
        "lat": 37.0859,
        "lon": -8.725,
        "name": "Praia da Luz",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Praia-Castelejo-Surf-Report/4326/",
        "guide": "/Praia-Castelejo-Surf-Guide/4326/",
        "id": 4326,
        "lat": 37.1006,
        "lon": -8.9466,
        "name": "Praia Castelejo",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Praia-da-Cordoama-Surf-Report/4327/",
        "guide": "/Praia-da-Cordoama-Surf-Guide/4327/",
        "id": 4327,
        "lat": 37.1102,
        "lon": -8.9398,
        "name": "Praia da Cordoama",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Praia-da-Bordeira-Surf-Report/4328/",
        "guide": "/Praia-da-Bordeira-Surf-Guide/4328/",
        "id": 4328,
        "lat": 37.2018,
        "lon": -8.9044,
        "name": "Praia da Bordeira",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Amoreira-Surf-Report/4329/",
        "guide": "/Amoreira-Surf-Guide/4329/",
        "id": 4329,
        "lat": 37.3533,
        "lon": -8.8497,
        "name": "Amoreira",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Monte-Clerigo-Surf-Report/4330/",
        "guide": "/Monte-Clerigo-Surf-Guide/4330/",
        "id": 4330,
        "lat": 37.3459,
        "lon": -8.8561,
        "name": "Monte Cl\u00e9rigo",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Monte-Clerigo-Surf-Report/4331/",
        "guide": "/Monte-Clerigo-Surf-Guide/4331/",
        "id": 4331,
        "lat": 37.3459,
        "lon": -8.8561,
        "name": "Monte Cl\u00e9rigo",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Carriagem-Surf-Report/4332/",
        "guide": "/Carriagem-Surf-Guide/4332/",
        "id": 4332,
        "lat": 37.3858,
        "lon": -8.8268,
        "name": "Carriagem",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Zambujeria-do-Mar-Surf-Report/4333/",
        "guide": "/Zambujeria-do-Mar-Surf-Guide/4333/",
        "id": 4333,
        "lat": 37.5238,
        "lon": -8.7902,
        "name": "Zambujeria do Mar",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Cogumelo-Surf-Report/4334/",
        "guide": "/Cogumelo-Surf-Guide/4334/",
        "id": 4334,
        "lat": 37.7212,
        "lon": -8.7958,
        "name": "Cogumelo",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Porto-Covo-Surf-Report/4335/",
        "guide": "/Porto-Covo-Surf-Guide/4335/",
        "id": 4335,
        "lat": 37.8571,
        "lon": -8.7943,
        "name": "Porto Covo",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Sao-Torpes-Surf-Report/4336/",
        "guide": "/Sao-Torpes-Surf-Guide/4336/",
        "id": 4336,
        "lat": 37.9197,
        "lon": -8.8078,
        "name": "S\u00e3o Torpes",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Sesimbra-Surf-Report/4337/",
        "guide": "/Sesimbra-Surf-Guide/4337/",
        "id": 4337,
        "lat": 38.4413,
        "lon": -9.0969,
        "name": "Sesimbra",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Bicas-Surf-Report/4338/",
        "guide": "/Bicas-Surf-Guide/4338/",
        "id": 4338,
        "lat": 38.4538,
        "lon": -9.2001,
        "name": "Bicas",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Lagoa-de-Albufeira-Surf-Report/4339/",
        "guide": "/Lagoa-de-Albufeira-Surf-Guide/4339/",
        "id": 4339,
        "lat": 38.5089,
        "lon": -9.1848,
        "name": "Lagoa de Albufeira",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Santa-Amaro-Surf-Report/4340/",
        "guide": "/Santa-Amaro-Surf-Guide/4340/",
        "id": 4340,
        "lat": 38.6819,
        "lon": -9.3138,
        "name": "Santa Amaro",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Praia-das-Macas-Surf-Report/4341/",
        "guide": "/Praia-das-Macas-Surf-Guide/4341/",
        "id": 4341,
        "lat": 38.8268,
        "lon": -9.472,
        "name": "Praia das Ma\u00e7\u00e1s",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Sao-Juliao-Surf-Report/4342/",
        "guide": "/Sao-Juliao-Surf-Guide/4342/",
        "id": 4342,
        "lat": 38.9323,
        "lon": -9.4221,
        "name": "S\u00e3o Juli\u00e3o",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Ribeira-dIlhas-Surf-Report/4343/",
        "guide": "/Ribeira-dIlhas-Surf-Guide/4343/",
        "id": 4343,
        "lat": 38.9881,
        "lon": -9.4226,
        "name": "Ribeira d\u2019Ilhas",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Coxos-Surf-Report/4344/",
        "guide": "/Coxos-Surf-Guide/4344/",
        "id": 4344,
        "lat": 39.0012,
        "lon": -9.4278,
        "name": "Coxos",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Sao-Lourenco-Surf-Report/4345/",
        "guide": "/Sao-Lourenco-Surf-Guide/4345/",
        "id": 4345,
        "lat": 39.0144,
        "lon": -9.425,
        "name": "S\u00e3o Louren\u00e7o",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Consolacao-Surf-Report/4346/",
        "guide": "/Consolacao-Surf-Guide/4346/",
        "id": 4346,
        "lat": 39.3235,
        "lon": -9.3623,
        "name": "Consola\u00e7\u00e3o",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Molho-Leste-Surf-Report/4347/",
        "guide": "/Molho-Leste-Surf-Guide/4347/",
        "id": 4347,
        "lat": 39.3502,
        "lon": -9.3692,
        "name": "Molho Leste",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Belgas-Surf-Report/4348/",
        "guide": "/Belgas-Surf-Guide/4348/",
        "id": 4348,
        "lat": 39.4165,
        "lon": -9.2527,
        "name": "Belgas",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Almagreira-Surf-Report/4349/",
        "guide": "/Almagreira-Surf-Guide/4349/",
        "id": 4349,
        "lat": 39.3798,
        "lon": -9.3156,
        "name": "Almagreira",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Foz-do-Arelho-Surf-Report/4350/",
        "guide": "/Foz-do-Arelho-Surf-Guide/4350/",
        "id": 4350,
        "lat": 39.4354,
        "lon": -9.2329,
        "name": "Foz do Arelho",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Sao-Pedro-do-Moel-Surf-Report/4351/",
        "guide": "/Sao-Pedro-do-Moel-Surf-Guide/4351/",
        "id": 4351,
        "lat": 39.7571,
        "lon": -9.034,
        "name": "S\u00e3o Pedro do Moel",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Leirosa-Surf-Report/4352/",
        "guide": "/Leirosa-Surf-Guide/4352/",
        "id": 4352,
        "lat": 40.0567,
        "lon": -8.8925,
        "name": "Leirosa",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Torreira-Surf-Report/4353/",
        "guide": "/Torreira-Surf-Guide/4353/",
        "id": 4353,
        "lat": 40.757,
        "lon": -8.7177,
        "name": "Torreira",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Furadouro-Surf-Report/4354/",
        "guide": "/Furadouro-Surf-Guide/4354/",
        "id": 4354,
        "lat": 40.8725,
        "lon": -8.6793,
        "name": "Furadouro",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Miramar-Surf-Report/4355/",
        "guide": "/Miramar-Surf-Guide/4355/",
        "id": 4355,
        "lat": 41.0683,
        "lon": -8.6596,
        "name": "Miramar",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Luz-Porto-Surf-Report/4356/",
        "guide": "/Luz-Porto-Surf-Guide/4356/",
        "id": 4356,
        "lat": 41.1521,
        "lon": -8.6793,
        "name": "Luz (Porto)",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Perafita-Surf-Report/4357/",
        "guide": "/Perafita-Surf-Guide/4357/",
        "id": 4357,
        "lat": 41.2204,
        "lon": -8.7176,
        "name": "Perafita",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Azurara-Surf-Report/4358/",
        "guide": "/Azurara-Surf-Guide/4358/",
        "id": 4358,
        "lat": 41.3339,
        "lon": -8.7412,
        "name": "Azurara",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Vila-do-Conde-Surf-Report/4359/",
        "guide": "/Vila-do-Conde-Surf-Guide/4359/",
        "id": 4359,
        "lat": 41.3512,
        "lon": -8.7562,
        "name": "Vila do Conde",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Povoa-do-Varzim-Surf-Report/4360/",
        "guide": "/Povoa-do-Varzim-Surf-Guide/4360/",
        "id": 4360,
        "lat": 41.3847,
        "lon": -8.777,
        "name": "P\u00f3voa do Varzim",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Fao-Surf-Report/4361/",
        "guide": "/Fao-Surf-Guide/4361/",
        "id": 4361,
        "lat": 41.5201,
        "lon": -8.7902,
        "name": "F\u00e3o",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Esposende-Surf-Report/4362/",
        "guide": "/Esposende-Surf-Guide/4362/",
        "id": 4362,
        "lat": 41.5466,
        "lon": -8.7944,
        "name": "Esposende",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Vila-Praia-de-Ancora-Surf-Report/4363/",
        "guide": "/Vila-Praia-de-Ancora-Surf-Guide/4363/",
        "id": 4363,
        "lat": 41.8071,
        "lon": -8.8687,
        "name": "Vila Praia de \u00c2ncora",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Praia-da-Tocha-Surf-Report/4572/",
        "guide": "/Praia-da-Tocha-Surf-Guide/4572/",
        "id": 4572,
        "lat": 40.3299,
        "lon": -8.8446,
        "name": "Praia da Tocha",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    },
    {
        "forecast": "/Praia-de-Faro-Surf-Report/4624/",
        "guide": "/Praia-de-Faro-Surf-Guide/4624/",
        "id": 4624,
        "lat": 37.0051,
        "lon": -7.9935,
        "name": "Praia de Faro",
        "offset": 3600,
        "timezone": "Europe/Lisbon"
    }
]
