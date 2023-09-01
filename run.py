from tkinter.constants import CENTER, DISABLED, GROOVE, HORIZONTAL, LEFT, RIDGE, RIGHT, W
from typing_extensions import IntVar
import scrambler
import conf
import tkinter as tk


def update_prefs():
    conf.dontUseCorners[0] = dont_use_entries[6].get()
    conf.dontUseCorners[1] = dont_use_entries[8].get()
    conf.dontUseCorners[2] = dont_use_entries[2].get()
    conf.dontUseCorners[3] = dont_use_entries[0].get()

    conf.dontUseCorners[4] = dont_use_entries[45].get()
    conf.dontUseCorners[5] = dont_use_entries[47].get()
    conf.dontUseCorners[6] = dont_use_entries[53].get()
    conf.dontUseCorners[7] = dont_use_entries[51].get()

    conf.dontUseCorners[8] = dont_use_entries[18].get()
    conf.dontUseCorners[9] = dont_use_entries[27].get()
    conf.dontUseCorners[10] = dont_use_entries[36].get()
    conf.dontUseCorners[11] = dont_use_entries[9].get()

    conf.dontUseCorners[12] = dont_use_entries[17].get()
    conf.dontUseCorners[13] = dont_use_entries[26].get()
    conf.dontUseCorners[14] = dont_use_entries[35].get()
    conf.dontUseCorners[15] = dont_use_entries[44].get()

    conf.dontUseCorners[16] = dont_use_entries[11].get()
    conf.dontUseCorners[17] = dont_use_entries[20].get()
    conf.dontUseCorners[18] = dont_use_entries[29].get()
    conf.dontUseCorners[19] = dont_use_entries[38].get()

    conf.dontUseCorners[20] = dont_use_entries[24].get()
    conf.dontUseCorners[21] = dont_use_entries[33].get()
    conf.dontUseCorners[22] = dont_use_entries[42].get()
    conf.dontUseCorners[23] = dont_use_entries[15].get()


    conf.dontUseEdges[0] = dont_use_entries[3].get()
    conf.dontUseEdges[1] = dont_use_entries[7].get()
    conf.dontUseEdges[2] = dont_use_entries[5].get()
    conf.dontUseEdges[3] = dont_use_entries[1].get()

    conf.dontUseEdges[4] = dont_use_entries[21].get()
    conf.dontUseEdges[5] = dont_use_entries[23].get()
    conf.dontUseEdges[6] = dont_use_entries[39].get()
    conf.dontUseEdges[7] = dont_use_entries[41].get()

    conf.dontUseEdges[8] = dont_use_entries[48].get()
    conf.dontUseEdges[9] = dont_use_entries[46].get()
    conf.dontUseEdges[10] = dont_use_entries[50].get()
    conf.dontUseEdges[11] = dont_use_entries[52].get()

    conf.dontUseEdges[12] = dont_use_entries[10].get()
    conf.dontUseEdges[13] = dont_use_entries[19].get()
    conf.dontUseEdges[14] = dont_use_entries[28].get()
    conf.dontUseEdges[15] = dont_use_entries[37].get()

    conf.dontUseEdges[16] = dont_use_entries[14].get()
    conf.dontUseEdges[17] = dont_use_entries[30].get()
    conf.dontUseEdges[18] = dont_use_entries[32].get()
    conf.dontUseEdges[19] = dont_use_entries[12].get()

    conf.dontUseEdges[20] = dont_use_entries[16].get()
    conf.dontUseEdges[21] = dont_use_entries[25].get()
    conf.dontUseEdges[22] = dont_use_entries[34].get()
    conf.dontUseEdges[23] = dont_use_entries[43].get()

    conf.moveEdgeCount = sc_edgeSwapCount.get()
    conf.allowEdgeCycles = var1.get()
    conf.edgeTwistCount = 0

    conf.moveCornerCount = sc_cornerSwapCount.get()
    conf.allowCornerCycles = var2.get()
    conf.cornerTwistCount = 0

    conf.cornerBuffer = corner_buffer_list.index(cornerBufferVar.get())
    conf.edgeBuffer = edge_buffer_list.index(edgeBufferVar.get())
    conf.saveConf()

