from google import genai
from google.genai import types

api_key='AIzaSyAnsGXa-qz8vKwlhbOahSaE9HQH0Z14s38'
system_instruction='Você é um agente especializado na criação de Roadmaps e busca de cursos gratuitos.'
request=input('Qual curso deseja aprender: ')
especialization=input('Dentro dessa área, deseja focar em qual especialização? ')
while request != 'sair':

  client=genai.Client(api_key=api_key)
  response=client.models.generate_content(
      model='gemini-2.0-flash',
      config=types.GenerateContentConfig(system_instruction=system_instruction),
      contents='Crie um roadmap completo para '+request+' que seja focado em '+especialization
  )
  print(response.text)
  request=input('Qual curso deseja aprender: ')
