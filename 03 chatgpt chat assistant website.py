import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are an expert of the California DMV guidelines and regulation"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "California DMV Expert")

demo.launch(share=True)