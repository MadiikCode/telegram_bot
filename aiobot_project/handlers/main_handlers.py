from aiogram import Router, types
from aiogram.filters import Command
from aiobot_project.config import OPENROUTER_API_KEY
from aiobot_project.keyboards.menu import main_menu
import aiohttp
import asyncio

router = Router()

@router.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(
        "Привет! Я бот с ИИ через OpenRouter.\nНапиши вопрос, и я постараюсь ответить 🧠",
        reply_markup=main_menu
    )

@router.message()
async def message_handler(message: types.Message):
    text = message.text.strip()

    # Если пользователь написал "Отправь фото" — отправляем картинку
    if text.lower() == "отправь фото":
        await message.answer_photo(
            photo="https://placekitten.com/500/500",
            caption="Вот котик 🐱"
        )
        return

    await message.answer("🤖 Думаю над ответом...")

    max_retries = 3
    for attempt in range(max_retries):
        try:
            async with aiohttp.ClientSession() as session:
                headers = {
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                    "Content-Type": "application/json"
                }
                data = {
                    "model": "baidu/ernie-4.5-300b-a47b",
                    "messages": [
                        {"role": "system", "content": "Ты полезный помощник."},
                        {"role": "user", "content": text}
                    ]
                }
                async with session.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data) as resp:
                    result = await resp.json()

                    if "error" in result:
                        error_msg = result['error'].get('message', 'Неизвестная ошибка API')
                        if attempt == max_retries - 1:
                            await message.answer(f"Ошибка API: {error_msg}")
                        else:
                            await asyncio.sleep(2)  # подождать перед повтором
                        continue

                    answer = result["choices"][0]["message"]["content"]
                    await message.answer(answer)
                    break  # успешный ответ — выход из цикла

        except Exception as e:
            if attempt == max_retries - 1:
                await message.answer(f"Ошибка при генерации ответа: {e}")
            else:
                await asyncio.sleep(2)
