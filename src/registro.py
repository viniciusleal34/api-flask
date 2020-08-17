from pymongo import MongoClient
from flask_restful import Resource, reqparse

#String de conexão do mongo
PATH_DEFAULT = " "

class Registro(Resource):
    def __init__(self, url = PATH_DEFAULT):
        self.server = MongoClient(url)
        self.db = self.server.Fatec


    def get(self):
        lista=[]
        argumento = reqparse.RequestParser() 
        argumento.add_argument('date')
        argumento.add_argument('hour_inicio')
        argumento.add_argument('min_inicio')
        argumento.add_argument('hour_final')
        argumento.add_argument('min_final')
        dados= argumento.parse_args()
        horario_inicial = float(str(dados['hour_inicio']) +"."+str(dados['min_inicio']))
        horario_final = float(str(dados['hour_final']) +"."+str(dados['min_final']))
        for post in self.db.registros.find({"date": dados['date']}):
  
            horarioaluno = float(str(post['hour'])+"."+str(post["min"]))
            if horarioaluno <= horario_final and horarioaluno >= horario_inicial:

                lista.append({'ra':post['codigo_user'],
                    'nome':post['nome'],
                    'latitude':post['latitude'],
                    'longitude':post['longitude'],
                    })
            
            
        return lista
            




