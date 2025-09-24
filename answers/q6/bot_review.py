# -*- coding: utf-8 -*-
import os, sys, traceback, logging, configparser
# REVIEW: `traceback`, `timedelta` e `timezone` não são usados; remover imports não utilizados.
import xlsxwriter
from datetime import datetime, timedelta, timezone
from apscheduler.schedulers.blocking import BlockingScheduler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from logging.handlers import RotatingFileHandler

def main(argv):
    greetings()

    print('Press Crtl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    app = Flask(__name__)
    handler = RotatingFileHandler('bot.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:123mudar@127.0.0.1:5432/bot_db'
    # REVIEW: Credenciais hardcoded. Usar variáveis de ambiente. Nunca versionar senhas.
    db = SQLAlchemy(app)
    config = configparser.ConfigParser()
    config.read('/tmp/bot/settings/config.ini')
    # REVIEW: Caminho absoluto frágil. Usar caminho relativo a `__file__` ou env (`BOT_CONFIG_PATH`).

    var1 = int(config.get('scheduler','IntervalInMinutes'))
    app.logger.warning('Intervalo entre as execucoes do processo: {}'.format(var1))
    # REVIEW: Este log deveria ser `INFO`, não `WARNING`.
    scheduler = BlockingScheduler()

    task1_instance = scheduler.add_job(task1(db), 'interval', id='task1_job', minutes=var1)
    # REVIEW: `task1_instance` não é usado, considerar remover atribuição.

    try:
        scheduler.start()
    except(KeyboardInterrupt, SystemExit):
        # REVIEW: Evitar `pass` silencioso. Registrar erro/encerramento e retornar código apropriado.
        pass

def greetings():
    print('             ##########################')
    print('             # - ACME - Tasks Robot - #')
    print('             # - v 1.0 - 2020-07-28 - #')
    print('             ##########################')

def task1(db):

    file_name = 'data_export_{0}.xlsx'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
    file_path = os.path.join(os.path.curdir, file_name)
    workbook = xlsxwriter.Workbook(file_path)
    worksheet = workbook.add_worksheet()
    # REVIEW: Envolver criação/fechamento do workbook em `try/finally` para garantir `close()` em caso de erro.

    orders = db.session.execute('SELECT * FROM users;')
    # REVIEW: variável `orders` aqui confunde (são usuários).
    
    index = 1
    
    worksheet.write('A{0}'.format(index),'Id')
    worksheet.write('B{0}'.format(index),'Name')
    worksheet.write('C{0}'.format(index),'Email')
    worksheet.write('D{0}'.format(index),'Password')
    # REVIEW: não exportar senha.
    worksheet.write('E{0}'.format(index),'Role Id')
    worksheet.write('F{0}'.format(index),'Created At')
    worksheet.write('G{0}'.format(index),'Updated At')
    
    for order in orders:
        index = index + 1

        print('Id: {0}'.format(order[0]))
        worksheet.write('A{0}'.format(index),order[0])
        print('Name: {0}'.format(order[1]))
        worksheet.write('B{0}'.format(index),order[1])
        print('Email: {0}'.format(order[2]))
        worksheet.write('C{0}'.format(index),order[2])
        print('Password: {0}'.format(order[3]))
        worksheet.write('D{0}'.format(index),order[3])
        # REVIEW: não logar senha/dados sensíveis.
        print('Role Id: {0}'.format(order[4]))
        worksheet.write('E{0}'.format(index),order[4])
        print('Created At: {0}'.format(order[5]))
        worksheet.write('F{0}'.format(index),order[5])
        print('Updated At: {0}'.format(order[6]))
        worksheet.write('G{0}'.format(index),order[6])
        
    workbook.close()
    # REVIEW: garantir fechamento em `finally`.
    print('job executed!')

if __name__ == '__main__':
    main(sys.argv)
