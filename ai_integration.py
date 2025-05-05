import openai
async def generate_backstory(npc_data):
    from openai import OpenAI
    client = OpenAI()

    prompt = f"""
    Создай подробную предысторию для RPG-персонажа. Вот его характеристики:
    - Полное имя: {npc_data['first_name']} {npc_data['last_name']}
    - Возраст: {npc_data['age']} лет
    - Семейное положение: {npc_data['marital_status']}
    - Профессия: {npc_data['occupation']}
    - Черты характера: {', '.join(npc_data['traits'])}
    - Внешность: {npc_data.get('appearance', 'не указана')}
    
    Предыстория должна быть:
    - На 2-3 абзаца
    - Учитывать все указанные характеристики
    - Содержать уникальные детали
    - Быть в стиле фэнтези (или другого вашего сеттинга)
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты опытный рассказчик, создающий живые истории для RPG-персонажей"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,  
            max_tokens=500    
        )
        
        
        backstory = response.choices[0].message.content.strip()
        return backstory if backstory else "Не удалось сгенерировать предысторию"
        
    except Exception as e:
        print(f"Ошибка при генерации предыстории: {e}")
        return "Произошла ошибка при создании предыстории персонажа"