from PyQt6 import uic
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QMovie
import re
import os.path
import tkinter as tk
import sys
import keyboard
import pygame

#ЗАБЛОКИРОВАТЬ ПРОБЕЛ
keyboard.block_key('space')
#Узнает разрешение экрана
root = tk.Tk()
screen_height = root.winfo_screenheight() #Длина
screen_width = root.winfo_screenwidth()   #Ширина

#Создание папки для файлов пользователей здесь будут распологаться txt файлы каждого
#зарегестрированного пользователся
#Если папки users нету, то она сделается
papka = os.path.exists("users")
if papka == False:
    os.mkdir("users")

Form, Window = uic.loadUiType("input.ui")
Form2, Window2 = uic.loadUiType("game.ui")

app = QApplication([])

window = Window()
form = Form()
form.setupUi(window)
window.show()

window2 = Window2()
form2 = Form2()
form2.setupUi(window2)


#убираю лишнее
form.error1.setVisible(False)
form.error2.setVisible(False)
form.error3.setVisible(False)
form.error4.setVisible(False)
form2.accept_b.setVisible(False)
form2.back_b.setVisible(False)
form2.sound_l.setVisible(False)
form2.music_l.setVisible(False)
form2.blackback.setVisible(False)
form2.sound.setVisible(False)
form2.music.setVisible(False)
form2.move_red_l.setVisible(False)
form2.move_blue_l.setVisible(False)
form2.s_play.setVisible(False)
form2.two_play.setVisible(False)
form2.cross_l.setVisible(False)
form2.naught_l.setVisible(False)
form2.n_c_b.setVisible(False)
form2.field_l.setVisible(False)
form2.left_b.setVisible(False)
form2.left_b_2.setVisible(False)
form2.right_b.setVisible(False)
form2.right_b_2.setVisible(False)
form2.field_k.setVisible(False)
form2.rows_l.setVisible(False)
form2.rows_k.setVisible(False)
form2.accept2_b.setVisible(False)
form2.back2_b.setVisible(False)
form2.s_play_l.setVisible(False)
form2.two_play_l.setVisible(False)
form2.timer_l.setVisible(False)
form2.whiteback.setVisible(False)
form2.example_b.setVisible(False)
form2.move_b_te.setVisible(False)
form2.move_r_te.setVisible(False)
form2.win_red_l.setVisible(False)
form2.win_blue_l.setVisible(False)
form2.game_draw_l.setVisible(False)
form2.again_b.setVisible(False)



#МУЗЫКА
pygame.mixer.init()
sound_font = pygame.mixer.Sound('resources/font.mp3')
sound_click = pygame.mixer.Sound('resources/click.mp3')
sound_navod = pygame.mixer.Sound('resources/navod.mp3')
sound_game = pygame.mixer.Sound('resources/game.mp3')
file = open('settings.txt', 'r', -1, 'utf-8')
for music_volume in file:
    if re.search('music', music_volume):
        music_volume = music_volume.replace('music: ', '')
        music_volume = music_volume.replace('\n', '')
        music_volume = int(music_volume)
        sound_font.set_volume(music_volume / 100)
        sound_game.set_volume(music_volume / 100)
file = open('settings.txt', 'r', -1, 'utf-8')
for sound_volume in file:
    if re.search('sound', sound_volume):
        sound_volume = sound_volume.replace('sound: ', '')
        sound_volume = sound_volume.replace('\n', '')
        sound_volume = int(sound_volume)
        sound_click.set_volume(sound_volume / 100)
        sound_navod.set_volume(sound_volume / 100)


#-----------------ЗВУКИ ПРИ НАВЕДЕНИИ НА КНОПКУ-------------------
def enter(event):
    sound_navod.play()
form.sign_in.enterEvent = enter
form.sign_up.enterEvent = enter
form2.exit_b.enterEvent = enter
form2.new_game_b.enterEvent = enter
form2.continue_b.enterEvent = enter
form2.settings_b.enterEvent = enter
form2.accept_b.enterEvent = enter
form2.back_b.enterEvent = enter
form2.s_play.enterEvent = enter
form2.two_play.enterEvent = enter
form2.n_c_b.enterEvent = enter
form2.left_b.enterEvent = enter
form2.left_b_2.enterEvent = enter
form2.right_b.enterEvent = enter
form2.right_b_2.enterEvent = enter
form2.accept2_b.enterEvent = enter
form2.back2_b.enterEvent = enter



def m_x(form):
    x = int(form.x())
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()  # Ширина
    start_width = 800
    if x == 0:
        x1 = 0
    else:
        mnozh = x
        while start_width % mnozh != 0 or x % mnozh != 0:
            mnozh -= 1
        p1 = start_width / mnozh
        p2 = x / mnozh
        p11 = screen_width / p1
        x1 = p11 * p2
    return int(x1)

def m_y(form):
    y = int(form.y())
    if y < 0:
        y = 0
    root = tk.Tk()
    screen_height = root.winfo_screenheight()  # Высота
    start_height = 450
    if y == 0:
        y1 = 0
    else:
        mnozh = y
        while start_height % mnozh != 0 or y % mnozh != 0:
            mnozh -= 1
        p1 = start_height / mnozh
        p2 = y / mnozh
        p11 = screen_height / p1
        y1 = p11 * p2
    return int(y1)

def m_w(form):
    w = int(form.width())
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()  # Ширина
    start_width = 800
    mnozh = w
    while start_width % mnozh != 0 or w % mnozh != 0:
        mnozh -= 1
    p1 = start_width / mnozh
    p2 = w / mnozh
    p11 = screen_width / p1
    w1 = p11 * p2
    return int(w1)

def m_h(form):
    h = int(form.height())
    root = tk.Tk()
    screen_height = root.winfo_screenheight()  # Высота
    start_height = 450
    mnozh = h
    while start_height % mnozh != 0 or h % mnozh != 0:
        mnozh -= 1
    p1 = start_height / mnozh
    p2 = h / mnozh
    p11 = screen_height / p1
    h1 = p11 * p2
    return int(h1)


#__________ФОРМА1_______________________________________


#----------------------РЕГИСТРАЦИЯ------------------------
def rreg():
    sound_click.play()
    #Скрываю лишнее
    form.error1.setVisible(False)
    form.error2.setVisible(False)
    form.error3.setVisible(False)
    form.error4.setVisible(False)
    #Использование только букв и цифр в имени
    bukvi = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    #62 это кол-во символов которые можно использовать
    bukvi_kol = 62
    #задаю значения имени и паролю
    name = form.login_le.text()
    parl = form.password_le.text()
    #тут делаю так, чтобы в имени можно было использовать буквы и цифры
    namei = len(name)
    a = 0
    for i in range(len(bukvi)):
        for j in range(len(name)):
            if bukvi[i] != name[j]:
                a += 1
    if ((bukvi_kol * namei) - a) == namei:
        a = 0
    else:
        a = 1
        form.error1.setVisible(True)
        form.error3.setVisible(False)

    #Длина имени и пароля от 4 до 16 символов
    if (len(name) < 4) or (len(name) > 14) or (len(parl) < 4) or (len(parl) > 14):
        form.error4.setVisible(True)
        form.error2.setVisible(False)
    if (len(name) > 3) and (len(name) < 15) and (len(parl) > 3) and (len(parl) < 15) and (a == 0):
        form.error4.setVisible(False)
        #запись данных в файл пользовотелей, тут будет имя пользователя и зашифрованный пароль
        file = open('dan.txt', 'r+', -1, 'utf-8')
        #тут проверяю мб пользователь с таким именем уже есть
        nas = 0
        for line in file:
            if re.search(sha1(name), line):
                form.error3.setVisible(True)
                form.error1.setVisible(False)
                nas = 1
        #тут вписываются данные пользователся
        if nas == 0:
            file.write('\n')
            file.write(sha1(name))
            file.write(' : ')
            file.write(sha1(parl))
        file.close()
        #создание личного файла пользователя, тут будет его текст
        user = r"users\Q.txt"
        user = user.replace('Q', sha1(name))
        my_file = open(user, "w")
        my_file.close()
        window2.showFullScreen()
        sound_font.play(-1)
        global name_p
        name_p = name
        window.hide()
 #активация кнопки регистрации
form.sign_up.clicked.connect(rreg)

#----------------------АВТОРИЗАЦИЯ------------------------
def avt():
    sound_click.play()
    form.error1.setVisible(False) #опять скрываю лишнее
    form.error2.setVisible(False)
    form.error3.setVisible(False)
    form.error4.setVisible(False)
    name = form.login_le.text()
    parl = form.password_le.text()
    #Проверка регистрации пользователя
    namei = len(name)
    po = 0
    file = open('dan.txt', 'r+', -1, 'utf-8') #тут проверка либо неверное имя либо пароль либо вообще не зарегистрирован
    for line in file:
        if re.search(sha1(name), line): #если нашел имя, то проверяю пароль
            linp = line
            lini = ''
            for i in range(len(linp)):
                if i >= 43:
                    lini = lini + linp[i]
            lini = lini.replace('\n', '')
            l = sha1(parl)
            if lini == l: #тут если пароль верный
                window2.showFullScreen()
                sound_font.play(-1)
                global name_p
                name_p = name
                window.hide()
            else:
                form.error2.setVisible(True) #опа пароль не совпал ты не зайдешь хехе)
                form.error4.setVisible(False)
                po = po + 0
        elif po == 0:
            form.error2.setVisible(True)
            form.error4.setVisible(False)
     #тут проверяю длинну имя и пароля
    if (len(name) < 4) or (len(name) > 14) or (len(parl) < 4) or (len(parl) > 14):
        form.error4.setVisible(True)
        form.error2.setVisible(False)
        #а тут проверяю использованные символы в имени
    bukvi = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    bukvi_kol = 62
    a = 0
    for i in range(len(bukvi)):
        for j in range(len(name)):
            if bukvi[i] != name[j]:
                a += 1
    if ((bukvi_kol * namei) - a) == namei:
        a = 0
    else:
        a = 1
        form.error1.setVisible(True)
        form.error3.setVisible(False)
form.sign_in.clicked.connect(avt)


#_______________________________________ФОРМА2_______________________________________________________________________

form2.s_play.setChecked(True)
global game_mode
game_mode = 1
figure = 1
kol = 15
row = 5
global x_e
x_e = m_x(form2.example_b)
global y_e
y_e = m_y(form2.example_b)
global mov
mov = 1
global rowq
movv = None
hod = None
ard = None
gm = None
#-------------ВЫХОД---------------------
def exit1():
    sound_click.play()
    window2.hide()
    sound_font.stop()
    sys.exit()
form2.exit_b.clicked.connect(exit1)

