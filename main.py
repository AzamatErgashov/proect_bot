import telebot
import requests
import requests as r
from bs4  import BeautifulSoup
from bs4  import BeautifulSoup as bs
import json
from telebot.types import KeyboardButton,ReplyKeyboardMarkup
import wikipedia
wikipedia.set_lang("uz")

# from prettytable import PrettyTable
# wikipedia.set_lang("eng")

TOKEN = "5498899020:AAHj28247c7OnmrH-0oQkylkJOIf_CzeFVI"
bot = telebot.TeleBot(TOKEN,parse_mode=None)
kurslar = []

def my_qalampir_parsing(id):
    url = "https://qalampir.uz/"
    res = requests.get(url)
    html = BeautifulSoup(res.text,"html.parser")
    my_ls = []
    for item in html.find_all("div",class_="title"):
        my_ls.append(str(item.text).replace("Facebook","").replace("Telegram","").replace("Instagram","").replace("Youtube",""))
    bot.send_message(id,"\n".join(my_ls))

def my_kun_uz(id):
    url_2 = "https://kun.uz/"
    res_2 = requests.get(url_2)
    html_2 = BeautifulSoup(res_2.text,"html.parser")
    xx_2 = []
    for item in html_2.find_all("div", class_="row"):
        xx_2.append(str(item.text))
    bot.send_message(id,"\n".join(xx_2))

# def all_infor_about_mach(id):
#     url = "https://www.sports.ru/epl/table/"
#     list = requests.get(url)
#     soup = BeautifulSoup(list.text, "html.parser")
#     page = soup.find_all("div", class_="accordion-group teaser-group")
#     ab = []
#     for a in page:
#         for b in a.find_all("div", class_="teaser-event__status"):
#             ab.append(b.text)
#     ij = []
#     for i in page:
#         for j in i.find_all("div", class_="teaser-event__board clearfix"):
#             ij.append(j.text)
#     zip_file = zip(ab, ij)
#     tuple_file = tuple(zip_file)
#     for lk in tuple_file:
#         bot.send_message(id,"".join(lk))

def all_infor_about_mach(id):
    url = "https://www.sports.ru/epl/table/"
    list = requests.get(url)
    soup = BeautifulSoup(list.text, "html.parser")
    page = soup.find_all("li", class_="teaser-event")
    for i in page:
        bot.send_message(id,i.text)

#######################################################################3
def photos_2022(id,text=None):
    f = open("D:\sa\proect_bot\photo_2022-08-02_13-56-59.jpg","rb")
    bot.send_photo(id,f)

def photos_2023(id,text=None):
    f = open("D:\sa\proect_bot\phosy59.jpg","rb")
    bot.send_photo(id,f)


def photos_2024(id,text=None):
    f = open("D:\sa\proect_bot\gorizontalniy-prosoy-calendar-2024.jpg","rb")
    bot.send_photo(id,f)


def photos_2025(id,text=None):
    f = open("D:\sa\proect_bot\календарь-шаблон-вектор-простой-минимальный-планировщик-223477382.jpg","rb")
    bot.send_photo(id,f)    

def photos_2026(id,text=None):
    f = open("D:\sa\proect_bot\photo.jpg","rb")
    bot.send_photo(id,f)


# def all_infor_in_crtpcoin(id):
#   # global a
#     url = "https://coincodex.com/trending/"
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, "html.parser")
#     find_all_infor_for_coin = soup.find("table", class_="coins")
#     # x = []
#     for l in find_all_infor_for_coin:
#         for k in l.find_all("tr", class_="coin coin-header"):
#             p = k.text.split(" ")
#         print("  ".join(p))
            
#     a = []
#     for i in find_all_infor_for_coin:
#         for j in i.find_all("tr", class_="coin"):
#             for i1 in j.find_all("div", class_="coin-base-data-wrapper"):

#                 a.append(i1.text)

#     a2 = []
#     for i2 in find_all_infor_for_coin:
#         for j2 in i2.find_all("tr", class_="coin"):
#             for i3 in j2.find_all("div", class_="currency"):
#                 a2.append(i3.text)

#     q = []
#     for i5 in find_all_infor_for_coin:
#         for i6 in i5.find_all("tr", class_="coin"):
#             for i12 in i6.find_all("td", class_="change"):
#                 q.append(i12.text)

