from dataclasses import dataclass
from typing import List, Dict, Any, Callable, Tuple
import random

class NumericalQuestions:
    """
    Contains all numerical patterns and sequences for both English and Czech languages.
    Each pattern includes a name, a function to generate the next number, and an explanation.
    """
    
    QUESTIONS = {
        'en': {
            'sequences': [
                # Basic arithmetic progressions
                {
                    'name': 'add_3',
                    'generator': lambda x: x + 3,
                    'start_range': (2, 10),
                    'steps': 4,
                    'explanation': 'Each number increases by 3',
                    'difficulty': 1
                },
                {
                    'name': 'add_5',
                    'generator': lambda x: x + 5,
                    'start_range': (1, 10),
                    'steps': 4,
                    'explanation': 'Each number increases by 5',
                    'difficulty': 1
                },
                
                # Multiplicative sequences
                {
                    'name': 'double',
                    'generator': lambda x: x * 2,
                    'start_range': (2, 6),
                    'steps': 4,
                    'explanation': 'Each number is doubled',
                    'difficulty': 2
                },
                {
                    'name': 'triple',
                    'generator': lambda x: x * 3,
                    'start_range': (1, 4),
                    'steps': 4,
                    'explanation': 'Each number is tripled',
                    'difficulty': 2
                },
                
                # More complex patterns
                {
                    'name': 'square',
                    'generator': lambda x: x ** 2,
                    'start_range': (2, 6),
                    'steps': 4,
                    'explanation': 'Each number is squared',
                    'difficulty': 3
                },
                {
                    'name': 'fibonacci_like',
                    'generator': lambda x, prev: x + prev,
                    'start_range': (1, 5),
                    'steps': 4,
                    'explanation': 'Each number is the sum of the two previous numbers',
                    'difficulty': 3
                },
                
                # Mixed operations
                {
                    'name': 'multiply_add',
                    'generator': lambda x: x * 2 + 1,
                    'start_range': (2, 5),
                    'steps': 4,
                    'explanation': 'Each number is doubled and then increased by 1',
                    'difficulty': 2
                },
                {
                    'name': 'alternate_operations',
                    'generator': lambda x, index: x + 3 if index % 2 == 0 else x * 2,
                    'start_range': (2, 5),
                    'steps': 4,
                    'explanation': 'Alternates between adding 3 and doubling the number',
                    'difficulty': 3
                }
            ],
            
            'number_relationships': [
                # Number pairs with relationships
                {
                    'pairs': [(2, 4), (3, 6), (4, 8)],
                    'question': 'If the pattern continues, what number pairs with 5?',
                    'options': ['10', '7', '9', '8'],
                    'correct': '10',
                    'explanation': 'Each second number is double the first number'
                },
                {
                    'pairs': [(1, 1), (2, 4), (3, 9)],
                    'question': 'If the pattern continues, what number pairs with 4?',
                    'options': ['16', '12', '8', '6'],
                    'correct': '16',
                    'explanation': 'Each second number is the square of the first number'
                }
            ]
        },
        
        'cs': {
            'sequences': [
                # Základní aritmetické posloupnosti
                {
                    'name': 'přičti_3',
                    'generator': lambda x: x + 3,
                    'start_range': (2, 10),
                    'steps': 4,
                    'explanation': 'Každé číslo se zvýší o 3',
                    'difficulty': 1
                },
                {
                    'name': 'přičti_5',
                    'generator': lambda x: x + 5,
                    'start_range': (1, 10),
                    'steps': 4,
                    'explanation': 'Každé číslo se zvýší o 5',
                    'difficulty': 1
                },
                
                # Násobné posloupnosti
                {
                    'name': 'dvojnásobek',
                    'generator': lambda x: x * 2,
                    'start_range': (2, 6),
                    'steps': 4,
                    'explanation': 'Každé číslo se vynásobí dvěma',
                    'difficulty': 2
                },
                {
                    'name': 'trojnásobek',
                    'generator': lambda x: x * 3,
                    'start_range': (1, 4),
                    'steps': 4,
                    'explanation': 'Každé číslo se vynásobí třemi',
                    'difficulty': 2
                },
                
                # Složitější vzorce
                {
                    'name': 'druhá_mocnina',
                    'generator': lambda x: x ** 2,
                    'start_range': (2, 6),
                    'steps': 4,
                    'explanation': 'Každé číslo se umocní na druhou',
                    'difficulty': 3
                },
                {
                    'name': 'fibonacci',
                    'generator': lambda x, prev: x + prev,
                    'start_range': (1, 5),
                    'steps': 4,
                    'explanation': 'Každé číslo je součtem dvou předchozích čísel',
                    'difficulty': 3
                },
                
                # Kombinované operace
                {
                    'name': 'násob_přičti',
                    'generator': lambda x: x * 2 + 1,
                    'start_range': (2, 5),
                    'steps': 4,
                    'explanation': 'Každé číslo se vynásobí dvěma a pak se přičte jedna',
                    'difficulty': 2
                },
                {
                    'name': 'střídavé_operace',
                    'generator': lambda x, index: x + 3 if index % 2 == 0 else x * 2,
                    'start_range': (2, 5),
                    'steps': 4,
                    'explanation': 'Střídá se přičtení trojky a násobení dvěma',
                    'difficulty': 3
                }
            ],
            
            'number_relationships': [
                # Vztahy mezi páry čísel
                {
                    'pairs': [(2, 4), (3, 6), (4, 8)],
                    'question': 'Pokud vzorec pokračuje, jaké číslo patří k číslu 5?',
                    'options': ['10', '7', '9', '8'],
                    'correct': '10',
                    'explanation': 'Každé druhé číslo je dvojnásobkem prvního čísla'
                },
                {
                    'pairs': [(1, 1), (2, 4), (3, 9)],
                    'question': 'Pokud vzorec pokračuje, jaké číslo patří k číslu 4?',
                    'options': ['16', '12', '8', '6'],
                    'correct': '16',
                    'explanation': 'Každé druhé číslo je druhou mocninou prvního čísla'
                }
            ]
        }
    }

    @staticmethod
    def generate_sequence(pattern: Dict[str, Any], lang: str = 'en') -> Tuple[str, List[str], str, str]:
        """
        Generates a sequence based on the given pattern and returns the question,
        options, correct answer, and explanation.
        """
        start = random.randint(*pattern['start_range'])
        sequence = [start]
        
        # Generate sequence
        for i in range(pattern['steps']):
            if 'prev' in pattern['generator'].__code__.co_varnames:
                if i == 0:
                    next_num = pattern['generator'](sequence[0], sequence[0])
                else:
                    next_num = pattern['generator'](sequence[-1], sequence[-2])
            elif 'index' in pattern['generator'].__code__.co_varnames:
                next_num = pattern['generator'](sequence[-1], i)
            else:
                next_num = pattern['generator'](sequence[-1])
            sequence.append(next_num)
        
        # Create question
        if lang == 'en':
            question = f"What comes next in the sequence: {', '.join(map(str, sequence[:-1]))}?"
        else:
            question = f"Jaké číslo následuje v posloupnosti: {', '.join(map(str, sequence[:-1]))}?"
        
        # Generate options
        correct = str(sequence[-1])
        wrong_options = [
            str(sequence[-2] + random.randint(1, 5)),
            str(sequence[-2] - random.randint(1, 5)),
            str(int(sequence[-2] * 1.5))
        ]
        options = [correct] + wrong_options
        random.shuffle(options)
        
        return question, options, correct, pattern['explanation']

    @staticmethod
    def get_random_sequence(lang: str = 'en', difficulty: int = None) -> Dict[str, Any]:
        """
        Returns a random sequence pattern, optionally filtered by difficulty.
        """
        sequences = NumericalQuestions.QUESTIONS[lang]['sequences']
        if difficulty is not None:
            sequences = [s for s in sequences if s['difficulty'] == difficulty]
        return random.choice(sequences)