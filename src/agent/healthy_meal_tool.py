import random
from typing import Dict, List, Optional
from agno.tools import Toolkit
from agno.utils.log import logger


class HealthyMealTool(Toolkit):
    """
    Healthy meal suggestion tool that implements a simple workflow
    Steps: get_recipe() -> get_calorie_count() -> sum_nutrition()
    """

    def __init__(self):
        super().__init__(name="healthy_meal_tool")

        # Sample recipes database
        self.recipes = {
            "quinoa_power_bowl": {
                "name": "Quinoa Power Bowl",
                "ingredients": ["quinoa", "chickpeas", "spinach"],
                "instructions": "Cook quinoa, add roasted chickpeas and fresh spinach. Dress with lemon vinaigrette."
            },
            "salmon_avocado_salad": {
                "name": "Salmon Avocado Salad",
                "ingredients": ["salmon", "avocado", "mixed_greens"],
                "instructions": "Grill salmon, slice avocado, toss with mixed greens and olive oil dressing."
            },
            "chicken_veggie_wrap": {
                "name": "Chicken Veggie Wrap",
                "ingredients": ["chicken_breast", "bell_peppers", "whole_wheat_tortilla"],
                "instructions": "Grill chicken, sauté peppers, wrap in whole wheat tortilla with hummus."
            }
        }

        # Calorie database (per 100g)
        self.calorie_data = {
            "quinoa": 120,
            "chickpeas": 164,
            "spinach": 23,
            "salmon": 208,
            "avocado": 160,
            "mixed_greens": 15,
            "chicken_breast": 165,
            "bell_peppers": 31,
            "whole_wheat_tortilla": 245
        }

    def suggest_healthy_meal(self, dietary_preferences: Optional[str] = None) -> str:
        """
        Main workflow function that orchestrates the meal suggestion process
        Implements the workflow: get_recipe() -> get_calorie_count() -> sum_nutrition()

        Args:
            dietary_preferences: Optional dietary preferences (vegetarian, high-protein, etc.)

        Returns:
            Complete meal recommendation with nutritional information
        """
        try:
            logger.info("Starting healthy meal suggestion workflow")

            # Step 1: Get recipe
            recipe = self._get_recipe(dietary_preferences)
            if not recipe:
                return "Unable to find a suitable recipe. Please try again."

            # Step 2: Get calorie count for each ingredient (parallel processing simulation)
            calorie_counts = self._get_calorie_count(recipe["ingredients"])

            # Step 3: Sum nutrition
            nutrition_summary = self._sum_nutrition(calorie_counts)

            # Format the complete recommendation
            recommendation = self._format_meal_recommendation(recipe, nutrition_summary)

            logger.info("Healthy meal suggestion workflow completed successfully")
            return recommendation

        except Exception as e:
            logger.error(f"Error in healthy meal suggestion workflow: {e}")
            return "Unable to generate meal suggestion. Please try again later."

    def _get_recipe(self, dietary_preferences: Optional[str] = None) -> Dict:
        """Step 1: Get a recipe based on preferences"""
        logger.info("Getting recipe based on dietary preferences")

        # Simple filtering based on preferences
        available_recipes = list(self.recipes.values())

        if dietary_preferences:
            if "vegetarian" in dietary_preferences.lower():
                # Filter out recipes with meat
                available_recipes = [r for r in available_recipes
                                     if not any(meat in r["ingredients"]
                                                for meat in ["salmon", "chicken_breast"])]
            elif "high-protein" in dietary_preferences.lower():
                # Prefer recipes with protein sources
                protein_recipes = [r for r in available_recipes
                                   if any(protein in r["ingredients"]
                                          for protein in ["salmon", "chicken_breast", "chickpeas"])]
                if protein_recipes:
                    available_recipes = protein_recipes

        if not available_recipes:
            return None

        # Return a random recipe from filtered options
        return random.choice(available_recipes)

    def _get_calorie_count(self, ingredients: List[str]) -> Dict[str, int]:
        """Step 2: Get calorie count for each ingredient (simulates parallel processing)"""
        logger.info(f"Getting calorie counts for ingredients: {ingredients}")

        calorie_counts = {}
        for ingredient in ingredients:
            if ingredient in self.calorie_data:
                # Simulate standard serving size (100g)
                calorie_counts[ingredient] = self.calorie_data[ingredient]
            else:
                # Default calorie count for unknown ingredients
                calorie_counts[ingredient] = 50
                logger.warning(f"Unknown ingredient {ingredient}, using default calories")

        return calorie_counts

    def _sum_nutrition(self, calorie_counts: Dict[str, int]) -> Dict:
        """Step 3: Aggregate nutritional data"""
        logger.info("Summing nutritional information")

        total_calories = sum(calorie_counts.values())

        # Simple nutrition estimation based on ingredients
        estimated_protein = total_calories * 0.2  # 20% of calories from protein
        estimated_carbs = total_calories * 0.5  # 50% of calories from carbs
        estimated_fat = total_calories * 0.3  # 30% of calories from fat

        return {
            "total_calories": total_calories,
            "protein_g": round(estimated_protein / 4, 1),  # 4 calories per gram
            "carbs_g": round(estimated_carbs / 4, 1),
            "fat_g": round(estimated_fat / 9, 1),  # 9 calories per gram
            "ingredient_breakdown": calorie_counts
        }

    def _format_meal_recommendation(self, recipe: Dict, nutrition: Dict) -> str:
        """Format the complete meal recommendation"""
        recommendation = f"🍽️ HEALTHY MEAL RECOMMENDATION\n"
        recommendation += "=" * 50 + "\n\n"

        recommendation += f"📋 **{recipe['name']}**\n\n"

        recommendation += "🥗 **Ingredients:**\n"
        for ingredient in recipe['ingredients']:
            calories = nutrition['ingredient_breakdown'].get(ingredient, 0)
            recommendation += f"  • {ingredient.replace('_', ' ').title()} ({calories} cal)\n"

        recommendation += f"\n👨‍🍳 **Instructions:**\n{recipe['instructions']}\n\n"

        recommendation += "📊 **Nutritional Information:**\n"
        recommendation += f"  • Total Calories: {nutrition['total_calories']} cal\n"
        recommendation += f"  • Protein: {nutrition['protein_g']}g\n"
        recommendation += f"  • Carbohydrates: {nutrition['carbs_g']}g\n"
        recommendation += f"  • Fat: {nutrition['fat_g']}g\n\n"

        recommendation += "💡 **Note:** This meal is designed to support your fitness goals "
        recommendation += "while considering your ACL recovery needs.\n"

        return recommendation


# Healthy Meal Tool
# meal_tool = HealthyMealTool()
# meal_suggestion = meal_tool.suggest_healthy_meal(dietary_preferences="high-protein")
# print("MEAL SUGGESTION:")
# print(meal_suggestion)