import httpx

async def generate_backstory_local(npc_data: dict) -> str:

    prompt = f"""
    Напиши краткую предысторию для персонажа RPG. Вот его данные:
    - Пол: {npc_data['gender']}
    - Имя: {npc_data['first_name']} {npc_data['last_name']}
    - Возраст: {npc_data['age']}
    - Профессия: {npc_data['occupation']}
    - Черты характера: {', '.join(npc_data['traits'])}
    
    Требования:
    - 2-3 предложения
    - Упоминай ключевые детали из данных выше
    - История обычного, не выдающегося человека
    """
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "mistral",
                    "prompt": prompt,
                    "stream": False, 
                    "options": {"temperature": 0.7}
                },
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()["response"]
        except Exception as e:
            print(f"Ошибка генерации: {e}")
            return "Не удалось создать предысторию."