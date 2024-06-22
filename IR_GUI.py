from tkinter import *
from Searching import QueryFromGUI
import Searching
import Indexing as Indexer
import os

window=Tk()

window.geometry("1250x650")
window.resizable(False,False)
window.config(bg="#8697C4")
window.title("Data Retrival system")

def getQueryfromuser():
    q=query.get()
    QueryFromGUI(q)
    

def readfile(diredctory):

    global display
    display.delete(1.0,END)
    f=open(diredctory,"r",encoding="utf8")
    display.insert(END,f.read())
    f.close()

#label for the name of the system
label=Label(window,text="Retrival System",font=("Helvetica",30),bg="#8697C4",fg="white")
label.grid(row=0,column=1,pady=20)

#lable for the input fild
label=Label(window,text="Query:",font=("Helvetica",12),fg="white",bg="#8697C4")
label.grid(row=1,column=0,padx=10)

#input fild
query=Entry(window,width=50)
query.grid(row=1,column=1)


#button for the search
searchbutton=Button(window,text="Search",padx=60,pady=3,command=getQueryfromuser,fg="#3D52A0")
searchbutton.grid(row=2,column=1,pady=20)

#buttons for indexing section
Indexing=Button(window,text="Reindex",padx=80,pady=3,command=Indexer.Indexing,fg="#3D52A0")
Indexing.grid(row=0,column=3,padx=20)


#buttons for RankedBarChart section
RankedBarChart=Button(window,text="BarChart",padx=80,pady=3,command= Indexer.showRankedBarChart,fg="#3D52A0")
RankedBarChart.grid(row=1,column=3,padx=0.01)

#label for the second header

label2=Label(window,text="Data Retrived ...",font=("Helvetica",20),fg="white",bg="#8697C4")
label2.grid(row=4,column=1,pady=20,)


#file buttons

file1=Button(window,text="FILE-1",padx=135,pady=1,fg="#3D52A0",command=lambda:readfile(os.path.join(Indexer.directoryCorpus, Searching.rankedSearch[0])))
file2=Button(window,text="FILE-2",padx=135,pady=1,fg="#3D52A0",command=lambda:readfile(os.path.join(Indexer.directoryCorpus, Searching.rankedSearch[1])))
file3=Button(window,text="FILE-3",padx=135,pady=1,fg="#3D52A0",command=lambda:readfile(os.path.join(Indexer.directoryCorpus, Searching.rankedSearch[2])))
file4=Button(window,text="FILE-4",padx=135,pady=1,fg="#3D52A0",command=lambda:readfile(os.path.join(Indexer.directoryCorpus, Searching.rankedSearch[3])))
file5=Button(window,text="FILE-5",padx=135,pady=1,fg="#3D52A0",command=lambda:readfile(os.path.join(Indexer.directoryCorpus, Searching.rankedSearch[4])))
file6=Button(window,text="FILE-6",padx=135,pady=1,fg="#3D52A0",command=lambda:readfile(os.path.join(Indexer.directoryCorpus, Searching.rankedSearch[5])))
file7=Button(window,text="FILE-7",padx=135,pady=1,fg="#3D52A0",command=lambda:readfile(os.path.join(Indexer.directoryCorpus, Searching.rankedSearch[6])))
file8=Button(window,text="FILE-8",padx=135,pady=1,fg="#3D52A0",command=lambda:readfile(os.path.join(Indexer.directoryCorpus, Searching.rankedSearch[7])))
file9=Button(window,text="FILE-9",padx=135,pady=1,fg="#3D52A0",command=lambda:readfile(os.path.join(Indexer.directoryCorpus, Searching.rankedSearch[8])))
file10=Button(window,text="FILE-10",padx=135,pady=1,fg="#3D52A0",command=lambda:readfile(os.path.join(Indexer.directoryCorpus, Searching.rankedSearch[9])))


file1.grid(row=5,column=1,pady=2,padx=20)
file2.grid(row=6,column=1,pady=2,padx=20)
file3.grid(row=7,column=1,pady=2,padx=20)
file4.grid(row=8,column=1,pady=2,padx=20)
file5.grid(row=9,column=1,pady=2,padx=20)
file6.grid(row=10,column=1,pady=2,padx=20)
file7.grid(row=11,column=1,pady=2,padx=20)
file8.grid(row=12,column=1,pady=2,padx=20)
file9.grid(row=13,column=1,pady=2,padx=20)
file10.grid(row=14,column=1,pady=2,padx=20)


#the input text
display=Text(window,width=70,height=39,highlightthickness=5,highlightbackground="#EDE8F5")
display.grid(row=0,column=2,rowspan=15)


#Exit button
quit=Button(window,text="EXIT",pady=3,padx=88,fg="#3D52A0",command=window.quit)
quit.grid(row=14,column=3,padx=20,pady=1)


window.mainloop()

