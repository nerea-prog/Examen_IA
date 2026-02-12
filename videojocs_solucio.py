import ollama
import numpy as np
from numpy.linalg import norm


# Metode de carrega de fitxer
def carregar_faqs():
    fitxer = "faqs.txt"
    llista_faqs = []

    try:
        with open(fitxer, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue

                questio, resposta = linea.split(";", 1)
                embedding = obtenir_embedding(questio)
                faq = {
                    "questio": questio,
                    "resposta": resposta,
                    "embedding": embedding
                }

                llista_faqs.append(faq)
        return llista_faqs
    except Exception as e:
        print(f"Error en carregar les FAQS: {e}")
        return []


# Metode que compara preguntes y obtens resposta
def comparar_pregunta(pregunta_usuari, llista_faqs_amb_embeddings, llindar):
    embedding_usuari = obtenir_embedding(pregunta_usuari)
    if embedding_usuari is None:
        return None

    best_similarity = 0
    best_match = None

    for faq in llista_faqs_amb_embeddings:
        similarity = calcular_similaridad(embedding_usuari, faq["embedding"])

        if similarity > best_similarity:
            best_similarity = similarity
            best_match = faq

    if best_similarity >= llindar:
        return {
            "resposta": best_match["resposta"],
            "similaritat": best_similarity,
            "pregunta_coincident": best_match["questio"]
        }
    else:
        return None


# Metode de obtenció del embedding
def obtenir_embedding(text):
    response = ollama.embed(model="nomic-embed-text", input=text)
    return response["embeddings"][0]


# Metode del calcul de la similaritat
def calcular_similaridad(embedding1, embedding2):
    A = np.array(embedding1)
    B = np.array(embedding2)
    cosine = np.dot(A, B) / (norm(A) * norm(B))
    return cosine


# Funció del chat
def xat():
    print("\n" + "=" * 50)
    print("       XAT AMB ASSISTENT")
    print("=" * 50)
    print("Escriu les teves preguntes.")
    print("Escriu 'SORTIR' per tornar al menú principal.\n")

    missatges = [
        {
            "role": "system",
            "content": "Ets un assistent d'atenció al client per una empresa de videojocs i tens que ajudar a l'usuari"
        }
    ]

    while True:
        pregunta = input("Tu: ").strip()

        if not pregunta:
            continue

        if pregunta.upper() == "SORTIR":
            print("Tornant al menu principal...")
            return

        missatges.append({
            "role": "user",
            "content": pregunta
        })

        try:
            print("Assistent: ", end="", flush=True)

            resposta = ""
            for response in ollama.chat(
                    model="llama3.2",
                    messages=missatges,
                    stream=True
            ):
                text = response["message"]["content"]
                print(text, end="", flush=True)
                resposta += text
            print("\n")

            missatges.append({
                "role": "assistant",
                "content": resposta
            })
        except Exception as e:
            print(f"Error durant la comunicació amb l'assistent: {e}")


# Menu de la aplicació
def mostrar_menu():
    print("\n" + "=" * 50)
    print("       APLICACIÓ D'ATENCIÓ AL CLIENT")
    print("1. Xat amb assistent")
    print("2. Consulta de FAQS")
    print("3. Sortir de l'aplicació")
    print("=" * 50)


# Metode main
def main():
    print("==== APLICACIÓ D'ATENCIÓ AL CLIENT ====")
    faqs = carregar_faqs()
    print(f"Carregant {len(faqs)} preguntes freqüents")
    while True:
        mostrar_menu()
        opcio = input("Selecciona una opció (1-3): ")
        if opcio == "1":
            xat()
        elif opcio == "2":
            print("==== CONSULTA DE FAQS ====")
            pregunta = input("Escriu la teva pregunta: ").strip()
            if not pregunta:
                print("No has introduit cap pregunta")
                continue
            llindar = 0.65
            resultat = comparar_pregunta(pregunta, faqs, llindar)
            if resultat:
                print("Resposta trobada:")
                print(f"Pregunta coincident: {resultat['pregunta_coincident']}")
                print(f"Resposta: {resultat['resposta']}")
                print(f"Similaritat: {resultat['similaritat']}")
            else:
                print("No s'ha trobat cap coincidència")
        elif opcio == "3":
            print("Gracies per utilitzar l'aplicació")
            break
        else:
            print("Opció no valida. Si us plau, tria 1, 2 o 3.")


main()