#     w = []
#     for i7 in find_all_infor_for_coin:
#         for i8 in i7.find_all("tr", class_="coin"):
#             for i9 in i8.find_all("td", class_="market-cap show"):
#                 w.append(i9.text)

#     e = []
#     for t in find_all_infor_for_coin:
#         for t1 in t.find_all("tr", class_="coin"):
#             for t2 in t1.find_all("td", class_="volume"):
#                 e.append(t2.text)
#     print()   
#     x_2 = []   
#     a3 = tuple(zip(a, a2, q, w, e))
#     for i4 in a3:
#         pri = "   ".join(i4)
#         # print(str(pri))
#         json_data = json.dumps(pri)
#         # print(json_data)
#         # print(pri)
#         bot.send_message(id,json_data)


########################## ###########################################  

def futboll_information_APL(id):
    url = "https://terrikon.com/football/england/championship/"
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")
    all_infor_in_list = soup.find_all("table", class_="grouptable")
    team_list = []
    for j in all_infor_in_list:
        for j1 in j.find_all("td", class_="team"):
            team_list.append(j1.text)
    win_list = []
    for i2 in all_infor_in_list:
        for j3 in i2.find_all("td", class_="win"):
            win_list.append(j3.text)
    draw_list = []
    for i3 in all_infor_in_list:
        for j4 in i3.find_all("td", class_="draw"):
            draw_list.append(j4.text)
    lose_list = []
    for i4 in all_infor_in_list:
        for j5 in i4.find_all("td", class_="lose"):
            lose_list.append(j5.text)
    # n = 0
    # while n < len(team_list):
    #   team = team_list[n]
    #   win = win_list[n]
    #   draw = draw_list[n]
    #   lose = lose_list[n]
    #   n += 1
    bot.send_message(id,"TEAM     W  D  L")
    zip_list = zip(team_list, win_list, draw_list, lose_list)
    p = tuple(zip_list)
    for format in p:
        bot.send_message(id,"  ".join(format))      

####################### ###########################
def all_infor_in_crtpcoin(id):
  # global a
    url = "https://coincodex.com/trending/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    find_all_infor_for_coin = soup.find("table", class_="coins")
    # x = []
    print("NAME      PRICE      24H CHANGE     VOLUME")
            
    a = []
    for i in find_all_infor_for_coin:
        for j in i.find_all("tr", class_="coin"):
            for i1 in j.find_all("div", class_="coin-base-data-wrapper"):

                a.append(i1.text)

    a2 = []
    for i2 in find_all_infor_for_coin:
        for j2 in i2.find_all("tr", class_="coin"):
            for i3 in j2.find_all("div", class_="currency"):
                a2.append(i3.text)

    q = []
    for i5 in find_all_infor_for_coin:
        for i6 in i5.find_all("tr", class_="coin"):
            for i12 in i6.find_all("td", class_="change"):
                q.append(i12.text)

    # w = []
    # for i7 in find_all_infor_for_coin:
    #   for i8 in i7.find_all("tr", class_="coin"):
    #     for i9 in i8.find_all("td", class_="market-cap show"):
    #       w.append(i9.text)

    e = []
    for t in find_all_infor_for_coin:
        for t1 in t.find_all("tr", class_="coin"):
            for t2 in t1.find_all("td", class_="volume"):
                e.append(t2.text)
    print()     
    if  True:
        a3 = tuple(zip(a[:10], a2[:10], q[:10], e[:10]))
        for i4 in a3:
            bot.send_message(id,"   ".join(i4))
    # elif message.text == "50":
    #     a3 = tuple(zip(a[:50], a2[:50], q[:50], e[:50]))
    #     for i4 in a3:
    #         bot.send_message(id,"   ".join(i4))
    else:
        print("NO found!!!")

############################## ###########################


