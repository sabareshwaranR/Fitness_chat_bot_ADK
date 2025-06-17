import datetime
from google.adk.agents import Agent

def calculate_bmi(weight: float, height: float) -> dict:
    """Calculates BMI from weight (kg) and height (cm).

    Args:
        weight (float): Weight in kilograms.
        height (float): Height in centimeters.

    Returns:
        dict: status and BMI result or error msg.
    """
    try:
        height_m = height / 100  # Convert cm to meters
        bmi = weight / (height_m ** 2)
        category = (
            "Underweight" if bmi < 18.5 else
            "Normal weight" if bmi < 24.9 else
            "Overweight" if bmi < 29.9 else
            "Obese"
        )
        return {
            "status": "success",
            "bmi": round(bmi, 2),
            "category": category,
            "message": f"Your BMI is {round(bmi, 2)} ({category})."
        }
    except Exception as e:
        return {"status": "error", "error_message": str(e)}


def fitness_tips(goal: str) -> dict:
    """Provides fitness tips based on the user's goal.

    Args:
        goal (str): User's goal, e.g., 'loss' or 'gain'.

    Returns:
        dict: status and fitness tips or error msg.
    """
    goal = goal.lower()
    if goal == "loss":
        tips = [
            "Incorporate cardio workouts like running or cycling.",
            "Maintain a calorie deficit.",
            "Eat more protein and fiber.",
            "Avoid sugary drinks."
        ]
    elif goal == "gain":
        tips = [
            "Include strength training in your routine.",
            "Increase your caloric intake with healthy foods.",
            "Consume more protein and carbs.",
            "Ensure adequate rest for muscle recovery."
        ]
    else:
        return {
            "status": "error",
            "error_message": f"Goal '{goal}' is not recognized. Use 'loss' or 'gain'."
        }

    return {
        "status": "success",
        "goal": goal,
        "tips": tips
    }

def calculate_maintenance_calories(weight: float) -> dict:
    """Estimates maintenance calories using simplified formula.

    Args:
        weight (float): Weight in kilograms.

    Returns:
        dict: Maintenance calories.
    """
    try:
        weight_lbs = weight * 2.2
        maintenance_calories = weight_lbs * 14
        return {
            "status": "success",
            "weight_kg": weight,
            "weight_lbs": round(weight_lbs, 2),
            "maintenance_calories": round(maintenance_calories, 2),
            "message": f"Estimated maintenance calories: {round(maintenance_calories, 2)} kcal/day."
        }
    except Exception as e:
        return {"status": "error", "error_message": str(e)}

def calculate_macronutrients(calories: float, goal: str = "loss") -> dict:
    """Calculates recommended macronutrient split for a given calorie goal.

    Args:
        calories (float): Total daily calorie intake.
        goal (str): 'loss', 'gain', or 'maintain'.

    Returns:
        dict: Macronutrient breakdown.
    """
    try:
        goal = goal.lower()
        if goal not in ["loss", "gain", "maintain"]:
            return {
                "status": "error",
                "error_message": f"Goal '{goal}' is invalid. Use 'loss', 'gain', or 'maintain'."
            }

        # Macronutrient ratios
        protein_ratio = 0.35
        fat_ratio = 0.25
        carbs_ratio = 0.40

        protein_cals = calories * protein_ratio
        fat_cals = calories * fat_ratio
        carbs_cals = calories * carbs_ratio

        protein_grams = protein_cals / 4
        fat_grams = fat_cals / 9
        carbs_grams = carbs_cals / 4

        return {
            "status": "success",
            "goal": goal,
            "calories": round(calories),
            "macronutrients": {
                "protein_grams": round(protein_grams, 2),
                "fat_grams": round(fat_grams, 2),
                "carbs_grams": round(carbs_grams, 2),
            },
            "message": (
                f"For a {goal} goal and {round(calories)} kcal/day:\n"
                f"- Protein: {round(protein_grams, 2)}g\n"
                f"- Fat: {round(fat_grams, 2)}g\n"
                f"- Carbs: {round(carbs_grams, 2)}g"
            )
        }
    except Exception as e:
        return {"status": "error", "error_message": str(e)}
