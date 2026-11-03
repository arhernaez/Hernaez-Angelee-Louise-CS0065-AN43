# PART 1: KNOWLEDGE REPRESENTATION (KR)

facts = {
    # Category 1: Temperature
    "temperature": 35,
    "feels_like": 38,

    # Category 2: Weather Conditions
    "is_raining": False,
    "humidity": 85,

    # Category 3: Weather Status
    "is_cloudy": True,
    "is_windy": False
}

print("Knowledge Base:")
for key, value in facts.items():
    print(key, ":", value)

# PART 2: RULE-BASED REASONING (RBR)

# Rule 1: Check temperature
def rule_hot(facts):
    if facts["temperature"] > 30:
        return "Turn on the aircon"

# Rule 2: Check rain
def rule_rain(facts):
    if facts["is_raining"]:
        return "Bring an umbrella"

# Rule 3: Check humidity
def rule_humidity(facts):
    if facts["humidity"] > 80:
        return "Stay hydrated"

# Rule 4: Check cloudy weather
def rule_cloudy(facts):
    if facts["is_cloudy"]:
        return "Expect possible rain"

def inference_engine(facts):
    rules = [
        rule_hot,
        rule_rain,
        rule_humidity,
        rule_cloudy
    ]

    actions = []

    for rule in rules:
        result = rule(facts)

        if result:
            actions.append(result)

    return actions

print("\nRule-Based Reasoning Actions:")

actions = inference_engine(facts)

for action in actions:
    print("-", action)

# PART 3: CASE-BASED REASONING (CBR)

case_base = [
    {
        "problem": {
            "temperature": 35,
            "is_raining": False,
            "humidity": 85
        },
        "solution": "Stay indoors and turn on the aircon."
    },

    {
        "problem": {
            "temperature": 25,
            "is_raining": True,
            "humidity": 70
        },
        "solution": "Bring an umbrella and wear a raincoat."
    },

    {
        "problem": {
            "temperature": 30,
            "is_raining": False,
            "humidity": 60
        },
        "solution": "Enjoy outdoor activities."
    }
]

def retrieve_case(new_problem, case_base):

    best_case = None
    highest_similarity = -1

    print("\nCBR Similarity Results:")

    for i, case in enumerate(case_base):

        similarity = 0

        for feature in new_problem:
            if new_problem[feature] == case["problem"][feature]:
                similarity += 1

        # Calculate similarity percentage
        percentage = (similarity / len(new_problem)) * 100

        print(f"Case {i + 1}: {percentage:.2f}% similarity")

        if percentage > highest_similarity:
            highest_similarity = percentage
            best_case = case

    print(f"\nHighest Similarity: {highest_similarity:.2f}%")

    return best_case

def reuse_solution(best_case):

    if best_case:
        return best_case["solution"]

    return "No similar case found."

def revise_solution(solution):

    print("\nCBR Suggested Solution:")
    print(solution)

    choice = input("\nDo you want to revise the solution? (yes/no): ")

    if choice.lower() == "yes":
        new_solution = input("Enter your revised solution: ")
        return new_solution

    return solution

def retain_case(new_problem, final_solution, case_base):

    new_case = {
        "problem": new_problem,
        "solution": final_solution
    }

    case_base.append(new_case)

    print("\nNew case successfully added to the case base!")

# New weather problem
new_problem = {
    "temperature": 34,
    "is_raining": False,
    "humidity": 85
}

# RETRIEVE
best_case = retrieve_case(new_problem, case_base)

# REUSE
if best_case:
    suggested_solution = reuse_solution(best_case)
else:
    suggested_solution = "No similar case found."

# REVISE
final_solution = revise_solution(suggested_solution)

# RETAIN
retain_case(new_problem, final_solution, case_base)

# Display final result
print("\nFinal CBR Solution:")
print(final_solution)

print("\nTotal Cases in Case Base:", len(case_base))