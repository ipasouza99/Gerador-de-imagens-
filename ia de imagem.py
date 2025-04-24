import openai
import os

openai.api_key = "SUA_CHAVE_API"
openai.Model.list()
openai.Image.create(
    prompt = "real person", # é no prompt onde definimos qual imagem gostariamos que gerasse.
    n = 2, 
    size = "512x512" # tamanho da imagem
)




