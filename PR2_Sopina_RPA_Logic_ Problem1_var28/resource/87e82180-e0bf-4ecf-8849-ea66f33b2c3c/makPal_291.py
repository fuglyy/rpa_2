# !/usr/bin/python 
# -*- coding: utf8 -*- 
# Puzzle RPA version: 2.2.3 
# remote
def downRange(start, stop, step):

    while start >= stop:
        yield start
        start -= abs(step)
def upRange(start, stop, step):

    while start <= stop:
        yield start
        start += abs(step)
import sys

sys.dont_write_bytecode = True

# storage:
from puzzle_logger import configure_logger, log_process, send_message_websocket
from trace_utils import format_traceback
from pathlib import Path

import excel_update_row
import interaction_with_excel_data
import read_from_excel
import str_to_int
import user_notice_2

# generated

logger = configure_logger()
puzzle_logger_path = Path(__file__).absolute()
logger.info(f'Старт робота: {puzzle_logger_path}')

if __name__ == "__main__":
    def main_makPal_291_proc():
        try:
            log_process(window_log=True,block_text='Присвоить значение переменной')
            #HMMTLu*^CbYii3Q*aqcO
            total_assignments_done = 0

            log_process(block_text='Присвоить значение переменной')

            log_process(window_log=True,block_text='Присвоить значение переменной')
            #0.h]=r*Mp3!*[(5BFRqU
            total_records = 0

            log_process(block_text='Присвоить значение переменной')

            log_process(window_log=True,block_text='Присвоить значение переменной')
            #fJ^lh(NEiUX9=5R!Vs;,
            incomplete_modules = 0

            log_process(block_text='Присвоить значение переменной')

            log_process(window_log=True,block_text='Присвоить значение переменной')
            #TlE/|%tD/:?ju92Es=aH
            low_quiz_score_days = 0

            log_process(block_text='Присвоить значение переменной')

            log_process(window_log=True,block_text='Присвоить значение переменной')
            #(h.fKM#iNGRPMsb?u]rC
            short_sessions = 0

            log_process(block_text='Присвоить значение переменной')

            log_process(window_log=True,block_text='Присвоить значение переменной')
            #cjz~D*9vluoCHhqzYx:u
            total_lessons = 0

            log_process(block_text='Присвоить значение переменной')

            #hSlH/8jvW~i}4G3$0-6j
            excel_update_row.add_row(path_file='D:\\univer\\korporat\\Пкс 2\\resource\\DesignCourses_Result.xlsx',sheet_name='Analysis_Q1',row_id=0,arr=['StudentId', 'CourseID', 'ModuleID', 'AssignmentRate', 'QuizScore', 'SessionMinutes', 'StatusCategory'],block_text="Модифицировать строку в Excel",window_log=True, current_language="ru")

            log_process(window_log=True,block_text='Группировка блоков')
            # Группировка блоков
            # Присваивает переменной значение вставки
            log_process(window_log=True,block_text='Присвоить значение переменной')
            #JDVyOm_Xeyl!!#iR~EI7
            table = read_from_excel.read_from_excel_2('D:\\univer\\korporat\\Пкс 2\\resource\\DesignCourses_Q1.xlsx','StudentActivity_Q1',True,dtype=None,block_text="Прочитать из Excel",window_log=True, current_language="ru")
            log_process(block_text='Присвоить значение переменной')
            log_process(window_log=True,block_text='Цикл по (от до с шагом)')
            #eekWuB5DOnEvi.X!K5AD
            i_end = len(table) - 1
            for i in (1 <= i_end) and upRange(1, i_end, 1) or downRange(1, i_end, 1):
                log_process(window_log=True,block_text='Присвоить значение переменной')
                #b[EwE#+0TH;FqzSfwfPI
                LessonsCompleted = interaction_with_excel_data.get_excel_cell_data(data=table,column='E',index=i,block_text="Получить значение ячейки табличных данных",window_log=True, current_language="ru")


                log_process(block_text='Присвоить значение переменной')

                log_process(window_log=True,block_text='Присвоить значение переменной')
                #63*x!({o}:FMOE9!dXE%
                AssignmentsDone = interaction_with_excel_data.get_excel_cell_data(data=table,column='F',index=i,block_text="Получить значение ячейки табличных данных",window_log=True, current_language="ru")


                log_process(block_text='Присвоить значение переменной')

                log_process(window_log=True,block_text='Присвоить значение переменной')
                #fk?Ij/5F#vr`e4p[{{0G
                TotalAssignments = interaction_with_excel_data.get_excel_cell_data(data=table,column='G',index=i,block_text="Получить значение ячейки табличных данных",window_log=True, current_language="ru")


                log_process(block_text='Присвоить значение переменной')

                log_process(window_log=True,block_text='Присвоить значение переменной')
                #9I]F[JsNrOh1}z1Xg(dR
                QuizScore = interaction_with_excel_data.get_excel_cell_data(data=table,column='H',index=i,block_text="Получить значение ячейки табличных данных",window_log=True, current_language="ru")


                log_process(block_text='Присвоить значение переменной')

                log_process(window_log=True,block_text='Присвоить значение переменной')
                #5Aek@f/lgkta+a`ke_~%
                SessionMinutes = interaction_with_excel_data.get_excel_cell_data(data=table,column='I',index=i,block_text="Получить значение ячейки табличных данных",window_log=True, current_language="ru")


                log_process(block_text='Присвоить значение переменной')

                log_process(window_log=True,block_text='Присвоить значение переменной')
                #G(dCLQJ{sv0P*S!O*}]a
                total_assignments_done = 0

                log_process(block_text='Присвоить значение переменной')

                log_process(window_log=True,block_text='Присвоить значение переменной')
                #l/`SF*@_K8VTaK~3d%0^
                StudentID = (interaction_with_excel_data.get_excel_cell_data(data=table,column='A',index=i,block_text="Получить значение ячейки табличных данных",window_log=True, current_language="ru")
                ).upper()

                log_process(block_text='Присвоить значение переменной')

                log_process(window_log=True,block_text='Присвоить значение переменной')
                #fZ=At3yw=,`X2uJx9K}2
                CourseID = (interaction_with_excel_data.get_excel_cell_data(data=table,column='B',index=i,block_text="Получить значение ячейки табличных данных",window_log=True, current_language="ru")
                ).upper()

                log_process(block_text='Присвоить значение переменной')

                log_process(window_log=True,block_text='Присвоить значение переменной')
                #zKt-:a!-QoA3G*#gSw[e
                ModuleID = (interaction_with_excel_data.get_excel_cell_data(data=table,column='C',index=i,block_text="Получить значение ячейки табличных данных",window_log=True, current_language="ru")
                ).upper()

                log_process(block_text='Присвоить значение переменной')

                log_process(window_log=True,block_text='Присвоить значение переменной')
                #`X}#o%%4rk+Gy?Dj)n;|
                ActivityDate = str(interaction_with_excel_data.get_excel_cell_data(data=table,column='D',index=i,block_text="Получить значение ячейки табличных данных",window_log=True, current_language="ru")
                )

                log_process(block_text='Присвоить значение переменной')

                log_process(window_log=True,block_text='Присвоить значение переменной')
                #fl,hMCHFb+!IIQ.G;vLA
                ModuleDueDate = str(interaction_with_excel_data.get_excel_cell_data(data=table,column='J',index=i,block_text="Получить значение ячейки табличных данных",window_log=True, current_language="ru")
                )

                log_process(block_text='Присвоить значение переменной')

                log_process(window_log=True,block_text='Если – выполнить')
                #Rci@~T1d(-?Q!DsqTI*0
                if TotalAssignments == 0:
                    log_process(window_log=True,block_text='Присвоить значение переменной')
                    #EAJuW*Tz{|cevc0ggR2m
                    assignment_completion_rate = 1

                    log_process(block_text='Присвоить значение переменной')

                else:
                    log_process(window_log=True,block_text='Присвоить значение переменной')
                    #@wzk97N3T=:s0C.OU-l9
                    assignment_completion_rate = AssignmentsDone / TotalAssignments

                    log_process(block_text='Присвоить значение переменной')


                log_process(block_text='Если – выполнить')

                log_process(window_log=True,block_text='Присвоить значение переменной')
                #-Mt8,jtVKWmVdjJ=S^6Y
                day1 = str_to_int.str_to_int((ModuleDueDate[8 : 10]),block_text="Преобразовать строку в число",window_log=True, current_language="ru")

                log_process(block_text='Присвоить значение переменной')

                log_process(window_log=True,block_text='Присвоить значение переменной')
                #I$(T(;O)A98q5su,4iTe
                day2 = str_to_int.str_to_int((ActivityDate[8 : 10]),block_text="Преобразовать строку в число",window_log=True, current_language="ru")

                log_process(block_text='Присвоить значение переменной')

                log_process(window_log=True,block_text='Присвоить значение переменной')
                #8D]s#cu.cz=O{n+ya#S6
                days_to_due = day1 - day2

                log_process(block_text='Присвоить значение переменной')

                log_process(window_log=True,block_text='Если – выполнить')
                #MEqHP=Of!/n;lCdG5WMV
                if assignment_completion_rate < 0.5:
                    log_process(window_log=True,block_text='Присвоить значение переменной')
                    #2/0a);Uu4`de;xX$`c},
                    incomplete_modules = incomplete_modules + 1

                    log_process(block_text='Присвоить значение переменной')


                log_process(block_text='Если – выполнить')

                log_process(window_log=True,block_text='Если – выполнить')
                #)8ihaEhYZ|KjQt5x4Zl0
                if QuizScore < 60:
                    log_process(window_log=True,block_text='Присвоить значение переменной')
                    #gbtAW,P[S!P?mXf]YyIH
                    low_quiz_score_days = low_quiz_score_days + 1

                    log_process(block_text='Присвоить значение переменной')


                log_process(block_text='Если – выполнить')

                log_process(window_log=True,block_text='Если – выполнить')
                #z_=4UBB/~oy4-y-i_w:R
                if SessionMinutes < 15:
                    log_process(window_log=True,block_text='Присвоить значение переменной')
                    #r%yf9U+;4y|(H+a,Pkl2
                    short_sessions = short_sessions + 1

                    log_process(block_text='Присвоить значение переменной')


                log_process(block_text='Если – выполнить')

                log_process(window_log=True,block_text='Присвоить значение переменной')
                #sRY2PP##3n2mO~wAl_[`
                total_lessons = LessonsCompleted

                log_process(block_text='Присвоить значение переменной')

                log_process(window_log=True,block_text='Присвоить значение переменной')
                #T~$/QrCMH@TI_1IPZene
                total_assignments_done = AssignmentsDone

                log_process(block_text='Присвоить значение переменной')

                log_process(window_log=True,block_text='Если – выполнить')
                #fm?8+.RkRf#LhKiyAgNm
                if assignment_completion_rate < 0.5:
                    log_process(window_log=True,block_text='Присвоить значение переменной')
                    #$G`mTB]rD/S5.hnw_vuZ
                    StatusCategory = 'Low Completion'

                    log_process(block_text='Присвоить значение переменной')

                elif QuizScore < 60:
                    log_process(window_log=True,block_text='Присвоить значение переменной')
                    #.%WSTAfE+f/Hj$4agE6H
                    StatusCategory = 'Low Quiz'

                    log_process(block_text='Присвоить значение переменной')

                elif SessionMinutes < 15:
                    log_process(window_log=True,block_text='Присвоить значение переменной')
                    #Os}CwZHnT~=tUo)2^gj[
                    StatusCategory = 'Short Session'

                    log_process(block_text='Присвоить значение переменной')

                else:
                    log_process(window_log=True,block_text='Присвоить значение переменной')
                    ##d3xn#d/^$c3U[hO8bH,
                    StatusCategory = 'Good'

                    log_process(block_text='Присвоить значение переменной')


                log_process(block_text='Если – выполнить')

                #]9{JfUQTf0lAS@$2f);|
                excel_update_row.add_row(path_file='D:\\univer\\korporat\\Пкс 2\\resource\\DesignCourses_Result.xlsx',sheet_name='Analysis_Q1',row_id=i,arr=[StudentID, CourseID, ModuleID, assignment_completion_rate, QuizScore, SessionMinutes, StatusCategory],block_text="Модифицировать строку в Excel",window_log=True, current_language="ru")

            log_process(block_text='Цикл по (от до с шагом)')
            log_process(window_log=True,block_text='Присвоить значение переменной')
            #pr2joO#Z@iWW1)S%E$LJ
            total_records = len(table) - 1
            log_process(block_text='Присвоить значение переменной')
            log_process(window_log=True,block_text='Присвоить значение переменной')
            #gs[2)Lvz];bQqHa!`hqL
            notification = ''.join([str(x) for x in ['Анализ активности студентов Q1 завершён.', ('' + '\n' +
            ''), ('' + '\n' +
            ''), f"Всего записей: {total_records}", ('' + '\n' +
            ''), f"Незавершённых модулей: {incomplete_modules}", ('' + '\n' +
            ''), f"Дней с низким баллом тестов: {low_quiz_score_days}", ('' + '\n' +
            ''), f"Коротких сессий: {short_sessions}", ('' + '\n' +
            ''), ('' + '\n' +
            ''), f"Всего завершённых уроков: {total_lessons}", f"Всего выполненных заданий: {total_assignments_done}", ('' + '\n' +
            ''), ('' + '\n' +
            ''), 'Отчёт сохранён в DesignCourses_Result.xlsx (лист Analysis_Q1).']])
            log_process(block_text='Присвоить значение переменной')
            #}!JE_T#-7v-VD.S*tc$n
            user_notice_2.user_notice(notification,None,block_text="Уведомление пользователя",window_log=True, current_language="ru")
            

            log_process(block_text='Группировка блоков')


            ''

            logger.info(f'Завершение работы робота: {puzzle_logger_path}')
            send_message_websocket(message_type="python_end")
        except Exception as error_puzzle:
            logger.error(f'{puzzle_logger_path} ' + f'Ошибка: {error_puzzle}')
            error_puzzle_format=format_traceback(error_puzzle)
            send_message_websocket(message_type="python_error", message=error_puzzle_format)
            raise Exception(error_puzzle)
    main_makPal_291_proc()