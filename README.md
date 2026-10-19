AI Customer Support Assistant with Function Calling and Chainlit

An interactive AI customer support assistant built using LangChain, Function Calling (Tool Calling), and Chainlit for the web user interface. The assistant interacts with users in natural language and autonomously invokes backend Python functions to inspect order statuses and register support tickets.

Key Features

Automated Tool Calling (Function Calling): The model evaluates user inquiries and determines whether to invoke backend tools (get_order_status or submit_ticket) with extracted arguments.

Web UI with Chainlit: Displays live execution steps (cl.Step) during tool invocations, showing transparency in the agent's reasoning and execution workflow.

Full Execution Loop: Returns tool output to the language model as a ToolMessage, allowing the agent to formulate a natural, human-like final response.

Isolated User Sessions: Manages chat history and model instances per session using cl.user_session.

OpenRouter Compatibility: Supports routing through OpenRouter to switch between various open-source or proprietary models.

Tech Stack

Language: Python 3.10+

Frameworks: LangChain, Chainlit

LLM Provider: OpenRouter API (langchain-openrouter / langchain-openai)

Protocol: Tool Calling / JSON Schema

Project Structure

├── main.py              # Core logic: mock database, backend functions, and console loop
├── app.py               # Web interface powered by Chainlit (event-driven)
├── .env.example         # Template for environment variables
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation


Getting Started

1. Clone the Repository and Set Up the Environment

git clone https://github.com/your-username/ai-customer-support-agent.git
cd ai-customer-support-agent

# Create virtual environment
python -m venv .venv

# Activate on Windows
.venv\Scripts\activate

# Activate on macOS/Linux
source .venv/bin/activate


2. Install Dependencies

pip install -r requirements.txt


3. Configure Environment Variables

Copy the template file to .env:

cp .env.example .env


Open .env and configure your API key:

OPENROUTER_API_KEY=your_openrouter_api_key_here


4. Run the Application

Launch the Chainlit web application:

chainlit run app.py -w


Open your browser at http://localhost:8000.

Example Prompts

Check Order Status:

"Hello, my name is Ali Mohammadi. Can you check the status of my order ORD-101?"

Submit a Support Ticket:

"I would like to submit a ticket. My name is Sara Karimi and my package has not arrived yet."

General Inquiry:

"What services can you assist me with?"
