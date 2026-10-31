from fastapi import APIRouter
from schemas.practice_schemas import Message, MessageOut

router = APIRouter(prefix='/practice', tags=['practice creating route'])


messages = []

@router.get('')
async def get_messages() -> MessageOut:
    return { 'data': messages }


@router.post('/create')
async def create_message(message: Message) -> MessageOut:
    messages.append(message)
    return { 'data': messages }


    

