# Bilingual Aptitude Test Platform

Live demo: [https://aptitude-test-9sgm.onrender.com](https://aptitude-test-9sgm.onrender.com)

A comprehensive aptitude testing platform supporting English and Czech languages. Built with Flask and modern web technologies.

## Features

- Three test sections: Verbal, Numerical, and Diagrammatic Analysis
- Bilingual support (English/Czech) with real-time language switching
- Timed test sections (5 minutes per section)
- Interactive matrix and pattern questions
- Immediate scoring and feedback
- Mobile-responsive design

## Technology Stack

- Backend: Flask (Python 3)
- Frontend: HTML, Tailwind CSS, JavaScript
- Deployment: Render

## Project Structure

```
aptitude-test/
├── app.py                 
├── questions/            
│   ├── verbal.py
│   ├── numerical.py
│   └── diagrammatic.py  
├── translations/        
│   ├── en.json
│   └── cs.json
├── templates/          
│   ├── base.html
│   ├── index.html
│   └── test.html
└── requirements.txt
```