def btn_pressed():
    global sequence
    update_prefs()
    sequence, scramble = scrambler.getScramble(conf.moveEdgeCount, conf.allowEdgeCycles, conf.dontUseEdges, conf.edgeTwistCount, conf.moveCornerCount, conf.allowCornerCycles, conf.dontUseCorners, conf.cornerTwistCount)
    if scramble == None:
        scramble = 'Scramble not possible with such settings'
    else:
        moves = scramble.count(' ')
        for _ in range(1):
            _sequence, _scramble = scrambler.getScramble(conf.moveEdgeCount, conf.allowEdgeCycles, conf.dontUseEdges, conf.edgeTwistCount, conf.moveCornerCount, conf.allowCornerCycles, conf.dontUseCorners, conf.cornerTwistCount)
            if moves > _scramble.count(' '):
                sequence, scramble = _sequence, _scramble
                moves = _scramble.count(' ')
    lb_scramble.config(text=scramble)
    toggleSequence()

def loadDontUse():
    dont_use_entries[6].set(conf.dontUseCorners[0])
    dont_use_entries[8].set(conf.dontUseCorners[1])
    dont_use_entries[2].set(conf.dontUseCorners[2])
    dont_use_entries[0].set(conf.dontUseCorners[3])

    dont_use_entries[45].set(conf.dontUseCorners[4])
    dont_use_entries[47].set(conf.dontUseCorners[5])
    dont_use_entries[53].set(conf.dontUseCorners[6])
    dont_use_entries[51].set(conf.dontUseCorners[7])

    dont_use_entries[18].set(conf.dontUseCorners[8])
    dont_use_entries[27].set(conf.dontUseCorners[9])
    dont_use_entries[36].set(conf.dontUseCorners[10])
    dont_use_entries[9].set(conf.dontUseCorners[11])

    dont_use_entries[17].set(conf.dontUseCorners[12])
    dont_use_entries[26].set(conf.dontUseCorners[13])
    dont_use_entries[35].set(conf.dontUseCorners[14])
    dont_use_entries[44].set(conf.dontUseCorners[15])

    dont_use_entries[11].set(conf.dontUseCorners[16])
    dont_use_entries[20].set(conf.dontUseCorners[17])
    dont_use_entries[29].set(conf.dontUseCorners[18])
    dont_use_entries[38].set(conf.dontUseCorners[19])

    dont_use_entries[24].set(conf.dontUseCorners[20])
    dont_use_entries[33].set(conf.dontUseCorners[21])
    dont_use_entries[42].set(conf.dontUseCorners[22])
    dont_use_entries[15].set(conf.dontUseCorners[23])


    dont_use_entries[3].set(conf.dontUseEdges[0])
    dont_use_entries[7].set(conf.dontUseEdges[1])
    dont_use_entries[5].set(conf.dontUseEdges[2])
    dont_use_entries[1].set(conf.dontUseEdges[3])

    dont_use_entries[21].set(conf.dontUseEdges[4])
    dont_use_entries[23].set(conf.dontUseEdges[5])
    dont_use_entries[39].set(conf.dontUseEdges[6])
    dont_use_entries[41].set(conf.dontUseEdges[7])

    dont_use_entries[48].set(conf.dontUseEdges[8])
    dont_use_entries[46].set(conf.dontUseEdges[9])
    dont_use_entries[50].set(conf.dontUseEdges[10])
    dont_use_entries[52].set(conf.dontUseEdges[11])

    dont_use_entries[10].set(conf.dontUseEdges[12])
    dont_use_entries[19].set(conf.dontUseEdges[13])
    dont_use_entries[28].set(conf.dontUseEdges[14])
    dont_use_entries[37].set(conf.dontUseEdges[15])

    dont_use_entries[14].set(conf.dontUseEdges[16])
    dont_use_entries[30].set(conf.dontUseEdges[17])
    dont_use_entries[32].set(conf.dontUseEdges[18])
    dont_use_entries[12].set(conf.dontUseEdges[19])

    dont_use_entries[16].set(conf.dontUseEdges[20])
    dont_use_entries[25].set(conf.dontUseEdges[21])
    dont_use_entries[34].set(conf.dontUseEdges[22])
    dont_use_entries[43].set(conf.dontUseEdges[23])

