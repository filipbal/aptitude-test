from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import random
import string
import datetime
import json
from dataclasses import dataclass
from typing import List, Dict, Any, Callable
import math
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Replace with secure key in production

# Load translations
def load_translations():
    translations = {}
    translations_dir = os.path.join(os.path.dirname(__file__), 'translations')
    for filename in os.listdir(translations_dir):
        if filename.endswith('.json'):
            lang_code = filename[:-5]  # Remove .json extension
            with open(os.path.join(translations_dir, filename), 'r', encoding='utf-8') as f:
                translations[lang_code] = json.load(f)
    return translations

TRANSLATIONS = load_translations()

@dataclass
class Question:
    question_text: str
    options: List[str]
    correct_answer: str
    explanation: str
    matrix_data: Dict = None  # New field for matrix data

    def to_dict(self):
        data = {
            'question_text': self.question_text,
            'options': self.options,
            'correct_answer': self.correct_answer,
            'explanation': self.explanation
        }
        if self.matrix_data:
            data['matrix_data'] = self.matrix_data
        return data

class VerbalQuestionGenerator:
    def __init__(self):
        # Move relationships and analogies to instance variables
        self.available_relationships = [
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
            # Antonyms
            {
                'pair': ('LIGHT', 'DARK'),
                'options': ['HOT:COLD', 'FAST:SLOW', 'BIG:SMALL', 'HAPPY:GLAD'],
                'correct': 'HOT:COLD',
                'explanation': 'LIGHT and DARK are opposites, as are HOT and COLD'
            },
            # Part-to-whole relationships
            {
                'pair': ('PETAL', 'FLOWER'),
                'options': ['WHEEL:CAR', 'BOOK:PAGE', 'TREE:FOREST', 'WATER:OCEAN'],
                'correct': 'WHEEL:CAR',
                'explanation': 'A PETAL is part of a FLOWER, as a WHEEL is part of a CAR'
            },
            # Cause and effect
            {
                'pair': ('RAIN', 'FLOOD'),
                'options': ['FIRE:SMOKE', 'DAY:NIGHT', 'SUMMER:WINTER', 'DOOR:WINDOW'],
                'correct': 'FIRE:SMOKE',
                'explanation': 'RAIN can cause a FLOOD, as FIRE causes SMOKE'
            },
            # Tool and user
            {
                'pair': ('HAMMER', 'CARPENTER'),
                'options': ['SCALPEL:SURGEON', 'PEN:BOOK', 'CAR:ROAD', 'HOUSE:BUILDER'],
                'correct': 'SCALPEL:SURGEON',
                'explanation': 'A HAMMER is used by a CARPENTER, as a SCALPEL is used by a SURGEON'
            }
        ]
        
        self.available_analogies = [
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
                'explanation': 'A keyboard is used to type, as a brush is used to paint - both are tools for their respective actions'
            }
        ]
        
        self.reset_pools()

    def reset_pools(self):
        """Reset question pools to their initial state"""
        self.relationships = self.available_relationships.copy()
        self.analogies = self.available_analogies.copy()

    def generate_word_relationship(self) -> Question:
        # If both pools are empty, refill them
        if not self.relationships and not self.analogies:
            self.reset_pools()
            
        # Choose which type to generate (but only if that pool isn't empty)
        can_use_relationships = bool(self.relationships)
        can_use_analogies = bool(self.analogies)
        
        if can_use_relationships and can_use_analogies:
            use_relationship = random.choice([True, False])
        else:
            use_relationship = can_use_relationships

        if use_relationship:
            # Generate a relationship question
            chosen = self.relationships.pop(random.randrange(len(self.relationships)))
            question_text = f"What is the relationship between {chosen['pair'][0]} and {chosen['pair'][1]}?"
        else:
            # Generate an analogy question
            chosen = self.analogies.pop(random.randrange(len(self.analogies)))
            question_text = chosen['question']
            
        return Question(
            question_text=question_text,
            options=chosen['options'],
            correct_answer=chosen['correct'],
            explanation=chosen['explanation']
        )

class NumericalQuestionGenerator:
    def __init__(self):
        self.available_patterns = [
            ('double', lambda x: x * 2),
            ('triple', lambda x: x * 3),
            ('add_3', lambda x: x + 3),
            ('add_5', lambda x: x + 5),
            ('square', lambda x: x ** 2),
            ('times_1.5', lambda x: int(x * 1.5))
        ]
        self.reset_pools()
        
    def reset_pools(self):
        """Reset patterns pool to initial state"""
        self.patterns = self.available_patterns.copy()
        
    def generate_number_sequence(self) -> Question:
        if not self.patterns:
            self.reset_pools()
            
        pattern_name, pattern_func = self.patterns.pop(random.randrange(len(self.patterns)))
        start = random.randint(2, 10)
        sequence = [start]
        
        # Generate sequence
        for _ in range(4):
            sequence.append(pattern_func(sequence[-1]))
        
        # Create question
        question_text = f"What comes next in the sequence: {', '.join(map(str, sequence[:-1]))}?"
        options = [
            str(sequence[-1]),  # Correct answer
            str(sequence[-2] + random.randint(1, 5)),
            str(sequence[-2] - random.randint(1, 5)),
            str(int(sequence[-2] * 1.2))
        ]
        random.shuffle(options)
        
        return Question(
            question_text=question_text,
            options=options,
            correct_answer=str(sequence[-1]),
            explanation=f"The pattern is: each number is {pattern_name}"
        )

