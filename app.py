from flask import Flask, render_template, request, jsonify, session
import random
import string
import datetime
from dataclasses import dataclass
from typing import List, Dict, Any
import math

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Replace with secure key in production

@dataclass
class Question:
    question_text: str
    options: List[str]
    correct_answer: str
    explanation: str

class VerbalQuestionGenerator:
    @staticmethod
    def generate_word_relationship() -> Question:
        # Sample word relationships
        relationships = [
            {
                'pair': ('FAST', 'SWIFT'),
                'options': ['SLOW:QUICK', 'TALL:HIGH', 'DARK:LIGHT', 'HOT:WARM'],
                'correct': 'SLOW:QUICK',
                'explanation': 'FAST and SWIFT are synonyms, as are SLOW and QUICK'
            },
            # Add more relationships here
        ]
        
        chosen = random.choice(relationships)
        question_text = f"What is the relationship between {chosen['pair'][0]} and {chosen['pair'][1]}?"
        return Question(
            question_text=question_text,
            options=chosen['options'],
            correct_answer=chosen['correct'],
            explanation=chosen['explanation']
        )

class NumericalQuestionGenerator:
    @staticmethod
    def generate_number_sequence() -> Question:
        # Generate a sequence based on a random mathematical pattern
        patterns = [
            lambda x: x * 2,  # Double
            lambda x: x + 3,  # Add 3
            lambda x: x ** 2,  # Square
            lambda x: int(x * 1.5)  # 1.5 times
        ]
        
        pattern = random.choice(patterns)
        start = random.randint(2, 10)
        sequence = [start]
        
        # Generate sequence
        for _ in range(4):
            sequence.append(pattern(sequence[-1]))
        
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
            explanation=f"The pattern is: each number is transformed by a mathematical operation"
        )

class DiagrammaticQuestionGenerator:
    @staticmethod
    def generate_pattern_completion() -> Question:
        # Simplified version using text-based patterns for now
        # In a real implementation, this would use actual diagrams
        patterns = [
            {
                'sequence': '□ → ■ → □ → ■',
                'options': ['□', '■', '△', '○'],
                'correct': '□',
                'explanation': 'The pattern alternates between filled and unfilled squares'
            },
            # Add more patterns here
        ]
        
        chosen = random.choice(patterns)
        question_text = f"What comes next in the pattern: {chosen['sequence']}?"
        return Question(
            question_text=question_text,
            options=chosen['options'],
            correct_answer=chosen['correct'],
            explanation=chosen['explanation']
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_test/<section_type>')
def start_test(section_type):
    test_manager = TestManager()
    questions = test_manager.generate_test_section(section_type)
    session['current_test'] = {
        'section_type': section_type,
        'questions': questions,
        'start_time': datetime.datetime.now().isoformat(),
        'answers': []
    }
    return render_template('test.html', section_type=section_type, questions=questions)

@app.route('/submit_test', methods=['POST'])
def submit_test():
    answers = request.json.get('answers', [])
    current_test = session.get('current_test', {})
    questions = current_test.get('questions', [])
    
    score = sum(1 for q, a in zip(questions, answers) if q.correct_answer == a)
    
    result = {
        'score': score,
        'total': len(questions),
        'percentage': (score / len(questions)) * 100 if questions else 0,
        'time_taken': (datetime.datetime.now() - 
                      datetime.datetime.fromisoformat(current_test['start_time'])).seconds
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)