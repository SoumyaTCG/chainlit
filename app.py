import chainlit as cl

@cl.on_message
async def main(user_message:cl.Message):

    response=ask_bot(user_message.content,instruction)
    
    # Send a response back to the user
    await cl.Message(
        content=f"Received: {response}",
    ).send()