class DiagrammaticQuestionGenerator:
    def __init__(self):
        self.available_patterns = [
            # Basic shape alternation
            {
                'sequence': '□ → ■ → □ → ■',
                'options': ['□', '■', '△', '○'],
                'correct': '□',
                'explanation': 'The pattern alternates between filled and unfilled squares'
            },
            # Shape progression
            {
                'sequence': '△ → □ → ○ → △ → □',
                'options': ['○', '△', '□', '■'],
                'correct': '○',
                'explanation': 'The sequence triangle-square-circle repeats'
            },
            # Size progression
            {
                'sequence': '○ → ◎ → ⊕ → ○ → ◎',
                'options': ['⊕', '○', '◎', '□'],
                'correct': '⊕',
                'explanation': 'The circles increase in complexity then restart'
            },
            # Rotation pattern
            {
                'sequence': '↑ → → → ↓ → ←',
                'options': ['↑', '→', '↓', '←'],
                'correct': '↑',
                'explanation': 'The arrow rotates 90 degrees clockwise each step'
            },
            # Combined shapes
            {
                'sequence': '□ → □△ → □△○ → □△',
                'options': ['□', '△', '○', '□△○'],
                'correct': '□',
                'explanation': 'The pattern adds and removes shapes cyclically'
            }
        ]
        
        self.available_matrices = [
            {
                'matrix': [
                    ['○', '□'],
                    ['□', None]  # None represents the question mark
                ],
                'options': ['○', '□', '△', '■'],
                'correct': '○',
                'explanation': 'The shapes alternate in a diagonal pattern'
            },
            {
                'matrix': [
                    ['■', '□', '■'],
                    ['□', '■', '□'],
                    ['■', '□', None]
                ],
                'options': ['■', '□', '△', '○'],
                'correct': '■',
                'explanation': 'The pattern alternates between filled and unfilled squares in each row'
            },
            {
                'matrix': [
                    ['△', '○', '△'],
                    ['○', '△', '○'],
                    ['△', '○', None]
                ],
                'options': ['△', '○', '□', '■'],
                'correct': '△',
                'explanation': 'The pattern alternates between triangle and circle in each row'
            }
        ]
        
        self.reset_pools()
        
    def reset_pools(self):
        """Reset both pattern pools to initial state"""
        self.patterns = self.available_patterns.copy()
        self.matrices = self.available_matrices.copy()

    def generate_pattern_completion(self) -> Question:
        # If both pools are empty, refill them
        if not self.patterns and not self.matrices:
            self.reset_pools()
            
        # Choose which type to generate (but only if that pool isn't empty)
        can_use_patterns = bool(self.patterns)
        can_use_matrices = bool(self.matrices)
        
        if can_use_patterns and can_use_matrices:
            use_pattern = random.choice([True, False])
        else:
            use_pattern = can_use_patterns

        if use_pattern:
            chosen = self.patterns.pop(random.randrange(len(self.patterns)))
            question_text = f"What comes next in the pattern: {chosen['sequence']}?"
            return Question(
                question_text=question_text,
                options=chosen['options'],
                correct_answer=chosen['correct'],
                explanation=chosen['explanation']
            )
        else:
            chosen = self.matrices.pop(random.randrange(len(self.matrices)))
            return Question(
                question_text="What should replace the question mark?",
                options=chosen['options'],
                correct_answer=chosen['correct'],
                explanation=chosen['explanation'],
                matrix_data={
                    'matrix': chosen['matrix'],
                    'rows': len(chosen['matrix']),
                    'cols': len(chosen['matrix'][0])
                }
            )

class TestManager:
    def __init__(self):
        self.verbal_generator = VerbalQuestionGenerator()
        self.numerical_generator = NumericalQuestionGenerator()
        self.diagrammatic_generator = DiagrammaticQuestionGenerator()
    
    def generate_test_section(self, section_type: str, num_questions: int = 5) -> List[Question]:
        generator_map = {
            'verbal': self.verbal_generator.generate_word_relationship,
            'numerical': self.numerical_generator.generate_number_sequence,
            'diagrammatic': self.diagrammatic_generator.generate_pattern_completion
        }
        
        generator = generator_map.get(section_type)
        if not generator:
            raise ValueError(f"Unknown section type: {section_type}")
            
        return [generator() for _ in range(num_questions)]

@app.before_request
def before_request():
    if 'lang' not in session:
        session['lang'] = 'en'

@app.route('/switch_language/<lang>')
def switch_language(lang):
    if lang in TRANSLATIONS:
        session['lang'] = lang
    return redirect(request.referrer or url_for('index'))

@app.route('/')
def index():
    translations = TRANSLATIONS[session.get('lang', 'en')]
    return render_template('index.html', t=translations)

@app.route('/start_test/<section_type>')
def start_test(section_type):
    translations = TRANSLATIONS[session.get('lang', 'en')]
    test_manager = TestManager()
    questions = test_manager.generate_test_section(section_type)
    
    questions_data = [q.to_dict() for q in questions]
    
    session['current_test'] = {
        'section_type': section_type,
        'questions': questions_data,
        'start_time': datetime.datetime.now().isoformat(),
        'answers': []
    }
    
    return render_template('test.html', section_type=section_type, questions=questions, t=translations)

@app.route('/submit_test', methods=['POST'])
def submit_test():
    answers = request.json.get('answers', [])
    current_test = session.get('current_test', {})
    questions = current_test.get('questions', [])
    
    score = sum(1 for q, a in zip(questions, answers) if q['correct_answer'] == a)
    
    result = {
        'score': score,
        'total': len(questions),
        'percentage': (score / len(questions)) * 100,
        'time_taken': (datetime.datetime.now() - 
                      datetime.datetime.fromisoformat(current_test['start_time'])).seconds
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)