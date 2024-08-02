import logging
import datetime

# Configuração básica do logger
logging.basicConfig(filename='log_file.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Função para registrar um passo no log
def registrar_log(registos):
    logging.info(f'{datetime.datetime.now()} - {registos}')

    registrar_log("Inicioprograma")
    registrar_log("Login")
    registrar_log("Criação de conta")
    registrar_log("Fim da execução do programa")
    