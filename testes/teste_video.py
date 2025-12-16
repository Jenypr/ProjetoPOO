from persistencia.database import Database
from persistencia.video_dao import VideoDAO
from modelo.video import Video


# Criar banco e conexão
db = Database()
conexao = db.conexao


# DAO
dao = VideoDAO(conexao)


# Criar objeto Video
video = Video(titulo='Aula POO', url='https://youtube.com/abc', assistido=False, quadro_id=1)


# Salvar no banco
dao.salvar(video)


# Ler do banco
video_banco = dao.buscar_por_id(1)


print(video_banco.titulo)
print(video_banco.url)