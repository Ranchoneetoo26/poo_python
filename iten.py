class item:
    def __init__(self, nome):
        self._nome = nome
        
        p = item("Pregador")
        print(p._nome) # acessar diretamente e possivel, mas nao recomendado
        