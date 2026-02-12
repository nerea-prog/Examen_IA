# ============================================================
#  EJERCICIO 1 — /api/generate
# ============================================================

import requests
import json

url = "http://localhost:11434/api/generate"

data = {
    "model": "llama3.2",
    "prompt": "Explica brevemente qué es un modelo de lenguaje."
}

response = requests.post(url, json=data, stream=True)

if response.status_code == 200:
    for line in response.iter_lines():
        if line:
            decoded = line.decode("utf-8")
            result = json.loads(decoded)
            print(result.get("response", ""), end="", flush=True)
else:
    print("Error:", response.status_code, response.text)



# ============================================================
#  EJERCICIO 2 — /api/chat con streaming
# ============================================================

import requests
import json

url = "http://localhost:11434/api/chat"

payload = {
    "model": "llama3.2",
    "messages": [
        {"role": "user", "content": "Define qué es un token en NLP."}
    ],
    "stream": True
}

response = requests.post(url, json=payload, stream=True)

if response.status_code == 200:
    for line in response.iter_lines():
        if line:
            decoded = line.decode("utf-8")
            chunk = json.loads(decoded)
            print(chunk["message"]["content"], end="", flush=True)
else:
    print("Error:", response.status_code, response.text)



# ============================================================
#  EJERCICIO 3 — /api/show
# ============================================================

import requests
import json

url = "http://localhost:11434/api/show"

payload = {
   "model": "llama3.2"
}

response = requests.post(url, json=payload)

if response.status_code == 200:
   info = response.json()
   print("Modelo:", info["model"])
   print("Familia:", info["details"]["family"])
   print("Parámetros:", info["parameters"])
else:
   print("Error:", response.status_code, response.text)



# ============================================================
#  EJERCICIO 4 — /api/pull
# ============================================================

import requests
import json

url = "http://localhost:11434/api/pull"

payload = {
   "name": "llama3.2"
}

response = requests.post(url, json=payload, stream=True)

if response.status_code == 200:
   for line in response.iter_lines():
       if line:
           decoded = line.decode("utf-8")
           chunk = json.loads(decoded)
           print(chunk.get("status", ""), end=" ")
else:
   print("Error:", response.status_code, response.text)



# ============================================================
#  EJERCICIO 5 — /api/create
# ============================================================

import requests
import json

url = "http://localhost:11434/api/create"

payload = {
   "name": "educado",
   "modelfile": "FROM llama3.2\nSYSTEM Este modelo responde de forma educada."
}

response = requests.post(url, json=payload)

if response.status_code == 200:
   print("Modelo creado correctamente.")
else:
   print("Error:", response.status_code, response.text)



# ============================================================
#  EJERCICIO 6 — /api/generate avanzado
# ============================================================

import requests
import json

url = "http://localhost:11434/api/generate"

payload = {
   "model": "llama3.2",
   "prompt": "Explica la diferencia entre top-k y top-p.",
   "options": {
       "temperature": 0.9,
       "top_k": 40,
       "top_p": 0.9
   },
   "stream": True
}

response = requests.post(url, json=payload, stream=True)

if response.status_code == 200:
   for line in response.iter_lines():
       if line:
           decoded = line.decode("utf-8")
           chunk = json.loads(decoded)
           print(chunk["response"], end="", flush=True)
else:
   print("Error:", response.status_code, response.text)

# ============================================================
# 🧪 NUEVO ENDPOINT — /api/version
# ============================================================

import requests

url = "http://localhost:11434/api/version"

response = requests.get(url)

if response.status_code == 200:
    info = response.json()
    print("Versión de Ollama:", info["version"])
else:
    print("Error:", response.status_code, response.text)



# ============================================================
# 🧪 NUEVO ENDPOINT — /api/ps (Modelos en ejecución)
# ============================================================

import requests

url = "http://localhost:11434/api/ps"

response = requests.get(url)

if response.status_code == 200:
    info = response.json()
    print("Modelos en ejecución:")
    for model in info.get("models", []):
        print("-", model["name"])
else:
    print("Error:", response.status_code, response.text)



# ============================================================
# 🧪 NUEVO ENDPOINT — /api/delete (Borrar modelo)
# ============================================================

import requests
import json

url = "http://localhost:11434/api/delete"

payload = {
    "name": "mi_modelo"   # Cambia por el modelo que quieras borrar
}

response = requests.delete(url, json=payload)

if response.status_code == 200:
    print("Modelo borrado correctamente.")
else:
    print("Error:", response.status_code, response.text)



# ============================================================
#  EJERCICIOS CON LA LIBRERÍA OLLAMA
# ============================================================

import ollama

# ------------------------------
# 1. ollama.show
# ------------------------------

info = ollama.show("llama3.2")

print("Modelo:", info["model"])
print("Familia:", info["details"]["family"])
print("Parámetros:", info["parameters"])


# ------------------------------
# 2. ollama.pull
# ------------------------------

for chunk in ollama.pull("llama3.2"):
   print(chunk.get("status", ""), end=" ")


# ------------------------------
# 3. ollama.create
# ------------------------------

modelfile = """
FROM llama3.2
SYSTEM ets un medic
"""

ollama.create(
   model="doctor",
   modelfile=modelfile
)

print("Modelo creado correctamente.")


# ------------------------------
# 4. ollama.generate avanzado
# ------------------------------

stream = ollama.generate(
   model="llama3.2",
   prompt="Explica la diferencia entre top-k y top-p.",
   options={
       "temperature": 0.9,
       "top_k": 40,
       "top_p": 0.9
   },
   stream=True
)

for chunk in stream:
   print(chunk["response"], end="", flush=True)


# ------------------------------
# 5. ollama.chat
# ------------------------------

stream = ollama.chat(
   model="llama3.2",
   messages=[
       {"role": "user", "content": "Define qué es un token en NLP."}
   ],
   stream=True
)

for chunk in stream:
   print(chunk["message"]["content"], end="", flush=True)


# ------------------------------
# 6. ollama.embed
# ------------------------------

res = ollama.embed(
   model="nomic-embed-text",
   input="Los modelos de lenguaje representan texto mediante vectores numéricos."
)

vector = res["embeddings"][0]

print("Dimensión del embedding:", len(vector))
print("Primeros valores:", vector[:5])


# ============================================================
# 📚 LIBRERÍA OLLAMA — VERSION, PS, DELETE
# ============================================================

import ollama

# VERSION
print("Versión (ollama):", ollama.version())

# PS
procesos = ollama.ps()
print("Modelos en ejecución (ollama):")
for model in procesos.get("models", []):
    print("-", model["name"])

# DELETE
ollama.delete("mi_modelo")  # Cambia el nombre
print("Modelo borrado con ollama.delete()")
