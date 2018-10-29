class autor:

	def __init__(self, primeiro_nome, ultimo_nome, data_nasc, meio_nome="",):
		self.primeiro_nome = primeiro_nome
		self.meio_nome = meio_nome
		self.ultimo_nome = ultimo_nome
		self.data_nasc = data_nasc

	@property
	def nome_como_citado(self):
		return "{} {}.".format(self.ultimo_nome.upper(), self.primeiro_nome[0])

	def __str__(self):
		return "{}".format(self.primeiro_nome)

class livro:

	def __init__(self, titulo, ano, autores=[]):
		self.titulo = titulo
		self.ano = ano
		self.autores = autores

	@property
	def titulo(self):
		return self.__titulo

	@titulo.setter
	def titulo(self, titulo):
		if titulo is None:
			raise ValueError("O titulo nao pode ser vazio")
		self.__titulo = titulo

	def __str__(self):
		autores =  [x.nome_como_citado for x in self.autores]
		return "{} - {} -- {}".format(self.titulo, self.ano, autores)

class biblioteca:

	def __init__(self, livros):
		self.livros = livros

	@property
	def livros_por_autor(self):
		dic = {}
		for livro in self.livros:
			for autor in livro.autores:
				if autor.nome_como_citado not in dic:
					dic[autor.nome_como_citado]=[]
				dic[autor.nome_como_citado].append(livro.titulo)
		return dic

	def __str__(self):
		return "\n".join([str(livro) for livro in self.livros])

if __name__ == "__main__":

	jose = autor("Jose", "Augusto", "12/03/1978")
	renato = autor("Renato", "Russo", "13/02/1995")

	pax = livro("PAX","2015", [jose])
	hue = livro("O poder dos seis", "2012", [renato])

	biblioteca = biblioteca([pax, hue])
	print(biblioteca)
	print(biblioteca.livros_por_autor)