def all_infor_in_crtpcoin_2(id):
  # global a
    url = "https://coincodex.com/trending/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    find_all_infor_for_coin = soup.find("table", class_="coins")
    # x = []
    print("NAME      PRICE      24H CHANGE     VOLUME")
            
    a = []
    for i in find_all_infor_for_coin:
        for j in i.find_all("tr", class_="coin"):
            for i1 in j.find_all("div", class_="coin-base-data-wrapper"):

                a.append(i1.text)

    a2 = []
    for i2 in find_all_infor_for_coin:
        for j2 in i2.find_all("tr", class_="coin"):
            for i3 in j2.find_all("div", class_="currency"):
                a2.append(i3.text)

    q = []
    for i5 in find_all_infor_for_coin:
        for i6 in i5.find_all("tr", class_="coin"):
            for i12 in i6.find_all("td", class_="change"):
                q.append(i12.text)

    # w = []
    # for i7 in find_all_infor_for_coin:
    #   for i8 in i7.find_all("tr", class_="coin"):
    #     for i9 in i8.find_all("td", class_="market-cap show"):
    #       w.append(i9.text)

    e = []
    for t in find_all_infor_for_coin:
        for t1 in t.find_all("tr", class_="coin"):
            for t2 in t1.find_all("td", class_="volume"):
                e.append(t2.text)
    print()     
    # if  True:
    #     a3 = tuple(zip(a[:10], a2[:10], q[:10], e[:10]))
    #     for i4 in a3:
    #         bot.send_message(id,"   ".join(i4))
    
    a3 = tuple(zip(a[:50], a2[:50], q[:50], e[:50]))
    for i4 in a3:
        bot.send_message(id,"   ".join(i4))
    else:
        print("NO found!!!")


#####################################################
def parsing(id,text=None):
    global kurs
    url = "https://hamkorbank.uz/exchange-rate/"
    res = r.get(url)
    html = bs(res.text,'html.parser')

    for item_2 in html.find_all('div', class_= 'list'):
        for i in item_2.find_all('ul', class_ = 'body'):
            # print(i.get_text())
            for item_a in i.find_all('li'):
                # print(item_a.get_text())
                kurslar.append(item_a.get_text())                                 

    bot.send_message(id,f"Валюта = <strong>{kurslar[0]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Код символа = <strong>{kurslar[1]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Курс ЦБ = <strong>{kurslar[2]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Покупка = <strong>{kurslar[3]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Продажа = <strong>{kurslar[4]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Динамика = <b>{kurslar[5]}</b>",parse_mode="HTML")


def parsing_new(id,text=None):
    global kurslar
    url = "https://hamkorbank.uz/exchange-rate/"
    res = r.get(url)
    html = bs(res.text,'html.parser')

    for item_2 in html.find_all('div', class_= 'list'):
        for i in item_2.find_all('ul', class_ = 'body'):
            # print(i.get_text())
            for item_a in i.find_all('li'):
                # print(item_a.get_text())
                kurslar.append(item_a.get_text())                                 

    bot.send_message(id,f"Валюта = <strong>{kurslar[12]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Код символа = <strong>{kurslar[13]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Курс ЦБ = <strong>{kurslar[14]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Покупка = <strong>{kurslar[15]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Продажа = <strong>{kurslar[16]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Динамика = <b>{kurslar[17]}</b>",parse_mode="HTML")

def parsing_now(id,text=None):
    global kurslar
    url = "https://hamkorbank.uz/exchange-rate/"
    res = r.get(url)
    html = bs(res.text,'html.parser')

    for item_2 in html.find_all('div', class_= 'list'):
        for i in item_2.find_all('ul', class_ = 'body'):
            # print(i.get_text())
            for item_a in i.find_all('li'):
                # print(item_a.get_text())
                kurslar.append(item_a.get_text())                                 

    bot.send_message(id,f"Валюта = <strong>{kurslar[6]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Код символа = <strong>{kurslar[7]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Курс ЦБ = <strong>{kurslar[8]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Покупка = <strong>{kurslar[9]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Продажа = <strong>{kurslar[10]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Динамика = <b>{kurslar[11]}</b>",parse_mode="HTML") 


def parsing_new(id,text=None):
    global kurslar
    url = "https://hamkorbank.uz/exchange-rate/"
    res = r.get(url)
    html = bs(res.text,'html.parser')

    for item_2 in html.find_all('div', class_= 'list'):
        for i in item_2.find_all('ul', class_ = 'body'):
            # print(i.get_text())
            for item_a in i.find_all('li'):
                # print(item_a.get_text())
                kurslar.append(item_a.get_text())                                 

    bot.send_message(id,f"Валюта = <strong>{kurslar[12]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Код символа = <strong>{kurslar[13]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Курс ЦБ = <strong>{kurslar[14]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Покупка = <strong>{kurslar[15]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Продажа = <strong>{kurslar[16]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Динамика = <b>{kurslar[17]}</b>",parse_mode="HTML")

