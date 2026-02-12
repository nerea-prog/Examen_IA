# ============================================================
# 🔁 EJERCICIO — /api/generate (Rellenar)
# ============================================================

import ________
import ________

url = "http://localhost:11434/________"

data = {
    "model": "________",
    "prompt": "Explica brevemente qué es un modelo de lenguaje."
}

response = requests.________(url, json=________, stream=________)

if response.status_code == ________:
    for line in response.________():
        if line:
            decoded = line.________("utf-8")
            result = json.________(decoded)
            print(result.get("________", ""), end="", flush=True)
else:
    print("Error:", response.________, response.________)



# ============================================================
# 🧪 EJERCICIO — Embeddings (Rellenar)
# ============================================================

import ________
import ________

url = "http://localhost:11434/________"

payload = {
    "model": "________",
    "input": "________"
}

response = requests.________(url, json=payload)

if response.status_code == ________:
    info = response.________()
    vector = info["________"][0]
    print("Dimensión:", len(________))
    print("Primeros valores:", ________[:5])
else:
    print("Error:", response.status_code, response.text)



# ============================================================
# 🧪 EJERCICIO — /api/chat con streaming (Rellenar)
# ============================================================

import ________
import ________

url = "http://localhost:11434/________"

payload = {
    "model": "________",
    "messages": [
        {"role": "________", "content": "Define qué es un token en NLP."}
    ],
    "stream": ________
}

response = requests.________(url, json=payload, stream=________)

if response.status_code == ________:
    for line in response.________():
        if line:
            decoded = line.________("utf-8")
            chunk = json.________(decoded)
            print(chunk["________"]["________"], end="", flush=True)
else:
    print("Error:", response.________, response.________)



# ============================================================
# 🧪 1. EJERCICIO — /api/show (Rellenar)
# ============================================================

import ________
import ________

url = "http://localhost:11434/________"

payload = {
   "model": "________"
}

response = requests.________(url, json=payload)

if response.status_code == 200:
   info = response.________()
   print("Modelo:", info["________"])
   print("Familia:", info["________"])
   print("Parámetros:", info["________"])
else:
   print("Error:", response.status_code, response.text)



# ============================================================
# 🧪 2. EJERCICIO — /api/pull (Rellenar)
# ============================================================

import ________
import ________

url = "http://localhost:11434/________"

payload = {
   "name": "________"
}

response = requests.________(url, json=payload, stream=True)

if response.status_code == 200:
   for line in response.________():
       if line:
           decoded = line.decode("utf-8")
           chunk = json.________(decoded)
           print(chunk.get("status", ""), end=" ")
else:
   print("Error:", response.status_code, response.text)



# ============================================================
# 🧪 3. EJERCICIO — /api/create (Rellenar)
# ============================================================

import ________
import ________

url = "http://localhost:11434/________"

payload = {
   "name": "________",
   "modelfile": "FROM llama3.2\nSYSTEM Este modelo responde de forma educada."
}

response = requests.________(url, json=payload)

if response.status_code == 200:
   print("Modelo creado correctamente.")
else:
   print("Error:", response.status_code, response.text)



# ============================================================
# 🧪 4. EJERCICIO — /api/generate avanzado (Rellenar)
# ============================================================

import ________
import ________

url = "http://localhost:11434/________"

payload = {
   "model": "llama3.2",
   "prompt": "Explica la diferencia entre top-k y top-p.",
   "options": {
       "temperature": ________,
       "top_k": ________,
       "top_p": ________
   },
   "stream": True
}

response = requests.________(url, json=payload, stream=True)

if response.status_code == 200:
   for line in response.________():
       if line:
           decoded = line.decode("utf-8")
           chunk = json.________(decoded)
           print(chunk["response"], end="", flush=True)
else:
   print("Error:", response.status_code, response.text)



# ============================================================
# 📚 LIBRERÍA OLLAMA — EJERCICIOS PARA RELLENAR
# ============================================================

# ------------------------------
# 🟦 1. ollama.show
# ------------------------------

import ________

info = ollama.________("________")

print("Modelo:", info["________"])
print("Familia:", info["________"])
print("Parámetros:", info["________"])


# ------------------------------
# 🟩 2. ollama.pull
# ------------------------------

import ________

for chunk in ollama.________("________"):
   print(chunk.get("________", ""), end=" ")


# ------------------------------
# 🟧 3. ollama.create
# ------------------------------

import ________

modelfile = """
FROM ________
SYSTEM ________
"""

ollama.________(
   model="________",
   modelfile=________
)

print("Modelo creado correctamente.")


# ------------------------------
# 🟥 4. ollama.generate avanzado
# ------------------------------

import ________

stream = ollama.________(
   model="________",
   prompt="Explica la diferencia entre top-k y top-p.",
   options={
       "temperature": ________,
       "top_k": ________,
       "top_p": ________
   },
   stream=________
)

for chunk in stream:
   print(chunk["________"], end="", flush=True)


# ------------------------------
# 🟪 5. ollama.chat
# ------------------------------

import ________

stream = ollama.________(
   model="________",
   messages=[
       {"role": "________", "content": "Define qué es un token en NLP."}
   ],
   stream=________
)

for chunk in stream:
   print(chunk["________"]["________"], end="", flush=True)


# ------------------------------
# 🟨 6. ollama.embed
# ------------------------------

import ________

res = ollama.________(
   model="________",
   input="Los modelos de lenguaje representan texto mediante vectores numéricos."
)

vector = res["________"][0]

print("Dimensión del embedding:", len(________))
print("Primeros valores:", ________[:5])
