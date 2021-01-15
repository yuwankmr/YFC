import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import Image , ImageTk
import time as sleeptime
main = ThemedTk(theme = 'scid')
main.title("Flow Chart Maker")
main.geometry('1150x700')
path = "C:\\Program Files (x86)\\yfc\\"
try:
    icon = Image.open(path + 'icon.jpg')
    icon = ImageTk.PhotoImage(icon)
    main.iconphoto(False,icon)
except:
    None
main.resizable(False,False)
sheet = tk.Canvas(main,height = 700 , width = 600 , background = 'pink')
sheet.place(x = 120 , y = 0)
render = tk.Canvas(main,height = 700, width = 1)
render.pack(side = 'right')
# Global Variables
n = -1
time = -1
ex = 0
ey = 0
xa = 0
ya = 0
xb = 0
yb = 0
xa1 = 0
ya1 = 0
xb1 = 0
yb1 = 0
xa2 = 0
ya2 = 0
xb2 = 0
yb2 = 0
ex1 = 0
ey1 = 0
ex2 = 0
ey2 = 0
exz1 = 0
eyz1 = 0
exz2 = 0
eyz2 = 0
ifa = 0
ifb = 0
elifx = 0
elify = 0
offx = 0
offy = 0
offz = 1
pos = -1
plusx = 0
faith = 0
xw = -1
nw = -1
codefile_name = 'code.py'
connection = "none"
firstelse = "none"
click = 0
joints = -1
l = 0
items = ['(None)','(None)']
colors = ['white smoke', 'gainsboro', 'floral white', 'old lace','linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff','navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender','lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray','light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue','slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue','dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue','light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise','cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green','dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green','lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green','forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow','light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown','indian red', 'saddle brown', 'sandy brown','dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange','coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink','pale violet red', 'maroon', 'medium violet red', 'violet red','medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple','thistle', 'snow2', 'snow3','snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2','AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2','PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4','LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3','cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4','LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3','MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3','SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4','DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2','SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4','SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2','LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3','SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3','LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4','LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2','PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3','CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3','cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4','aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3','DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2','PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4','green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4','OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2','DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4','LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4','LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4','gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4','DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4','RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2','IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1','burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1','tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2','firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2','salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2','orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4','coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2','OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4','HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4','LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1','PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2','maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4','magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1','plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3','MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4','purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2','MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4','gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10','gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19','gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28','gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37','gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47','gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56','gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65','gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74','gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83','gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92','gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']
def renderer():
    global joints,codefile_name
    if codefile_name == 'code.py':
        save = tk.Toplevel(main)
        save.title("   Name")
        save.geometry('200x100')
        name = tk.StringVar()
        lab = ttk.Label(save,text ="    ")
        lab.grid(row = 0,column = 0)
        lab = ttk.Label(save,text ="Name ")
        lab.grid(row = 1,column = 0)
        moon = ttk.Entry(save,textvar= name)
        name.set("Untitled")
        moon.focus()
        moon.grid(row = 1,column = 1)
        lab = ttk.Label(save,text =".py ")
        lab.grid(row = 1,column = 2)
        def judo():
            global codefile_name
            codefile_name = name.get()+".py"
            save.destroy()
            code_w = open(codefile_name,'w+')
            time = 0
            gap = 0
            line = 0
            itemto = []
            loopcon = 0
            firstif_pos = 250
            iftime = 0
            while True:
                # first text = time
                try:
                    a = render.itemconfig("from"+str(time))['text'][-1]
                    g = " " * gap
                    type = sheet.type(str(time)+"shape")
                    if type == 'rectangle':
                        try:
                            s = a.split('\n')
                            q = 0
                            while q < len(s):
                                try:
                                    code_w.write(g+s[q]+"\n")
                                    q = q +1
                                except:
                                    break
                        except:
                            None
                    else:
                        code_w.write(g+a+"\n")
                    line = line + 1
                    tag =  render.gettags('from'+str(time))
                # if that object is If
                    try:
                        if tag[2]=="if"+str(time):
                           ifnum = tag[1].replace("to","")
                           var = a
                           gap = gap + 4
                           elsetime = int(time)+50
                           ifline = line
                           iftime = iftime + 1
                           if ifline < firstif_pos:
                               firstif_pos = line
                    except:
                        None
                    # gap after else
                    if int(time) > 49:
                        gap = gap + 4
                   # finding next shape
                    to = tag[1].replace("to","from")
                    time = to.replace("from","")
                    time = int(time) # tag [1] = 'to'+??shape
                # If while loop found
                    # 1 shape connected by 2 shapes
                    if tag[1] in itemto:
                        loopcon = loopcon + 1
                        # after loop
                        if loopcon == 2:
                            fromtag = tag[1].replace("to","")
                            tag = render.gettags("from"+fromtag)
                            # if shape = if
                            try:
                                if tag[2] == 'if'+str(fromtag):
                                    time = tag[1].replace('to','')
                                    gap = gap - 4
                            # else : any process?
                            except:
                                time = int(fromtag)
                                loopcon = loopcon - 1
                        # Loop closing point
                        elif loopcon == 3 :
                            code_w.close()
                            break
                        # loop starting point
                        else:
                            code_w.close()
                            m = open(codefile_name,'r+')
                            a = m.readlines(0)
                        # Morethen one if (else:if:else:while)<<<<<< like This
                        # <Pass><Pass><Pass><Pass><Pass><Pass><Pass><Pass><Pass>
                            if iftime >= 2:
                                print(" > ifs")
                                if elseline+1 == line :
                                    x = a[int(firstif_pos)-1:]
                                    v = 4
                                    j = 0
                                else:
                                    x = a[int(firstif_pos)-1:]
                                    v = 0
                                    j = 4
                                a[elseline] = a[elseline]+g+(" "*v)+"while True:\n"+(" "*j)+g[:(v-(2*v))]
                        # Just One if
                            elif iftime == 1 :
                                x = a[int(firstif_pos)-1:]
                                if not(elseline+1 == line) :
                                    v = 4
                                    j = 0
                                else:
                                    v = 0
                                    j = 4
                                a[elseline] = a[elseline]+g+" "*j+"while True:\n"+g
                            m.close()
                            code_w = open(codefile_name,'w+')
                            h = -1
                            q = ""
                            while h < line-1:
                                h = h + 1
                                if h == elseline+2:
                                    q = " "*4
                                code_w.write(q+a[h])
                        # getting loop process
                            gap = gap + 4
                            fromtag = tag[1].replace("to","")
                            tag = render.gettags("from"+fromtag)
                            # if shape = if
                            try:
                                if tag[2] == 'if'+str(fromtag):
                                    None
                            # else : any process?
                            except:
                                time = int(fromtag)
                                gap = gap - 4
                                while True:
                                    try:
                                        a = render.itemconfig("from"+str(time))['text'][-1]
                                        g = " " * gap
                                        code_w.write(g+"    "+a+"\n")
                                        line = line + 1
                                        tag =  render.gettags('from'+str(time))
                                        #gap = gap + 4
                                        try:
                                            if tag[2]=="if"+str(time):
                                                break
                                        except:
                                            time = tag[1].replace('to',"")
                                            tag =  render.gettags('from'+str(time))
                                            try:
                                                if tag[2]=="if"+str(time):
                                                    gap = gap + 4
                                                    break
                                            except:
                                                    None
                                    except:
                                        break
                        #code_w.write("hear")
                            code_w.close()
                            line = line + 1
                            code_w = open(codefile_name,'a+')
                            d = 0
                            c = -1
                            # copying codes after loop starts
                            while True:
                                c = c +1
                                if 'else:' in x[c] :
                                    d = d + 1
                                    if d == iftime:
                                        code_w.write(" "*gap+" "*(4*d)+'break\n')
                                        break
                                    code_w.write(" "*gap+" "*(4*d)+'break\n')
                                code_w.write(" "*gap+x[c])
                            time = elsetime
                    # confirming the shape is the lead to the loop       
                    else:
                        itemto.append(tag[1])
                # after fining first flow (begining of the else:)
                except:
                    try:
                        if int(elsetime) > 0 :
                            time = int(elsetime)
                            gap = gap - 4
                            elsetime = int(-1)
                            elseline = line
                        else:
                            code_w.close()
                            break
                    # File Closer without no if:else: statment (simple code)
                    except:
                        code_w.close()
                        break
                    messagebox.showinfo("Success!","Rendered python file saved in C:\\Program Files (x86)\\")
        but = ttk.Button(save,text = "Ok",command = judo)
        but.place(x = 10,y = 60)
        def destroy():
            save.destroy()
            render.destroy()
        but = ttk.Button(save,text = "Cancel",command = destroy)
        but.place(x = 100,y = 60)
        save.mainloop()  
