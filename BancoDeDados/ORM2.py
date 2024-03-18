from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from inicio import Categoria, Produto

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

x = Produto(nome='maça',
            idCategoria=1)

y = Produto(nome='tomate',
            idCategoria=2)

z = Produto(nome='frango',
            idCategoria=3)

session.add_all([ x, y, z ])
session.commit()

