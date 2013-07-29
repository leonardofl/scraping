class Pessoa:
   def __init__(self, ano_nascimento):
      self.ano_nascimento = ano_nascimento

   def idade(self):
      return 2013 - self.ano_nascimento


p = Pessoa('1987')
p.ano_nascimento = 1988
print p.idade()

