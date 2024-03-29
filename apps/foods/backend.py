from config.settings import OPENAI_API_KEY
import openai

from datetime import date
# from apps.weather.models import Weather 

System_Role="""음식을 주어진 날짜와 날씨를 기반해 추천하고 간단한 음식 설명과 추천 이유를 설명
                 3개의 음식을 추천하고 먼저 음식이름들을 []안에 ,로 구분하여 말해 ex) [삼계탕,불고기,스파게티]"""
    
# 인자 user --> user에 해당하는 
def food_by_gpt_api(user):
    weather = "흐림" # Weather.objects.get(user = user).status
    Prompt =f"오늘은 {date.today()}이고, 오늘의 날씨는 {weather}입니다. 오늘 음식 메뉴를 추천해"
    openai.api_key = OPENAI_API_KEY
    print('???')
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role": "system", "content": System_Role},
            {"role": "user", "content": Prompt},
            ],
            max_tokens = 500,
            temperature = 0.9
        )   
        return response.choices[0].message.content
    except Exception:
        print('dk   ')
        return ''
    
def food_names_from(text):
    start = text.find('[') + 1  
    end = text.find(']', start)  
    if start > 0 and end > start:
        food_names = text[start:end]
        return food_names
    else:
        return ""