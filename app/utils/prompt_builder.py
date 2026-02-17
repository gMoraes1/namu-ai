from app.models.user import User

def build_prompt(user: User, context: str | None) -> str:
    system_message = """
Você é um especialista em saúde e bem-estar.
Responda exclusivamente em JSON válido.
Não inclua texto fora do JSON.
"""

    user_context =  f"""
Perfil do usuário:
Nome: {user.name}
Idade: {user.age}
Objetivos: {", ".join(user.goals)}
Restrições: {user.restrictions}
Nível de experiência: {user.experience_level}
"""
    
    additional_context = f" Contexto adicional: {context}" if context else ""

    output_format = """
Formato obrigatório da resposta:

{
  "activities": [
    {
      "name": "",
      "description": "",
      "duration": "",
      "category": ""
    }
  ],
  "reasoning": "",
  "precautions": ""
}
"""
    
    return f"{system_message}\n{user_context}\n{additional_context}\n{output_format}"       