#---------------НАСТРОЙКИ-----------------
def setting():
    sound_click.play()
    form2.exit_b.setVisible(False)
    form2.new_game_b.setVisible(False)
    form2.continue_b.setVisible(False)
    form2.settings_b.setVisible(False)
    form2.accept_b.setVisible(True)
    form2.sound_l.setVisible(True)
    form2.music_l.setVisible(True)
    form2.sound.setVisible(True)
    form2.music.setVisible(True)
    file = open('settings.txt', 'r', -1, 'utf-8')
    for line in file:
        if re.search('sound', line):
            line = line.replace('sound: ', '')
            line = line.replace('\n', '')
            line = int(line)
            form2.sound.setSliderPosition(int(line))
    file = open('settings.txt', 'r', -1, 'utf-8')
    for linea in file:
        if re.search('music', linea):
            linea = linea.replace('music: ', '')
            linea = linea.replace('\n', '')
            linea = int(linea)
            form2.music.setSliderPosition(int(linea))
form2.settings_b.clicked.connect(setting)


#----------------ПРИНЯТЬ НАСТРОЙКИ-------------------
def acc_set():
    sound_click.play()
    form2.exit_b.setVisible(True)
    form2.new_game_b.setVisible(True)
    form2.continue_b.setVisible(True)
    form2.settings_b.setVisible(True)
    form2.accept_b.setVisible(False)
    form2.sound_l.setVisible(False)
    form2.music_l.setVisible(False)
    form2.sound.setVisible(False)
    form2.music.setVisible(False)
    sound = str(form2.sound.value())
    music = str(form2.music.value())
    file = open('settings.txt', 'w', -1, 'utf-8')
    file.write('settings:\n')
    file.write('sound: ' + sound + '\n')
    file.write('music: ' + music + '\n')
    sound_font.set_volume(int(music) / 100)
    sound_game.set_volume(int(music) / 100)
    sound_click.set_volume(int(sound) / 100)
    sound_navod.set_volume(int(sound) / 100)
form2.accept_b.clicked.connect(acc_set)


#НОВАЯ ИГРА
def ng():
    sound_click.play()

    form2.exit_b.setVisible(False)
    form2.new_game_b.setVisible(False)
    form2.continue_b.setVisible(False)
    form2.settings_b.setVisible(False)


    form2.s_play.setVisible(True)
    form2.two_play.setVisible(True)
    form2.cross_l.setVisible(True)
    form2.naught_l.setVisible(False)
    form2.n_c_b.setVisible(True)
    form2.field_l.setVisible(True)
    form2.left_b.setVisible(True)
    form2.left_b_2.setVisible(True)
    form2.right_b.setVisible(True)
    form2.right_b_2.setVisible(True)
    form2.field_k.setVisible(True)
    form2.rows_l.setVisible(True)
    form2.rows_k.setVisible(True)
    form2.accept2_b.setVisible(True)
    form2.back2_b.setVisible(True)
    form2.s_play_l.setVisible(True)
    form2.two_play_l.setVisible(True)

    if form2.n_c_b.text() == "CROSS":
        form2.cross_l.setVisible(True)
        form2.naught_l.setVisible(False)
    else:
        form2.cross_l.setVisible(False)
        form2.naught_l.setVisible(True)

form2.new_game_b.clicked.connect(ng)

#КОНОПКА ОДИНОЧНОГО РЕЖИМА
def s_p():
    sound_click.play()
    global game_mode
    game_mode = 1
    form2.s_play.setChecked(True)
    form2.two_play.setChecked(False)
form2.s_play.clicked.connect(s_p)


def t_p():
    sound_click.play()
    global game_mode
    game_mode = 2
    form2.two_play.setChecked(True)
    form2.s_play.setChecked(False)
form2.two_play.clicked.connect(t_p)


def n_c_b():
    sound_click.play()
    global figure
    if figure == 1:
        form2.cross_l.setVisible(False)
        form2.naught_l.setVisible(True)
        figure = 0
        form2.n_c_b.setText("NAUGHT")
    elif figure == 0:
        form2.naught_l.setVisible(False)
        form2.cross_l.setVisible(True)
        figure = 1
        form2.n_c_b.setText("CROSS")
form2.n_c_b.clicked.connect(n_c_b)

def l_b():
    sound_click.play()
    kol = int(form2.field_k.text())
    if kol == 3:
        kol = 15
        form2.field_k.setText(str(kol))
    else:
        kol -= 1
        form2.field_k.setText(str(kol))

    if (kol == 4) and (int(form2.rows_k.text()) > 4):
        form2.rows_k.setText(str(kol))

    if (kol == 3) and (int(form2.rows_k.text()) > 3):
        form2.rows_k.setText(str(kol))

    if (kol > 3) and (int(form2.rows_k.text()) == 3):
        form2.rows_k.setText('4')
form2.left_b.clicked.connect(l_b)


def r_b():
    sound_click.play()
    kol = int(form2.field_k.text())
    if kol == 15:
        kol = 3
        form2.field_k.setText(str(kol))
    else:
        kol += 1
        form2.field_k.setText(str(kol))

    if (kol == 4) and (int(form2.rows_k.text()) > 4):
        form2.rows_k.setText(str(kol))

    if (kol == 3) and (int(form2.rows_k.text()) > 3):
        form2.rows_k.setText(str(kol))

    if (kol > 3) and (int(form2.rows_k.text()) == 3):
        form2.rows_k.setText('4')

form2.right_b.clicked.connect(r_b)


def l_b_2():
    sound_click.play()
    row = int(form2.rows_k.text())
    if row == 3:
        row = 5
        form2.rows_k.setText(str(row))
    else:
        row -= 1
        form2.rows_k.setText(str(row))


    if (row == 4) and (int(form2.field_k.text()) < 4):
        form2.field_k.setText(str(row))

    if (row == 5) and (int(form2.field_k.text()) < 5):
        form2.field_k.setText(str(row))

    if row == 3:
        form2.field_k.setText(str(row))
form2.left_b_2.clicked.connect(l_b_2)


def r_b_2():
    sound_click.play()
    row = int(form2.rows_k.text())
    if row == 5:
        row = 3
        form2.rows_k.setText(str(row))
    else:
        row += 1
        form2.rows_k.setText(str(row))

    if (row == 4) and (int(form2.field_k.text()) < 4):
        form2.field_k.setText(str(row))

    if (row == 5) and (int(form2.field_k.text()) < 5):
        form2.field_k.setText(str(row))

    if row == 3:
        form2.field_k.setText(str(row))
form2.right_b_2.clicked.connect(r_b_2)


#Таймер
global sec
global minut
def sec_t():
    null = '0'
    global sec
    sec += 1
    global minut
    if sec < 10:
        if minut < 10:
            form2.timer_l.setText(null + str(minut) + ':' + null + str(sec))
        else:
            form2.timer_l.setText(str(minut) + ':' + null + str(sec))
    if sec > 9:
        if minut < 10:
            form2.timer_l.setText(null + str(minut) + ':' + str(sec))
        else:
            form2.timer_l.setText(str(minut) + ':' + str(sec))
    if sec == 59:
        minut += 1
        sec = -1
    if minut == 60:
        form2.timer.stop()

form2.timer = QTimer()
form2.timer.setInterval(1000)
form2.timer.timeout.connect(sec_t)

def acc_2():
    sound_click.play()
    form2.timer.start()
    sound_font.stop()
    sound_game.play()

    file = open('users/'+str(sha1(name_p))+'.txt', 'w', -1, 'utf-8')
    file.write('gamemode = '+str(game_mode)+'\nfigure = '+str(figure)+'\nfield = '+str(int(form2.field_k.text()))+'\n'
    'rows = '+str(int(form2.rows_k.text()))+'\nminutes = 0\nseconds = 0')
    file.close()
    global minut
    minut = 0
    global sec
    sec = 0
    global mov
    mov = 1


    form2.blackback.setVisible(True)
    form2.move_red_l.setVisible(True)
    form2.back_b.setVisible(True)
    form2.timer_l.setVisible(True)
    form2.whiteback.setVisible(True)
    form2.move_b_te.setVisible(True)
    form2.move_r_te.setVisible(True)
    form2.again_b.setVisible(True)
    form2.timer_l.setText('00:00')


    form2.s_play.setVisible(False)
    form2.s_play_l.setVisible(False)
    form2.two_play.setVisible(False)
    form2.two_play_l.setVisible(False)
    form2.cross_l.setVisible(False)
    form2.naught_l.setVisible(False)
    form2.n_c_b.setVisible(False)
    form2.left_b.setVisible(False)
    form2.left_b_2.setVisible(False)
    form2.right_b.setVisible(False)
    form2.right_b_2.setVisible(False)
    form2.field_k.setVisible(False)
    form2.field_l.setVisible(False)
    form2.rows_k.setVisible(False)
    form2.rows_l.setVisible(False)
    form2.back2_b.setVisible(False)
    form2.accept2_b.setVisible(False)

    file = open('users/'+str(sha1(name_p))+'.txt', 'r', -1, 'utf-8')
    for line in file:
        if re.search('field', line):
            field = line
            field = field.replace('field = ', '')
            field = field.replace('\n', '')
            field = int(field)
        if re.search('rows', line):
            rows = line
            rows = rows.replace('rows = ', '')
            rows = rows.replace('\n', '')
            rows = int(rows)
    global arr_blue
    arr_blue = []
    global arr_red
    arr_red = []

    glav(field)

form2.accept2_b.clicked.connect(acc_2)












#---------------------ИГРА----------------------


