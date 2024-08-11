from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from config import client


router = Router()


@router.message(Command('add_file'))
async def add_file(message: Message,  state: FSMContext) -> None:
    vector_store = await client.beta.vector_stores.create(name="Anxiety")

    file_paths = ["openai_tool/files/anxiety.docx", ]
    file_streams = [open(path, "rb") for path in file_paths]

    file_batch = await client.beta.vector_stores.file_batches.upload_and_poll(
        vector_store_id=vector_store.id, files=file_streams
    )

    assistant_id = (await state.get_data())['assistant_id']

    await client.beta.assistants.update(
        assistant_id=assistant_id,
        tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
    )

