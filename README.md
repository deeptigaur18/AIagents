# AI Agent-Based Educational Content Generator

## Overview

This project implements a simple agent-based AI system that generates and evaluates educational content based on a given grade and topic. It consists of two main components: a Generator Agent and a Reviewer Agent, along with a basic user interface to demonstrate the workflow.

---

## Features

* Generates structured educational content including explanations and multiple-choice questions
* Evaluates generated content for clarity, correctness, and age appropriateness
* Supports a single-step refinement process if the content fails evaluation
* Provides an interactive user interface using Streamlit
* Maintains clear separation between logic (agents) and presentation (UI)

---

## System Architecture

User Input → Generator Agent → Reviewer Agent → (if fail) → Generator (Refined) → Output Display

---

## Project Structure

```
ai_agents_project/
│── app.py              # Streamlit UI
│── agents.py           # Generator and Reviewer logic
│── requirements.txt    # Dependencies
```

---

## Input Format

```json
{
  "grade": 4,
  "topic": "Types of angles"
}
```

---

## Output Format

### Generator Output

```json
{
  "explanation": "...",
  "mcqs": [
    {
      "question": "...",
      "options": ["A", "B", "C", "D"],
      "answer": "B"
    }
  ]
}
```

### Reviewer Output

```json
{
  "status": "pass",
  "feedback": []
}
```

---

## Refinement Logic

If the Reviewer Agent returns a "fail" status, the Generator Agent is executed again with feedback. Only one refinement attempt is allowed.

---

## Installation and Setup

1. Clone the repository

```
git clone <your-repo-link>
cd ai_agents_project
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the application

```
streamlit run app.py
```

---

## User Interface

The UI allows users to input a grade and topic, then displays:

* Generated content
* Reviewer feedback
* Refined output (if applicable)

---

## Evaluation Criteria

The Reviewer Agent evaluates content based on:

* Age appropriateness
* Conceptual correctness
* Clarity

---

## Technologies Used

* Python
* Streamlit

---

## Future Improvements

* Integration with language models for better content generation
* Enhanced evaluation using NLP techniques
* Additional customization such as difficulty levels and subjects
* Data persistence using a database

---

## Author

Deepti Gaur
---

## License

This project is created for assessment purposes.
