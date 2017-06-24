import collections

PLAYERS = {
    "AquaZephyron": "AquaZephyron-1818",
    "Bentobox": "bentobox-11644",
    "Cangzter": "Cangzter-1459",
    "Jerapah": "Jerapah-1484",
    "Marcel": "Marcel-1694",
    "MaxKusnad": "MaxKusnad-1427",
    "Sanctumsacre": "Sanctumsacre-1927",
    "Stikman": "StikMan-11838",
    "Shirousagi": "shirousagi-11769",
    "TitaniumBro": "titaniumBro-1595",
    "Blindtrek": "BlindTrek-1514",
    "Bebekterbang": "bebekterbang-1271",
    "Dinarys": "Dinarys-11713",
    "Vortex": "Vortex-1240"
}

HEROES = {
    "Hanzo": "hanzo",
    "Zenyatta": "zenyatta",
    "Ana": "ana",
    "Lucio": "lucio",
    "Zarya": "zarya",
    "Genji": "genji",
    "Roadhog": "roadhog",
    "Mercy": "mercy",
    "Tracer": "tracer",
    "D.VA": "dva",
    "Widowmaker": "widowmaker",
    "McCree": "mccree",
    "Soldier:76": "soldier76",
    "Reinhardt": "reinhardt",
    "Mei": "mei",
    "Pharah": "pharah",
    "Reaper": "reaper",
    "Torbjorn": "torbjorn",
    "Bastion": "bastion",
    "Winston": "winston",
    "Junkrat": "junkrat",
    "Symmetra": "symmetra",
    "Sombra": "sombra"
}

PLAYERS = collections.OrderedDict(sorted(PLAYERS.items()))
HEROES = collections.OrderedDict(sorted(HEROES.items()))
