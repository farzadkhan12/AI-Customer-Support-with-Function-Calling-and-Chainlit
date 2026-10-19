import chainlit as cl
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,ToolMessage,HumanMessage
from langchain_openrouter import ChatOpenRouter

from main import tools, execute_tool_call

load_dotenv()

@cl.on_chat_start
async def on_chat_start():
    llm = ChatOpenRouter(
        model="dots-studio/dots-3-note-preview:free", 
        temperature=0.1
    )
    llm_with_tools = llm.bind_tools(tools)

    messages = [
        SystemMessage(content="You're a helpful Persian customer support assistant.")
    ]

    cl.user_session.set("llm", llm)
    cl.user_session.set("llm_with_tools", llm_with_tools)
    cl.user_session.set("messages", messages)

    await cl.Message(
        content="سلام! به سامانه پشتیبانی خوش آمدید. چگونه می‌توانم کمکتان کنم؟"
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    messages = cl.user_session.get("messages")
    llm = cl.user_session.get("llm")
    llm_with_tools = cl.user_session.get("llm_with_tools")

    messages.append(HumanMessage(content=message.content))

    response = await llm_with_tools.ainvoke(messages)
    messages.append(response)

    if response.tool_calls:
        for tool in response.tool_calls:
            func_name = tool["name"]
            func_args = tool["args"]

            async with cl.Step(name=f"اجرای ابزار: {func_name}") as step:
                step.input = str(func_args)
                result = execute_tool_call(func_name, func_args)
                step.output = str(result)

            messages.append(ToolMessage(content=str(result), tool_call_id=tool["id"]))

        final_response = await llm.ainvoke(messages)
        messages.append(final_response)
        await cl.Message(content=final_response.content).send()
    else:
        await cl.Message(content=response.content).send()