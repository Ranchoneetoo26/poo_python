class filme:
    def __init__(self, nome):
        self.__nome = nome
            
p = filme(" E o vento levou")
print(p.__nome) # Resultado: Bugou -> AttributeeRROR