def glav(field):
    global rowq
    file = open('users/' + str(sha1(name_p)) + '.txt', 'r', -1, 'utf-8')
    for line in file:
        if re.search('row', line):
            rowq = line
            rowq = rowq.replace('rows = ', '')
            rowq = rowq.replace('\n', '')
            rowq = int(rowq)

    global gm
    file = open('users/' + str(sha1(name_p)) + '.txt', 'r', -1, 'utf-8')
    for line in file:
        if re.search('gamemode', line):
            gm = line
            gm = gm.replace('gamemode = ', '')
            gm = gm.replace('\n', '')
            gm = int(gm)




    # ------------------------СОЗДАНИЕ ПОЛЯ-----------------
    # МАТРИЦЫ
    arr = []
    arr_line = ['1`', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
    arr_column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    for i in range(field):
        arr.append([2] * field)
    global arr_2
    arr_2 = arr
    for i in range(len(arr_2)):
        for j in range(len(arr_2)):
            arr_2[i][j] = arr_column[j] + arr_line[i]

    # Кнопка экземпляр
    form2.example_b.setGeometry(x_e, y_e, int((int(form2.whiteback.width()) - 1) / field),
                                int((int(form2.whiteback.height()) - 1) / field))
    # Генерация поля
    for i in range(len(arr_2)):
        for j in range(len(arr_2)):
            globals()[arr_2[i][j]] = QtWidgets.QPushButton(form2.centralwidget)
            globals()[arr_2[i][j]].setGeometry(QtCore.QRect(int(x_e + int(form2.example_b.width() * (i))),
                                                            int(y_e + int(form2.example_b.width() * (j))),
                                                            int((int(form2.whiteback.width()) - 1) / field),
                                                            int((int(form2.whiteback.height()) - 1) / field)))
            globals()[arr_2[i][j]].setStyleSheet("QPushButton\n"
                                                 "{\n"
                                                 "border: 2px solid #ffffff;\n"
                                                 "\n"
                                                 "color: rgb(255, 255, 255);\n"
                                                 "}\n"
                                                 "QPushButton:hover\n"
                                                 "{\n"
                                                 "background-color: rgb(255, 255, 127);\n"
                                                 "}")
            globals()[arr_2[i][j]].setText("")
            globals()[arr_2[i][j]].setObjectName(arr_2[i][j])
            globals()[arr_2[i][j]].setCheckable(True)
            globals()[arr_2[i][j]].setVisible(True)
            globals()[arr_2[i][j]].enterEvent = enter
    #ПРОВЕРКА НА ЛИШНИЕ СТРОКИ
    check = 0
    file = open('users/'+str(sha1(name_p))+'.txt', 'r', -1, 'utf-8')
    for line in file:
        if re.search('red', line):
            check = check + 1
        else:
            check = check + 0
    if check == 0:
        file = open('users/' + str(sha1(name_p)) + '.txt', 'a', -1, 'utf-8')
        file.write('\nred = \n')
    check = 0
    file = open('users/' + str(sha1(name_p)) + '.txt', 'r', -1, 'utf-8')
    for line in file:
        if re.search('blue', line):
            check = check + 1
        else:
            check = check + 0
    if check == 0:
        file = open('users/' + str(sha1(name_p)) + '.txt', 'a', -1, 'utf-8')
        file.write('\nblue = \n')

    #Заменяет клетки с прошлой игры
    file = open('users/' + str(sha1(name_p)) + '.txt', 'r', -1, 'utf-8')
    for line in file:
        for i in range(len(arr_2)):
            for j in range(len(arr_2)):
                if (re.search('red =', line)) and (re.search(str(arr_2[i][j]), line)):
                    globals()[arr_2[i][j]].setStyleSheet("QPushButton\n"
                                                         "{\n"
                                                         "border: 2px solid #ffffff;\n"
                                                         "\n"
                                                         "border-image: url(resources/cross.png);\n"
                                                         "}\n")
                    globals()[arr_2[i][j]].setChecked(False)
                    globals()[arr_2[i][j]].setCheckable(False)
                    globals()[arr_2[i][j]].enterEvent = 0
    file = open('users/' + str(sha1(name_p)) + '.txt', 'r', -1, 'utf-8')
    for line in file:
        for i in range(len(arr_2)):
            for j in range(len(arr_2)):
                if (re.search('blue =', line)) and (re.search(str(arr_2[i][j]), line)):
                    globals()[arr_2[i][j]].setStyleSheet("QPushButton\n"
                                                         "{\n"
                                                         "border: 2px solid #ffffff;\n"
                                                         "\n"
                                                         "border-image: url(resources/naught.png);\n"
                                                         "}\n")
                    globals()[arr_2[i][j]].setChecked(False)
                    globals()[arr_2[i][j]].setCheckable(False)
                    globals()[arr_2[i][j]].enterEvent = 0

    file = open('users/' + str(sha1(name_p)) + '.txt', 'r', -1, 'utf-8')
    for line in file:
        if re.search('red =', line):
            red = line
            red = red.replace('red = ', '')
            red = red.replace('`', '')
            red = red.replace('\n', '')
        if re.search('blue =', line):
            blue = line
            blue = blue.replace('blue = ', '')
            blue = blue.replace('`', '')
            blue = blue.replace('\n', '')
    form2.move_b_te.setText(blue)
    form2.move_r_te.setText(red)




    #ЗАПОЛНЕНИЕ ВТОРОЙ МАТРИЦЫ
    global arria
    arria = []
    for i in range(field):
        arria.append([2] * field)
    for i in range(len(arr_2)):
        for j in range(len(arr_2)):
            if globals()[arr_2[i][j]].styleSheet() == ("QPushButton\n"
                                                         "{\n"
                                                         "border: 2px solid #ffffff;\n"
                                                         "\n"
                                                         "border-image: url(resources/naught.png);\n"
                                                         "}\n"):
                arria[j][i] = 0
            if globals()[arr_2[i][j]].styleSheet() == ("QPushButton\n"
                                                       "{\n"
                                                       "border: 2px solid #ffffff;\n"
                                                       "\n"
                                                       "border-image: url(resources/cross.png);\n"
                                                       "}\n"):
                arria[j][i] = 1




    # ПРОВЕРКА НА ПОБЕДУ
    def win():
        global arria
        global win_blue
        global win_red
        win_blue = 0
        win_red = 0
        r_w = str('1' * rowq)
        b_w = str('0' * rowq)

        # СТРОКИ
        arr = arria
        for i in range(len(arr)):
            ard = str(arr[i])
            ard = ard.replace('[', '')
            ard = ard.replace(']', '')
            ard = ard.replace(',', '')
            ard = ard.replace(' ', '')
            ard = ard.replace('\n', '')
            if re.search(r_w, ard):
                win_red = 1
            if re.search(b_w, ard):
                win_blue = 1
        # СТОЛБЦЫ
        arr = []
        for i in range(len(arria)):
            arr.append([0] * len(arria))
        for i in range(len(arria)):
            for j in range(len(arria)):
                arr[j][i] = arria[i][j]
        for i in range(len(arr)):
            ard = str(arr[i])
            ard = ard.replace('[', '')
            ard = ard.replace(']', '')
            ard = ard.replace(',', '')
            ard = ard.replace(' ', '')
            ard = ard.replace('\n', '')
            if re.search(r_w, ard):
                win_red = 1
            if re.search(b_w, ard):
                win_blue = 1
        # ДИАГОНАЛЬ СЛЕВА НАПРАВО
        arr = arria
        diagonals = [[] for i in range(len(arria) + len(arria) - 1)]
        for i in range(-(len(arria) - 1), len(arria)):
            for j in range(len(arria)):
                qq, col = j, i + j
                if 0 <= qq < len(arr) and 0 <= col < len(arr[0]):
                    diagonals[i + len(arr) - 1].append(arr[qq][col])
        arr = diagonals
        for i in range(len(arr)):
            ard = str(arr[i])
            ard = ard.replace('[', '')
            ard = ard.replace(']', '')
            ard = ard.replace(',', '')
            ard = ard.replace(' ', '')
            ard = ard.replace('\n', '')
            if re.search(r_w, ard):
                win_red = 1
            if re.search(b_w, ard):
                win_blue = 1
        # ДИАГОНАЛЬ СПРАВА НАЛЕВО
        arr = arria
        for i in range(len(arr)):
            for j in range(len(arr)):
                if j <= ((len(arria) / 2) - 1):
                    ard = arr[i][j]
                    arr[i][j] = arr[i][len(arria) - j - 1]
                    arr[i][len(arria) - j - 1] = ard
        diagonals = [[] for i in range(len(arria) + len(arria) - 1)]
        for i in range(-(len(arria) - 1), len(arria)):
            for j in range(len(arria)):
                qq, col = j, i + j
                if 0 <= qq < len(arr) and 0 <= col < len(arr[0]):
                    diagonals[i + len(arr) - 1].append(arr[qq][col])
        arr = diagonals
        for i in range(len(arr)):
            ard = str(arr[i])
            ard = ard.replace('[', '')
            ard = ard.replace(']', '')
            ard = ard.replace(',', '')
            ard = ard.replace(' ', '')
            ard = ard.replace('\n', '')
            if re.search(r_w, ard):
                win_red = 1
            if re.search(b_w, ard):
                win_blue = 1

        arr = arria
        for i in range(len(arr)):
            for j in range(len(arr)):
                if j <= ((len(arr) / 2) - 1):
                    ard = arr[i][j]
                    arr[i][j] = arr[i][len(arr) - j - 1]
                    arr[i][len(arr) - j - 1] = ard

        draw = 0
        for i in range(len(arria)):
            for j in range(len(arria)):
                if arria[i][j] == 2:
                    draw += 1

        if win_red == 1:
            for i in range(len(arr_2)):
                for j in range(len(arr_2)):
                    globals()[arr_2[i][j]].setChecked(False)
                    globals()[arr_2[i][j]].setCheckable(False)
                    globals()[arr_2[i][j]].enterEvent = 0
                    form2.timer.stop()
                    form2.win_red_l.setVisible(True)
                    form2.blackback.setMovie(form2.wr_fon)
                    form2.wr_fon.start()
        if win_blue == 1:
            for i in range(len(arr_2)):
                for j in range(len(arr_2)):
                    globals()[arr_2[i][j]].setChecked(False)
                    globals()[arr_2[i][j]].setCheckable(False)
                    globals()[arr_2[i][j]].enterEvent = 0
                    form2.timer.stop()
                    form2.win_blue_l.setVisible(True)
                    form2.blackback.setMovie(form2.wb_fon)
                    form2.wb_fon.start()
        if (draw == 0) and (win_red == 0) and (win_blue == 0):
            form2.timer.stop()
            form2.game_draw_l.setVisible(True)
    win()


    #ЧЕЙ ХОД СЛЕДУЩИЙ
    global mov
    if mov == 1:
        form2.move_red_l.setVisible(True)
        form2.move_blue_l.setVisible(False)
    else:
        form2.move_red_l.setVisible(False)
        form2.move_blue_l.setVisible(True)




    #ИИ
    def bot():
        cr = rowq
        global matr
        matr = []
        for i in range(len(arria)):
            matr.append([3] * len(arria))
        for i in range(len(arria)):
            for j in range(len(arria)):
                matr[i][j] = arria[i][j]
        first = 0
        global movv
        movv = 0
        global hod
        global ard

        # Первый ход
        for i in range(len(matr)):
            for j in range(len(matr)):
                if matr[i][j] == fig:
                    first = 1
                else:
                    first = first + 0
        if first == 0:
            if matr[int(len(matr) / 2)][int(len(matr) / 2)] == 2:
                matr[int(len(matr) / 2)][int(len(matr) / 2)] = fig
                movv = 1
            else:
                matr[int(len(matr) / 2) + 1][int(len(matr) / 2) + 1] = fig
                movv = 1
        # НЕОБХОДИМЫЕ КОМБИНАЦИИ
        if cr == 3:
            win_move = ['xx2', 'x2x', '2xx']
            protection_move = ['oo2', 'o2o', '2oo']
            attack1_move = ['x22', '2x2', '22x']
            attack2_move = ['222']
            for i in range(len(win_move)):
                ch = str(win_move[i])
                if fig == 1:
                    ch = ch.replace('x', '1')
                    win_move[i] = ch
                else:
                    ch = ch.replace('x', '0')
                    win_move[i] = ch
            for i in range(len(protection_move)):
                ch = str(protection_move[i])
                if fig == 1:
                    ch = ch.replace('o', '0')
                    protection_move[i] = ch
                else:
                    ch = ch.replace('o', '1')
                    protection_move[i] = ch
            for i in range(len(attack1_move)):
                ch = str(attack1_move[i])
                if fig == 1:
                    ch = ch.replace('x', '1')
                    attack1_move[i] = ch
                else:
                    ch = ch.replace('x', '0')
                    attack1_move[i] = ch
        if cr == 4:
            win_move = ['xxx2', 'xx2x', 'x2xx', '2xxx']
            protection_move = ['ooo2', 'oo2o', 'o2oo', '2ooo']
            protection2_move = ['2oo22', '2o2o2', '22oo2']
            attack1_move = ['2x2x', '2xx2', 'x22x', 'x2x2', 'xx22', '22xx']
            attack2_move = ['x222', '2x22', '22x2', '222x']
            attack3_move = ['2222']
            for i in range(len(win_move)):
                ch = str(win_move[i])
                if fig == 1:
                    ch = ch.replace('x', '1')
                    win_move[i] = ch
                else:
                    ch = ch.replace('x', '0')
                    win_move[i] = ch
            for i in range(len(protection_move)):
                ch = str(protection_move[i])
                if fig == 1:
                    ch = ch.replace('o', '0')
                    protection_move[i] = ch
                else:
                    ch = ch.replace('o', '1')
                    protection_move[i] = ch
            for i in range(len(protection2_move)):
                ch = str(protection2_move[i])
                if fig == 1:
                    ch = ch.replace('o', '0')
                    protection2_move[i] = ch
                else:
                    ch = ch.replace('o', '1')
                    protection2_move[i] = ch
            for i in range(len(attack1_move)):
                ch = str(attack1_move[i])
                if fig == 1:
                    ch = ch.replace('x', '1')
                    attack1_move[i] = ch
                else:
                    ch = ch.replace('x', '0')
                    attack1_move[i] = ch
            for i in range(len(attack2_move)):
                ch = str(attack2_move[i])
                if fig == 1:
                    ch = ch.replace('x', '1')
                    attack2_move[i] = ch
                else:
                    ch = ch.replace('x', '0')
                    attack2_move[i] = ch
        if cr == 5:
            win_move = ['xxxx2', 'xxx2x', 'xx2xx', 'x2xxx', '2xxxx']
            protection_move = ['oooo2', 'ooo2o', 'oo2oo', 'o2ooo', '2oooo']
            protection2_move = ['2ooo22', '2oo2o2', '2o2oo2', '22ooo2']
            attack1_move = ['xxx22', 'xx2x2', 'xx22x', 'x2xx2', 'x2x2x', '2xxx2', '2xx2x', '2x2xx', '22xxx', 'x22xx']
            attack2_move = ['222xx', '22x2x', '22xx2', '2x22x', '2x2x2', '2xx22', 'x222x', 'x22x2', 'x2x22', 'xx222']
            attack3_move = ['2222x', '222x2', '22x22', '2x222', 'x2222']
            attack4_move = ['22222']
            for i in range(len(win_move)):
                ch = str(win_move[i])
                if fig == 1:
                    ch = ch.replace('x', '1')
                    win_move[i] = ch
                else:
                    ch = ch.replace('x', '0')
                    win_move[i] = ch
            for i in range(len(protection_move)):
                ch = str(protection_move[i])
                if fig == 1:
                    ch = ch.replace('o', '0')
                    protection_move[i] = ch
                else:
                    ch = ch.replace('o', '1')
                    protection_move[i] = ch
            for i in range(len(protection2_move)):
                ch = str(protection2_move[i])
                if fig == 1:
                    ch = ch.replace('o', '0')
                    protection2_move[i] = ch
                else:
                    ch = ch.replace('o', '1')
                    protection2_move[i] = ch
            for i in range(len(attack1_move)):
                ch = str(attack1_move[i])
                if fig == 1:
                    ch = ch.replace('x', '1')
                    attack1_move[i] = ch
                else:
                    ch = ch.replace('x', '0')
                    attack1_move[i] = ch
            for i in range(len(attack2_move)):
                ch = str(attack2_move[i])
                if fig == 1:
                    ch = ch.replace('x', '1')
                    attack2_move[i] = ch
                else:
                    ch = ch.replace('x', '0')
                    attack2_move[i] = ch
            for i in range(len(attack3_move)):
                ch = str(attack3_move[i])
                if fig == 1:
                    ch = ch.replace('x', '1')
                    attack3_move[i] = ch
                else:
                    ch = ch.replace('x', '0')
                    attack3_move[i] = ch

        # РАСЧЕТЫ ХОДА
        def win_m():
            global ard, hod, movv
            if movv == 0:
                for S in range(len(win_move)):
                    if (re.search(win_move[S], ard)) and (movv == 0):
                        hod = win_move[S]
                        hod = hod.replace('2', str(fig))
                        ard = ard.replace(win_move[S], hod)
                        are = []
                        for u in range(len(ard)):
                            are.append(int(ard[u]))
                        matr[i] = are
                        movv = 1

        def protection_m():
            global ard, hod, movv
            if fig == 1:
                figv = '0'
            else:
                figv = '1'
            if movv == 0:
                for S in range(len(protection_move)):
                    if (re.search(protection_move[S], ard)) and (movv == 0):
                        hod = protection_move[S]
                        hod = hod.replace('2', str(fig), 1)
                        if (protection_move[S] == ('2' + str(figv) + str(figv) + '22')) and (cr == 4) and (movv == 0):
                            hod = '2' + str(figv) + str(figv) + str(fig) + '2'
                            movv = 1
                        if (protection_move[S] == ('2' + str(figv) + '2' + str(figv) + '2')) and (cr == 4) and (movv == 0):
                            hod = '2' + str(figv) + str(fig) + str(figv) + '2'
                            movv = 1
                        if (protection_move[S] == ('22' + str(figv) + str(figv) + '2')) and (cr == 4) and (movv == 0):
                            hod = '2' + str(fig) + str(figv) + str(figv) + '2'
                            movv = 1
                        if (protection_move[S] == ('2' + str(figv) + str(figv) + str(figv) + '22')) and (cr == 5) and (movv == 0):
                            hod = '2' + str(figv) + str(figv) + str(figv) + str(fig) + '2'
                            movv = 1
                        if (protection_move[S] == ('2' + str(figv) + str(figv) + '2' + str(figv) + '2')) and (cr == 5) and (movv == 0):
                            hod = '2' + str(figv) + str(figv) + str(fig) + str(figv) + '2'
                            movv = 1
                        if (protection_move[S] == ('2' + str(figv) + '2' + str(figv) + str(figv) + '2')) and (cr == 5) and (movv == 0):
                            hod = '2' + str(figv) + str(fig) + str(figv) + str(figv) + '2'
                            movv = 1
                        if (protection_move[S] == ('22' + str(figv) + str(figv) + str(figv) + '2')) and (cr == 5) and (movv == 0):
                            hod = '2' + str(fig) + str(figv) + str(figv) + str(figv) + '2'
                            movv = 1
                        ard = ard.replace(protection_move[S], hod)
                        are = []
                        for u in range(len(ard)):
                            are.append(int(ard[u]))
                        matr[i] = are
                        movv = 1

        def protection2_m():
            global ard, hod, movv
            if fig == 1:
                figv = '0'
            else:
                figv = '1'
            if movv == 0:
                for S in range(len(protection2_move)):
                    if (re.search(protection2_move[S], ard)) and (movv == 0):
                        hod = protection2_move[S]
                        if (protection2_move[S] == ('2' + figv + figv + '22')) and (cr == 4) and (movv == 0):
                            hod = '2' + figv + figv + str(fig) + '2'
                            movv = 1
                        if (protection2_move[S] == ('2' + figv + '2' + figv + '2')) and (cr == 4)  and (movv == 0):
                            hod = '2' + figv + str(fig) + figv + '2'
                            movv = 1
                        if (protection2_move[S] == ('22' + str(figv) + str(figv) + '2')) and (cr == 4)  and (movv == 0):
                            hod = '2' + str(fig) + str(figv) + str(figv) + '2'
                            movv = 1
                        if (protection2_move[S] == ('2' + str(figv) + str(figv) + str(figv) + '22')) and (cr == 5) and (movv == 0):
                            hod = '2' + str(figv) + str(figv) + str(figv) + str(fig) + '2'
                            movv = 1
                        if (protection2_move[S] == ('2' + str(figv) + str(figv) + '2' + str(figv) + '2')) and (cr == 5) and (movv == 0):
                            hod = '2' + str(figv) + str(figv) + str(fig) + str(figv) + '2'
                            movv = 1
                        if (protection2_move[S] == ('2' + str(figv) + '2' + str(figv) + str(figv) + '2')) and (cr == 5) and (movv == 0):
                            hod = '2' + str(figv) + str(fig) + str(figv) + str(figv) + '2'
                            movv = 1
                        if (protection2_move[S] == ('22' + str(figv) + str(figv) + str(figv) + '2')) and (cr == 5) and (movv == 0):
                            hod = '2' + str(fig) + str(figv) + str(figv) + str(figv) + '2'
                            movv = 1
                        ard = ard.replace(protection2_move[S], hod)
                        are = []
                        for u in range(len(ard)):
                            are.append(int(ard[u]))
                        matr[i] = are
                        movv = 1

        def attack1_m():
            global ard, hod, movv
            if movv == 0:
                for S in range(len(attack1_move)):
                    if (re.search(attack1_move[S], ard)) and (movv == 0):
                        hod = attack1_move[S]
                        hod = hod.replace('2', str(fig), 1)
                        if (attack1_move[S] == ('22' + str(fig))) and (cr == 3) and (movv == 0):
                            hod = str(fig) + '2' + str(fig)
                            movv = 1
                        if (attack1_move[S] == ('22' + str(fig) + str(fig))) and (cr == 4) and (movv == 0):
                            hod = '2' + str(fig) + str(fig) + str(fig)
                            movv = 1
                        if (attack1_move[S] == ('2' + str(fig) + str(fig) + '2' + str(fig))) and (cr == 5) and (movv == 0):
                            hod = '2' + str(fig) + str(fig) + str(fig) + str(fig)
                            movv = 1
                        if (attack1_move[S] == ('2' + str(fig) + '2' + str(fig) + str(fig))) and (cr == 5) and (movv == 0):
                            hod = '2' + str(fig) + str(fig) + str(fig) + str(fig)
                            movv = 1
                        if (attack1_move[S] == ('22' + str(fig) + str(fig) + str(fig))) and (cr == 5) and (movv == 0):
                            hod = '2' + str(fig) + str(fig) + str(fig) + str(fig)
                            movv = 1
                        if (attack1_move[S] == (str(fig) + '22' + str(fig) + str(fig))) and (cr == 5) and (movv == 0):
                            hod = str(fig) + '2' + str(fig) + str(fig) + str(fig)
                            movv = 1
                        ard = ard.replace(attack1_move[S], hod)
                        are = []
                        for u in range(len(ard)):
                            are.append(int(ard[u]))
                        matr[i] = are
                        movv = 1

        def attack2_m():
            global ard, hod, movv
            if movv == 0:
                for S in range(len(attack2_move)):
                    if (re.search(attack2_move[S], ard)) and (movv == 0):
                        hod = attack2_move[S]
                        hod = hod.replace('2', str(fig), 1)
                        if (attack2_move[S] == ('22' + str(fig) + '2')) and (cr == 4) and (movv == 0):
                            hod = '2' + str(fig) + str(fig) + '2'
                            movv = 1
                        if (attack2_move[S] == ('222' + str(fig))) and (cr == 4) and (movv == 0):
                            hod = '22' + str(fig) + str(fig)
                            movv = 1
                        if (attack2_move[S] == ('222' + str(fig) + str(fig))) and (cr == 5) and (movv == 0):
                            hod = '22' + str(fig) + str(fig) + str(fig)
                            movv = 1
                        if (attack2_move[S] == ('22' + str(fig) + '2' + str(fig))) and (cr == 5) and (movv == 0):
                            hod = '22' + str(fig) + str(fig) + str(fig)
                            movv = 1
                        if (attack2_move[S] == ('22' + str(fig) + str(fig) + '2')) and (cr == 5) and (movv == 0):
                            hod = '2' + str(fig) + str(fig) + str(fig) + '2'
                            movv = 1
                        if (attack2_move[S] == ('2' + str(fig) + '2' + str(fig) + '2')) and (cr == 5) and (movv == 0):
                            hod = '2' + str(fig) + str(fig) + str(fig) + '2'
                            movv = 1
                        if (attack2_move[S] == ('2' + str(fig) + str(fig) + '22')) and (cr == 5) and (movv == 0):
                            hod = '2' + str(fig) + str(fig) + str(fig) + '2'
                            movv = 1
                        ard = ard.replace(attack2_move[S], hod)
                        are = []
                        for u in range(len(ard)):
                            are.append(int(ard[u]))
                        matr[i] = are
                        movv = 1

        def attack3_m():
            global ard, hod, movv
            if movv == 0:
                for S in range(len(attack3_move)):
                    if (re.search(attack3_move[S], ard)) and (movv == 0):
                        hod = attack3_move[S]
                        hod = hod.replace('2', str(fig), 1)
                        if (attack2_move[S] == ('222' + str(fig) + '2')) and (cr == 5) and (movv == 0):
                            hod = '22' + str(fig) + str(fig) + '2'
                            movv = 1
                        if (attack2_move[S] == ('22' + str(fig) + '22')) and (cr == 5) and (movv == 0):
                            hod = '2' + str(fig) + str(fig) + '22'
                            movv = 1
                        if (attack2_move[S] == ('2' + str(fig) + '222')) and (cr == 5) and (movv == 0):
                            hod = '2' + str(fig) + str(fig) + '22'
                            movv = 1
                        if (attack2_move[S] == (str(fig) + '2222')) and (cr == 5) and (movv == 0):
                            hod = str(fig) + str(fig) + '222'
                            movv = 1
                        if (attack2_move[S] == ('2222' + str(fig))) and (cr == 5) and (movv == 0):
                            hod = '222' + str(fig) + str(fig)
                            movv = 1
                        ard = ard.replace(attack3_move[S], hod)
                        are = []
                        for u in range(len(ard)):
                            are.append(int(ard[u]))
                        matr[i] = are
                        movv = 1

        def attack4_m():
            global ard, hod, movv
            if movv == 0:
                for S in range(len(attack4_move)):
                    if (re.search(attack4_move[S], ard)) and (movv == 0):
                        hod = attack4_move[S]
                        hod = hod.replace('2', str(fig), 1)
                        ard = ard.replace(attack4_move[S], hod)
                        are = []
                        for u in range(len(ard)):
                            are.append(int(ard[u]))
                        matr[i] = are
                        movv = 1

        # РЕАЛИЗАЦИЯ ХОДА
        cic = True
        cicc = 0
        while (cic == True):
            # СТРОКИ
            if movv == 0:
                for i in range(len(matr)):
                    ard = str(matr[i])
                    ard = ard.replace('[', '')
                    ard = ard.replace(']', '')
                    ard = ard.replace(',', '')
                    ard = ard.replace(' ', '')
                    ard = ard.replace('\n', '')
                    if cicc == 0:
                        win_m()
                    if cicc == 1:
                        protection_m()
                    if (cicc == 2) and (cr > 3):
                        protection2_m()
                    if cicc == 3:
                        attack1_m()
                    if cicc == 4:
                        attack2_m()
                    if (cicc == 5) and (cr > 3):
                        attack3_m()
                    if (cicc == 6) and (cr > 4):
                        attack4_m()
                if movv == 1:
                    cic = False

            # СТОЛБЦЫ
            if movv == 0:
                matr = []
                for i in range(len(arria)):
                    matr.append([0] * len(arria))
                for i in range(len(arria)):
                    for j in range(len(arria)):
                        matr[j][i] = arria[i][j]
                for i in range(len(matr)):
                    ard = str(matr[i])
                    ard = ard.replace('[', '')
                    ard = ard.replace(']', '')
                    ard = ard.replace(',', '')
                    ard = ard.replace(' ', '')
                    ard = ard.replace('\n', '')
                    if cicc == 0:
                        win_m()
                    if cicc == 1:
                        protection_m()
                    if (cicc == 2) and (cr > 3):
                        protection2_m()
                    if cicc == 3:
                        attack1_m()
                    if cicc == 4:
                        attack2_m()
                    if (cicc == 5) and (cr > 3):
                        attack3_m()
                    if (cicc == 6) and (cr > 4):
                        attack4_m()
                matr2 = []
                for i in range(len(matr)):
                    matr2.append([0] * len(matr))
                for i in range(len(matr)):
                    for j in range(len(matr)):
                        matr2[j][i] = matr[i][j]
                matr = matr2
                if movv == 1:
                    cic = False

            # ДИАГОНАЛЬ СЛЕВА НАПРАВО
            if movv == 0:
                matr = []
                for i in range(len(arria)):
                    matr.append([3] * len(arria))
                for i in range(len(arria)):
                    for j in range(len(arria)):
                        matr[i][j] = arria[i][j]
                matr_2 = matr
                jg = 3
                diagonals = [[] for i in range(len(arria) + len(arria) - 1)]
                for i in range(-(len(arria) - 1), len(arria)):
                    for j in range(len(arria)):
                        rqq, col = j, i + j
                        if 0 <= rqq < len(matr) and 0 <= col < len(matr[0]):
                            diagonals[i + len(matr) - 1].append(matr[rqq][col])
                matr = diagonals
                for i in range(len(matr_2)):
                    for j in range(len(matr_2)):
                        matr_2[i][j] = jg
                        jg = jg + 1
                diagonals = [[] for i in range(len(arria) + len(arria) - 1)]
                for i in range(-(len(arria) - 1), len(arria)):
                    for j in range(len(arria)):
                        rqq, col = j, i + j
                        if 0 <= rqq < len(matr_2) and 0 <= col < len(matr_2[0]):
                            diagonals[i + len(matr_2) - 1].append(matr_2[rqq][col])
                matr_3 = diagonals
                for i in range(len(matr)):
                    ard = str(matr[i])
                    ard = ard.replace('[', '')
                    ard = ard.replace(']', '')
                    ard = ard.replace(',', '')
                    ard = ard.replace(' ', '')
                    ard = ard.replace('\n', '')
                    if cicc == 0:
                        win_m()
                    if cicc == 1:
                        protection_m()
                    if (cicc == 2) and (cr > 3):
                        protection2_m()
                    if cicc == 3:
                        attack1_m()
                    if cicc == 4:
                        attack2_m()
                    if (cicc == 5) and (cr > 3):
                        attack3_m()
                    if (cicc == 6) and (cr > 4):
                        attack4_m()

                for I in range(len(matr_3)):
                    matr_4 = matr_3[I]
                    matr_5 = matr[I]
                    for i in range(len(matr_2)):
                        for j in range(len(matr_2)):
                            for ii in range(len(matr_4)):
                                if matr_4[ii] == matr_2[i][j]:
                                    matr_2[i][j] = matr_5[ii]
                matr = matr_2
                if movv == 1:
                    cic = False

            # ДИАГОНАЛЬ СПРАВА НАЛЕВО
            if movv == 0:
                matr = []
                for i in range(len(arria)):
                    matr.append([3] * len(arria))
                for i in range(len(arria)):
                    for j in range(len(arria)):
                        matr[i][j] = arria[i][j]
                matr_2 = matr
                jg = 3
                for i in range(len(matr)):
                    for j in range(len(matr)):
                        if j <= ((len(matr) / 2) - 1):
                            ard = matr[i][j]
                            matr[i][j] = matr[i][len(matr) - j - 1]
                            matr[i][len(matr) - j - 1] = ard
                diagonals = [[] for i in range(len(arria) + len(arria) - 1)]
                for i in range(-(len(arria) - 1), len(arria)):
                    for j in range(len(arria)):
                        rqq, col = j, i + j
                        if 0 <= rqq < len(matr) and 0 <= col < len(matr[0]):
                            diagonals[i + len(matr) - 1].append(matr[rqq][col])
                matr = diagonals

                for i in range(len(matr_2)):
                    for j in range(len(matr_2)):
                        matr_2[i][j] = jg
                        jg = jg + 1
                for i in range(len(matr_2)):
                    for j in range(len(matr_2)):
                        if j <= ((len(matr_2) / 2) - 1):
                            ard = matr_2[i][j]
                            matr_2[i][j] = matr_2[i][len(matr_2) - j - 1]
                            matr_2[i][len(matr_2) - j - 1] = ard
                diagonals = [[] for i in range(len(arria) + len(arria) - 1)]
                for i in range(-(len(arria) - 1), len(arria)):
                    for j in range(len(arria)):
                        rqq, col = j, i + j
                        if 0 <= rqq < len(matr_2) and 0 <= col < len(matr_2[0]):
                            diagonals[i + len(matr_2) - 1].append(matr_2[rqq][col])
                matr_3 = diagonals

                for i in range(len(matr)):
                    ard = str(matr[i])
                    ard = ard.replace('[', '')
                    ard = ard.replace(']', '')
                    ard = ard.replace(',', '')
                    ard = ard.replace(' ', '')
                    ard = ard.replace('\n', '')
                    if cicc == 0:
                        win_m()
                    if cicc == 1:
                        protection_m()
                    if (cicc == 2) and (cr > 3):
                        protection2_m()
                    if cicc == 3:
                        attack1_m()
                    if cicc == 4:
                        attack2_m()
                    if (cicc == 5) and (cr > 3):
                        attack3_m()
                    if (cicc == 6) and (cr > 4):
                        attack4_m()

                for I in range(len(matr_3)):
                    matr_4 = matr_3[I]
                    matr_5 = matr[I]
                    for i in range(len(matr_2)):
                        for j in range(len(matr_2)):
                            for ii in range(len(matr_4)):
                                if matr_4[ii] == matr_2[i][j]:
                                    matr_2[i][j] = matr_5[ii]

                for i in range(len(matr_2)):
                    for j in range(len(matr_2)):
                        if j <= ((len(matr_2) / 2) - 1):
                            ard = matr_2[i][j]
                            matr_2[i][j] = matr_2[i][len(matr_2) - j - 1]
                            matr_2[i][len(matr_2) - j - 1] = ard
                matr = matr_2
                if movv == 1:
                    cic = False

            cicc = cicc + 1
            if cicc == 7:
                cic = False

        if (cic == False) and (movv == 0):
            cic = 0
            for i in range(len(matr)):
                for j in range(len(matr)):
                    if (matr[i][j] == 2) and (cic == 0):
                        matr[i][j] = fig
                        cic = 1

    # ХОД
    def move():
        global arria
        global fig
        global matr
        if figure == 1:
            fig = 0
        else:
            fig = 1
        for i in range(len(arr_2)):
            for j in range(len(arr_2)):
                if (globals()[arr_2[i][j]].isChecked() == True) and (globals()[arr_2[i][j]].isCheckable() == True):
                    sound_click.play()
                    global mov
                    if mov == 1:
                        globals()[arr_2[i][j]].setStyleSheet("QPushButton\n"
                                                                "{\n"
                                                                "border: 2px solid #ffffff;\n"
                                                                "\n"
                                                                "border-image: url(resources/cross.png);\n"
                                                                "}\n")
                        mov = 0
                        form2.move_red_l.setVisible(False)
                        form2.move_blue_l.setVisible(True)
                        arr_red.append(arr_2[i][j])

                        #ВЫВОД ХОДА
                        rep = arr_2[i][j]
                        rep = rep.replace('`', '')
                        if form2.move_r_te.toPlainText() == '':
                                form2.move_r_te.setText(rep)
                        else:
                            form2.move_r_te.setText(form2.move_r_te.toPlainText() + ', ' + rep)

                        file = open('users/' + str(sha1(name_p)) + '.txt', 'r', -1, 'utf-8')
                        for line in file:
                            if re.search('gamemode', line):
                                linp = str(line)
                            if re.search('figure', line):
                                linp = linp + str(line)
                            if re.search('field', line):
                                linp = linp + str(line)
                            if re.search('rows', line):
                                linp = linp + str(line)
                            if re.search('blue', line):
                                linp = linp + str(line)
                        file = open('users/' + str(sha1(name_p)) + '.txt', 'w', -1, 'utf-8')
                        file.write(linp + '\nred = ' + str(arr_red))
                        arria[j][i] = 1
                        if (gm == 1) and (figure == 1):
                            
                            fig = 0
                            
                            bot()
                            
                            for III in range(len(arr_2)):
                                for JJJ in range(len(arr_2)):
                                    if matr[JJJ][III] != arria[JJJ][III]:
                                        arria[JJJ][III] = matr[JJJ][III]
                                        if mov == 0:
                                            globals()[arr_2[III][JJJ]].setStyleSheet("QPushButton\n"
                                                                                 "{\n"
                                                                                 "border: 2px solid #ffffff;\n"
                                                                                 "\n"
                                                                                 "border-image: url(resources/naught.png);\n"
                                                                                 "}\n")
                                            form2.move_blue_l.setVisible(False)
                                            form2.move_red_l.setVisible(True)
                                            arr_blue.append(arr_2[III][JJJ])
                                            mov = 1

                                            # ВЫВОД ХОДА
                                            rep = arr_2[III][JJJ]
                                            rep = rep.replace('`', '')
                                            if form2.move_b_te.toPlainText() == '':
                                                form2.move_b_te.setText(rep)
                                            else:
                                                form2.move_b_te.setText(form2.move_b_te.toPlainText() + ', ' + rep)

                                            file = open('users/' + str(sha1(name_p)) + '.txt', 'r', -1, 'utf-8')
                                            for line in file:
                                                if re.search('gamemode', line):
                                                    linp = str(line)
                                                if re.search('figure', line):
                                                    linp = linp + str(line)
                                                if re.search('field', line):
                                                    linp = linp + str(line)
                                                if re.search('rows', line):
                                                    linp = linp + str(line)
                                                if re.search('red', line):
                                                    linp = linp + str(line)
                                            file = open('users/' + str(sha1(name_p)) + '.txt', 'w', -1, 'utf-8')
                                            file.write(linp + '\nblue = ' + str(arr_blue))
                                            arria[JJJ][III] = 0
                                        globals()[arr_2[III][JJJ]].setChecked(False)
                                        globals()[arr_2[III][JJJ]].setCheckable(False)
                                        globals()[arr_2[III][JJJ]].enterEvent = 0

                    elif mov == 0:
                        globals()[arr_2[i][j]].setStyleSheet("QPushButton\n"
                                                                 "{\n"
                                                                 "border: 2px solid #ffffff;\n"
                                                                 "\n"
                                                                 "border-image: url(resources/naught.png);\n"
                                                                 "}\n")
                        mov = 1
                        form2.move_blue_l.setVisible(False)
                        form2.move_red_l.setVisible(True)
                        arr_blue.append(arr_2[i][j])

                        # ВЫВОД ХОДА
                        rep = arr_2[i][j]
                        rep = rep.replace('`', '')
                        if form2.move_b_te.toPlainText() == '':
                            form2.move_b_te.setText(rep)
                        else:
                            form2.move_b_te.setText(form2.move_b_te.toPlainText() + ', ' + rep)

                        file = open('users/' + str(sha1(name_p)) + '.txt', 'r', -1, 'utf-8')
                        for line in file:
                            if re.search('gamemode', line):
                                linp = str(line)
                            if re.search('figure', line):
                                linp = linp + str(line)
                            if re.search('field', line):
                                linp = linp + str(line)
                            if re.search('rows', line):
                                linp = linp + str(line)
                            if re.search('red', line):
                                linp = linp + str(line)
                        file = open('users/' + str(sha1(name_p)) + '.txt', 'w', -1, 'utf-8')
                        file.write(linp + '\nblue = ' + str(arr_blue))
                        arria[j][i] = 0
                        if (gm == 1) and (figure == 0):
                            fig = 1
                            bot()
                            for III in range(len(arr_2)):
                                for JJJ in range(len(arr_2)):
                                    if matr[JJJ][III] != arria[JJJ][III]:
                                        arria[JJJ][III] = matr[JJJ][III]
                                        if mov == 1:
                                            globals()[arr_2[III][JJJ]].setStyleSheet("QPushButton\n"
                                                                                 "{\n"
                                                                                 "border: 2px solid #ffffff;\n"
                                                                                 "\n"
                                                                                 "border-image: url(resources/cross.png);\n"
                                                                                 "}\n")
                                            mov = 0
                                            form2.move_red_l.setVisible(False)
                                            form2.move_blue_l.setVisible(True)
                                            arr_red.append(arr_2[III][JJJ])

                                            # ВЫВОД ХОДА
                                            rep = arr_2[III][JJJ]
                                            rep = rep.replace('`', '')
                                            if form2.move_r_te.toPlainText() == '':
                                                form2.move_r_te.setText(rep)
                                            else:
                                                form2.move_r_te.setText(form2.move_r_te.toPlainText() + ', ' + rep)

                                            file = open('users/' + str(sha1(name_p)) + '.txt', 'r', -1, 'utf-8')
                                            for line in file:
                                                if re.search('gamemode', line):
                                                    linp = str(line)
                                                if re.search('figure', line):
                                                    linp = linp + str(line)
                                                if re.search('field', line):
                                                    linp = linp + str(line)
                                                if re.search('rows', line):
                                                    linp = linp + str(line)
                                                if re.search('blue', line):
                                                    linp = linp + str(line)
                                            file = open('users/' + str(sha1(name_p)) + '.txt', 'w', -1, 'utf-8')
                                            file.write(linp + '\nred = ' + str(arr_red))
                                            arria[JJJ][III] = 1


                    globals()[arr_2[i][j]].setChecked(False)
                    globals()[arr_2[i][j]].setCheckable(False)
                    globals()[arr_2[i][j]].enterEvent = 0

        win()
    for i in range(len(arr_2)):
        for j in range(len(arr_2)):
            globals()[arr_2[i][j]].clicked.connect(move)

    # ЗАНОВО
    def again():
        global sec
        global minut
        global arr_red
        global arr_blue
        global arria
        global mov
        sec = 0
        minut = 0
        for i in range(len(arr_2)):
            for j in range(len(arr_2)):
                globals()[arr_2[i][j]].setStyleSheet("QPushButton\n"
                                                     "{\n"
                                                     "border: 2px solid #ffffff;\n"
                                                     "\n"
                                                     "color: rgb(255, 255, 255);\n"
                                                     "}\n"
                                                     "QPushButton:hover\n"
                                                     "{\n"
                                                     "background-color: rgb(255, 255, 127);\n"
                                                     "}")
                globals()[arr_2[i][j]].setCheckable(True)
                globals()[arr_2[i][j]].setVisible(True)
                globals()[arr_2[i][j]].enterEvent = enter

        linp = ''
        file = open('users/' + str(sha1(name_p)) + '.txt', 'r', -1, 'utf-8')
        for line in file:
            if re.search('gamemode', line):
                linp = linp + line
            if re.search('figure', line):
                linp = linp + line
            if re.search('field', line):
                linp = linp + line
            if re.search('rows', line):
                linp = linp + line
        file = open('users/' + str(sha1(name_p)) + '.txt', 'w', -1, 'utf-8')
        file.write(linp)

        form2.move_b_te.setText('')
        form2.move_r_te.setText('')

        arr_blue = []
        arr_red = []

        for i in range(len(arria)):
            for j in range(len(arria)):
                arria[i][j] = 2
        mov = 1

        form2.blackback.setMovie(form2.game_fon_a)
        form2.game_fon_a.start()
        form2.move_red_l.setVisible(True)
        form2.game_draw_l.setVisible(False)
        form2.win_red_l.setVisible(False)
        form2.win_blue_l.setVisible(False)
        form2.move_blue_l.setVisible(False)
        form2.timer_l.setText('00:00')
        form2.timer.start()

        # Первый ход бота
        global fig
        if figure == 1:
            fig = 0
        if figure == 0:
            fig = 1
        global matr
        if (gm == 1) and (figure == 0):
            bot()
            for i in range(len(arr_2)):
                for j in range(len(arr_2)):
                    if matr[j][i] != arria[j][i]:
                        arria[j][i] = matr[j][i]
                        globals()[arr_2[i][j]].setStyleSheet("QPushButton\n"
                                                             "{\n"
                                                             "border: 2px solid #ffffff;\n"
                                                             "\n"
                                                             "border-image: url(resources/cross.png);\n"
                                                             "}\n")
                        mov = 0
                        form2.move_red_l.setVisible(False)
                        form2.move_blue_l.setVisible(True)
                        arr_red.append(arr_2[i][j])

                        # ВЫВОД ХОДА
                        rep = arr_2[i][j]
                        rep = rep.replace('`', '')
                        if form2.move_r_te.toPlainText() == '':
                            form2.move_r_te.setText(rep)
                        else:
                            form2.move_r_te.setText(form2.move_r_te.toPlainText() + ', ' + rep)

                        file = open('users/' + str(sha1(name_p)) + '.txt', 'r', -1, 'utf-8')
                        for line in file:
                            if re.search('gamemode', line):
                                linp = str(line)
                            if re.search('figure', line):
                                linp = linp + str(line)
                            if re.search('field', line):
                                linp = linp + str(line)
                            if re.search('rows', line):
                                linp = linp + str(line)
                            if re.search('blue', line):
                                linp = linp + str(line)
                        file = open('users/' + str(sha1(name_p)) + '.txt', 'w', -1, 'utf-8')
                        file.write(linp + '\nred = ' + str(arr_red))
                        globals()[arr_2[i][j]].setChecked(False)
                        globals()[arr_2[i][j]].setCheckable(False)
                        globals()[arr_2[i][j]].enterEvent = 0

    form2.again_b.clicked.connect(again)

    # Первый ход бота
    if figure == 1:
        fig = 0
    if figure == 0:
        fig = 1
    global matr
    if (gm == 1) and (figure == 0):
        bot()
        for i in range(len(arr_2)):
            for j in range(len(arr_2)):
                if matr[j][i] != arria[j][i]:
                    arria[j][i] = matr[j][i]
                    if mov == 1:
                        globals()[arr_2[i][j]].setStyleSheet("QPushButton\n"
                                                             "{\n"
                                                             "border: 2px solid #ffffff;\n"
                                                             "\n"
                                                             "border-image: url(resources/cross.png);\n"
                                                             "}\n")
                        mov = 0
                        form2.move_red_l.setVisible(False)
                        form2.move_blue_l.setVisible(True)
                        arr_red.append(arr_2[i][j])

                        # ВЫВОД ХОДА
                        rep = arr_2[i][j]
                        rep = rep.replace('`', '')
                        if form2.move_r_te.toPlainText() == '':
                            form2.move_r_te.setText(rep)
                        else:
                            form2.move_r_te.setText(form2.move_r_te.toPlainText() + ', ' + rep)

                        file = open('users/' + str(sha1(name_p)) + '.txt', 'r', -1, 'utf-8')
                        for line in file:
                            if re.search('gamemode', line):
                                linp = str(line)
                            if re.search('figure', line):
                                linp = linp + str(line)
                            if re.search('field', line):
                                linp = linp + str(line)
                            if re.search('rows', line):
                                linp = linp + str(line)
                            if re.search('blue', line):
                                linp = linp + str(line)
                        file = open('users/' + str(sha1(name_p)) + '.txt', 'w', -1, 'utf-8')
                        file.write(linp + '\nred = ' + str(arr_red))
                    globals()[arr_2[i][j]].setChecked(False)
                    globals()[arr_2[i][j]].setCheckable(False)
                    globals()[arr_2[i][j]].enterEvent = 0



def back2():
    sound_click.play()


    form2.exit_b.setVisible(True)
    form2.new_game_b.setVisible(True)
    form2.continue_b.setVisible(True)
    form2.settings_b.setVisible(True)

    form2.s_play.setVisible(False)
    form2.two_play.setVisible(False)
    form2.cross_l.setVisible(False)
    form2.naught_l.setVisible(False)
    form2.n_c_b.setVisible(False)
    form2.field_l.setVisible(False)
    form2.left_b.setVisible(False)
    form2.left_b_2.setVisible(False)
    form2.right_b.setVisible(False)
    form2.right_b_2.setVisible(False)
    form2.field_k.setVisible(False)
    form2.rows_l.setVisible(False)
    form2.rows_k.setVisible(False)
    form2.accept2_b.setVisible(False)
    form2.back2_b.setVisible(False)
    form2.s_play_l.setVisible(False)
    form2.two_play_l.setVisible(False)
form2.back2_b.clicked.connect(back2)


#ПРОДОЛЖИТЬ
def cont():
    sound_click.play()
    global name_p


    check_file = os.stat('users/' + str(sha1(name_p)) + '.txt').st_size == 0
    if check_file == False:
        sound_font.stop()
        sound_game.play()
        form2.blackback.setVisible(True)
        form2.back_b.setVisible(True)
        form2.move_blue_l.setVisible(True)
        form2.move_red_l.setVisible(True)
        form2.timer_l.setVisible(True)
        form2.whiteback.setVisible(True)
        form2.move_b_te.setVisible(True)
        form2.move_r_te.setVisible(True)
        form2.again_b.setVisible(True)
        form2.timer.start()
        file = open('users/' + str(sha1(name_p)) + '.txt', 'r', -1, 'utf-8')
        for line in file:
            if re.search('field =', line):
                field = line
                field = field.replace('field = ', '')
                field = field.replace('\n', '')
                field = int(field)
            if re.search('minutes =', line):
                linp1 = line
                linp1 = linp1.replace('minutes = ', '')
                linp1 = linp1.replace('\n', '')
                global minut
                minut = int(linp1)
            if re.search('seconds =', line):
                linp2 = line
                linp2 = linp2.replace('seconds = ', '')
                linp2 = linp2.replace('\n', '')
                global sec
                sec = int(linp2)
            if re.search('red =', line):
                global arr_red
                arr_red = []
                linp = line
                linp = linp.replace('red = ', '')
                linp = linp.replace('\n', '')
                linp = linp.replace('[', '')
                linp = linp.replace(']', '')
                linp = linp.replace("'", "")
                if linp != '':
                    arr_red.append(linp)
            if re.search('blue =', line):
                global arr_blue
                arr_blue = []
                linp = line
                linp = linp.replace('blue = ', '')
                linp = linp.replace('\n', '')
                linp = linp.replace('[', '')
                linp = linp.replace(']', '')
                linp = linp.replace("'", "")
                if linp != '':
                    arr_blue.append(linp)
        if int(linp1) < 10:
            linp1 = '0'+str(linp1)
        if int(linp2) < 10:
            linp2 = '0'+str(linp2)
        form2.timer_l.setText(str(linp1)+':'+str(linp2))


        #Чей ход следущий
        blue = 1
        red = 1
        file = open('users/' + str(sha1(name_p)) + '.txt', 'r', -1, 'utf-8')
        for line in file:
            if re.search('blue', line):
                linp = line
                for i in range(len(linp)):
                    if linp[i] == ',':
                        blue += 1
                if blue == 1:
                    linp = linp.replace('blue = ', '')
                    linp = linp.replace('\n', '')
                    if linp == '':
                        blue = 0
                    else:
                        blue = 1
        file = open('users/' + str(sha1(name_p)) + '.txt', 'r', -1, 'utf-8')
        for line in file:
            if re.search('red', line):
                linp = line
                for i in range(len(linp)):
                    if linp[i] == ',':
                        red += 1
                if red == 1:
                    linp = linp.replace('red = ', '')
                    linp = linp.replace('\n', '')
                    if linp == '':
                        red = 0
                    else:
                        red = 1
        global mov
        if red == blue:
            mov = 1
        else:
            mov = 0

        glav(field)

    else:
        form2.exit_b.setVisible(False)
        form2.new_game_b.setVisible(False)
        form2.continue_b.setVisible(False)
        form2.settings_b.setVisible(False)

        form2.s_play.setVisible(True)
        form2.two_play.setVisible(True)
        form2.cross_l.setVisible(True)
        form2.naught_l.setVisible(False)
        form2.n_c_b.setVisible(True)
        form2.field_l.setVisible(True)
        form2.left_b.setVisible(True)
        form2.left_b_2.setVisible(True)
        form2.right_b.setVisible(True)
        form2.right_b_2.setVisible(True)
        form2.field_k.setVisible(True)
        form2.rows_l.setVisible(True)
        form2.rows_k.setVisible(True)
        form2.accept2_b.setVisible(True)
        form2.back2_b.setVisible(True)
        form2.s_play_l.setVisible(True)
        form2.two_play_l.setVisible(True)
form2.continue_b.clicked.connect(cont)


#ПАУЗА
def back():
    sound_click.play()
    sound_game.stop()
    sound_font.play()

    form2.timer.stop()
    global sec
    global minut
    file = open('users/' + str(sha1(name_p)) + '.txt', 'r', -1, 'utf-8')
    for line in file:
        if re.search('gamemode', line):
            linp = str(line)
        if re.search('figure', line):
            linp = linp + str(line)
        if re.search('field', line):
            linp = linp + str(line)
        if re.search('rows', line):
            linp = linp + str(line)
        if re.search('red', line):
            lini = str(line)
            lini = lini.replace('[', '')
            lini = lini.replace(']', '')
            lini = lini.replace("'", "")
            lini = lini.replace(' ,', '')
            linp = linp + lini
        if re.search('blue', line):
            lini = str(line)
            lini = lini.replace('[', '')
            lini = lini.replace(']', '')
            lini = lini.replace("'", "")
            lini = lini.replace(' ,', '')
            linp = linp + lini
    file = open('users/' + str(sha1(name_p)) + '.txt', 'w', -1, 'utf-8')
    file.write(linp+'\nminutes = '+str(minut)+'\nseconds = '+str(sec))
    form2.move_b_te.setText('')
    form2.move_r_te.setText('')

    form2.blackback.setVisible(False)
    form2.back_b.setVisible(False)
    form2.move_blue_l.setVisible(False)
    form2.move_red_l.setVisible(False)
    form2.timer_l.setVisible(False)
    form2.whiteback.setVisible(False)
    form2.move_b_te.setVisible(False)
    form2.move_r_te.setVisible(False)
    form2.win_red_l.setVisible(False)
    form2.win_blue_l.setVisible(False)
    form2.again_b.setVisible(False)
    form2.game_draw_l.setVisible(False)
    for i in range(len(arr_2)):
        for j in range(len(arr_2)):
            globals()[arr_2[i][j]].setVisible(False)

    form2.new_game_b.setVisible(True)
    form2.continue_b.setVisible(True)
    form2.settings_b.setVisible(True)
    form2.exit_b.setVisible(True)

form2.back_b.clicked.connect(back)


#НАСТРОЙКА РАЗМЕРА
form2.exit_b.setGeometry(m_x(form2.exit_b), m_y(form2.exit_b), m_w(form2.exit_b), m_h(form2.exit_b))
form2.new_game_b.setGeometry(m_x(form2.new_game_b), m_y(form2.new_game_b), m_w(form2.new_game_b), m_h(form2.new_game_b))
form2.continue_b.setGeometry(m_x(form2.continue_b), m_y(form2.continue_b), m_w(form2.continue_b), m_h(form2.continue_b))
form2.settings_b.setGeometry(m_x(form2.settings_b), m_y(form2.settings_b), m_w(form2.settings_b), m_h(form2.settings_b))
form2.accept_b.setGeometry(m_x(form2.accept_b), m_y(form2.accept_b), m_w(form2.accept_b), m_h(form2.accept_b))
form2.back_b.setGeometry(m_x(form2.back_b), m_y(form2.back_b), m_w(form2.back_b), m_h(form2.back_b))
form2.title.setGeometry(m_x(form2.title), m_y(form2.title), m_w(form2.title), m_h(form2.title))
form2.move_blue_l.setGeometry(m_x(form2.move_blue_l), m_y(form2.move_blue_l), m_w(form2.move_blue_l), m_h(form2.move_blue_l))
form2.move_red_l.setGeometry(m_x(form2.move_red_l), m_y(form2.move_red_l), m_w(form2.move_red_l), m_h(form2.move_red_l))
form2.sound_l.setGeometry(m_x(form2.sound_l), m_y(form2.sound_l), m_w(form2.sound_l), m_h(form2.sound_l))
form2.music_l.setGeometry(m_x(form2.music_l), m_y(form2.music_l), m_w(form2.music_l), m_h(form2.music_l))
form2.blackback.setGeometry(m_x(form2.blackback), m_y(form2.blackback), m_w(form2.blackback), m_h(form2.blackback))
form2.sound.setGeometry(m_x(form2.sound), m_y(form2.sound), m_w(form2.sound), m_h(form2.sound))
form2.music.setGeometry(m_x(form2.music), m_y(form2.music), m_w(form2.music), m_h(form2.music))
form2.s_play.setGeometry(m_x(form2.s_play), m_y(form2.s_play), m_w(form2.s_play), m_h(form2.s_play))
form2.two_play.setGeometry(m_x(form2.two_play), m_y(form2.two_play), m_w(form2.two_play), m_h(form2.two_play))
form2.s_play_l.setGeometry(m_x(form2.s_play_l), m_y(form2.s_play_l), m_w(form2.s_play_l), m_h(form2.s_play_l))
form2.two_play_l.setGeometry(m_x(form2.two_play_l), m_y(form2.two_play_l), m_w(form2.two_play_l), m_h(form2.two_play_l))
form2.cross_l.setGeometry(m_x(form2.cross_l), m_y(form2.cross_l), m_w(form2.cross_l), m_h(form2.cross_l))
form2.naught_l.setGeometry(m_x(form2.naught_l), m_y(form2.naught_l), m_w(form2.naught_l), m_h(form2.naught_l))
form2.n_c_b.setGeometry(m_x(form2.n_c_b), m_y(form2.n_c_b), m_w(form2.n_c_b), m_h(form2.n_c_b))
form2.field_l.setGeometry(m_x(form2.field_l), m_y(form2.field_l), m_w(form2.field_l), m_h(form2.field_l))
form2.left_b.setGeometry(m_x(form2.left_b), m_y(form2.left_b), m_w(form2.left_b), m_h(form2.left_b))
form2.left_b_2.setGeometry(m_x(form2.left_b_2), m_y(form2.left_b_2), m_w(form2.left_b_2), m_h(form2.left_b_2))
form2.right_b.setGeometry(m_x(form2.right_b), m_y(form2.right_b), m_w(form2.right_b), m_h(form2.right_b))
form2.right_b_2.setGeometry(m_x(form2.right_b_2), m_y(form2.right_b_2), m_w(form2.right_b_2), m_h(form2.right_b_2))
form2.field_k.setGeometry(m_x(form2.field_k), m_y(form2.field_k), m_w(form2.field_k), m_h(form2.field_k))
form2.rows_l.setGeometry(m_x(form2.rows_l), m_y(form2.rows_l), m_w(form2.rows_l), m_h(form2.rows_l))
form2.rows_k.setGeometry(m_x(form2.rows_k), m_y(form2.rows_k), m_w(form2.rows_k), m_h(form2.rows_k))
form2.accept2_b.setGeometry(m_x(form2.accept2_b), m_y(form2.accept2_b), m_w(form2.accept2_b), m_h(form2.accept2_b))
form2.back2_b.setGeometry(m_x(form2.back2_b), m_y(form2.back2_b), m_w(form2.back2_b), m_h(form2.back2_b))
form2.timer_l.setGeometry(m_x(form2.timer_l), m_y(form2.timer_l), m_w(form2.timer_l), m_h(form2.timer_l))
form2.whiteback.setGeometry(m_x(form2.whiteback), m_y(form2.whiteback), m_w(form2.whiteback), m_h(form2.whiteback))
form2.move_b_te.setGeometry(m_x(form2.move_b_te), m_y(form2.move_b_te), m_w(form2.move_b_te), m_h(form2.move_b_te))
form2.move_r_te.setGeometry(m_x(form2.move_r_te), m_y(form2.move_r_te), m_w(form2.move_r_te), m_h(form2.move_r_te))
form2.win_red_l.setGeometry(m_x(form2.win_red_l), m_y(form2.win_red_l), m_w(form2.win_red_l), m_h(form2.win_red_l))
form2.win_blue_l.setGeometry(m_x(form2.win_blue_l), m_y(form2.win_blue_l), m_w(form2.win_blue_l), m_h(form2.win_blue_l))
form2.game_draw_l.setGeometry(m_x(form2.game_draw_l), m_y(form2.game_draw_l), m_w(form2.game_draw_l), m_h(form2.game_draw_l))
form2.again_b.setGeometry(m_x(form2.again_b), m_y(form2.again_b), m_w(form2.again_b), m_h(form2.again_b))



#ЗАПРЕЩАЕТ ВВОД ТЕКСТА В ИГРЕ
form2.move_b_te.setReadOnly(True)
form2.move_r_te.setReadOnly(True)
#Размер цифр таймера
form2.timer_l.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size:"+(str(int(form2.timer_l.width()/4)))+"px;\n"
"font-family:Retro Land Mayhem;")

