from requests import get, post
from functions import wp_list, openai_ans, media_from_url, heading2, dict_list, wp_headers
from pprint import pprint
import os
api_url = 'https://www.themealdb.com/api/json/v1/1/search.php?f=a'
res = get(api_url)
data = res.json()
meals = data.get('meals')
for meal in meals:
    meal_name = meal.get('strMeal')
    meal_area = meal.get('strArea')
    meal_instruction = meal.get('strInstructions')
    instruction_list = meal_instruction.split('\r\n')
    meal_category = meal.get('strCategory')
    thumbnail = meal.get('strMealThumb')
    youtube_links = meal.get('strYoutube')
    ingredients = {}
    i = 1
    while i < 20:
        key_ingredient = f'strIngredient{i}'
        key_measure = f'strMeasure{i}'
        if (meal.get(key_ingredient) != None) and (meal.get(key_measure) != ''):
            ingredients[meal.get(key_ingredient)] = meal.get(key_measure)
        i += 1


    title = f'Best {meal_name} Recipe for Newyear'
    image = media_from_url(thumbnail, meal_name)
    intro_text = f'Write short intro about {meal_name} recipe'
    intro = openai_ans(intro_text)
    instruction = heading2('Instruction for the recipe')
    description = wp_list(instruction_list)
    used_ingredient = heading2('Used ingredients are here : ')
    list_of_ingredients = dict_list(ingredients)
    full_content = f'{image} {intro} {instruction} {description} {used_ingredient} {list_of_ingredients}'

    data = {
        'title': title,
        'content': full_content,
        'slug': title.lower().strip().replace(' ', '-'),
        'status': 'publish'
    }
    posts_url = 'https://pentagrowthdigital.com/practice/wp-json/wp/v2/posts'
    from dotenv import load_dotenv
    load_dotenv()
    web_pass = os.getenv('WEBSITE_PASS')
    headers = wp_headers('admin', web_pass)
    res = post(posts_url, data=data, headers=headers)