def limit():
    if n >43:
        tk.messagebox.showinfo("Out of Range","Maximum flow amount is 44")
def destroyer():
    print('')
    main.destroy()
# Button Click
def b1click(event):
        global n,time,ex,ey,xa,xb,ya,yb,ifa,ifb,click,l,xa1,xb1,ya1,yb1,xa2,xb2,ya2,yb2,connection,ex1,ey1,ex2,ey2,elifx,elify,firstelse,exz1,eyz1,exz2,eyz2
        ex = event.x
        ey = event.y
        clickcoord = [ex,ey]
        exa = clickcoord[0]
        eya = clickcoord[1]
        time = n+1
        while int(time) >= 0:
                time = int(time) - 1                    
                coord = sheet.coords(str(time)+"shape")
                l = len(coord)
                # Find Shape
                if l < 2 :
                        print("out")
                        click = 2002
                        time = -1
                        # click = -1
                        break
                elif l > 5:
                        xa = coord[6]
                        ya = coord[1]
                        xb = coord[2]
                        yb = coord[5]
                        ifa = coord[0]
                        ifb = coord[3]
                elif l < 5:
                        xa = coord[0]
                        ya = coord[1]
                        xb = coord[2]
                        yb = coord[3]
                # Find Connection
                if ((exa>xa)and(exa<xb))and((eya>ya)and(eya<yb)):
                        click = int(time)
                        try:
                            try:
                                fro = sheet.gettags("from"+str(click))
                                to = fro[1]
                                to = to.replace('to',"")
                                tocoord = sheet.coords(str(to)+"shape")
                                o = len(tocoord)
                                if o > 5:
                                    xa1 = tocoord[6]
                                    ya1 = tocoord[1]
                                    xb1 = tocoord[2]
                                    yb1 = tocoord[5]
                                elif o < 5:
                                    xa1 = tocoord[0]
                                    ya1 = tocoord[1]
                                    xb1 = tocoord[2]
                                    yb1 = tocoord[3]
                                fro = sheet.gettags("to"+str(click))
                                to = fro[0]
                                to = to.replace('from',"")
                                tocoord = sheet.coords(str(to)+"shape")
                                o = len(tocoord)
                                if o > 5:
                                    xa2 = tocoord[6]
                                    ya2 = tocoord[1]
                                    xb2 = tocoord[2]
                                    yb2 = tocoord[5]
                                elif o < 5:
                                    xa2 = tocoord[0]
                                    ya2 = tocoord[1]
                                    xb2 = tocoord[2]
                                    yb2 = tocoord[3]
                                connection = "from and to"
                            except:
                                # From
                                try:
                                    fro = sheet.gettags("from"+str(click))
                                    to = fro[1]
                                    to = to.replace('to',"")
                                    tocoord = sheet.coords(str(to)+"shape")
                                    o = len(tocoord)
                                    if o > 5:
                                        xa1 = tocoord[6]
                                        ya1 = tocoord[1]
                                        xb1 = tocoord[2]
                                        yb1 = tocoord[5]
                                    elif o < 5:
                                        xa1 = tocoord[0]
                                        ya1 = tocoord[1]
                                        xb1 = tocoord[2]
                                        yb1 = tocoord[3]
                                    connection = 'from'                              
                                # To
                                except:
                                    try:
                                        fro = sheet.gettags("to"+str(click))
                                        to = fro[0]
                                        to = to.replace('from',"")
                                        tocoord = sheet.coords(str(to)+"shape")
                                        o = len(tocoord)
                                        if o > 5:
                                            xa1 = tocoord[6]
                                            ya1 = tocoord[1]
                                            xb1= tocoord[2]
                                            yb1 = tocoord[5]
                                        elif o < 5:
                                            xa1 = tocoord[0]
                                            ya1= tocoord[1]
                                            xb1 = tocoord[2]
                                            yb1 = tocoord[3]
                                        connection = "to"
                                    except:
                                        fro = sheet.gettags("to"+str(click))
                                        to = fro[1]
                                        to = to.replace('else',"")
                                        tocoord = sheet.coords(str(to)+"shape")
                                        o = len(tocoord)
                                        if o > 5:
                                            xa1 = tocoord[6]
                                            ya1 = tocoord[1]
                                            xb1= tocoord[2]
                                            yb1 = tocoord[5]
                                            elifx = tocoord[0]
                                            elify = tocoord[3]
                                        elif o < 5:
                                            xa1 = tocoord[0]
                                            ya1= tocoord[1]
                                            xb1 = tocoord[2]
                                            yb1 = tocoord[3]
                                        connection = "eto"
                        except:
                            None
                        # From If To First Else
                        try:
                            to = sheet.gettags("else"+str(click))
                            coord = to[0]
                            coord = coord.replace("to","")
                            tocoord = sheet.coords(str(coord)+"shape")
                            o = len(tocoord)
                            if o > 5:
                                ex1 = tocoord[6]
                                ey1 = tocoord[1]
                                ex2 = tocoord[2]
                                ey2 = tocoord[5]
                            elif o < 5:
                                ex1 = tocoord[0]
                                ey1 = tocoord[1]
                                ex2 = tocoord[2]
                                ey2 = tocoord[3]
                        # First Else
                        except:
                            try:
                                to = sheet.gettags("elseb"+str(click))
                                coord = to[1]
                                coord = coord.replace("else","")
                                tocoord = sheet.coords(str(coord)+"shape")
                                firstelse = "yes"
                                exz1 = tocoord[6]
                                eyz1 = tocoord[1]
                                exz2 = tocoord[2]
                                eyz2 = tocoord[3]
                            except:
                                None
                        time = -1
                        break
def move(a,b):
    global offx,offy
    sheet.move('all',a,b)
    offx = offx+a
    offy = offy+b
    f = tk.Label(main,text = "X:"+str(offx) + " , "+"Y:"+str(offy),width = 20)
    f.place(x = 610, y = 680)
def left(event):
            move(-10,0)
def right(event):
            move(10,0)
def up(event):
            move(0,-10)
