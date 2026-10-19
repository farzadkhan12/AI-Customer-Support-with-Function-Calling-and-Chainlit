import random
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
import os
import getpass
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage
load_dotenv()

if not os.getenv("OPENROUTER_API_KEY"):
    os.environ["OPENROUTER_API_KEY"] = getpass.getpass("Enter your OpenRouter API key: ")

ORDERS_DB = {
    "ORD-101": {
        "customer_name": "Ali mohammadi",
        "status": "in progress",
        "items": ["headphone","mouse"],
        "total_price": 2400000
    },
    "ORD-102": {
        "customer_name": "sara karimi",
        "status": "pass",
        "items": ["book"],
        "total_price": 350000
    },
    "ORD-103": {
        "customer_name": "reza jafari",
        "status": "in payment",
        "items": [" keyboard", "pad"],
        "total_price": 1850000
    }
}

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_order_status",
            "description": "get order id and return customer name and status of order",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "The unique identifier of the order, e.g. ORD-101"
                    }
                },
                "required": ["order_id"]
            }
        }
    },
    {
            "type": "function",
            "function": {
                "name": "submit_ticket",
                "description": "This function registers the user's tickets and stores them in the tickets database. ",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_name": {
                            "type": "string",
                            "description": "Buyer's name, such as 'Ali' "
                        },
                        "issue":{
                            "type": "string",
                            "description": "Ticket Subject like 'After-sales services' "
                        }

                    },
                    "required": ["customer_name", "issue"]
                }
            }
        },
]



TICKETS_DB = []



def get_order_status(order_id):

    if order_id in ORDERS_DB:
        return ORDERS_DB[order_id]["customer_name"],ORDERS_DB[order_id]["status"]
    else :
        return "NOT FOUND!"

def submit_ticket(customer_name, issue):
    num = random.randint(100,10000)

    TICKETS_DB.append({"ticket_id": num, "customer_name": customer_name, "issue": issue})


    return f"Your Ticket is Done!\nThe ID of Ticket : {num}"



available_functions = {
    "get_order_status":get_order_status,
    "submit_ticket":submit_ticket
}


def execute_tool_call(function_name, function_args):
    if function_name in available_functions:
        func = available_functions[function_name]
        result = func(**function_args)
        return result
    else:
        return f"Error: Function '{function_name}' not found."


def chat_with_bot():

    messages = [
        SystemMessage(content="You're a helpful Persian customer support assistant."),
        
    ]
    llm = ChatOpenRouter(
        model="dots-studio/dots-3-note-preview:free",
        temperature=0.1
    )

    llm_with_tools = llm.bind_tools(tools)
    while True:
        user_prompt = input("you: ")

        if user_prompt == "q":
            break

        messages.append(HumanMessage(content=user_prompt))

        response = llm_with_tools.invoke(messages)
        messages.append(response)

        if response.tool_calls:
            for tool in response.tool_calls:
                func_name = tool["name"]
                func_args = tool["args"]

                result = execute_tool_call(func_name,func_args)

                messages.append(ToolMessage(content=str(result), tool_call_id=tool["id"]))
                final_response = llm.invoke(messages)
                print(final_response.content)
                
        
        else:
            print(response.content)


if __name__=="__main__":
    chat_with_bot()

        



    

