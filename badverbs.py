from playsound import playsound
from random import choice, randint, shuffle
from colorama import Fore, Back, init


def que(vid, n):
    def result_of_otv(vern_otv, itog, problem_word):
        if itog:
            print(Back.GREEN+"Верно✔ "+Back.BLACK+" Продолжаем!")
            playsound("Sluzbsaund/tada(uspeh1).mp3")
            print(Back.BLACK+Fore.WHITE)
            return (1, [])
        print(Back.RED+"Ошибка✖ "+Back.BLACK+" Верный ответ:", Fore.GREEN+vern_otv)
        playsound("Sluzbsaund/proval1.mp3")
        print(Back.BLACK+Fore.WHITE)
        return (0, problem_word)


    def vvod_otv(name_sound, text):
        otv = ""
        while otv == "":
            print(text)
            playsound(name_sound)
            otv = input()
        return otv #ввод для аудио-вопросв


    if  vid ==  "1_1":
        otv = input("Переведи на русский ифнинитив"+" "+Fore.CYAN+n[0]+Fore.WHITE+": ")
        return result_of_otv(n[2][0], (otv in n[2]), (n[0], n[2]))
    elif vid == "1_2":
        otv = input("Напиши форму прошедшего времени глагола"+" "+Fore.CYAN+n[0]+Fore.WHITE+": ")
        return result_of_otv(n[1], (otv == n[1]), (n[0], n[2]))
    elif vid == "1_3":
        otv = input("Напиши на английском начальную форму глагола"+" "+Fore.CYAN+n[1]+Fore.WHITE+": ")
        return result_of_otv(n[0], (otv == n[0]), (n[0], n[2]))
    elif vid == "1_4":
        otv = input("Переведи на русский слово в форме прошедшего времени"+" "+Fore.CYAN+n[1]+Fore.WHITE+": ")
        return result_of_otv(n[3][0], (otv in n[3]), (n[0], n[2]))
    elif vid == "1_5":
        otv = input("Переведи на английский слово"+" "+Fore.CYAN+n[2][0]+Fore.WHITE+": ")
        return result_of_otv(n[0], (otv == n[0] or (n[2][0] in ("сказать", "говорить") and otv in ("say", "tell", "speak"))), (n[0], n[2]))
    elif vid == "1_6":
        otv = input("Переведи на английский слово"+" "+Fore.CYAN+n[3][0]+Fore.WHITE+": ")
        return result_of_otv(n[1], (otv == n[1] or (n[3][0] in ("сказал", "говорил") and otv in ("said", "told", "spoke"))), (n[0], n[2]))
    elif vid == "2_1":
        otv = vvod_otv("Nast/"+n[0]+'_n.mp3', "Напиши услышенное слово, если хочешь ещё прослушать, жми ENTER ")
        return result_of_otv(n[0], (otv == n[0]), (n[0], n[2]))
    elif vid == "2_2":
        otv = vvod_otv("Last/"+n[1]+'_p.mp3', "Напиши услышенное слово, если хочешь ещё прослушать, жми ENTER ")
        return result_of_otv(n[1], (otv == n[1]), (n[0], n[2]))
    elif vid == "2_3":
        otv = vvod_otv("Nast/"+n[0]+'_n.mp3',"Переведи на русский услышенное слово, если хочешь ещё прослушать, жми ENTER ")
        return result_of_otv(n[2][0], (otv in n[2] or (otv in n[3] and n[0]==n[1] and n[0]!='read')), (n[0], n[2]))
    elif vid == "2_4":
        otv = vvod_otv("Last/"+n[1]+'_p.mp3', "Переведи на русский услышенное слово, если хочешь ещё прослушать, жми ENTER ")
        return result_of_otv(n[3][0], (otv in n[3] or (otv in n[2] and n[0]==n[1] and n[0]!='read')), (n[0], n[2]))


init()
spisok = [] # делаем список со строками формата: инфинитив; прош.вр.; [переводы инфинитива]; [переводы прош.вр] и встряхиваем его
for i in open("words.txt", encoding='utf-8'):
    x = i.split("; ")
    x = [x[0], x[1]] + [[j for j in x[2].split()]] + [[j for j in x[3].split()]]
    spisok.append(x)
shuffle(spisok)

print(Back.RED+"\tСея прога предназначена для заучивания неправильных глаголов в английском. \n\t\
Пиши букву ё, там где она пишется, иначе ответ не зачтётся.\n\t\
При переводе глаголов прошедшего времени пиши их в ед.ч. муж.р.")

k='0'
while (k not in '12') or k=="":
    k=input(Back.BLACK+"\tТы хочешь потренироваться (Введи 1 или 2)\n\t\t1. Без аудио\n\t\t2. С аудио\n")

n=""
print("Из скольки вопросов будет состоять тэст?")
while 1: #требуем ввести число вопросов
    while not(n.isdigit()):
        n=input("\tВведи число от 8 до"+" "+str(len(spisok))+": ")
    if not(8<=int(n)<=len(spisok)):
        n=''
        continue
    break
spisok = spisok[:int(n)]

print("Погнали!\n")
verno=0
mistakes = []
for n in spisok:
    c = randint(1, int(k)) # определяет тип вопросов
    s = que(str(c)+"_"+str(randint(1, 8-2*c)), n) # а это я ловко придумал
    verno += s[0]
    mistakes.append(s[1])

mistakes = [i for i in mistakes if i!=[]]
print("Обрати внимание на слова, в которых ошибся:")
for i in mistakes:
    print(Fore.YELLOW+i[0]+" - "+i[1][0])
print(Fore.WHITE)
print("Штош, твой результат: ")
playsound("Sluzbsaund/zvuk-barabannoj-drobi.mp3")
print(str(verno)+"/"+str(len(spisok)))
if verno == len(spisok):
    print("Супермега харош, легенда!")
    print("Держи кубок")
    print("""
   \           /
    \_________/
      |     |
      | /|  |
      |  |  |
     _|_ _ _|_
       """)
    playsound("Sluzbsaund/music_ideal.mp3")
elif verno/len(spisok) >= 0.8:
    print("Круто, но не идеально! Ты можешь ещё лучше!")
    playsound("Sluzbsaund/music_08-1.mp3")
elif 0.5 < verno/len(spisok) < 0.8:
    print("Средний результат, но всё в твоих руках")
    playsound("Sluzbsaund/music_norm.mp3")
elif 0.2 < verno/len(spisok) <= 0.5:
    print("Дерьмом ты не был, но и до вершин не добрался")
    playsound("Sluzbsaund/music_xpeHoBo.mp3")
else:
    print("Ты меня расстраиваешь своими знаниями")
    print("""
          |   |
          |   |

            |

          ______
        /        /
         """)
    print("Не делай так больше!")
    playsound("Sluzbsaund/music_pzdc.mp3")
input()
