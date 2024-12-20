from dataclasses import dataclass
from typing import List, Tuple, Dict, Any

class VerbalQuestions:
    """
    Contains all verbal questions for both English and Czech languages.
    Questions are organized by type (relationships and analogies) and language.
    """
    
    QUESTIONS = {
        'en': {
            'relationships': [
                # Synonyms
                {
                    'pair': ('FAST', 'SWIFT'),
                    'options': ['SLOW:QUICK', 'TALL:HIGH', 'DARK:LIGHT', 'HOT:WARM'],
                    'correct': 'SLOW:QUICK',
                    'explanation': 'FAST and SWIFT are synonyms, as are SLOW and QUICK'
                },
                {
                    'pair': ('BRAVE', 'COURAGEOUS'),
                    'options': ['TIMID:FEARFUL', 'HAPPY:SAD', 'STRONG:WEAK', 'WISE:SMART'],
                    'correct': 'TIMID:FEARFUL',
                    'explanation': 'BRAVE and COURAGEOUS are synonyms, as are TIMID and FEARFUL'
                },
                {
                    'pair': ('HAPPY', 'JOYFUL'),
                    'options': ['SAD:MISERABLE', 'COLD:HOT', 'BIG:LARGE', 'FAST:SLOW'],
                    'correct': 'SAD:MISERABLE',
                    'explanation': 'HAPPY and JOYFUL are synonyms, as are SAD and MISERABLE'
                },
                
                # Antonyms
                {
                    'pair': ('LIGHT', 'DARK'),
                    'options': ['HOT:COLD', 'FAST:SLOW', 'BIG:SMALL', 'HAPPY:GLAD'],
                    'correct': 'HOT:COLD',
                    'explanation': 'LIGHT and DARK are opposites, as are HOT and COLD'
                },
                {
                    'pair': ('SUCCESS', 'FAILURE'),
                    'options': ['VICTORY:DEFEAT', 'DAY:NIGHT', 'WATER:ICE', 'TREE:LEAF'],
                    'correct': 'VICTORY:DEFEAT',
                    'explanation': 'SUCCESS and FAILURE are opposites, as are VICTORY and DEFEAT'
                },
                {
                    'pair': ('BEGINNING', 'END'),
                    'options': ['START:FINISH', 'MORNING:NIGHT', 'SUMMER:WINTER', 'BOOK:PAGE'],
                    'correct': 'START:FINISH',
                    'explanation': 'BEGINNING and END are opposites, as are START and FINISH'
                },
                
                # Part-to-whole relationships
                {
                    'pair': ('PETAL', 'FLOWER'),
                    'options': ['WHEEL:CAR', 'BOOK:PAGE', 'TREE:FOREST', 'WATER:OCEAN'],
                    'correct': 'WHEEL:CAR',
                    'explanation': 'A PETAL is part of a FLOWER, as a WHEEL is part of a CAR'
                },
                {
                    'pair': ('PAGE', 'BOOK'),
                    'options': ['BRANCH:TREE', 'STUDENT:CLASS', 'CLOUD:SKY', 'SUN:DAY'],
                    'correct': 'BRANCH:TREE',
                    'explanation': 'A PAGE is part of a BOOK, as a BRANCH is part of a TREE'
                },
                {
                    'pair': ('PIXEL', 'SCREEN'),
                    'options': ['BRICK:WALL', 'ROAD:MAP', 'HOUSE:CITY', 'LETTER:WORD'],
                    'correct': 'BRICK:WALL',
                    'explanation': 'A PIXEL is part of a SCREEN, as a BRICK is part of a WALL'
                },
                
                # Cause and effect
                {
                    'pair': ('RAIN', 'FLOOD'),
                    'options': ['FIRE:SMOKE', 'DAY:NIGHT', 'SUMMER:WINTER', 'DOOR:WINDOW'],
                    'correct': 'FIRE:SMOKE',
                    'explanation': 'RAIN can cause a FLOOD, as FIRE causes SMOKE'
                },
                {
                    'pair': ('STUDY', 'KNOWLEDGE'),
                    'options': ['PRACTICE:SKILL', 'BOOK:PAGE', 'TEACHER:STUDENT', 'SCHOOL:CLASS'],
                    'correct': 'PRACTICE:SKILL',
                    'explanation': 'STUDY leads to KNOWLEDGE, as PRACTICE leads to SKILL'
                },
                {
                    'pair': ('EXERCISE', 'FITNESS'),
                    'options': ['DIET:HEALTH', 'SPORT:GAME', 'RUN:WALK', 'GYM:WORKOUT'],
                    'correct': 'DIET:HEALTH',
                    'explanation': 'EXERCISE leads to FITNESS, as DIET contributes to HEALTH'
                },
                
                # Tool and user
                {
                    'pair': ('HAMMER', 'CARPENTER'),
                    'options': ['SCALPEL:SURGEON', 'PEN:BOOK', 'CAR:ROAD', 'HOUSE:BUILDER'],
                    'correct': 'SCALPEL:SURGEON',
                    'explanation': 'A HAMMER is used by a CARPENTER, as a SCALPEL is used by a SURGEON'
                },
                {
                    'pair': ('BRUSH', 'ARTIST'),
                    'options': ['CAMERA:PHOTOGRAPHER', 'PAINT:CANVAS', 'ART:MUSEUM', 'MUSIC:SONG'],
                    'correct': 'CAMERA:PHOTOGRAPHER',
                    'explanation': 'A BRUSH is used by an ARTIST, as a CAMERA is used by a PHOTOGRAPHER'
                }
            ],
            'analogies': [
                {
                    'question': 'BIRD is to SKY as FISH is to?',
                    'options': ['WATER', 'BOAT', 'SCALE', 'NET'],
                    'correct': 'WATER',
                    'explanation': 'Birds move through the sky as fish move through water - both are natural habitats'
                },
                {
                    'question': 'CANVAS is to PAINTER as STAGE is to?',
                    'options': ['ACTOR', 'CURTAIN', 'AUDIENCE', 'THEATRE'],
                    'correct': 'ACTOR',
                    'explanation': 'A canvas is the workspace of a painter, as a stage is the workspace of an actor'
                },
                {
                    'question': 'KEYBOARD is to TYPE as BRUSH is to?',
                    'options': ['PAINT', 'HAIR', 'CLEAN', 'BRISTLE'],
                    'correct': 'PAINT',
                    'explanation': 'A keyboard is used to type, as a brush is used to paint'
                },
                {
                    'question': 'STUDENT is to SCHOOL as PATIENT is to?',
                    'options': ['HOSPITAL', 'DOCTOR', 'MEDICINE', 'AMBULANCE'],
                    'correct': 'HOSPITAL',
                    'explanation': 'A student goes to school to learn, as a patient goes to hospital for treatment'
                },
                {
                    'question': 'SEED is to PLANT as EGG is to?',
                    'options': ['BIRD', 'NEST', 'SHELL', 'TREE'],
                    'correct': 'BIRD',
                    'explanation': 'A seed grows into a plant, as an egg develops into a bird'
                }
            ]
        },
        'cs': {
			'relationships': [
				# Synonyma
				{
					'pair': ('KRÁSNÝ', 'NÁDHERNÝ'),
					'options': ['OŠKLIVÝ:ŠKAREDÝ', 'RYCHLÝ:POMALÝ', 'MALÝ:VELKÝ', 'TEPLÝ:STUDENÝ'],
					'correct': 'OŠKLIVÝ:ŠKAREDÝ',
					'explanation': 'KRÁSNÝ a NÁDHERNÝ jsou synonyma, stejně jako OŠKLIVÝ a ŠKAREDÝ'
				},
				{
					'pair': ('ODVÁŽNÝ', 'STATEČNÝ'),
					'options': ['BOJÁCNÝ:ZBABĚLÝ', 'SILNÝ:SLABÝ', 'MLADÝ:STARÝ', 'TICHÝ:HLASITÝ'],
					'correct': 'BOJÁCNÝ:ZBABĚLÝ',
					'explanation': 'ODVÁŽNÝ a STATEČNÝ jsou synonyma, stejně jako BOJÁCNÝ a ZBABĚLÝ'
				},
				{
					'pair': ('CHYTRÝ', 'MOUDRÝ'),
					'options': ['HLOUPÝ:POŠETILÝ', 'RYCHLÝ:POMALÝ', 'VYSOKÝ:NÍZKÝ', 'TEPLÝ:HORKÝ'],
					'correct': 'HLOUPÝ:POŠETILÝ',
					'explanation': 'CHYTRÝ a MOUDRÝ jsou synonyma, stejně jako HLOUPÝ a POŠETILÝ'
				},

				# Antonyma
				{
					'pair': ('RADOST', 'SMUTEK'),
					'options': ['LÁSKA:NENÁVIST', 'DEN:RÁNO', 'JARO:LÉTO', 'MOŘE:VODA'],
					'correct': 'LÁSKA:NENÁVIST',
					'explanation': 'RADOST a SMUTEK jsou protiklady, stejně jako LÁSKA a NENÁVIST'
				},
				{
					'pair': ('ŽIVOT', 'SMRT'),
					'options': ['ZAČÁTEK:KONEC', 'STROM:LIST', 'SLUNCE:MĚSÍC', 'VODA:LED'],
					'correct': 'ZAČÁTEK:KONEC',
					'explanation': 'ŽIVOT a SMRT jsou protiklady, stejně jako ZAČÁTEK a KONEC'
				},
				{
					'pair': ('BOHATSTVÍ', 'CHUDOBA'),
					'options': ['ÚSPĚCH:NEÚSPĚCH', 'ŠKOLA:TŘÍDA', 'MĚSTO:VESNICE', 'LÉTO:ZIMA'],
					'correct': 'ÚSPĚCH:NEÚSPĚCH',
					'explanation': 'BOHATSTVÍ a CHUDOBA jsou protiklady, stejně jako ÚSPĚCH a NEÚSPĚCH'
				},

				# Vztah část-celek
				{
					'pair': ('KAPKA', 'MOŘE'),
					'options': ['LIST:STROM', 'DEN:ROK', 'MĚSTO:ZEMĚ', 'KÁMEN:HORA'],
					'correct': 'LIST:STROM',
					'explanation': 'KAPKA je částí MOŘE, stejně jako LIST je částí STROMU'
				},
				{
					'pair': ('PÍSMENO', 'SLOVO'),
					'options': ['SLOKA:BÁSEŇ', 'KNIHA:KNIHOVNA', 'DŮM:ULICE', 'HORA:POHOŘÍ'],
					'correct': 'SLOKA:BÁSEŇ',
					'explanation': 'PÍSMENO je částí SLOVA, stejně jako SLOKA je částí BÁSNĚ'
				},
				{
					'pair': ('DLAŽDICE', 'MOZAIKA'),
					'options': ['CIHLA:ZEĎ', 'BARVA:OBRAZ', 'NOTA:MELODIE', 'KVĚT:ZAHRADA'],
					'correct': 'CIHLA:ZEĎ',
					'explanation': 'DLAŽDICE je částí MOZAIKY, stejně jako CIHLA je částí ZDI'
				},

				# Příčina a následek
				{
					'pair': ('UČENÍ', 'ZNALOST'),
					'options': ['TRÉNINK:DOVEDNOST', 'ŠKOLA:ŽÁCI', 'KNIHA:STRÁNKA', 'PENÍZE:BANKA'],
					'correct': 'TRÉNINK:DOVEDNOST',
					'explanation': 'UČENÍ vede ke ZNALOSTI, stejně jako TRÉNINK vede k DOVEDNOSTI'
				},
				{
					'pair': ('SUCHO', 'NEÚRODA'),
					'options': ['MRÁZ:ZMRZLINA', 'SLUNCE:TEPLO', 'NEMOC:LÉČBA', 'BOUŘE:POVODEŇ'],
					'correct': 'BOUŘE:POVODEŇ',
					'explanation': 'SUCHO způsobuje NEÚRODU, stejně jako BOUŘE způsobuje POVODEŇ'
				},
				{
					'pair': ('ZÁTĚŽ', 'ÚNAVA'),
					'options': ['STRES:VYČERPÁNÍ', 'SPÁNEK:ODPOČINEK', 'JÍDLO:HLAD', 'PRÁCE:MZDA'],
					'correct': 'STRES:VYČERPÁNÍ',
					'explanation': 'ZÁTĚŽ způsobuje ÚNAVU, stejně jako STRES způsobuje VYČERPÁNÍ'
				},

				# Nástroj a uživatel
				{
					'pair': ('ŠTĚTEC', 'MALÍŘ'),
					'options': ['HOUSLE:HOUSLISTA', 'BARVA:OBRAZ', 'PAPÍR:TUŽKA', 'SVĚTLO:LAMPA'],
					'correct': 'HOUSLE:HOUSLISTA',
					'explanation': 'ŠTĚTEC používá MALÍŘ, stejně jako HOUSLE používá HOUSLISTA'
				},
				{
					'pair': ('VAŘEČKA', 'KUCHAŘ'),
					'options': ['JEHLA:ŠVADLENA', 'JÍDLO:TALÍŘ', 'NŮŽ:VIDLIČKA', 'HRNEC:SPORÁK'],
					'correct': 'JEHLA:ŠVADLENA',
					'explanation': 'VAŘEČKU používá KUCHAŘ, stejně jako JEHLU používá ŠVADLENA'
				}
			],
			'analogies': [
				{
					'question': 'HŘEBEN je k VLASŮM jako KARTÁČ k?',
					'options': ['ZUBŮM', 'HLAVĚ', 'ŠAMPÓNU', 'ČESÁNÍ'],
					'correct': 'ZUBŮM',
					'explanation': 'HŘEBEN používáme na úpravu VLASŮ, stejně jako KARTÁČ používáme na čištění ZUBŮ'
				},
				{
					'question': 'KNIHOVNA je ke KNIHÁM jako GARÁŽ k?',
					'options': ['AUTŮM', 'ŘIDIČI', 'MECHANIKOVI', 'BENZÍNU'],
					'correct': 'AUTŮM',
					'explanation': 'KNIHOVNA je místo pro uložení KNIH, stejně jako GARÁŽ je místo pro uložení AUT'
				},
				{
					'question': 'REŽISÉR je k FILMU jako SKLADATEL k?',
					'options': ['HUDBĚ', 'ORCHESTRU', 'DIVADLU', 'NÁSTROJI'],
					'correct': 'HUDBĚ',
					'explanation': 'REŽISÉR tvoří FILM, stejně jako SKLADATEL tvoří HUDBU'
				},
				{
					'question': 'VČELA je k MEDU jako KRÁVA k?',
					'options': ['MLÉKU', 'TRÁVĚ', 'FARMĚ', 'STÁJI'],
					'correct': 'MLÉKU',
					'explanation': 'VČELA produkuje MED, stejně jako KRÁVA produkuje MLÉKO'
				},
				{
					'question': 'SEMÍNKO je k ROSTLINĚ jako VAJÍČKO k?',
					'options': ['PTÁKU', 'HNÍZDU', 'SKOŘÁPCE', 'STROMU'],
					'correct': 'PTÁKU',
					'explanation': 'Ze SEMÍNKA vyroste ROSTLINA, stejně jako z VAJÍČKA se vylíhne PTÁK'
				}
			]
		}
	}