#Размер чекбоксов
form2.two_play.setStyleSheet("QCheckBox {\n""color: rgb(255, 255, 255);\n"
"spacing: 20px;\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: " + str(form2.two_play.height()) +"px;\n"
"    height: " + str(form2.two_play.height()) + "px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    border-image: url(resources/check_f.png);\n"
"}\n"
"QCheckBox::indicator:unchecked:hover {\n"
"   border-image: url(resources/check_f_h.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"   border-image: url(resources/check_t.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"   border-image: url(resources/check_t_h.png)\n"
"}")
form2.s_play.setStyleSheet("QCheckBox {\n""color: rgb(255, 255, 255);\n"
"spacing: 20px;\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: " + str(form2.s_play.height()) +"px;\n"
"    height: " + str(form2.s_play.height()) + "px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    border-image: url(resources/check_f.png);\n"
"}\n"
"QCheckBox::indicator:unchecked:hover {\n"
"   border-image: url(resources/check_f_h.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"   border-image: url(resources/check_t.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"   border-image: url(resources/check_t_h.png)\n"
"}")


#АНИМАЦИИ
    #НАЗВАНИЕ
form2.title_a = QMovie("resources/name_game1.gif")
form2.title_a.setScaledSize(QtCore.QSize(int(form2.title.width()), int(form2.title.height())))
form2.title_a.setSpeed(150)
form2.title.setMovie(form2.title_a)
form2.title_a.start()
    #КОРОЛИ норм
form2.game_fon_a = QMovie("resources/game_fon_a.gif")
form2.game_fon_a.setScaledSize(QtCore.QSize(int(form2.blackback.width()), int(form2.blackback.height())))
form2.blackback.setMovie(form2.game_fon_a)
form2.game_fon_a.start()
    #КРАСНЫЙ ВЫЙГРАЛ
form2.wr_fon = QMovie("resources/wr_fon.gif")
form2.wr_fon.setScaledSize(QtCore.QSize(int(form2.blackback.width()), int(form2.blackback.height())))
    #КОРОЛИ норм
form2.wb_fon = QMovie("resources/wb_fon.gif")
form2.wb_fon.setScaledSize(QtCore.QSize(int(form2.blackback.width()), int(form2.blackback.height())))
# ------------------------код шифрования SHA1---------------------------------
def sha1(data):
    bytes = ""

    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    for n in range(len(data)):
        bytes+='{0:08b}'.format(ord(data[n]))
    bits = bytes+"1"
    pBits = bits

    while len(pBits)%512 != 448:
        pBits+="0"

    pBits+='{0:064b}'.format(len(bits)-1)

    def chunks(l, n):
        return [l[i:i+n] for i in range(0, len(l), n)]

    def rol(n, b):
        return ((n << b) | (n >> (32 - b))) & 0xffffffff

    for c in chunks(pBits, 512):
        words = chunks(c, 32)
        w = [0]*80
        for n in range(0, 16):
            w[n] = int(words[n], 2)
        for i in range(16, 80):
            w[i] = rol((w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]), 1)

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        for i in range(0, 80):
            if 0 <= i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = rol(a, 5) + f + e + k + w[i] & 0xffffffff
            e = d
            d = c
            c = rol(b, 30)
            b = a
            a = temp

        h0 = h0 + a & 0xffffffff
        h1 = h1 + b & 0xffffffff
        h2 = h2 + c & 0xffffffff
        h3 = h3 + d & 0xffffffff
        h4 = h4 + e & 0xffffffff

    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)

app.exec()