def down(event):
            move(0,10)
def zoomin(event):
    global offz,offx,offy
    sheet.scale('all',300,350,2,2)
    offz = offz*2
    offx = offx-150*offz
    offy = offy-175*offz
    f = tk.Label(main,text = ("%.2f" % (100*float(offz)))+"%",width = 10)
    f.place(x = 30, y = 680)
    f = tk.Label(main,text = "X:"+str(offx) + " , "+"Y:"+str(offy),width = 20)
    f.place(x = 610, y = 680)
def zoomout(event):
    global offz,offx,offy
    sheet.scale('all',300,350,0.5,0.5)
    offz = offz*0.5
    offx = offx+ 300*offz
    offy = offy+ 350*offz
    f = tk.Label(main,text = ("%.2f" % (100*float(offz)))+"%",width = 10)
    f.place(x = 30, y = 680)
    f = tk.Label(main,text = "X:"+str(offx) + " , "+"Y:"+str(offy),width = 20)
    f.place(x = 610, y = 680)
def rescale():
    global offz,offx,offy
    if offz > 1:
        num = 0
        while offz > 1:
            num = num+1
            offz = offz//2
        rescale = 0.5**num
    else:
        num = 0
        while offz < 1:
            num = num+1
            offz = offz*2
        rescale = 2**num
    sheet.scale('all',300,350,rescale,rescale)
    #sheet.move('all',offx+r,offy+j)
    if offx < 1:
        offx = 0
    else:
        offx = offx
    if offy < 1:
        offy = 0
    else:
        offy = offy
    f = tk.Label(main,text = "100.00"+"%",width = 10)
    f.place(x = 30, y = 680)
    f = tk.Label(main,text = "X:"+str(offx) + " , "+"Y:"+str(offy),width = 20)
    f.place(x = 610, y = 680)
