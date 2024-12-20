from dataclasses import dataclass
from typing import List, Dict, Any, Optional
import random

class DiagrammaticQuestions:
    """
    Contains all diagrammatic patterns and matrices for both English and Czech languages.
    Questions include shape sequences, transformations, and pattern matrices.
    """
    
    QUESTIONS = {
        'en': {
            'sequences': [
                # Basic shape alternation
                {
                    'name': 'simple_alternation',
                    'sequence': '□ → ■ → □ → ■',
                    'options': ['□', '■', '△', '○'],
                    'correct': '□',
                    'explanation': 'The pattern alternates between filled and unfilled squares',
                    'difficulty': 1
                },
                {
                    'name': 'three_shape_cycle',
                    'sequence': '△ → □ → ○ → △ → □',
                    'options': ['○', '△', '□', '■'],
                    'correct': '○',
                    'explanation': 'The sequence triangle-square-circle repeats in order',
                    'difficulty': 1
                },
                
                # Size progression
                {
                    'name': 'growing_circle',
                    'sequence': '○ → ◎ → ⊕ → ○ → ◎',
                    'options': ['⊕', '○', '◎', '□'],
                    'correct': '⊕',
                    'explanation': 'The circles increase in complexity before returning to the start',
                    'difficulty': 2
                },
                {
                    'name': 'size_rotation',
                    'sequence': '• → ○ → ⊙ → • → ○',
                    'options': ['⊙', '•', '○', '◎'],
                    'correct': '⊙',
                    'explanation': 'The dot grows larger in each step, then returns to small',
                    'difficulty': 2
                },
                
                # Rotation patterns
                {
                    'name': 'arrow_rotation',
                    'sequence': '↑ → → → ↓ → ←',
                    'options': ['↑', '→', '↓', '←'],
                    'correct': '↑',
                    'explanation': 'The arrow rotates 90 degrees clockwise in each step',
                    'difficulty': 2
                },
                {
                    'name': 'triangle_rotation',
                    'sequence': '△ → ▷ → ▽ → ◁',
                    'options': ['△', '▷', '▽', '◁'],
                    'correct': '△',
                    'explanation': 'The triangle rotates 90 degrees clockwise in each step',
                    'difficulty': 2
                },
                
                # Combined transformations
                {
                    'name': 'shape_addition',
                    'sequence': '□ → □△ → □△○ → □△',
                    'options': ['□', '△', '○', '□△○'],
                    'correct': '□',
                    'explanation': 'Shapes are added and removed in a cyclic pattern',
                    'difficulty': 3
                },
                {
                    'name': 'fill_rotation',
                    'sequence': '□ → ■ → ▲ → △',
                    'options': ['□', '■', '▲', '△'],
                    'correct': '□',
                    'explanation': 'The shape alternates between filled and unfilled while changing form',
                    'difficulty': 3
                }
            ],
            
            'matrices': [
                # 2x2 matrices
                {
                    'name': 'simple_alternation',
                    'matrix': [
                        ['○', '□'],
                        ['□', None]
                    ],
                    'options': ['○', '□', '△', '■'],
                    'correct': '○',
                    'explanation': 'Shapes alternate in a diagonal pattern',
                    'difficulty': 1
                },
                {
                    'name': 'opposite_corners',
                    'matrix': [
                        ['■', '□'],
                        ['□', None]
                    ],
                    'options': ['■', '□', '○', '△'],
                    'correct': '■',
                    'explanation': 'Opposite corners contain the same shape',
                    'difficulty': 1
                },
                
                # 3x3 matrices
                {
                    'name': 'alternating_fills',
                    'matrix': [
                        ['■', '□', '■'],
                        ['□', '■', '□'],
                        ['■', '□', None]
                    ],
                    'options': ['■', '□', '△', '○'],
                    'correct': '■',
                    'explanation': 'Filled and unfilled squares alternate in each row and column',
                    'difficulty': 2
                },
                {
                    'name': 'rotating_shapes',
                    'matrix': [
                        ['△', '○', '△'],
                        ['○', '△', '○'],
                        ['△', '○', None]
                    ],
                    'options': ['△', '○', '□', '■'],
                    'correct': '△',
                    'explanation': 'Triangles and circles alternate in a regular pattern',
                    'difficulty': 2
                },
                
                # Complex patterns
                {
                    'name': 'shape_progression',
                    'matrix': [
                        ['○', '◎', '⊕'],
                        ['◎', '⊕', '○'],
                        ['⊕', '○', None]
                    ],
                    'options': ['◎', '○', '⊕', '□'],
                    'correct': '◎',
                    'explanation': 'Each row and column shows a progression of circle complexity',
                    'difficulty': 3
                }
            ]
        },
        
        'cs': {
            'sequences': [
                # Základní střídání tvarů
                {
                    'name': 'jednoduché_střídání',
                    'sequence': '□ → ■ → □ → ■',
                    'options': ['□', '■', '△', '○'],
                    'correct': '□',
                    'explanation': 'Vzor střídá prázdné a plné čtverce',
                    'difficulty': 1
                },
                {
                    'name': 'tři_tvary',
                    'sequence': '△ → □ → ○ → △ → □',
                    'options': ['○', '△', '□', '■'],
                    'correct': '○',
                    'explanation': 'Sekvence trojúhelník-čtverec-kruh se opakuje',
                    'difficulty': 1
                },
                
                # Postupné zvětšování
                {
                    'name': 'rostoucí_kruh',
                    'sequence': '○ → ◎ → ⊕ → ○ → ◎',
                    'options': ['⊕', '○', '◎', '□'],
                    'correct': '⊕',
                    'explanation': 'Kruhy se postupně zvětšují a pak se vrací na začátek',
                    'difficulty': 2
                },
                {
                    'name': 'velikost_rotace',
                    'sequence': '• → ○ → ⊙ → • → ○',
                    'options': ['⊙', '•', '○', '◎'],
                    'correct': '⊙',
                    'explanation': 'Tečka se v každém kroku zvětšuje a pak se vrací k malé',
                    'difficulty': 2
                },
                
                # Vzory rotace
                {
                    'name': 'rotace_šipky',
                    'sequence': '↑ → → → ↓ → ←',
                    'options': ['↑', '→', '↓', '←'],
                    'correct': '↑',
                    'explanation': 'Šipka se otáčí o 90 stupňů ve směru hodinových ručiček',
                    'difficulty': 2
                },
                {
                    'name': 'rotace_trojúhelníku',
                    'sequence': '△ → ▷ → ▽ → ◁',
                    'options': ['△', '▷', '▽', '◁'],
                    'correct': '△',
                    'explanation': 'Trojúhelník se otáčí o 90 stupňů ve směru hodinových ručiček',
                    'difficulty': 2
                },
                
                # Kombinované transformace
                {
                    'name': 'přidávání_tvarů',
                    'sequence': '□ → □△ → □△○ → □△',
                    'options': ['□', '△', '○', '□△○'],
                    'correct': '□',
                    'explanation': 'Tvary se přidávají a odebírají v cyklickém vzoru',
                    'difficulty': 3
                },
                {
                    'name': 'výplň_rotace',
                    'sequence': '□ → ■ → ▲ → △',
                    'options': ['□', '■', '▲', '△'],
                    'correct': '□',
                    'explanation': 'Tvar se střídá mezi plným a prázdným a současně mění formu',
                    'difficulty': 3
                }
            ],
            
            'matrices': [
                # 2x2 matice
                {
                    'name': 'jednoduché_střídání',
                    'matrix': [
                        ['○', '□'],
                        ['□', None]
                    ],
                    'options': ['○', '□', '△', '■'],
                    'correct': '○',
                    'explanation': 'Tvary se střídají v diagonálním vzoru',
                    'difficulty': 1
                },
                {
                    'name': 'protilehlé_rohy',
                    'matrix': [
                        ['■', '□'],
                        ['□', None]
                    ],
                    'options': ['■', '□', '○', '△'],
                    'correct': '■',
                    'explanation': 'Protilehlé rohy obsahují stejný tvar',
                    'difficulty': 1
                },
                
                # 3x3 matice
                {
                    'name': 'střídání_výplně',
                    'matrix': [
                        ['■', '□', '■'],
                        ['□', '■', '□'],
                        ['■', '□', None]
                    ],
                    'options': ['■', '□', '△', '○'],
                    'correct': '■',
                    'explanation': 'Plné a prázdné čtverce se střídají v každém řádku a sloupci',
                    'difficulty': 2
                },
                {
                    'name': 'rotující_tvary',
                    'matrix': [
                        ['△', '○', '△'],
                        ['○', '△', '○'],
                        ['△', '○', None]
                    ],
                    'options': ['△', '○', '□', '■'],
                    'correct': '△',
                    'explanation': 'Trojúhelníky a kruhy se střídají v pravidelném vzoru',
                    'difficulty': 2
                },
                
                # Složité vzory
                {
                    'name': 'posloupnost_tvarů',
                    'matrix': [
                        ['○', '◎', '⊕'],
                        ['◎', '⊕', '○'],
                        ['⊕', '○', None]
                    ],
                    'options': ['◎', '○', '⊕', '□'],
                    'correct': '◎',
                    'explanation': 'Každý řádek a sloupec ukazuje posloupnost složitosti kruhů',
                    'difficulty': 3
                }
            ]
        }
    }

    @staticmethod
    def get_random_sequence(lang: str = 'en', difficulty: Optional[int] = None) -> Dict[str, Any]:
        """
        Returns a random sequence pattern, optionally filtered by difficulty.
        """
        sequences = DiagrammaticQuestions.QUESTIONS[lang]['sequences']
        if difficulty is not None:
            sequences = [s for s in sequences if s['difficulty'] == difficulty]
        return random.choice(sequences)

    @staticmethod
    def get_random_matrix(lang: str = 'en', difficulty: Optional[int] = None) -> Dict[str, Any]:
        """
        Returns a random matrix pattern, optionally filtered by difficulty.
        """
        matrices = DiagrammaticQuestions.QUESTIONS[lang]['matrices']
        if difficulty is not None:
            matrices = [m for m in matrices if m['difficulty'] == difficulty]
        return random.choice(matrices)

    @staticmethod
    def format_sequence_question(sequence: Dict[str, Any], lang: str = 'en') -> str:
        """
        Formats a sequence question in the specified language.
        """
        if lang == 'en':
            return f"What comes next in the pattern: {sequence['sequence']}?"
        else:
            return f"Jaký tvar následuje ve vzoru: {sequence['sequence']}?"

    @staticmethod
    def format_matrix_question(lang: str = 'en') -> str:
        """
        Returns the matrix question text in the specified language.
        """
        return "What should replace the question mark?" if lang == 'en' else "Jaký tvar má být místo otazníku?"