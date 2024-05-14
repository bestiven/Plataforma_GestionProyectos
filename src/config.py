from pymongo import MongoClient
import certifi

MONGO='mongodb+srv://bbaqueroalonso:brayanbaquero@cluster0.7hl6pdy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'#string de mongo
certificado=certifi.where() #de donde biene la conexion de mongo db 

def conexion ():
    try:
        client= MongoClient(MONGO,tlsCAFile=certificado)
        bd = client["Plataforma"] #crea la linea 
        print('conexion exitosa')
    except ConnectionError:
        print('error de conexion')
    return bd


conexion()
