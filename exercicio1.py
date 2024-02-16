# Crie uma classe Carro:
# Adicione atributos como modelo, cor, ano, e preço.
# Implemente métodos para exibir informações do carro e calcular o preço com desconto.

class Carro():
  def __init__(self, modelo, cor, ano, preco):
    self.modelo = modelo
    self.cor = cor
    self.ano = ano
    self.preco = preco

  def exibir_info(self):
    return "Modelo do carro: " + self.modelo +  "\n , ano: " + self.ano

meuCarro = Carro("Modelão", "azul", 1998, 10.000)

meuCarro.exibir_info()