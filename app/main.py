import requests
from fastapi import FastAPI, Depends
from sqlalchemy import insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import questions
from app.utilits import get_obj_datetime
from database import get_async_session

app = FastAPI(
    title='Quize'
)


@app.get('/questions')
def get_questions(count: int):
    url = "https://jservice.io/api/random"
    params = {
        "count": count,
    }
    response = requests.get(url, params=params)
    data = []
    for question in response.json():
        current_dict = {
            "id": question.get('id'),
            "question": question.get('question'),
            "answer": question.get('answer'),
            "created_at": question.get('created_at'),
        }
        data.append(current_dict)
    return data


@app.post('/questions')
async def add_questions(count: int, session: AsyncSession = Depends(get_async_session)):
    url = "https://jservice.io/api/random"
    params = {
        "count": count,
    }
    response = requests.get(url, params=params)

    for question in response.json():
        current_dict = {
            "id": question.get('id'),
            "question": question.get('question'),
            "answer": question.get('answer'),
            "created_at": get_obj_datetime(question.get('created_at')),
        }
        count_questions = 0
        try:
            add_new_question = insert(questions).values(**current_dict)
            await session.execute(add_new_question)
            await session.commit()
            count_questions += 1
        except IntegrityError:
            continue

        return current_dict if count_questions != 0 else {}

