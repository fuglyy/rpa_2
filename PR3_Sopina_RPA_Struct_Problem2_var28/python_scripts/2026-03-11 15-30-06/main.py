# !/usr/bin/python 
# -*- coding: utf8 -*- 
# Puzzle RPA version: 2.2.3 
# remote
from numbers import Number
import math
import sys

sys.dont_write_bytecode = True

# storage:
from puzzle_logger import configure_logger, log_process, send_message_websocket
from trace_utils import format_traceback
from pathlib import Path

import add_to_dict
import files_and_folders
import read_file
import user_notice_2

# generated

logger = configure_logger()
puzzle_logger_path = Path(__file__).absolute()
logger.info(f'Старт робота: {puzzle_logger_path}')

if __name__ == "__main__":
    def main_sentry_262_proc():
        try:
            # Присваивает переменной значение вставки
            log_process(window_log=True,block_text='Присвоить значение переменной')
            ##E;tJSv^nf5*9o6:a+}g
            file_content = read_file.read_json_file(None,(files_and_folders.get_executable_path('realestate.json',binary_path='TRUE',block_text="Относительный путь",window_log=True, current_language="ru")),block_text="Прочитать текст из json-файла",window_log=True, current_language="ru")

            log_process(block_text='Присвоить значение переменной')

            log_process(window_log=True,block_text='Присвоить значение переменной')
            #uFrN]h2f@`WO!S3^Jo!G
            rental_market = file_content['rental_market']

            log_process(block_text='Присвоить значение переменной')

            log_process(window_log=True,block_text='Присвоить значение переменной')
            #k:nGFnegC6Qf:Rq?Sa-v
            owners = rental_market['owners']

            log_process(block_text='Присвоить значение переменной')

            log_process(window_log=True,block_text='Присвоить значение переменной')
            #Ye:]m|7e/nxaeDYIM2bH
            total_owners = len(owners)

            log_process(block_text='Присвоить значение переменной')

            log_process(window_log=True,block_text='Присвоить значение переменной')
            #7^vk!GZQ**7Y[5}Lj}yW
            is_owners_empty = False

            log_process(block_text='Присвоить значение переменной')

            log_process(window_log=True,block_text='Если – выполнить')
            #5d0rs,C(#6#?jCD,}Loo
            if total_owners == 0:
                log_process(window_log=True,block_text='Присвоить значение переменной')
                #uhAwkm;v0yed1P@IS-;^
                is_owners_empty = True

                log_process(block_text='Присвоить значение переменной')


            log_process(block_text='Если – выполнить')

            log_process(window_log=True,block_text='Присвоить значение переменной')
            #JqXlj3Y*2CAN=P;U%#~X
            all_apartments = []

            log_process(block_text='Присвоить значение переменной')

            log_process(window_log=True,block_text='Цикл для каждого элемента')
            #6vbp,+P+0lF3IjdE@#i#
            for owner in owners:
                log_process(window_log=True,block_text='Цикл для каждого элемента')
                #|j!v4|WOvleY@C5=+|`P
                for apartment in (owner['apartments']):
                    log_process(window_log=True,block_text='Добавить элемент в список')
                    #h{iQtVZ.kk-)0,GO#L#9
                    all_apartments.append(apartment)

                    log_process(block_text='Добавить элемент в список')


                log_process(block_text='Цикл для каждого элемента')


            log_process(block_text='Цикл для каждого элемента')

            log_process(window_log=True,block_text='Присвоить значение переменной')
            #^CS:#b%gyEI*SfX.Lpfl
            total_apartments = len(all_apartments)

            log_process(block_text='Присвоить значение переменной')

            log_process(window_log=True,block_text='Присвоить значение переменной')
            #IzwObj,8NlY[_N1[u2XJ
            max_tenant = 0

            log_process(block_text='Присвоить значение переменной')

            log_process(window_log=True,block_text='Цикл для каждого элемента')
            #zidNIBR7#5QmcyIg./Il
            for apartment in all_apartments:
                log_process(window_log=True,block_text='Присвоить значение переменной')
                #`2#KcAA*ZONZ#{wCTpZY
                tenant_count = len(apartment['tenants'])

                log_process(block_text='Присвоить значение переменной')

                #7z4ir;}[aZ;u)eR*T4pq
                add_to_dict.add_to_dict(apartment,'tenant_count',tenant_count,block_text="Добавить элемент в словарь",window_log=True, current_language="ru")

                log_process(window_log=True,block_text='Присвоить значение переменной')
                #UI;zeYPpqGQSiD*!,QR=
                total_rent = (apartment['rent_price']) * (apartment['tenant_count'])

                log_process(block_text='Присвоить значение переменной')

                #KmG~-QcHg}-X33RbYs)K
                add_to_dict.add_to_dict(apartment,'total_rent',total_rent,block_text="Добавить элемент в словарь",window_log=True, current_language="ru")

                log_process(window_log=True,block_text='Если – выполнить')
                #2cd+D:f-2++%j%C!l(vN
                if max_tenant < tenant_count:
                    log_process(window_log=True,block_text='Присвоить значение переменной')
                    #x!74,,?mWap^8)5se/b6
                    max_tenant = tenant_count

                    log_process(block_text='Присвоить значение переменной')

                    log_process(window_log=True,block_text='Присвоить значение переменной')
                    #0J+*2c.RlMrC;Bt469BO
                    max_apartment = apartment

                    log_process(block_text='Присвоить значение переменной')


                log_process(block_text='Если – выполнить')


            log_process(block_text='Цикл для каждого элемента')

            log_process(window_log=True,block_text='Присвоить значение переменной')
            #-u=l.ZU,qaeW`*@k=];t
            most_occupied_apartment = {
                'address': (max_apartment['address']),
                'tenant_count': (max_apartment['tenant_count'])
            }

            log_process(block_text='Присвоить значение переменной')

            log_process(window_log=True,block_text='Присвоить значение переменной')
            #J6lb8eJLU}3=gb8YXN-w
            owner_occupancy = {}

            log_process(block_text='Присвоить значение переменной')

            log_process(window_log=True,block_text='Цикл для каждого элемента')
            #86Jad`.dLSi*THN0h[Q!
            for owner in owners:
                log_process(window_log=True,block_text='Присвоить значение переменной')
                #Lc%93a4jSFZ(6knv_VN7
                all_tenant = 0

                log_process(block_text='Присвоить значение переменной')

                log_process(window_log=True,block_text='Цикл для каждого элемента')
                #]_%Av;{#Pb53]u5H+BE!
                for apartment in (owner['apartments']):
                    log_process(window_log=True,block_text='Увеличить значение переменной')
                    #qP2^5pvIwnCEf~R8]6S]
                    all_tenant = (all_tenant if isinstance(all_tenant, Number) else 0) + (apartment['tenant_count'])

                    log_process(block_text='Увеличить значение переменной')


                log_process(block_text='Цикл для каждого элемента')

                log_process(window_log=True,block_text='Присвоить значение переменной')
                #JDHT`n%x;O~G-~l{a=A4
                all_max_tenant = len(owner['apartments']) * 10

                log_process(block_text='Присвоить значение переменной')

                log_process(window_log=True,block_text='Присвоить значение переменной')
                #1fh5BCYyG8p=NG?liP)o
                percent = round((all_tenant / all_max_tenant) * 100)

                log_process(block_text='Присвоить значение переменной')

                #:;;ft-dGSGx_WQUZP)C3
                add_to_dict.add_to_dict(owner_occupancy,(owner['name']),percent,block_text="Добавить элемент в словарь",window_log=True, current_language="ru")


            log_process(block_text='Цикл для каждого элемента')

            log_process(window_log=True,block_text='Присвоить значение переменной')
            #{meXD4|//IY!fe5v,Iu[
            rental_basic_report = {
                'TotalOwners': total_owners,
                'TotalApartments': total_apartments,
                'OwnerOccupancy': owner_occupancy,
                'MostOccupiedApartment': most_occupied_apartment
            }

            log_process(block_text='Присвоить значение переменной')

            #7?.z=V/^2H!a!k8KZ=VY
            user_notice_2.user_notice(rental_basic_report,None,block_text="Уведомление пользователя",window_log=True, current_language="ru")


            log_process(window_log=True,block_text='Присвоить значение переменной')
            #l~5Gi|6+1*#-ue^uHBO|
            max_tenant = 0

            log_process(block_text='Присвоить значение переменной')


            logger.info(f'Завершение работы робота: {puzzle_logger_path}')
            send_message_websocket(message_type="python_end")
        except Exception as error_puzzle:
            logger.error(f'{puzzle_logger_path} ' + f'Ошибка: {error_puzzle}')
            error_puzzle_format=format_traceback(error_puzzle)
            send_message_websocket(message_type="python_error", message=error_puzzle_format)
            raise Exception(error_puzzle)
    main_sentry_262_proc()