def parsing_con(id,text=None):
    global kurslar
    url = "https://hamkorbank.uz/exchange-rate/"
    res = r.get(url)
    html = bs(res.text,'html.parser')

    for item_2 in html.find_all('div', class_= 'list'):
        for i in item_2.find_all('ul', class_ = 'body'):
            # print(i.get_text())
            for item_a in i.find_all('li'):
                # print(item_a.get_text())
                kurslar.append(item_a.get_text())                                 

    bot.send_message(id,f"Валюта = <strong>{kurslar[18]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Код символа = <strong>{kurslar[19]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Курс ЦБ = <strong>{kurslar[20]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Покупка = <strong>{kurslar[21]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Продажа = <strong>{kurslar[22]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Динамика = <b>{kurslar[23]}</b>",parse_mode="HTML")

def parsing_can(id,text=None):
    global kurslar
    url = "https://hamkorbank.uz/exchange-rate/"
    res = r.get(url)
    html = bs(res.text,'html.parser')

    for item_2 in html.find_all('div', class_= 'list'):
        for i in item_2.find_all('ul', class_ = 'body'):
            # print(i.get_text())
            for item_a in i.find_all('li'):
                # print(item_a.get_text())
                kurslar.append(item_a.get_text())                                 

    bot.send_message(id,f"Валюта = <strong>{kurslar[24]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Код символа = <strong>{kurslar[25]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Курс ЦБ = <strong>{kurslar[26]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Покупка = <strong>{kurslar[27]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Продажа = <strong>{kurslar[28]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Динамика = <b>{kurslar[29]}</b>",parse_mode="HTML")

def parsing_cashn(id,text=None):
    global kurslar
    url = "https://hamkorbank.uz/exchange-rate/"
    res = r.get(url)
    html = bs(res.text,'html.parser')

    for item_2 in html.find_all('div', class_= 'list'):
        for i in item_2.find_all('ul', class_ = 'body'):
            # print(i.get_text())
            for item_a in i.find_all('li'):
                # print(item_a.get_text())
                kurslar.append(item_a.get_text())                                 

    bot.send_message(id,f"Валюта = <strong>{kurslar[30]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Код символа = <strong>{kurslar[31]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Курс ЦБ = <strong>{kurslar[32]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Покупка = <strong>{kurslar[33]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Продажа = <strong>{kurslar[34]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Динамика = <b>{kurslar[35]}</b>",parse_mode="HTML")
     
# def my_table(id):
#     my_list = []
#     table = PrettyTable()
#     table.field_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saterdey', 'Sunday']
#     table.add_row(['1', '2', '3', '4', '5', '6', '7'])
#     table.add_row(['8', '9', '10', '11', '12', '13', '14'])
#     table.add_row(['15', '16', '17', '18', '19', '20', '21'])
#     table.add_row(['22', '23', '24', '25', '26', '27', '28'])
#     table.add_row([29, 30, 31, None, None, None, None])
#     my_list.append(table)
#     bot.send_message(id,my_list)
    
