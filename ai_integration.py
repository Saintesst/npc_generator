import openai
import asyncio
from config import Config

async def generate_backstory(npc_data: dict) -> str:
    prompt = f"""
    Создай подробную предысторию для персонажа:
    Имя: {npc_data['first_name']} {npc_data['last_name']}
    Возраст: {npc_data['age']}
    Статус: {npc_data['marital_status']}
    Профессия: {npc_data['occupation']}
    Черты: {', '.join(npc_data['traits'])}
    Внешность: {npc_data['appearance']}
    
    Предыстория должна быть реалистичной и детализированной.
    """
    
    try:
        response = await asyncio.to_thread(
            openai.ChatCompletion.create,
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            api_key=Config.OPENAI_KEY
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Не удалось сгенерировать предысторию: {str(e)}"