def calculate_weight_loss_plan(target_weight_loss: float) -> dict:
    """
    Calculates the daily calorie deficit needed to achieve a weekly weight loss goal (0.5kg to 1kg per week only).

    Args:
        target_weight_loss (float): Target weight loss in kg (only 0.5 to 1 allowed).

    Returns:
        dict: Daily calorie deficit and recommendations.
    """
    try:
        CALORIES_PER_KG = 7700  # 1 kg fat ≈ 7700 kcal
        days = 7  # per week

        # Validate weight loss range
        if target_weight_loss < 0.5 or target_weight_loss > 1:
            return {
                "status": "error",
                "error_message": "Only 0.5 kg to 1 kg per week is recommended for healthy weight loss."
            }

        total_deficit = target_weight_loss * CALORIES_PER_KG
        daily_deficit = total_deficit / days

        return {
            "status": "success",
            "target_weight_loss_kg": target_weight_loss,
            "daily_calorie_deficit": round(daily_deficit, 2),
            "message": (
                f"To lose {target_weight_loss} kg per week, aim for a daily calorie deficit of "
                f"{round(daily_deficit)} kcal. This can be achieved through a combination of diet "
                f"(eating fewer calories) and exercise (e.g., 30–60 minutes of cardio)."
            ),
            "recommendations": [
                "Track your food intake and stay in a calorie deficit.",
                "Do cardio exercises like brisk walking, running, or cycling daily.",
                "Stay hydrated and get enough sleep.",
                "Avoid sugary drinks and processed snacks."
            ]
        }
    except Exception as e:
        return {"status": "error", "error_message": str(e)}
def calculate_weight_gain_plan(target_weight_gain: float) -> dict:
    """
    Calculates the daily calorie surplus needed to achieve a weekly weight gain goal (0.25kg to 0.5kg per week only).

    Args:
        target_weight_gain (float): Target weight gain in kg.

    Returns:
        dict: Daily calorie surplus and muscle-building advice.
    """
    try:
        CALORIES_PER_KG = 7700
        days = 7

        # Validate range
        if target_weight_gain < 0.25 or target_weight_gain > 0.5:
            return {
                "status": "error",
                "error_message": "Only 0.25 kg to 0.5 kg per week is recommended for healthy weight gain."
            }

        total_surplus = target_weight_gain * CALORIES_PER_KG
        daily_surplus = total_surplus / days

        return {
            "status": "success",
            "target_weight_gain_kg": target_weight_gain,
            "daily_calorie_surplus": round(daily_surplus, 2),
            "message": (
                f"To gain {target_weight_gain} kg per week, aim for a daily calorie surplus of "
                f"{round(daily_surplus)} kcal. Focus on strength training and consuming calorie-dense, nutritious foods."
            ),
            "recommendations": [
                "Eat 3 large meals and 2–3 snacks each day.",
                "Include protein-rich foods: eggs, meat, legumes, dairy.",
                "Strength train 3–5 times a week (compound lifts are best).",
                "Add healthy fats (nuts, seeds, olive oil) to meals.",
                "Track progress weekly to adjust intake."
            ]
        }

    except Exception as e:
        return {"status": "error", "error_message": str(e)}

root_agent = Agent(
    name="fitness_agent",
    model="gemini-2.0-flash",
    description="Agent to provide fitness-related guidance.",
    instruction="You can calculate BMI, maintenance calories, macronutrient breakdown, and offer tips based on fitness goals.",
    tools=[calculate_bmi, fitness_tips, calculate_maintenance_calories, calculate_macronutrients,calculate_weight_loss_plan, calculate_weight_gain_plan, ],
)