def saveConf():
    conf.cornerLetters[0] = conf_entries[6].get()
    conf.cornerLetters[1] = conf_entries[8].get()
    conf.cornerLetters[2] = conf_entries[2].get()
    conf.cornerLetters[3] = conf_entries[0].get()

    conf.cornerLetters[4] = conf_entries[45].get()
    conf.cornerLetters[5] = conf_entries[47].get()
    conf.cornerLetters[6] = conf_entries[53].get()
    conf.cornerLetters[7] = conf_entries[51].get()

    conf.cornerLetters[8] = conf_entries[18].get()
    conf.cornerLetters[9] = conf_entries[27].get()
    conf.cornerLetters[10] = conf_entries[36].get()
    conf.cornerLetters[11] = conf_entries[9].get()

    conf.cornerLetters[12] = conf_entries[17].get()
    conf.cornerLetters[13] = conf_entries[26].get()
    conf.cornerLetters[14] = conf_entries[35].get()
    conf.cornerLetters[15] = conf_entries[44].get()

    conf.cornerLetters[16] = conf_entries[11].get()
    conf.cornerLetters[17] = conf_entries[20].get()
    conf.cornerLetters[18] = conf_entries[29].get()
    conf.cornerLetters[19] = conf_entries[38].get()

    conf.cornerLetters[20] = conf_entries[24].get()
    conf.cornerLetters[21] = conf_entries[33].get()
    conf.cornerLetters[22] = conf_entries[42].get()
    conf.cornerLetters[23] = conf_entries[15].get()


    conf.edgeLetters[0] = conf_entries[3].get()
    conf.edgeLetters[1] = conf_entries[7].get()
    conf.edgeLetters[2] = conf_entries[5].get()
    conf.edgeLetters[3] = conf_entries[1].get()

    conf.edgeLetters[4] = conf_entries[21].get()
    conf.edgeLetters[5] = conf_entries[23].get()
    conf.edgeLetters[6] = conf_entries[39].get()
    conf.edgeLetters[7] = conf_entries[41].get()

    conf.edgeLetters[8] = conf_entries[48].get()
    conf.edgeLetters[9] = conf_entries[46].get()
    conf.edgeLetters[10] = conf_entries[50].get()
    conf.edgeLetters[11] = conf_entries[52].get()

    conf.edgeLetters[12] = conf_entries[10].get()
    conf.edgeLetters[13] = conf_entries[19].get()
    conf.edgeLetters[14] = conf_entries[28].get()
    conf.edgeLetters[15] = conf_entries[37].get()

    conf.edgeLetters[16] = conf_entries[14].get()
    conf.edgeLetters[17] = conf_entries[30].get()
    conf.edgeLetters[18] = conf_entries[32].get()
    conf.edgeLetters[19] = conf_entries[12].get()

    conf.edgeLetters[20] = conf_entries[16].get()
    conf.edgeLetters[21] = conf_entries[25].get()
    conf.edgeLetters[22] = conf_entries[34].get()
    conf.edgeLetters[23] = conf_entries[43].get()
    
    conf.cornerBuffer = corner_buffer_list.index(cornerBufferVar.get())
    conf.edgeBuffer = edge_buffer_list.index(edgeBufferVar.get())
    conf.moveEdgeCount = sc_edgeSwapCount.get()
    conf.moveCornerCount = sc_cornerSwapCount.get()
    conf.saveConf()
    
    saveButton.config(state=tk.DISABLED)

