import sys
sys.dont_write_bytecode = True

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import random
import datetime
import json
import os
from dataclasses import dataclass
from typing import List, Dict, Any

# Import our new question modules
from questions.verbal import VerbalQuestions
from questions.numerical import NumericalQuestions
from questions.diagrammatical import DiagrammaticQuestions

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
    matrix_data: Dict = None

    def to_dict(self):
        """Convert question to dictionary format for session storage"""
        data = {
            'question_text': self.question_text,
            'options': self.options,
            'correct_answer': self.correct_answer,
            'explanation': self.explanation
        }
        if self.matrix_data:
            data['matrix_data'] = self.matrix_data
        return data

class TestManager:
    """
    Manages test generation and handles different question types and languages.
    """
    def __init__(self, lang='en'):
        self.lang = lang
        # Initialize question banks based on language
        self.questions = {
            'verbal': VerbalQuestions.QUESTIONS[lang],
            'numerical': NumericalQuestions.QUESTIONS[lang],
            'diagrammatic': DiagrammaticQuestions.QUESTIONS[lang]
        }

    def generate_verbal_question(self) -> Question:
        """Generate a verbal reasoning question"""
        # Randomly choose between relationships and analogies
        question_type = random.choice(['relationships', 'analogies'])
        question_bank = self.questions['verbal'][question_type]
        
        # Select a random question from the bank
        question_data = random.choice(question_bank)
        
        if question_type == 'relationships':
            question_text = (
                f"What is the relationship between {question_data['pair'][0]} and {question_data['pair'][1]}?"
                if self.lang == 'en' else
                f"Jaký je vztah mezi slovy {question_data['pair'][0]} a {question_data['pair'][1]}?"
            )
        else:
            question_text = question_data['question']

        return Question(
            question_text=question_text,
            options=question_data['options'],
            correct_answer=question_data['correct'],
            explanation=question_data['explanation']
        )

    def generate_numerical_question(self) -> Question:
        """Generate a numerical reasoning question"""
        # Get a random sequence pattern
        pattern = NumericalQuestions.get_random_sequence(self.lang)
        
        # Generate the sequence and question
        question_text, options, correct, explanation = (
            NumericalQuestions.generate_sequence(pattern, self.lang)
        )

        return Question(
            question_text=question_text,
            options=options,
            correct_answer=correct,
            explanation=explanation
        )

    def generate_diagrammatic_question(self) -> Question:
        """Generate a diagrammatic reasoning question"""
        # Randomly choose between sequence and matrix questions
        if random.choice([True, False]):
            # Sequence question
            sequence = DiagrammaticQuestions.get_random_sequence(self.lang)
            question_text = DiagrammaticQuestions.format_sequence_question(sequence, self.lang)
            
            return Question(
                question_text=question_text,
                options=sequence['options'],
                correct_answer=sequence['correct'],
                explanation=sequence['explanation']
            )
        else:
            # Matrix question
            matrix = DiagrammaticQuestions.get_random_matrix(self.lang)
            question_text = DiagrammaticQuestions.format_matrix_question(self.lang)
            
            return Question(
                question_text=question_text,
                options=matrix['options'],
                correct_answer=matrix['correct'],
                explanation=matrix['explanation'],
                matrix_data={
                    'matrix': matrix['matrix'],
                    'rows': len(matrix['matrix']),
                    'cols': len(matrix['matrix'][0])
                }
            )

    def generate_test_section(self, section_type: str, num_questions: int = 5) -> List[Question]:
        """Generate a complete test section of specified type"""
        generator_map = {
            'verbal': self.generate_verbal_question,
            'numerical': self.generate_numerical_question,
            'diagrammatic': self.generate_diagrammatic_question
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
    """Start a new test section with questions in the current language"""
    lang = session.get('lang', 'en')
    translations = TRANSLATIONS[lang]
    
    # Create test manager with current language
    test_manager = TestManager(lang)
    questions = test_manager.generate_test_section(section_type)
    
    # Store test data in session
    questions_data = [q.to_dict() for q in questions]
    session['current_test'] = {
        'section_type': section_type,
        'questions': questions_data,
        'start_time': datetime.datetime.now().isoformat(),
        'answers': []
    }
    
    return render_template('test.html', 
                         section_type=section_type, 
                         questions=questions, 
                         t=translations)

@app.route('/submit_test', methods=['POST'])
def submit_test():
    """Handle test submission and calculate results"""
    answers = request.json.get('answers', [])
    current_test = session.get('current_test', {})
    questions = current_test.get('questions', [])
    
    # Calculate score
    score = sum(1 for q, a in zip(questions, answers) if q['correct_answer'] == a)
    
    # Calculate time taken
    start_time = datetime.datetime.fromisoformat(current_test['start_time'])
    time_taken = (datetime.datetime.now() - start_time).seconds
    
    # Prepare results
    result = {
        'score': score,
        'total': len(questions),
        'percentage': (score / len(questions)) * 100,
        'time_taken': time_taken
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)