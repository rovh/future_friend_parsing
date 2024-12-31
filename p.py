# import time
# import webbrowser
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup
# import datetime
# import requests

# session = requests.Session()
# link = "https://accounts.lambdatest.com/login"

# data = {
#     'email':'rovhwork@gmail.com',
#     'password':'29082002aA!'
# }


# responce_1 = session.post(link, data=data).text

# print(responce_1)




# def run_parsing():

    # # инициализация веб-драйвера с полным путем к исполняемому драйверу
    # driver = webdriver.Chrome()

    # # засыпание программы на 2 миллисекунды
    # # time.sleep(2)

    # # открытие драйвером сайта
    # driver.get("https://kaf.dmami.ru/site/login")

    # # поиск элементов формы по описанию в html коде
    # login = driver.find_element(By.NAME, "username")
    # password = driver.find_element(By.NAME, "password")

    # # отправка данных в найденные формы
    # login.send_keys("kolotilin_aa")
    # password.send_keys("bhdfyg37")

    # driver.find_element(By.TAG_NAME , "button").click()

    # time.sleep(1)

    # driver.find_element(By.CLASS_NAME , "col-lg-2.col-md-2.col-sm-4.col-xs-6.alert-warning.line2.text-center.btn-warning.border5wt.bold").click()

    # time.sleep(1)

    # clicks_array = [ 
    # "448",# Аудитория 338
    # "426",# Аудитория 409
    # "1380",# Аудитория 409A
    # "424", # Аудитория 403
    # "1379",# Аудитория 403A
    # ]


    # date_now = datetime.datetime.now().strftime('%A')

    # date_now = "Friday"

    # match date_now:
        
    #     case "Monday":
    #         date_name = "Понедельник"
    #         index = 1
    #     case "Tuesday":
    #         date_name = "Вторник"
    #         index = 2
    #     case "Wednesday":
    #         date_name = "Среда"
    #         index = 3
    #     case "Thursday":
    #         date_name = "Четверг"
    #         index = 4
    #     case "Friday":
    #         date_name = "Пятница"
    #         index = 5
    #     case "Saturday":
    #         date_name = "Суббота"
    #         index = 6


    # with open('Preview.txt', 'w'):
    #     pass

    # with open("Preview.txt", "a", encoding="utf-8") as f:

    #     f.write(date_name)
    #     f.write("\n")

    # text = [
    #     " 9:00-10:30:",
    #     "10:40-12:10:",
    #     "12:20-13:50:",
    #     "14:30-16:00:",
    #     "16:10-17:40:",
    #     "17:50-19:20:",
    #     "19:30-21:00:",
    # ]

    # dictionary = []



    # for auditory_index in clicks_array:
    #     driver.find_element(By.ID , auditory_index).click()

    #     time.sleep(1)

    #     html = driver.page_source
    #     soup = BeautifulSoup(html, 'lxml')

    #     auditory_name = soup.find('span', class_ = "h2").text
    #     # auditory_name = auditory_name + " "
    #     # auditory_name  = auditory_name[:6]

    #     level_1 = soup.find('div', class_ = "auditory_schedule")

    #     #Проcматриваем все строчки таблицы
    #     for i in level_1.find_all('tr', class_ = "grid__row"): 
                    
    #         #Проcматриваем все столбцы одной строки, то есть смотрим каждую ячейку строки
    #         for u in i.find_all('td', class_ = "js-droppable js-lessons-pack grid__lessons"):

    #             match auditory_name:
    #                 case 'ПК338':
    #                     column = 1
    #                 case 'ПК403а':
    #                     column = 2
    #                 case 'ПК403':
    #                     column = 3
    #                 case 'ПК409а':
    #                     column = 4
    #                 case 'ПК409':
    #                     column = 5

    #             if u.get("data-day-id") == str(index):

    #                 row = int(u.get("data-time-id"))

    #                 if u.find('div', class_ = "js-draggable lesson") != None:
                        
    #                     dictionary.append(   (   row,   column,    auditory_name      )     )
                        
    #                 else:
    #                     dictionary.append(   (   row,    column,   None      )     )


    #     dictionary.sort(key=lambda auditory: (auditory[0], auditory[1]))

    # with open("Preview.txt", "a", encoding="utf-8") as f:

    #     for index, i in enumerate(text):
    #         f.write("----------------------------")
    #         f.write("\n")
    #         f.write(i)
    #         f.write("\n")
    #         f.write("\n")

    #         for u in dictionary:
    #             if u[0] == index+1 and u[2] != None:
    #                 f.write(' ')
    #                 f.write(u[2])

    #         f.write("\n")
    #         f.write('\n')


    # driver.quit()

# run_parsing()


