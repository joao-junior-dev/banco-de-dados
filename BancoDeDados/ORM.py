from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_
from inicio import Pessoa

'''
Session é uma camada intermediária entre o python e
o banco de dados. Podemos ter multiplas sessions 
e cada session e independente da outra.
'''

'''
Tutorial: Como fazer INSERT INTO de dados numa tabela
'''

# 1. crie uma session
def retornaSession():
    USUARIO = 'root'
    SENHA = 'root'
    HOST = 'localhost'
    BANCO = 'pythondb'
    PORT = '3306'

    CONN = f'mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}'

    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

session = retornaSession()

# 2. instancie uma classe tabela
x = Pessoa(nome='João',
           usuario='joao',
           senha='1234'
           )

y = Pessoa(usuario='marcos',
           senha='padrao')

# 3. adicione-a a session e faça o commit

# session.add(x) -> para um único insert
# session.add_all([ x, y ]) -> múltiplos inserts
# session.commit() -> não esqueça de fazer o commit

# CASO queira fazer uma limpeza da session use o comando:
# session.rollback()

'''
Tutorial de como fazer SELECT de dados da tabela
'''

x = session.query(Pessoa).all() # retorna uma lista de instâncias do objeto Pessoa e armazena em x
x = session.query(Pessoa).filter(Pessoa.nome == 'joão').filter(Pessoa.usuario == 'joao') # filtra com duas condicionais
x = session.query(Pessoa).filter_by(usuario = 'joao', nome = 'joao') # maneira mais enxuta de filtrar
x = session.query(Pessoa).filter(or_(Pessoa.usuario == 'joao', Pessoa.usuario == 'marcos')) # usando condicional or



# for i in x:
#    print(i.nome)


'''
Tutorial de como fazer UPDATE no banco de dados
'''

# 1 - filtre a linha que deseja alterar
x = session.query(Pessoa).filter(Pessoa.id == 12).all()
# 2 - altere o dado usando python
x[0].nome = 'bruno'
# 3 - faça o commit
session.commit()

