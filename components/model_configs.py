
import os
import openai
import os
from openai import OpenAI
import anthropic
from groq import Groq

# Configuration dictionary for different models
MODEL_CONFIGS = {
    "OpenAI GPT": {
        "init_client": lambda api_key: OpenAI(api_key=api_key) if api_key else None,  # Initialize client only if API key is provided
        "call_api": lambda client, prompt: client.chat.completions.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        ).choices[0].message.content if client else "Client not initialized.",
    },
    "Anthropic Claude": {
        "init_client": lambda api_key: anthropic.Anthropic(api_key=api_key) if api_key else None,
        "call_api": lambda client, prompt: client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        ).content if client else "Client not initialized.",
    },
    "Groq": {
        "init_client": lambda api_key: Groq(api_key=api_key) if api_key else None,
        "call_api": lambda client, prompt: client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192"
        ).choices[0].message["content"] if client else "Client not initialized.",
    },
    "Custom Model": {
        "init_client": lambda api_key: None,  # Placeholder for custom models
        "call_api": lambda client, prompt: "Custom model API not yet implemented.",
    },
}




# # model_configs.py
# # model_configs.py

# MODEL_CONFIGS = {
#     "OpenAI GPT": {
#         "url_format": "https://api.openai.com/v1/completions",
#         "headers": lambda api_key: {"Authorization": f"Bearer {api_key}"},
#         "payload": lambda prompt: {"model": "text-davinci-003", "prompt": prompt, "temperature": 0.5},
#     },
#     "Azure OpenAI": {
#         "url_format": lambda api_key: f"https://<your-resource-name>.openai.azure.com/openai/deployments/<deployment-name>/completions?api-version=2022-12-01",
#         "headers": lambda api_key: {"api-key": api_key},
#         "payload": lambda prompt: {"prompt": prompt, "max_tokens": 100},
#     },
#     "Anthropic Claude": {
#         "url_format": "https://api.anthropic.com/v1/complete",
#         "headers": lambda api_key: {
#             "x-api-key": api_key,
#             "Content-Type": "application/json"
#         },
#         "payload": lambda prompt: {
#             "prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
#             "model": "claude-v1.3",  # Specify the exact model variant if needed
#             "max_tokens_to_sample": 300,
#             "temperature": 0.7
#         },
#     },
#     "Groq": {
#         "url_format": "https://api.groq.com/v1/completions",
#         "headers": lambda api_key: {"Authorization": f"Bearer {api_key}"},
#         "payload": lambda prompt: {
#             "model": "groq-1.0",  # Specify the exact model version if needed
#             "input": prompt,
#             "temperature": 0.5,
#             "max_tokens": 150
#         },
#     },
#     "Custom Model": {
#         "url_format": "https://<custom-model-api>/generate",
#         "headers": lambda api_key: {"Authorization": f"Bearer {api_key}"},
#         "payload": lambda prompt: {"input": prompt},
#     },
#     # Add more models here as needed
# }
