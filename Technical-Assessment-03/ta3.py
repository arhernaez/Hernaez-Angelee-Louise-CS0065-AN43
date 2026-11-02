
# ==========================================
# CASE-BASED REASONING (CBR) INTELLIGENT TUTORING SYSTEM (ITS)
# ==========================================

# 1. CASE BASE: Five Previous Student Cases
case_base = [
    {
        "problem": {
            "student": "Student A",
            "topic": "Algebra",
            "grade_level": "8",
            "error_type": "Incorrect formula",
            "difficulty": "High"
        },
        "solution": {
            "feedback": "Review the correct algebraic formula.",
            "lesson": "Practice solving basic algebraic equations.",
            "intervention": "Provide step-by-step examples."
        }
    },
    {
        "problem": {
            "student": "Student B",
            "topic": "Algebra",
            "grade_level": "8",
            "error_type": "Sign error",
            "difficulty": "Medium"
        },
        "solution": {
            "feedback": "Pay attention to positive and negative signs.",
            "lesson": "Practice integer operations.",
            "intervention": "Give exercises involving negative numbers."
        }
    },
    {
        "problem": {
            "student": "Student C",
            "topic": "Geometry",
            "grade_level": "9",
            "error_type": "Incorrect formula",
            "difficulty": "High"
        },
        "solution": {
            "feedback": "Review the formulas used in geometry.",
            "lesson": "Study area and perimeter formulas.",
            "intervention": "Provide visual diagrams and examples."
        }
    },
    {
        "problem": {
            "student": "Student D",
            "topic": "Fractions",
            "grade_level": "7",
            "error_type": "Calculation error",
            "difficulty": "Medium"
        },
        "solution": {
            "feedback": "Check each calculation carefully.",
            "lesson": "Practice addition and subtraction of fractions.",
            "intervention": "Provide guided calculation exercises."
        }
    },
    {
        "problem": {
            "student": "Student E",
            "topic": "Algebra",
            "grade_level": "8",
            "error_type": "Incorrect formula",
            "difficulty": "Medium"
        },
        "solution": {
            "feedback": "Identify the correct formula before solving.",
            "lesson": "Practice substituting values into equations.",
            "intervention": "Provide guided algebra exercises."
        }
    }
]


# 2. SIMILARITY ASSESSMENT
# Each attribute has different importance
weights = {
    "topic": 0.30,
    "grade_level": 0.20,
    "error_type": 0.35,
    "difficulty": 0.15
}


def calculate_similarity(new_problem, old_problem):
    score = 0

    for attribute, weight in weights.items():
        if new_problem[attribute].lower() == old_problem[attribute].lower():
            score += weight

    return score * 100


# 3. RETRIEVE THE MOST SIMILAR CASE
def retrieve_case(new_problem):
    results = []

    for case in case_base:
        old_problem = case["problem"]

        similarity = calculate_similarity(
            new_problem, old_problem
        )

        results.append({
            "case": case,
            "similarity": similarity
        })

    results.sort(
        key=lambda item: item["similarity"],
        reverse=True
    )

    return results


# 4. ADAPT THE RETRIEVED SOLUTION
def adapt_solution(new_problem, retrieved_case):

    old_solution = retrieved_case["solution"]

    adapted = old_solution.copy()

    if new_problem["error_type"] == "Incorrect formula":
        adapted["feedback"] = (
            "Review the correct formula for "
            + new_problem["topic"]
            + ". Identify the formula before solving."
        )

        adapted["lesson"] = (
            "Study the important formulas in "
            + new_problem["topic"]
            + " and practice applying them."
        )

    elif new_problem["error_type"] == "Sign error":
        adapted["feedback"] = (
            "Pay close attention to positive and negative signs."
        )

        adapted["lesson"] = (
            "Practice exercises involving positive and negative numbers."
        )

    elif new_problem["error_type"] == "Calculation error":
        adapted["feedback"] = (
            "Review your calculations and solve each step carefully."
        )

        adapted["lesson"] = (
            "Practice step-by-step calculations in "
            + new_problem["topic"] + "."
        )

    if new_problem["difficulty"] == "High":
        adapted["intervention"] = (
            "Provide detailed explanations, guided examples, "
            "and additional practice exercises."
        )

    elif new_problem["difficulty"] == "Medium":
        adapted["intervention"] = (
            "Provide guided exercises followed by independent practice."
        )

    else:
        adapted["intervention"] = (
            "Provide short review exercises and independent practice."
        )

    return adapted


# 5. RETAIN: SAVE THE NEW CASE
def retain_case(new_problem, final_solution):

    new_case = {
        "problem": new_problem.copy(),
        "solution": final_solution.copy()
    }

    case_base.append(new_case)

    print("\nNEW CASE SAVED SUCCESSFULLY!")


# 6. DISPLAY THE UPDATED CASE BASE
def display_case_base():

    print("\n========== UPDATED CASE BASE ==========")

    for index, case in enumerate(case_base, start=1):

        problem = case["problem"]

        print(f"\nCase {index}")
        print("Student:", problem["student"])
        print("Topic:", problem["topic"])
        print("Grade Level:", problem["grade_level"])
        print("Error Type:", problem["error_type"])
        print("Difficulty:", problem["difficulty"])


# 7. MAIN PROGRAM
def main():

    print("======================================")
    print(" INTELLIGENT TUTORING SYSTEM (ITS)")
    print(" CASE-BASED REASONING PROGRAM")
    print("======================================")

    # Get new student information
    print("\nENTER NEW STUDENT INFORMATION")

    new_problem = {
        "student": input("Student Name: "),
        "topic": input("Learning Topic: "),
        "grade_level": input("Grade Level: "),
        "error_type": input(
            "Error Type (Incorrect formula / Sign error / Calculation error): "
        ),
        "difficulty": input(
            "Difficulty (Low / Medium / High): "
        )
    }

    # Display new problem
    print("\n========== NEW PROBLEM ==========")

    for key, value in new_problem.items():
        print(key.replace("_", " ").title() + ":", value)

    # Retrieve similar cases
    results = retrieve_case(new_problem)

    print("\n========== SIMILARITY RESULTS ==========")

    for index, result in enumerate(results, start=1):

        print(
            f"Rank {index}: "
            f"{result['case']['problem']['student']} - "
            f"{result['similarity']:.2f}% similarity"
        )

    # Select the most relevant case
    best_match = results[0]["case"]

    print("\n========== RETRIEVED CASE ==========")

    print("Student:", best_match["problem"]["student"])
    print("Topic:", best_match["problem"]["topic"])
    print("Error:", best_match["problem"]["error_type"])

    # Adapt the retrieved solution
    final_solution = adapt_solution(
        new_problem,
        best_match
    )

    print("\n========== ADAPTED FINAL SOLUTION ==========")

    print("Personalized Feedback:",
          final_solution["feedback"])

    print("Recommended Lesson:",
          final_solution["lesson"])

    print("Teaching Intervention:",
          final_solution["intervention"])

    # Retain the new case
    retain_case(new_problem, final_solution)

    # Display updated case base
    display_case_base()

    print("\n======================================")
    print(" CBR PROCESS COMPLETED SUCCESSFULLY")
    print("======================================")


if __name__ == "__main__":
    main()
