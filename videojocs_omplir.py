import ________
import ________
from numpy.linalg import ________




# Mètode de càrrega de fitxer
def carregar_faqs():
   fitxer = "________"
   llista_faqs = []


   try:
       with open(fitxer, "________", encoding="utf-8") as f:
           for linea in f:
               linea = linea.________()
               if not linea:
                   continue


               questio, resposta = linea.split("________", 1)
               embedding = obtenir_embedding(________)
               faq = {
                   "questio": questio,
                   "resposta": resposta,
                   "embedding": ________
               }


               llista_faqs.append(________)
       return llista_faqs
   except Exception as e:
       print(f"Error en carregar les FAQS: {________}")
       return []




# Mètode que compara preguntes i obté resposta
def comparar_pregunta(pregunta_usuari, llista_faqs_amb_embeddings, llindar):
   embedding_usuari = obtenir_embedding(________)
   if embedding_usuari is ________:
       return None


   best_similarity = ________
   best_match = ________


   for faq in llista_faqs_amb_embeddings:
       similarity = calcular_similaridad(________, faq["________"])


       if similarity > best_similarity:
           best_similarity = similarity
           best_match = ________


   if best_similarity >= ________:
       return {
           "resposta": best_match["________"],
           "similaritat": ________,
           "pregunta_coincident": best_match["________"]
       }
   else:
       return ________




# Mètode d’obtenció de l’embedding
def obtenir_embedding(text):
   response = ollama.________(model="________", input=________)
   return response["________"][0]




# Mètode del càlcul de la similaritat
def calcular_similaridad(embedding1, embedding2):
   A = np.array(________)
   B = np.array(________)
   cosine = np.dot(A, B) / (________(A) * ________(B))
   return ________




# Funció del xat
def xat():
   print("\n" + "=" * ________)
   print("       XAT AMB ASSISTENT")
   print("=" * ________)
   print("Escriu les teves preguntes.")
   print("Escriu '________' per tornar al menú principal.\n")


   missatges = [
       {
           "role": "________",
           "content": "Ets un assistent d'atenció al client per una empresa de videojocs i tens que ajudar a l'usuari"
       }
   ]


   while True:
       pregunta = input("Tu: ").________()


       if not pregunta:
           continue


       if pregunta.upper() == "________":
           print("Tornant al menu principal...")
           return


       missatges.append({
           "role": "________",
           "content": pregunta
       })


       try:
           print("Assistent: ", end="", flush=True)


           resposta = ""
           for response in ollama.________(
                   model="________",
                   messages=________,
                   stream=________
           ):
               text = response["________"]["________"]
               print(text, end="", flush=True)
               resposta += ________
           print("\n")


           missatges.append({
               "role": "________",
               "content": resposta
           })
       except Exception as e:
           print(f"Error durant la comunicació amb l'assistent: {________}")




# Menú de l’aplicació
def mostrar_menu():
   print("\n" + "=" * ________)
   print("       APLICACIÓ D'ATENCIÓ AL CLIENT")
   print("1. ________")
   print("2. ________")
   print("3. ________")
   print("=" * ________)




# Mètode main
def main():
   print("==== APLICACIÓ D'ATENCIÓ AL CLIENT ====")
   faqs = carregar_faqs()
   print(f"Carregant {________} preguntes freqüents")
   while True:
       mostrar_menu()
       opcio = input("Selecciona una opció (1-3): ")
       if opcio == "1":
           ________()
       elif opcio == "2":
           print("==== CONSULTA DE FAQS ====")
           pregunta = input("Escriu la teva pregunta: ").________()
           if not pregunta:
               print("No has introduit cap pregunta")
               continue
           llindar = ________
           resultat = comparar_pregunta(________, faqs, llindar)
           if resultat:
               print("Resposta trobada:")
               print(f"Pregunta coincident: {resultat['________']}")
               print(f"Resposta: {resultat['________']}")
               print(f"Similaritat: {resultat['________']}")
           else:
               print("No s'ha trobat cap coincidència")
       elif opcio == "3":
           print("________ per utilitzar l'aplicació")
           break
       else:
           print("Opció no valida. Si us plau, tria 1, 2 o 3.")




main()