# Event Drag                
def recoords(event):
        global ex,ey,xa,ya,xb,yb,click,ifa,ifb,l,exz2,eyz2,xa1,xb1,ya1,yb1,xa2,xb2,ya2,yb2,connection,offz,ex1,ex2,ey1,elify,firstelse
        if ((ex>xa)and(ex<xb))and((ey>ya)and(ey<yb)):
            nx = event.x-ex
            ny = event.y-ey
            x1 = xa +nx
            y1 = ya +ny
            x2 = xb +nx
            y2 = yb +ny
            if0 = ifa +nx
            if3 = ifb +ny
            xa1 = xa1
            ya1 = ya1
            xb1 = xb1
            yb1 = yb1
            xa2 = xa2
            ya2 = ya2
            xb2 = xb2
            yb2 = yb2
            # Begin,End,Process
            if l < 5:
                    sheet.coords(str(click)+"shape",x1,y1,x2,y2)
                    sheet.coords(str(click)+"text",((x2-x1)//2)+x1,((y2-y1)//2)+y1)
            # Inout
            elif if3 == y1:
                    sheet.coords(str(click)+"shape",x2-(100*offz),y1,x2,y1,x2-(30*offz),y2,x1,y2)
                    sheet.coords(str(click)+"text",((x2-x1)//2)+x1,((y2-y1)//2)+y1)
            # If..Else..
            else:
                    sheet.coords(str(click)+"shape",if0,y1,x2,if3,if0,y2,x1,if3)
                    sheet.coords(str(click)+"text",((x2-x1)//2)+x1,((y2-y1)//2)+y1)
            # Connection
            if connection == 'from and to':
                sheet.coords("from"+str(click),(x2-x1)+x1-(50*offz),y2,(xb1-xa1)+xa1-(50*offz),ya1)
                sheet.coords("to"+str(click),(xb2-xa2)+xa2-(50*offz),yb2,(x2-x1)+x1-(50*offz),y1)
                try:
                    sheet.coords("else"+str(click),x2,if3,(ex2-ex1)+ex1-(50*offz),ey1)
                except:
                    None
               # Connection From______________________________________________________________________
            elif connection == 'from':
                sheet.coords("from"+str(click),(x2-x1)+x1-(50*offz),y2,(xb1-xa1)+xa1-(50*offz),ya1) # DONT'T
                try:
                    sheet.coords("else"+str(click),x2,if3,(ex2-ex1)+ex1-(50*offz),ey1)
                except:
                    None
              # Connection to
            elif connection =='to':
                sheet.coords("to"+str(click),(xb1-xa1)+xa1-(50*offz),yb1,(x2-x1)+x1-(50*offz),y1)
            # Else Connection
            elif connection == 'eto':
                sheet.coords("to"+str(click),xb1,elify,(x2-x1)+x1-(50*offz),y1)
            if firstelse == "yes":
                try:
                    try:
                        sheet.coords("elseb"+str(click),exz2,eyz2,(x2-x1)+x1-(50*offz),y1)
                    except:
                        sheet.coords("elseb"+str(click),x2,if3,(exz2-exz1)+exz1-(50*offz),eyz1)
                except:
                    print("yes")
# Event Double Tap                  
def double_tap(event):
        global n,time,faith
        ex = event.x
        ey = event.y
        clickcoord = [ex,ey]
        exa = clickcoord[0]
        eya = clickcoord[1]
        while int(time) <= int(n):
                time = int(time) + 1
                coord = sheet.coords(str(time)+"shape")
                l = len(coord)
                if l < 2 :
                        print("out")
                        time = -1
                        # click = -1
                        break
                elif l > 5:
                        xa = coord[6]
                        ya = coord[1]
                        xb = coord[2]
                        yb = coord[5]
                elif l < 5:
                        xa = coord[0]
                        ya = coord[1]
                        xb = coord[2]
                        yb = coord[3]
                if ((exa>xa)and(exa<xb))and((eya>ya)and(eya<yb)):
                        name = str(time)+"shape"
                        shape = sheet.type(name)
                        edit = tk.Toplevel()
                        edit.title("Edit"+name) 
                        edit.geometry('300x200')
                        edit.resizable(False,False)
                        f  = tk.StringVar()
                        t  = tk.StringVar()
                        a  = tk.StringVar()
                        rb0 = tk.IntVar()
                        a2 = tk.StringVar()
                        a3 = tk.StringVar()
                        i  = tk.StringVar()
                        #h = tk.StringVar()
                        ma = tk.StringVar()
                        hp0 = tk.StringVar()
                        hp1 = tk.StringVar()
                        hp2 = tk.StringVar()
                        h0 = tk.StringVar()
                        h01 = tk.StringVar()
                        h1 = tk.StringVar()
                        h11 = tk.StringVar()
                        h2 = tk.StringVar()
                        h21 = tk.StringVar()
                        h3 = tk.StringVar()
                        h31 = tk.StringVar()
                        iff1 = tk.StringVar()
                        iff2 = tk.StringVar()
                        iff3 = tk.StringVar()
                        mid0 = tk.StringVar()
                        mid1 = tk.StringVar()
                        mid2 = tk.StringVar()
                        mid3 = tk.StringVar()
                        colorcom = ttk.Combobox(edit,width = 17)
                        colorcom['value'] = colors
                        color_lab = ttk.Label(edit, text = "Shape Color")
                        color_lab.place(x = 10,y =20)
                        colorcom.place(x = 170 , y = 20)
                        texcol = ttk.Combobox(edit , width = 17)
                        texcol['value'] = colors
                        texcol.place(x = 170, y = 40)
                        texcol_lab = ttk.Label(edit, text = "Text Color")
                        texcol_lab.place(x = 10,y =40)
            # Changes
                        def changes():
                            col = colorcom.get()
                            if col == '':
                                None
                            else:
                                sheet.itemconfig(str(time)+"shape", fill = col)
                            texco = texcol.get()
                            if texco == '':
                                None
                            else:
                                try:
                                    sheet.itemconfig(str(time)+"text", fill = texco)
                                except:
                                    None
                    # If Oval
                            if shape == 'oval':
                                tex = a.get()
                                if tex == '':
                                    None
                                else:
                                    sheet.itemconfig(str(time)+"text", text = tex)
                                    render.itemconfig("from"+str(time) , text = tex)
                    # If Rectangle
                            if shape == 'rectangle':
                                pr1 = a.get()
                                pr2 = a2.get()
                                pr3 = a3.get()
                                if pr1 == "":
                                    None
                                elif pr2 == "":
                                    sheet.itemconfig(str(time)+"text",text = hp0.get()+"="+pr1)
                                    render.itemconfig('from'+str(time),text = hp0.get()+"="+pr1)
                                elif pr3 == "":
                                    mm = hp0.get()+"="+pr1 + "\n"+ hp1.get()+"="+pr2
                                    sheet.itemconfig(str(time)+"text",text = mm)
                                    render.itemconfig('from'+str(time),text = mm)
                                elif not(pr3 == ""):
                                    mm = hp0.get()+"="+pr1 + "\n"+hp1.get()+"="+pr2 + "\n"+ hp2.get()+"="+pr3
                                    sheet.itemconfig(str(time)+"text",text = mm)
                                    render.itemconfig('from'+str(time),text = mm)
                                else:
                                    mm = "ERROR"
                                    sheet.itemconfig(str(time)+"text",text = mm)
                        # If Pol#ygon
                            if shape == 'polygon':
                                coord = sheet.coords(name)
                                y1 = coord[1]
                                y2 = coord[3]
                                y3 = coord[5]
                                y4 = coord[7]
                    # If Inout window
                                if (y2 == y1)and(y4==y3):
                                    tex = a.get()
                                    tex2 = a2.get()
                                    if (ctext.get() == True)and(cvar.get() == False):
                                        try:
                                            printer = tex2.replace("'","")
                                        except:
                                            try:

                                                printer= a2.get().replace('"',"")
                                            except:
                                                printer = a2.get()
                                        printer = '"'+printer+'"'
                                    else:
                                        printer = a2.get()
                                    if (not(tex == ""))and(not(tex2 == "")):
                                        if '"' in tex:
                                            tex = tex.replace('"',"")
                                        if '"' in tex:
                                            tex = tex.replace("'","")
                                        if rb0.get() == 0:
                                            mm = i.get()+" = " + "input("+'"'+tex+'"'+")"+"\n"+"print("+printer+")"
                                        else:
                                            mm = i.get()+" = " + "int(input("+'"'+tex+'"'+")"+"\n"+"print("+printer+"))"
                                        sheet.itemconfig(str(time)+"text", text = mm)
                                        render.itemconfig('from'+str(time),text = mm)
                                    elif (not(tex2 == "")):
                                        mm = "print("+printer+")"
                                        sheet.itemconfig(str(time)+"text", text = mm)
                                        render.itemconfig('from'+str(time),text = mm)
                                    elif (not(tex == "")):
                                        if '"' in tex:
                                            tex = tex.replace('"',"")
                                        if '"' in tex:
                                            tex = tex.replace("'","")  
                                        if rb0.get() == 0:
                                            mm = i.get()+" = " + "input("+'"'+tex+'"'+")"
                                        else:
                                            mm = i.get()+" = " + "int(input("+'"'+tex+'"'+"))"
                                        sheet.itemconfig(str(time)+"text", text = mm)
                                        render.itemconfig('from'+str(time),text = mm)
                    # If Else Window
                                else:
                                    yh0   = h0.get()
                                    yh1   = h1.get()
                                    yh2   = h2.get()
                                    yh3   = h3.get()
                                    yiff1 = iff1.get()
                                    yiff2 = iff2.get()
                                    yiff3 = iff3.get()
                                    if faith == 3 :
                                        mm = "if (("+yh0+mid0.get()+h01.get()+")"+yiff1+"("+yh1+mid1.get()+h11.get()+"))"+yiff2+"(("+yh2+mid2.get()+h21.get()+")"+yiff3+"("+yh3+mid3.get()+h31.get()+")) :"
                                        sheet.itemconfig(str(time)+"text", text = mm)
                                        render.itemconfig('from'+str(time),text = mm)
                                    elif faith == 2 :
                                        mm = "if (("+yh0+mid0.get()+h01.get()+")"+yiff1+"("+yh1+mid1.get()+h11.get()+"))"+yiff2+"("+yh2+mid2.get()+h21.get()+") :"
                                        sheet.itemconfig(str(time)+"text", text = mm)
                                        render.itemconfig('from'+str(time),text = mm)
                                    elif faith == 1 :
                                        mm = "if (("+yh0+mid0.get()+h01.get()+")"+yiff1+"("+yh1+mid1.get()+h11.get()+")):"
                                        sheet.itemconfig(str(time)+"text", text = mm)
                                        render.itemconfig('from'+str(time),text = mm)
                                    elif not(yh0 == ""):
                                        mm = "if "+yh0+mid0.get()+h01.get()+" :"
                                        sheet.itemconfig(str(time)+"text", text = mm)
                                        render.itemconfig('from'+str(time),text = mm)
            # Window
                # If Oval Window                         
                        if shape == 'oval':
                            tex  = ttk.Entry(edit , textvar = a)
                            tex.focus()
                            tex.place(x = 170 , y = 60)
                            tex_lab = tk.Label(edit, text = "Text")
                            tex_lab.place(x = 10,y=60)
                # If rectangle Window
                        if shape == 'rectangle':
                            # Process 1
                            tex = ttk.Entry(edit , textvar = hp0,width = 4)
                            tex.focus()
                            tex.place(x = 170 , y = 60)
                            tex = ttk.Entry(edit , textvar = a,width = 10)
                            tex.place(x = 229 , y = 60)
                            tex_lab = ttk.Label(edit, text = "Process")
                            tex_lab.place(x = 10,y =60)
                            tex_lab = ttk.Label(edit, text = " = ")
                            tex_lab.place(x = 205,y =61)
                            # Process 2
                            tex = ttk.Entry(edit , textvar = hp1,width = 4)
                            tex.place(x = 170 , y = 80)
                            tex = ttk.Entry(edit , textvar = a2,width = 10)
                            tex.place(x = 229 , y = 80)
                            tex_lab = ttk.Label(edit, text = "Process 2")
                            tex_lab.place(x = 10,y =80)
                            tex_lab = ttk.Label(edit, text = " = ")
                            tex_lab.place(x = 205,y =80)
                            # Process 3
                            tex = ttk.Entry(edit , textvar = hp2,width = 4)
                            tex.place(x = 170 , y = 100)
                            tex = ttk.Entry(edit , textvar = a3,width = 10)
                            tex.place(x = 229 , y = 100)
                            tex_lab = ttk.Label(edit, text = "Process 3")
                            tex_lab.place(x = 10,y =100)
                            tex_lab = ttk.Label(edit, text = " = ")
                            tex_lab.place(x = 205,y =100)
                # If Polygon Window
                        if shape =='polygon':
                            # Input
                            coord = sheet.coords(name)
                            y1 = coord[1]
                            y2 = coord[3]
                            y3 = coord[5]
                            y4 = coord[7]
                # If Inout window
                            if (y2 == y1)and(y4==y3):
                                # input Var
                                tex = ttk.Entry(edit ,width = 3, textvar = i)
                                tex.focus()
                                tex.place(x = 107 , y = 60)
                                tex_lab = ttk.Label(edit, text = " = ")
                                tex_lab.place(x = 140,y =57)
                                # Input
                                tex = ttk.Entry(edit , textvar = a)
                                tex.place(x = 170 , y = 60)
                                tex_lab = ttk.Label(edit, text = f"Input")
                                tex_lab.place(x = 10,y =60)
                                # Int Or String
                                con = ttk.Label(edit,text = "Input Type")
                                con.place(x= 10, y= 83)
                                rb = ttk.Radiobutton(edit,text = "String",variable = rb0,value = 0)
                                rb.place(x =170,y = 83)
                                rb = ttk.Radiobutton(edit,text = "Numeric",variable = rb0,value = 1)
                                rb.place(x =230,y = 83)
                                # output
                                tex = ttk.Entry(edit , textvar = a2)
                                tex.place(x = 170 , y = 105)
                                tex_lab = ttk.Label(edit, text = f"Output")
                                tex_lab.place(x = 10,y =105)
                                ctext = tk.BooleanVar()
                                ctext.set(True)
                                cvar = tk.BooleanVar()
                                cvar.set(True)
                                cb = ttk.Checkbutton(edit,text = "Text",variable = ctext)
                                cb.place(x = 70,y = 105)
                                cb = ttk.Checkbutton(edit,text = "Vars",variable = cvar)
                                cb.place(x = 120,y = 105)
                # If if:else: Window
                            else:
                                # Entry
                                symbols = ['(None)','==','!=','>','<','>=','<=']
                                tex = ttk.Label(edit,text = "if ",font = ('Bold'))
                                tex.place(x = 13 ,y = 65)
                                tex = ttk.Entry(edit ,width = 15, textvar = h0)
                                tex.focus()
                                tex.place(x = 37 , y = 65)
                                join = ttk.OptionMenu(edit,mid0,*symbols)
                                mid0.set('==')
                                join.place(x= 134,y = 64)
                                tex = ttk.Entry(edit ,width = 15, textvar = h01)
                                tex.place(x = 185 , y = 65)
                                then = ttk.Label(edit,text = ":",font = ('Bold'))
                                then.place(x= 290,y = 64)
                                def add():
                                    global faith                                    
                                    faith = faith + 1                                                  
                                    if faith < 2:
                                        join = ttk.OptionMenu(edit,iff1,*['  ','and','or'])
                                        iff1.set('and')
                                        join.place(x= 130,y = 40+(50*faith))
                                        tex = ttk.Entry(edit ,width = 15, textvar = h1)
                                        tex.place(x = 37 , y = 65+(50*faith))
                                        join2 = ttk.OptionMenu(edit,mid1,*symbols)
                                        mid1.set('==')
                                        join2.place(x= 134,y = 64+(50*faith))
                                        tex2 = ttk.Entry(edit ,width = 15, textvar = h11)
                                        tex2.place(x = 185 , y = 65+(50*faith))
                                    elif faith < 3:
                                        join = ttk.OptionMenu(edit,iff2,*['  ','and','or'])
                                        iff2.set('and')
                                        join.place(x= 130,y = 40+(50*faith))
                                        tex2 = ttk.Entry(edit ,width = 15, textvar = h2)
                                        tex2.place(x = 37 , y = 65+(50*faith))
                                        join2 = ttk.OptionMenu(edit,mid2,*symbols)
                                        mid2.set('==')
                                        join2.place(x= 134,y = 64+(50*faith))
                                        tex = ttk.Entry(edit ,width = 15, textvar = h21)
                                        tex.place(x = 185 , y = 65+(50*faith))
                                    elif faith < 4:
                                        join = ttk.OptionMenu(edit,iff3,*['  ','and','or'])
                                        iff3.set('and')
                                        join.place(x= 130,y = 40+(50*faith))
                                        tex = ttk.Entry(edit ,width = 15, textvar = h3)
                                        tex.place(x = 37 , y = 65+(50*faith))
                                        join2 = ttk.OptionMenu(edit,mid3,*symbols)
                                        mid3.set('==')
                                        join2.place(x= 134,y = 64+(50*faith))
                                        tex2 = ttk.Entry(edit ,width = 15, textvar = h31)
                                        tex2.place(x = 185 , y = 65+(50*faith))
                                    then.place(x= 290,y = 64+(50*faith))
                                    if faith < 3 :
                                        add.place(x = 90,y= 90+(50*faith))
                                        edit.geometry('300x'+str(200+(50*faith)))
                                        ok.place(x = 10, y = 150+(50*faith))
                                        close.place(x = 200, y = 150+(50*faith))
                                    else:
                                        add.destroy()
                                add = ttk.Button(edit,text = "Add another Condition",command = add)
                                add.place(x = 90 ,y = 90)
            # End of the Editing
                        def changer(event):
                            changes()
                            edit.destroy()
                        edit.bind('<Return>',changer)
                        ok = ttk.Button(edit, text = "Ok", width = 10 ,command = changes)
                        ok.place(x = 20 , y = 150)
                        close = ttk.Button(edit, text = "Close", width = 10 ,command = edit.destroy)
                        close.place(x = 200 , y = 150)
                        edit.mainloop() 
                        time = -1
                        break
# Event Delete
def delete(event):
        global time,n
        ex = event.x
        ey = event.y
        clickcoord = [ex,ey]
        exa = clickcoord[0]
        eya = clickcoord[1]
        while int(time) <= int(n):
                time = int(time) + 1
                coord = sheet.coords(str(time)+"shape")
                l = len(coord)
                if l < 2 :
                        print("out")
                        time = -1
                        # click = -1
                        break
                elif l > 5:
                        xa = coord[6]
                        ya = coord[1]
                        xb = coord[2]
                        yb = coord[5]
                elif l < 5:
                        xa = coord[0]
                        ya = coord[1]
                        xb = coord[2]
                        yb = coord[3]
                else:
                        print("no")
                if (((exa>xa)and(exa<xb))and((eya>ya)and(eya<yb))):
                    if time == n:
                        name = str(time)+"shape"
                        text = str(time)+"text"
                        time = -1
                        confirm = tk.messagebox.askyesno(f"Delete",f"Doyou want to Delete?")
                        if confirm == True:
                            sheet.delete(name)
                            sheet.delete(text)
                            n = n-1
                            break
                        else:
                            break
                    else:
                         tk.messagebox.showwarning("Delete","You can Delete the Last Shape only")
# Id Counter            
def counter():
    global n
    n = int(n)+1
# Begin Shape
def begin():
    counter()
    global n,offx,offy,plusx,pos,nw,xw,joints
    if n >43:
        tk.messagebox.showinfo("Out of Range","Maximum flow amount is 42")
        n = n -1   
    else:
        pos = pos + 1
        if pos > 7:
            plusx = plusx + 150
            pos = 0
        nw = nw + 1
        if nw > 21:
            xw = xw + 210
            nw = 0
        d = nw
        b = xw
        Id = "Begin_"+str(n)
        (1,"Begin")
        x1 = ((250+plusx)*offz)+offx
        y1 = ((10+ 100*pos)*offz)+offy
        x2 = ((350+plusx)*offz)+offx
        y2 = ((60+ 100*pos)*offz)+offy
        xc = ((int(x2)-int(x1))//2)+x1
        yc = ((int(y2)-int(y1))//2)+y1
        n = str(n)
        sheet.create_oval(x1 ,y1,x2,y2 ,fill = "blue", activefill = "gray",tag = n+"shape")                    
        sheet.create_text( xc,yc,text = "BEGIN",font = "bold",fill = "white",tag = n+"text")
        text = render.create_text(15,10,text = "# Begin", tag = "from"+str(n))
        joints = joints + 1
        items.append(Id)
        n = int(n)
        lab = ttk.Label(main, text = items[n+2])
        lab.place(x=730+b,y = 14+30*nw)
        c = n
        f = tk.StringVar()
        l2 = 0
        def join():
            global l2,joints
            joiner = sheet.create_line(0,0,0,0,width = 3)
            def x():
                global l2,joints
                l = f.get()
                if "Begin_" in str(l):
                    l = l.replace("Begin_","")
                elif "In/Out_" in str(l):
                    l = l.replace("In/Out_","")
                elif "Process_" in str(l):
                    l = l.replace("Process_","")
                elif "Ifs_" in str(l):
                    l = l.replace("Ifs_","")
                elif "End_" in str(l):
                    l = l.replace("End_","")
                elif "(None)" in str(l):
                    print("none")
                    l = "None_"                
                coord = sheet.coords(str(l)+"shape")
                l2 = len(coord)                     
                if int(l2) > 5:
                        xa = coord[6]
                        ya = coord[1]
                        xb = coord[2]
                        #yb = coord[5]
                elif int(l2) < 5:
                        xa = coord[0]
                        ya = coord[1]
                        xb = coord[2]
                        #yb = coord[3]
                coord2 = sheet.coords(str(c)+"shape")
                b = len(coord2)                       
                if b > 5:
                        x1 = coord2[6]
                        #y1 = coord2[1]
                        x2 = coord2[2]
                        y2 = coord2[5]
                elif b < 5:
                        x1 = coord2[0]
                        #y1 = coord2[1]
                        x2 = coord2[2]
                        y2 = coord2[3]
                if l == "None_":
                    sheet.coords(joiner,0,0,0,0)
                    sheet.itemconfig(joiner,tag = ("from"+str(l),"to"+str(l)))
                else:
                    sheet.coords(joiner,(x2-x1)+x1-(50*offz),y2,(xb-xa)+xa-(50*offz),ya)
                    sheet.itemconfig(joiner,tag = ("from"+str(c),"to"+str(l)))
                    render.itemconfig(text,tag = ("from"+str(c),"to"+str(l)))
                        
            def y():
                b2 = ttk.Button(main,text = "Ok",command = x,width = 5)
                b2.place(x = 895+b,y = 12+30*d)
            b1.destroy()
            con = ttk.OptionMenu(main,f,*items,command = y())
            f.set("Connect To")
            con.config(width = 10)
            con.place(x=800+b,y = 12+30*d)
        b1 = ttk.Button(main,text = "Connect",command = join)
        b1.place(x=800+b,y = 12+30*nw)
# Inout Shape
def inout():
    counter()
    global n,offx,offy,plusx,pos,nw,xw,joints
    if n >43:
        tk.messagebox.showinfo("Out of Range","Maximum flow amount is 42")
        n = n -1
    else:
        pos = pos + 1
        if pos > 7:
            plusx = plusx + 150
            pos = 0
        nw = nw + 1
        if nw > 21:
            xw = xw + 195
            nw = 0
        d = nw
        b = xw
        x1 = ((266+plusx)*offz)+offx
        y1 = ((10+pos*100)*offz)+offy
        x2 = ((366+plusx)*offz)+offx
        y2 = y1
        x3 = ((336+plusx)*offz)+offx
        y3 = ((60+pos*100)*offz)+offy
        x4 = ((236+plusx)*offz)+offx
        y4 = y3
        xc = ((int(x2)-int(x4))//2)+x4
        yc = ((int(y4)-int(y1))//2)+y1
        sheet.create_polygon((x1 ,y1),(x2,y2),(x3,y3),(x4,y4) ,fill = "green", activefill = "gray",outline = "Black",tag = str(n)+"shape")
        sheet.create_text( xc,yc,text = "In/Outputs",font = ("bold",10),fill = "white", justify = 'center',tag = str(n)+"text")
        text = render.create_text(15,10,text = "# Inout", tag = "from"+str(n))
        joints = joints + 1
        items.append("In/Out_"+str(n))
        n = int(n)
        lab = ttk.Label(main, text = "In/out_"+str(n))
        lab.place(x=730+xw,y = 14+30*nw)
        f = tk.StringVar()
        c = n
        def join():
            global joints
            joiner = sheet.create_line(0,0,0,0,width = 3)
            def x():
                 global joints
                 l = f.get()
                 if "Begin_" in str(l):
                     l = l.replace("Begin_","")
                 elif "In/Out_" in str(l):
                     l = l.replace("In/Out_","")
                 elif "Process_" in str(l):
                     l = l.replace("Process_","")
                 elif "Ifs_" in str(l):
                     l = l.replace("Ifs_","")
                 elif "End_" in str(l):
                     l = l.replace("End_","")
                 elif "(None)" in str(l):
                    print("none")
                    l = "None_"  
                 coord = sheet.coords(str(l)+"shape")
                 l2 = len(coord)                       
                 if l2> 5:
                         xa = coord[6]
                         ya = coord[1]
                         xb = coord[2]
                         #yb = coord[5]
                 elif l2 < 5:
                         xa = coord[0]
                         ya = coord[1]
                         xb = coord[2]
                         #yb = coord[3]
                 coord2 = sheet.coords(str(c)+"shape")
                 b = len(coord2)                       
                 if b > 5:
                         x1 = coord2[6]
                         #y1 = coord2[1]
                         x2 = coord2[2]
                         y2 = coord2[5]
                 elif b < 5:
                         x1 = coord2[0]
                         #y1 = coord2[1]
                         x2 = coord2[2]
                         y2 = coord2[3]
                 if l == "None_":
                    sheet.coords(joiner,0,0,0,0)
                    sheet.itemconfig(joiner,tag = ("from"+str(l),"to"+str(l)))
                 else:
                    sheet.coords(joiner,(x2-x1)+x1-(50*offz),y2,(xb-xa)+xa-(50*offz),ya)
                    sheet.itemconfig(joiner,tag = ("from"+str(c),"to"+str(l)))
                    render.itemconfig(text,tag = ("from"+str(c),"to"+str(l)))
            def y():
                b2 = ttk.Button(main,text = "Ok",command = x,width = 5)
                b2.place(x = 895+b,y = 12+30*d)
                #sheet.bind('<B1-Motion>',x)
            b1.destroy()
            con = ttk.OptionMenu(main,f,*items,command = y())
            f.set("Connect To")
            con.config(width = 10)
            con.place(x=800+b,y = 12+30*d)
        b1 = ttk.Button(main,text = "Connect",command = join)
        b1.place(x=800+b,y = 12+30*nw)
# If Shape
def ifs():
    counter()
    global n,offx,offy,plusx,pos,nw,xw,joints
    if n >43:
        tk.messagebox.showinfo("Out of Range","Maximum flow amount is 42")
        n = n -1
    else:
        pos = pos + 1
        if pos > 7:
            plusx = plusx + 150
            pos = 0
        x1 = ((300+plusx)*offz)+offx
        y1 = ((5+pos*100)*offz)+offy
        x2 = ((350+plusx)*offz)+offx
        y2 = ((40+pos*100)*offz)+offy
        x3 = x1
        y3 = ((75+pos*100)*offz)+offy
        x4 = ((250+plusx)*offz)+offx
        y4 = y2
        xc = ((int(x2)-int(x4))//2)+x4
        yc = ((int(y3)-int(y1))//2)+y1
        sheet.create_polygon((x1 ,y1),(x2,y2),(x3,y3),(x4,y4) ,fill = "red", activefill = "gray",outline = "Black",tag = str(n)+"shape")
        sheet.create_text( xc,yc,text = "If:\nElse:",font = ("bold",10),fill = "white", justify = 'center',tag = str(n)+"text")
        text = render.create_text(15,10,text = "# if", tag = "from"+str(n))
        text2 = render.create_text(15,10,text = "# else", tag = "from"+str(int(n)+50))
        joints = joints + 1
        items.append("Ifs_"+str(n))
        n = int(n)
        # If
        nw = nw + 2
        if nw > 21:
            xw = xw + 195
            nw = 0
        d = nw
        b = xw
        de = nw -1
        be = xw
        lab = ttk.Label(main, text = items[n+2])
        lab.place(x=730+be,y = 14+30*de)
        lab = ttk.Label(main, text = "Else_"+str(n))
        lab.place(x=730+b,y = 14+30*d)
        f = tk.StringVar()
        fe = tk.StringVar()
        c = n
        def join():
            global joints
            joiner = sheet.create_line(0,0,0,0,width = 3)
            def x():
                 global joints
                 l = f.get()
                 if "Begin_" in str(l):
                     l = l.replace("Begin_","")
                 elif "In/Out_" in str(l):
                     l = l.replace("In/Out_","")
                 elif "Process_" in str(l):
                     l = l.replace("Process_","")
                 elif "Ifs_" in str(l):
                     l = l.replace("Ifs_","")
                 elif "End_" in str(l):
                     l = l.replace("End_","")
                 elif "(None)" in str(l):
                    print("none")
                    l = "None_"  
                 coord = sheet.coords(str(l)+"shape")
                 l2 = len(coord)                       
                 if l2> 5:
                         xa = coord[6]
                         ya = coord[1]
                         xb = coord[2]
                         #yb = coord[5]
                 elif l2 < 5:
                         xa = coord[0]
                         ya = coord[1]
                         xb = coord[2]
                         #yb = coord[3]
                 coord2 = sheet.coords(str(c)+"shape")
                 b = len(coord2)                       
                 if b > 5:
                         x1 = coord2[6]
                         #y1 = coord2[1]
                         x2 = coord2[2]
                         y2 = coord2[5]
                 elif b < 5:
                         x1 = coord2[0]
                         #y1 = coord2[1]
                         x2 = coord2[2]
                         y2 = coord2[3]
                 if l == "None_":
                    sheet.coords(joiner,0,0,0,0)
                    sheet.itemconfig(joiner,tag = ("from"+str(l),"to"+str(l)))
                 else:
                    sheet.coords(joiner,(x2-x1)+x1-(50*offz),y2,(xb-xa)+xa-(50*offz),ya)
                    sheet.itemconfig(joiner,tag = ("from"+str(c),"to"+str(l),"if"+str(c)))
                    render.itemconfig(text,tag = ("from"+str(c),"to"+str(l),"if"+str(c)))
            def y():
                b2 = ttk.Button(main,text = "Ok",command = x,width = 5)
                b2.place(x = 895+be,y = 12+30*de)
                #sheet.bind('<B1-Motion>',x)
            b1.destroy()
            con = ttk.OptionMenu(main,f,*items,command = y())
            f.set("Connect To")
            con.config(width = 10)
            con.place(x=800+be,y = 12+30*de)
        def joine():
            global joints
            joiner = sheet.create_line(0,0,0,0,width = 3)
            def xe():
                 global joints
                 l = fe.get()
                 if "Begin_" in str(l):
                     l = l.replace("Begin_","")
                 elif "In/Out_" in str(l):
                     l = l.replace("In/Out_","")
                 elif "Process_" in str(l):
                     l = l.replace("Process_","")
                 elif "Ifs_" in str(l):
                     l = l.replace("Ifs_","")
                 elif "End_" in str(l):
                     l = l.replace("End_","")
                 elif "(None)" in str(l):
                    print("none")
                    l = "None_"  
                 coord = sheet.coords(str(l)+"shape")
                 l2 = len(coord)                       
                 if l2> 5:
                         xa = coord[6]
                         ya = coord[1]
                         xb = coord[2]
                         #yb = coord[5]
                 elif l2 < 5:
                         xa = coord[0]
                         ya = coord[1]
                         xb = coord[2]
                         #yb = coord[3]
                 coord2 = sheet.coords(str(c)+"shape")
                 b = len(coord2)                       
                 if b > 5:
                         #x1 = coord2[6]
                         #y1 = coord2[1]
                         x2 = coord2[2]
                         y2 = coord2[5]
                 elif b < 5:
                         #x1 = coord2[0]
                         #y1 = coord2[1]
                         x2 = coord2[2]
                         y2 = coord2[3]
                 if l == "None_":
                    sheet.coords(joiner,0,0,0,0)
                    sheet.itemconfig(joiner,tag = ("from"+str(l),"to"+str(l)))
                 else:
                    sheet.coords(joiner,x2,y2-35*offz,(xb-xa)+xa-(50*offz),ya)
                    sheet.itemconfig(joiner,tag = ("to"+str(l),"else"+str(c),"elseb"+str(l)))
                    render.itemconfig(text2,text = "else:",tag = ("from"+str(int(c)+50),"to"+str(l)))
            def ye():
                b2 = ttk.Button(main,text = "Ok",command = xe,width = 5)
                b2.place(x = 895+b,y = 12+30*d)
                #sheet.bind('<B1-Motion>',x)
            b2.destroy()
            con = ttk.OptionMenu(main,fe,*items,command = ye())
            fe.set("Connect To")
            con.config(width = 10)
            con.place(x=800+b,y = 12+30*d)
        b1 = ttk.Button(main,text = "Connect",command = join)
        b1.place(x=800+be,y = 12+30*de)
        b2 = ttk.Button(main,text = "Connect",command = joine)
        b2.place(x=800+b,y = 12+30*d)
# Process Shape
def proc():
    counter()
    global n,offx,offy,offz,plusx,pos,xw,nw,joints
    if n >43:
        tk.messagebox.showinfo("Out of Range","Maximum flow amount is 42")
        n = n -1
    else:
        pos = pos + 1
        if pos > 7:
            plusx = plusx + 150
            pos = 0
        nw = nw + 1
        if nw > 21:
            xw = xw + 195
            nw = 0
        x1 = ((250+plusx)*offz)+offx
        y1 = ((7+pos*100)*offz)+offy
        x2 = ((350+plusx)*offz)+offx
        y2 = ((60+pos*100)*offz)+offy
        xc = ((int(x2)-int(x1))//2)+x1
        yc = ((int(y2)-int(y1))//2)+y1
        sheet.create_rectangle(x1 ,y1,x2,y2 ,fill = "orange",activefill = "gray",tag = str(n)+"shape")
        sheet.create_text( xc,yc,text = "Process",font =("bold",10),fill = "white",tag = str(n)+"text")
        text = render.create_text(15,10,text = "# Proc", tag = "from"+str(n))
        joints = joints + 1
        items.append("Process_"+str(n))
        n = int(n)
        lab = ttk.Label(main, text = "Process_"+str(n))
        lab.place(x=730+xw,y = 14+30*nw)
        c = n
        d = nw
        b = xw
        f = tk.StringVar()
        def join():
            global joints
            joiner = sheet.create_line(0,0,0,0,width = 3)
            def x():
                 global joints
                 l = f.get()
                 if "Begin_" in str(l):
                     l2 = l.replace("Begin_","")
                 elif "In/Out_" in str(l):
                     l2 = l.replace("In/Out_","")
                 elif "Process_" in str(l):
                     l2 = l.replace("Process_","")
                 elif "Ifs_" in str(l):
                     l2 = l.replace("Ifs_","")
                 elif "End_" in str(l):
                     l2 = l.replace("End_","")
                 elif "(None)" in str(l):
                    print("none")
                    l2 = "None_"  
                 coord = sheet.coords(str(l2)+"shape")
                 l = len(coord)                       
                 if l > 5:
                         xa = coord[6]
                         ya = coord[1]
                         xb = coord[2]
                         #yb = coord[5]
                 elif l < 5:
                         xa = coord[0]
                         ya = coord[1]
                         xb = coord[2]
                         #yb = coord[3]
                 coord2 = sheet.coords(str(c)+"shape")
                 b = len(coord2)                       
                 if b > 5:
                         x1 = coord2[6]
                         #y1 = coord2[1]
                         x2 = coord2[2]
                         y2 = coord2[5]
                 elif b < 5:
                         x1 = coord2[0]
                         #y1 = coord2[1]
                         x2 = coord2[2]
                         y2 = coord2[3]
                 if l == "None_":
                    sheet.coords(joiner,0,0,0,0)
                    sheet.itemconfig(joiner,tag = ("from"+str(l2),"to"+str(l2)))
                 else:
                    sheet.coords(joiner,(x2-x1)+x1-(50*offz),y2,(xb-xa)+xa-(50*offz),ya)
                    sheet.itemconfig(joiner,tag = ("from"+str(c),"to"+str(l2)))
                    render.itemconfig(text,tag = ("from"+str(c),"to"+str(l2)))
            def y():
                b2 = ttk.Button(main,text = "Ok",command = x,width = 5)
                b2.place(x = 895+b,y = 12+30*d)
            b1.destroy()
            con = ttk.OptionMenu(main,f,*items,command = y())
            f.set("Connect To")
            con.config(width = 10)
            con.place(x=800+b,y = 12+30*d)
        b1 = ttk.Button(main,text = "Connect",command = join)
        b1.place(x=800+xw,y = 12+30*nw)
# End Shape
def end():
    counter()
    global n,offx,offy,plusx,pos,nw,xw,joints
    if n >43:
        tk.messagebox.showinfo("Out of Range","Maximum flow amount is 42")
        n = n -1   
    else:
        pos = pos + 1
        if pos > 7:
            plusx = plusx + 150
            pos = 0
        nw = nw + 1
        if nw > 21:
            xw = xw + 210
            nw = 0
        b = xw
        Id = "End_"+str(n)
        x1 = ((250+plusx)*offz)+offx
        y1 = ((10+ 100*pos)*offz)+offy
        x2 = ((350+plusx)*offz)+offx
        y2 = ((60+ 100*pos)*offz)+offy
        xc = ((int(x2)-int(x1))//2)+x1
        yc = ((int(y2)-int(y1))//2)+y1
        n = str(n)
        sheet.create_oval(x1 ,y1,x2,y2 ,fill = "dark blue", activefill = "gray",tag = n+"shape")                    
        sheet.create_text( xc,yc,text = "END",font = "bold",fill = "white",tag = n+"text")
        items.append(Id)
        n = int(n)
        lab = ttk.Label(main, text = "End_"+str(n))
        lab.place(x=730+b,y = 14+30*nw)
def b(event):
    begin()
def g(event):
    inout()
def i(event):
    ifs()
def p(event):
    proc()
def e(event):
    end()
def rendererb(event):
    renderer()
sheet.bind('<Button-1>',b1click)                 
sheet.bind('<B1-Motion>',recoords)
sheet.bind('<Double-Button-1>',double_tap)     
sheet.bind('<Button-3>',delete)                   
main.bind('<Left>',right)                         
main.bind('<Right>',left)                         
main.bind('<Up>',down)                            
main.bind('<Down>',up)                            
main.bind('<Control-Up>',zoomin)              
main.bind('+',zoomin)                         
main.bind('<Control-Down>',zoomout)           
main.bind('<Control-i>',i)                    
main.bind('<Control-b>',b)                     
main.bind('<Control-g>',g)
main.bind('<Control-p>',p)
main.bind('<Control-e>',e)
main.bind('<Control-r>',rendererb) 
main.bind('<Control-q>',destroyer)       
f = tk.Button(main, text = "Begin" ,width = 10 ,bg = "blue",fg = "White",command = begin)
f.place(x = 20,y = 50)
f = tk.Button(main, text = "input/output" ,width = 10 ,bg = "green",fg = "White", command = inout)
f.place(x = 20,y = 100)
f = tk.Button(main, text = "If:else:" ,width = 10 ,bg = "red",fg = "White", command = ifs)
f.place(x = 20,y = 150)
f = tk.Button(main, text = "Process" ,width = 10 ,bg = "orange",fg = "White", command = proc)
f.place(x = 20,y = 200)
f = tk.Button(main, text = "End" ,width = 10 ,bg = "dark blue",fg = "White", command = end)
f.place(x = 20,y = 250)
#yl = sheet.create_text(300,300,text = "{Y}",font = ("Berlin Sans FB Demi",200),fill = "white")
statusbar = tk.Label(main,text= " ",width = 1000)
statusbar.place(x = 0, y = 680)  # Status Bar
f = tk.Button(main,text = "Scale ",command = rescale,border = 0)
f.place(x = 0, y = 680)
f = tk.Label(main,text = "100.00%",width = 10)
f.place(x = 30,y = 680)
f = tk.Label(main,text = "X:"+str(offx) + " , "+"Y:"+str(offy),width = 20)
f.place(x = 610, y = 680)
f = ttk.Button(main, text = "Quit" , command = main.destroy)
f.place(x = 850,y = 670)
f = ttk.Button(main, text = "Render" , command = renderer)
f.place(x = 950,y = 670)

menu = tk.Menu(main) 
main.config(menu=menu) 
filemenu = tk.Menu(menu, tearoff = 0) 
menu.add_cascade(    label='File', menu=filemenu) 
filemenu.add_command(label='New Flow Cahart    Ctrl+N') 
filemenu.add_command(label='Save                          Ctrl+S') 
filemenu.add_command(label='Render                      Ctrl+R',command = renderer) 
filemenu.add_separator() 
filemenu.add_command(label='Exit                          Ctrl+Q', command=main.destroy) 
helpmenu = tk.Menu(menu , tearoff = 0) 
menu.add_cascade(    label='Help', menu=helpmenu) 
helpmenu.add_command(label='About Flow Chart')

main.mainloop()
