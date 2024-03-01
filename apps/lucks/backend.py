from config.settings import OPENAI_API_KEY
import openai

from datetime import date
# from apps.weather.models import Weather 

System_Role="""넌 사주팔자 운세를 보는 사람이야 내 생일과 이름, 오늘 날짜를 기반으로 오늘의 운세를 봐줘
    먼저 오늘의 운세를 한단어로 표현해줘 ex) [만전지책] 그 다음 설명을 해줘"""
    
# 인자 user --> user에 해당하는 
def luck_by_gpt_api(user):
    
    weather = "맑음" # Weather.objects.get(user = user).status
    
    Prompt =f"오늘은 {date.today()}, 날씨는 {weather} 태어난 날은 {user.birth} 이름은 {user.name}. 오늘 운세를 알려줘"
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
        return ''
    
def luck_names_from(text):
    start = text.find('[') + 1  
    end = text.find(']', start)  
    if start > 0 and end > start:
        luck_names = text[start:end]
        return luck_names
    else:
        return ""