def updatePossiblility(data=None):
    update_prefs()
    cornerCount = 0
    tmp = sc_cornerSwapCount.get()
    for i in range(8):
        if i == conf.cornerBuffer%8:
            continue
        if not conf.dontUseCorners[i] or not conf.dontUseCorners[i+8] or not conf.dontUseCorners[i+16]:
            cornerCount += 1
    edgeCount = 0
    for i in range(12):
        if i == conf.edgeBuffer%12:
            continue
        if not conf.dontUseEdges[i] or not conf.dontUseEdges[i+12]:
            edgeCount += 1

    if var1.get():
        sc_edgeSwapCount.config(to=((edgeCount-1)//2)*3 + 1)
    else:
        sc_edgeSwapCount.config(to=edgeCount)
    
    cornerTo = cornerCount
    if var2.get():
        cornerTo = ((cornerCount-1)//2)*3 + 1
    
    if sc_edgeSwapCount.get()%2 == 1:
        sc_cornerSwapCount.config(from_=1, to=cornerTo+cornerTo%2-1)
        sc_cornerSwapCount.set(tmp-tmp%2+1)
    else:
        sc_cornerSwapCount.config(from_=0, to=cornerTo-cornerTo%2)
        sc_cornerSwapCount.set(tmp-tmp%2)

def toggleSequence():
    if var3.get():
        sequence_label.config(text=sequence)
    else:
        sequence_label.config(text='')

def activateSaveButton(arg1=None):
    saveButton.config(state=tk.ACTIVE)

window = tk.Tk()
window.title('Blindfolded Master')
upside = tk.Frame()
params = tk.Frame(upside)
# ------------------------------ Edge Parameters ----------------------------- #
fr_edgeParams = tk.Frame(params, relief=tk.GROOVE, borderwidth=5)

var1 = tk.IntVar()
var1.set(conf.allowEdgeCycles)
cb_allowEdgeCycles = tk.Checkbutton(fr_edgeParams, text='Allow edge cycles', variable=var1, command=updatePossiblility)
cb_allowEdgeCycles.pack(fill=tk.BOTH)

sc_edgeSwapCount = tk.Scale(fr_edgeParams, from_=0, to=20, orient=HORIZONTAL, label='Edge Swap Count', command=updatePossiblility)
sc_edgeSwapCount.set(conf.moveEdgeCount)
sc_edgeSwapCount.pack(fill=tk.BOTH)

fr_edgeParams.pack(fill=tk.BOTH)

# ----------------------------- Corner Parameters ---------------------------- #
fr_cornerParams = tk.Frame(params, relief=tk.GROOVE, borderwidth=5)

var2 = tk.IntVar()
var2.set(conf.allowCornerCycles)
cb_allowCornerCycles = tk.Checkbutton(fr_cornerParams, text='Allow corner cycles', variable=var2, command=updatePossiblility)
cb_allowCornerCycles.pack(fill=tk.BOTH)

sc_cornerSwapCount = tk.Scale(fr_cornerParams, from_=0, to=10, orient=HORIZONTAL, resolution=2, label='Corner Swap Count', command=updatePossiblility)
sc_cornerSwapCount.set(conf.moveCornerCount)
sc_cornerSwapCount.pack(fill=tk.BOTH)

fr_cornerParams.pack(fill=tk.BOTH)

params.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

# ------------------------------ Configurations ------------------------------ #
fr_conf = tk.Frame(upside, relief=GROOVE, borderwidth=5)
fr_letters = tk.Frame(fr_conf)
conf_entries = []
for ii, jj in [(1, 3), (4, 0), (4, 3), (4, 6), (4, 9), (7, 3)]:
    for i in range(ii, ii+3):
        for j in range(jj, jj+3):
            if i == ii+1 and j == jj+1:
                conf_entries.append(tk.Entry(fr_letters, width=2, justify=CENTER, state=DISABLED))
            else:
                conf_entries.append(tk.Entry(fr_letters, width=2, justify=CENTER))
            conf_entries[-1].grid(row=i, column=j)
            conf_entries[-1].bind('<KeyRelease>', activateSaveButton)

conf_entries[6].insert(0, conf.cornerLetters[0])
conf_entries[8].insert(0, conf.cornerLetters[1])
conf_entries[2].insert(0, conf.cornerLetters[2])
conf_entries[0].insert(0, conf.cornerLetters[3])

conf_entries[45].insert(0, conf.cornerLetters[4])
conf_entries[47].insert(0, conf.cornerLetters[5])
conf_entries[53].insert(0, conf.cornerLetters[6])
conf_entries[51].insert(0, conf.cornerLetters[7])

conf_entries[18].insert(0, conf.cornerLetters[8])
conf_entries[27].insert(0, conf.cornerLetters[9])
conf_entries[36].insert(0, conf.cornerLetters[10])
conf_entries[9].insert(0, conf.cornerLetters[11])

conf_entries[17].insert(0, conf.cornerLetters[12])
conf_entries[26].insert(0, conf.cornerLetters[13])
conf_entries[35].insert(0, conf.cornerLetters[14])
conf_entries[44].insert(0, conf.cornerLetters[15])

conf_entries[11].insert(0, conf.cornerLetters[16])
conf_entries[20].insert(0, conf.cornerLetters[17])
conf_entries[29].insert(0, conf.cornerLetters[18])
conf_entries[38].insert(0, conf.cornerLetters[19])

conf_entries[24].insert(0, conf.cornerLetters[20])
conf_entries[33].insert(0, conf.cornerLetters[21])
conf_entries[42].insert(0, conf.cornerLetters[22])
conf_entries[15].insert(0, conf.cornerLetters[23])


conf_entries[3].insert(0, conf.edgeLetters[0])
conf_entries[7].insert(0, conf.edgeLetters[1])
conf_entries[5].insert(0, conf.edgeLetters[2])
conf_entries[1].insert(0, conf.edgeLetters[3])

conf_entries[21].insert(0, conf.edgeLetters[4])
conf_entries[23].insert(0, conf.edgeLetters[5])
conf_entries[39].insert(0, conf.edgeLetters[6])
conf_entries[41].insert(0, conf.edgeLetters[7])

conf_entries[48].insert(0, conf.edgeLetters[8])
conf_entries[46].insert(0, conf.edgeLetters[9])
conf_entries[50].insert(0, conf.edgeLetters[10])
conf_entries[52].insert(0, conf.edgeLetters[11])

conf_entries[10].insert(0, conf.edgeLetters[12])
conf_entries[19].insert(0, conf.edgeLetters[13])
conf_entries[28].insert(0, conf.edgeLetters[14])
conf_entries[37].insert(0, conf.edgeLetters[15])

conf_entries[14].insert(0, conf.edgeLetters[16])
conf_entries[30].insert(0, conf.edgeLetters[17])
conf_entries[32].insert(0, conf.edgeLetters[18])
conf_entries[12].insert(0, conf.edgeLetters[19])

conf_entries[16].insert(0, conf.edgeLetters[20])
conf_entries[25].insert(0, conf.edgeLetters[21])
conf_entries[34].insert(0, conf.edgeLetters[22])
conf_entries[43].insert(0, conf.edgeLetters[23])

lbl = tk.Label(fr_conf, text='Configurations')
lbl.pack(fill=tk.BOTH)
fr_letters.pack(fill=tk.BOTH)
#* Corner Buffer
cb_frame = tk.Frame(fr_conf)
cb_label = tk.Label(cb_frame, text='Corner Buffer: ')
cb_label.pack(side=LEFT)
corner_buffer_list = ['UFL', 'UFR', 'UBR', 'UBL', 'DFL', 'DFR', 'DBR', 'DBL', 'FUL', 'RUF', 'BUR', 'LUB', 'LDF', 'FDR', 'RDB', 'BDL', 'LUF', 'FUR', 'RUB', 'BUL', 'FDL', 'RDF', 'BDR', 'LDB']
cornerBufferVar = tk.StringVar()
cornerBufferVar.set(corner_buffer_list[conf.cornerBuffer])
selectCornerBuffer = tk.OptionMenu(cb_frame, cornerBufferVar, *corner_buffer_list, command=activateSaveButton)
selectCornerBuffer.pack(fill=tk.BOTH, side=RIGHT)
#* Edge Buffer
eb_frame = tk.Frame(fr_conf)
eb_label = tk.Label(eb_frame, text='Edge Buffer: ')
eb_label.pack(side=LEFT)
edge_buffer_list = ['UL', 'UF', 'UR', 'UB', 'FL', 'FR', 'BR', 'BL', 'DL', 'DF', 'DR', 'DB', 'LU', 'FU', 'RU', 'BU', 'LF', 'RF', 'RB', 'LB', 'LD', 'FD', 'RD', 'BD']
edgeBufferVar = tk.StringVar()
edgeBufferVar.set(edge_buffer_list[conf.edgeBuffer])
selectEdgeBuffer = tk.OptionMenu(eb_frame, edgeBufferVar, *edge_buffer_list, command=activateSaveButton)
selectEdgeBuffer.pack(fill=tk.BOTH, side=RIGHT)
cb_frame.pack()
eb_frame.pack()
#* Save Button
saveButton = tk.Button(fr_conf, text='SAVE', command=saveConf, state=tk.DISABLED)
saveButton.pack()
fr_conf.pack(side=RIGHT, fill=tk.BOTH)
upside.pack(fill=tk.BOTH)

# ------------------------------ Dont Use ------------------------------ #
fr_dontuse = tk.Frame(upside, relief=tk.GROOVE, borderwidth=5)
fr_checkboxes = tk.Frame(fr_dontuse)
dont_use_entries = []
off_image = tk.PhotoImage(width=24, height=24)
off_image.put(('white'), to=(0, 0, 48, 48))
on_image = tk.PhotoImage(width=24, height=24)
on_image.put(('red'), to=(0, 0, 24, 24))
for ii, jj in [(0, 3), (3, 0), (3, 3), (3, 6), (3, 9), (6, 3)]:
    for i in range(ii, ii+3):
        for j in range(jj, jj+3):
            dont_use_entries.append(tk.IntVar())
            tmp = tk.Checkbutton(fr_checkboxes, variable=dont_use_entries[-1], selectimage=on_image, image=off_image, indicator=False, command=updatePossiblility)
            tmp.grid(row=i, column=j)
            if i == ii+1 and j == jj+1:
                tmp.config(state=DISABLED)
loadDontUse()
dontuselabel = tk.Label(fr_dontuse, text="Don't Scramble Pieces")
dontuselabel.pack()
fr_checkboxes.pack()
fr_dontuse.pack(side=RIGHT, fill=tk.BOTH)

# -------------------------------- Last Frame -------------------------------- #
lastframe = tk.Frame(relief=tk.GROOVE, borderwidth=5)

sequence_frame = tk.Frame(lastframe)
var3 = tk.IntVar()
cb_showSeq = tk.Checkbutton(sequence_frame, text='Show Sequence: ', variable=var3, command=toggleSequence)
cb_showSeq.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

sequence = ''
sequence_label = tk.Label(sequence_frame)
sequence_label.pack(fill=tk.BOTH, side=tk.RIGHT)

button = tk.Button(lastframe, text='Get New Scramble', command=btn_pressed)
button.pack(fill=tk.BOTH, side=tk.TOP)

lb_scramble = tk.Label(lastframe)
lb_scramble.pack()

sequence_frame.pack()

lastframe.pack(fill=tk.BOTH)

window.mainloop()
