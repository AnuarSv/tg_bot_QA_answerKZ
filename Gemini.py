import google.generativeai as genai
from config import GEMINI_API
from texts import bot_purpose

async def gpt(promt: str, history: str, context: str) -> str:
    try:
        genai.configure(api_key=GEMINI_API)

        # Set up the model
        generation_config = {
            "temperature": 0.1,
            "top_p": 0.95,
            "top_k": 64,
        }

        model = genai.GenerativeModel(model_name="gemini-1.5-flash",
                                      generation_config=generation_config,
                                      system_instruction=bot_purpose,)

        response = await model.generate_content_async([f'GIVE ONLY CORRECT CLEAR ANSWER: Choose correct clear answer from dataset: {context}, History: {history}\n User Question: {promt}'])
        return response.text

    except Exception as e:
        return 'ERROR' + '\n' + str(e)
