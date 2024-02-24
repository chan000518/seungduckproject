from config.settings import OPENAI_API_KEY
import openai

from datetime import date
# from apps.weather.models import Weather 

System_Role="""당신은 한국에서 유행하는 음식 위주로 친절하게 음식을 추천해 주고 그 간단하게 음식 설명과 추천 이유를 설명해줍니다
                 3개의 음식을 추천하고 먼저 음식이름들을 ,로 구분하여 []안에 넣어 말해줍니다 """
    
# 인자 user --> user에 해당하는 
def food_by_gpt_api(user):
    weather = "맑음" # Weather.objects.get(user = user).status
    Prompt =f"저는 한국에 살고 오늘은 {date.today()}이고, 오늘의 날씨는 {weather}입니다. 오늘 음식 메뉴를 추천해주세요"
    openai.api_key = OPENAI_API_KEY

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": System_Role},
        {"role": "user", "content": Prompt},
        ],
        max_tokens = 50,
        temperature = 0.5
    )   
    return response.choices[0].message.content

def food_names_from(text):
    start = text.find('[') + 1  
    end = text.find(']', start)  
    if start > 0 and end > start:
        food_names = text[start:end]
        return food_names
    else:
        return ""