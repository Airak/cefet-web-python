class autor:

	def __init__(self, primeiro_nome, ultimo_nome, data_nasc, meio_nome="",):
		self.primeiro_nome = primeiro_nome
		self.meio_nome = meio_nome
		self.ultimo_nome = ultimo_nome
		self.data_nasc = data_nasc

	def nome_como_citado(self):
		print( self.ultimo_nome.upper() + " " + self.primeiro_nome[0].upper() + ".")

	def __str__(self):
		return "{primeiro_nome}".format(primeiro_nome=self.primeiro_nome)

class livro:

	def __init__(self, titulo, ano, autores):
		self.titulo = titulo
		self.ano = ano
		self.autores = []#lista de autores

	@property	
	def titulo_vazio(self):
		if len(self.titulo)==0:
			raise ValueError("O titulo nao pode ser vazio")

	def adiciona_autor(self, autor):
		self.autores.append(autor)

	def __str__(self):
		return "{titulo} - {ano} -- {autores}".format(titulo=self.titulo, ano=self.ano, autores=self.autores)

class biblioteca:

	def __init__(self, livros):
		self.livros = [] #lista de livros

	def adiciona_livro(self, livro):
		self.livros.append(livro)

	def livros_por_autor():
		 #utilizará a lista de livros para retornar um dicionário onde cada chave será o nome de um autor e, cada valor, será a lista de livros deste autor.
		 dic = {}
		 for livro in self.livros:
		 	for autor in livro.autores:
		 		#verifica se ha uma chave para o autor no dicionario, se n tiver cria.
		 		dic[autor.primeiro_nome]=livro.titulo
		 return dic

if __name__ == "__main__":
	jose = autor("José", "Augusto", "12/03/1978")
	jose.nome_como_citado()

	pax = livro("PAX", "2015")

	print(pax)
