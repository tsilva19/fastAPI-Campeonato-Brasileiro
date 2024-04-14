from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração da URL de conexão com o banco de dados MySQL
SQLALCHEMY_DATABASE_URL = "mysql://root:root@localhost:3306/cpbr24"

# Cria uma instância de engine do SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Cria uma classe base para as definições de modelos
Base = declarative_base()


# Define a classe SessionLocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Função para inicializar o banco de dados
def initialize_database():
    Base.metadata.create_all(bind=engine)

