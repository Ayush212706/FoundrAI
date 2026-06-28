from src.ai.langchain_service import ask_with_langchain

answer = ask_with_langchain(
    "Suggest a startup idea for a college student interested in AI."
)

print(answer)