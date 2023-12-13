#classe de teste para veiculo
class veiculo(object):
    #metodo contrutor
    def __init__(self, marca, modelo, cor, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade = velocidade

#fucionalidade get e set
    #encapsulamento

    def setmarca(self, marca):
        self.marca = marca

    def getmarca(self):
        return self.marca

    def setmodelo(self, modelo):
        self.modelo = modelo

    def getmodelo(self):
        return self.modelo

    def setcor(self, cor):
        self.cor = cor

    def getcor(self):
        return self.cor


    def setvelocidade(self, velocidade):
        self.velocidade = velocidade

    def getvelocidade(self):
        return self.velocidade

#mostrar dados do objeto
    def __str__(self):
        return(
              '\n Marca: ' +str(self.getmarca()) +
              '\n modelo: ' + str(self.getmodelo()) +
              '\n cor: ' + str(self.getcor()) +
              '\n velocidade: ' + str(self.getvelocidade())  +  ' Km/h'
    )

    def acelerar(self):
        if self.velocidade < 120:
            self.velocidade += 1

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 1