@bot.message_handler(commands=['start'])
def my_func(message):
    bot.send_message(message.chat.id,"salom")
    print(message.from_user)
    print(f"""
    
██████████████████████▀█████████████████████████████▀████████████████████████████████████████████████████████████
█▄─▄─▀█─▄▄─█─▄─▄─█─▄▄▄▄██▀▄─████▄─█─▄█▄─▄█▄─▄▄▀█─▄▄▄▄██▀▄─██▄─▀█▄─▄███▄─▄█▄─▀█▄─▄█─▄▄▄▄█─▄▄─█▄─▀█▄─▄█▄─▀█▄─▄█▄─▄█
██─▄─▀█─██─███─███─██▄─██─▀─█████─▄▀███─███─▄─▄█─██▄─██─▀─███─█▄▀─█████─███─█▄▀─██▄▄▄▄─█─██─██─█▄▀─███─█▄▀─███─██
▀▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▀▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▀▀▄▄▀▄▄▄▀
█████████████████████████████████████████████████████████████████████████████
█▄─▀█▀─▄██▀▄─██▄─▄███▄─██─▄█▄─▀█▀─▄█─▄▄─█─▄─▄─█▄─▄████▀▄─██▄─▄▄▀█▄─▄█░█░█░█░█
██─█▄█─███─▀─███─██▀██─██─███─█▄█─██─██─███─████─██▀██─▀─███─▄─▄██─██▄█▄█▄█▄█
▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▀▄▄▄▀▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▄▀▄▀▄▀▄▀
    {message}
    
░█▀▀█ █──█ 　 ─▀─ █▀▀▄ █▀▀ █▀▀█ █▀▀▄ 　 █▀▀▄ █▀▀█ ▀▀█▀▀ ─▀─ █▀▄▀█ ─▀─ ▀▀█ █▀▀▄ █▀▀█ █ █ █ 
░█▀▀▄ █──█ 　 ▀█▀ █──█ ▀▀█ █──█ █──█ 　 █▀▀▄ █──█ ──█── ▀█▀ █─▀─█ ▀█▀ ▄▀─ █──█ █▄▄█ ▀ ▀ ▀ 
░█▄▄█ ─▀▀▀ 　 ▀▀▀ ▀──▀ ▀▀▀ ▀▀▀▀ ▀──▀ 　 ▀▀▀─ ▀▀▀▀ ──▀── ▀▀▀ ▀───▀ ▀▀▀ ▀▀▀ ▀▀▀─ ▀──▀ ▄ ▄ ▄
    
    {message.from_user.first_name}
    """)
    markup = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    pul_kursi = KeyboardButton('Pul kurslari')
    treding = KeyboardButton('Treding kurslari')
    kalendar = KeyboardButton('Kalendar')
    wki_data = KeyboardButton('Wikipedia')
    football = KeyboardButton("Footbal news")
    qalampir_ = KeyboardButton("Qalampir uz")
    kun_uz = KeyboardButton("Kun uz")
    # kun_yangiliklari = KeyboardButton("Kun Yangiliklari")
    # qalampir_uz = KeyboardButton("Qalampir_uz")
    # kun_uz = KeyboardButton("Kun_uz")
    markup.add(pul_kursi,kalendar,treding,wki_data,football,qalampir_,kun_uz)
    bot.send_message(message.chat.id,f' Salom {message.from_user.first_name} Botimizga hush kelibsiz!', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def my_texts(message):
    if message.text == 'Pul kurslari':
        markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        dolllar = KeyboardButton('$ - Dollar')
        rubl = KeyboardButton('₽ - Ruble')
        euro = KeyboardButton('€ - Euro')
        gpb = KeyboardButton('£ - Gbp')
        iena = KeyboardButton('¥ - Iena')
        frank = KeyboardButton('₣ - Shveytsariya franki')
        basck = KeyboardButton("Back <<<")
        markup.add(dolllar,rubl,euro,gpb,iena,frank,basck)
        bot.send_message(message.chat.id,f' Salom {message.from_user.first_name} Botimizga hush kelibsiz!', reply_markup=markup)
        bot.send_message(message.chat.id,f"{message.from_user.first_name} -- Bu bot sizga hozirgi mashxur 6ta valyutalarni so'mda qancha qiymatga tengligini ko'rsatadi !")
        bot.send_message(message.chat.id,'Sinash uchun tugmalardan birontasinni bosing')
        bot.send_message(message.chat.id,"Siz pul kurslarini tanladinggiz")
    elif message.text == '$ - Dollar':
        parsing(message.chat.id)
    elif message.text == '₽ - Ruble' :
        parsing_new(message.chat.id)
    elif message.text == '€ - Euro':
        parsing_now(message.chat.id)
    elif message.text == '£ - Gbp':
        parsing_con(message.chat.id)
    elif message.text == '¥ - Iena':
        parsing_can(message.chat.id)
    elif message.text == "Back <<<":
        my_func(message)    
    elif message.text == '₣ - Shveytsariya franki':
        parsing_cashn(message.chat.id)      
    elif message.text == "Qalampir uz":
        my_qalampir_parsing(message.chat.id)
    # elif message.text == "Kun Yangiliklari":
    #     markup = ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    #     # kun_uz = KeyboardButton("Qalampir uz")

    #     back_qalampir = KeyboardButton("Back <<<")
    #     markup.add(back_qalampir)
    #     bot.send_message(message.chat.id,'...Typing', reply_markup=markup)
        # my_qalampir_parsing(message.chat.id)
    elif message.text == "Kun uz":
        my_kun_uz(message.chat.id)

    elif message.text == "Back <<<":
        my_func(message)

    elif message.text == 'Treding kurslari':  
        markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        parsing_treding = KeyboardButton('Back <<<')
        sanoq_10 = KeyboardButton("10")
        sanoq_50 = KeyboardButton("50")
        markup.add(sanoq_10,sanoq_50,parsing_treding)
        bot.send_message(message.chat.id,'............... ..............', reply_markup=markup)
    elif message.text == "Back <<<":
        my_func(message)
    elif message.text == "10":
        all_infor_in_crtpcoin(message.chat.id)
    elif message.text == "50":
        all_infor_in_crtpcoin_2(message.chat.id)   

    elif message.text == "Footbal news":
        markup = ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
        mach = KeyboardButton("Oyinlar royhati")
        tablitsa = KeyboardButton("Jadval")
        my_back = KeyboardButton("Back <<<")
        markup.add(mach,tablitsa,my_back)
        bot.send_message(message.chat.id,f' Salom {message.from_user.first_name} Botimizga hush kelibsiz!', reply_markup=markup)
    elif message.text == "Jadval":
        futboll_information_APL(message.chat.id)
    elif message.text == "Oyinlar royhati":
        all_infor_about_mach(message.chat.id)
        ############################# ##################################    
    elif message.text == 'Kalendar':    
        markup = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        kalendar_2022 = KeyboardButton('2022')
        kalendar_2023 = KeyboardButton('2023')
        kalendar_2024 = KeyboardButton('2024')
        kalendar_2025 = KeyboardButton('2025')
        kalendar_2026 = KeyboardButton('2026')
        ortga = KeyboardButton('Back <<<')
        markup.add(kalendar_2022,kalendar_2023,kalendar_2024,kalendar_2025,kalendar_2026,ortga)
        bot.send_message(message.chat.id,'Yilni tanlang!', reply_markup=markup)
    elif message.text == "2022":
        photos_2022(message.chat.id)
    elif message.text == "2023":
        photos_2023(message.chat.id)
    elif message.text == "2024":
        photos_2024(message.chat.id)    
    elif message.text == "2025":
        photos_2025(message.chat.id)
    elif message.text == "2026":
        photos_2026(message.chat.id)
    elif message.text == "Back <<<":
        my_func(message)   
        # photos(message.chat.id)
        # my_table(message.chat.id)
    else:
        if message.text == "Wikipedia":
            markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            basck_2 = KeyboardButton("Back <<<")
            markup.add(basck_2)
            bot.send_message(message.chat.id,'HOHLAGANIZNI QIDIRING', reply_markup=markup)
            if message.text == "Back <<<":
                my_func(message)
        elif message.text not in "Wikipedia":
            try:
                bot.send_message(message.chat.id, wikipedia.summary(message.text))
            except:
                print(f"""
            
██████╗░░█████╗░░██████╗████████╗██╗░░░██╗██████╗░██████╗░░█████╗░
██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██║░░░██║██╔══██╗██╔══██╗██╔══██╗
██║░░██║███████║╚█████╗░░░░██║░░░██║░░░██║██████╔╝██║░░██║███████║
██║░░██║██╔══██║░╚═══██╗░░░██║░░░██║░░░██║██╔══██╗██║░░██║██╔══██║
██████╔╝██║░░██║██████╔╝░░░██║░░░╚██████╔╝██║░░██║██████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝

██╗░░██╗░█████╗░████████╗░█████╗░██╗░░░░░██╗██╗░░██╗
██║░░██║██╔══██╗╚══██╔══╝██╔══██╗██║░░░░░██║██║░██╔╝
███████║███████║░░░██║░░░██║░░██║██║░░░░░██║█████═╝░
██╔══██║██╔══██║░░░██║░░░██║░░██║██║░░░░░██║██╔═██╗░
██║░░██║██║░░██║░░░██║░░░╚█████╔╝███████╗██║██║░╚██╗
╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚══════╝╚═╝╚═╝░░╚═╝
             """)    

# @bot.message_handler(content_types=['text'])
# def my_wikipade(message):
    

# print(ERROR)
bot.polling()