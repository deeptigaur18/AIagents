import json

class GeneratorAgent:
    def generate(self, grade, topic, feedback=None):
        # Basic content generation (can be improved with LLM later)

        explanation = f"{topic} are important in mathematics. " \
                      f"For Grade {grade}, angles can be understood as the space between two lines."

        if feedback:
            explanation += " This explanation has been simplified based on feedback."

        mcqs = [
            {
                "question": f"What is an acute angle?",
                "options": ["Less than 90°", "Equal to 90°", "More than 90°", "360°"],
                "answer": "Less than 90°"
            },
            {
                "question": f"What is a right angle?",
                "options": ["45°", "60°", "90°", "120°"],
                "answer": "90°"
            }
        ]

        return {
            "explanation": explanation,
            "mcqs": mcqs
        }


class ReviewerAgent:
    def review(self, content):
        feedback = []
        explanation = content.get("explanation", "")

        # Simple checks
        if len(explanation.split()) > 25:
            feedback.append("Explanation is too long for the grade level")

        for i, mcq in enumerate(content.get("mcqs", [])):
            if "?" not in mcq["question"]:
                feedback.append(f"Question {i+1} is not clear")

        status = "pass" if len(feedback) == 0 else "fail"

        return {
            "status": status,
            "feedback": feedback
        }


def run_pipeline(grade, topic):
    generator = GeneratorAgent()
    reviewer = ReviewerAgent()

    # Step 1: Generate
    output = generator.generate(grade, topic)

    # Step 2: Review
    review = reviewer.review(output)

    refined_output = None

    # Step 3: Refinement (only once)
    if review["status"] == "fail":
        refined_output = generator.generate(grade, topic, feedback=review["feedback"])
        review = reviewer.review(refined_output)

    return output, review, refined_output