import tkinter as tk
from tkinter import *
from tkinter import ttk


class ToggledFrame(tk.Frame):

    def __init__(self, parent, text="", *args, **options):
        tk.Frame.__init__(self, parent, *args, **options)

       
        self.show = tk.IntVar()
        self.show.set(0)

        self.title_frame = ttk.Frame(self)
        self.title_frame.pack(fill="x", expand=1)

        ttk.Label(self.title_frame, text=text, font='50').pack(side="left", fill="x", expand=1)

        self.toggle_button = ttk.Checkbutton(self.title_frame, width=2, text='﹀', command=self.toggle,
                                            variable=self.show, style='Toolbutton')
        self.toggle_button.pack(side="left")

        self.sub_frame = tk.Frame(self, relief="sunken", borderwidth=1)

    def toggle(self):
        if bool(self.show.get()):
            self.sub_frame.pack(fill="x", expand=1)
            self.toggle_button.configure(text='︿')
        else:
            self.sub_frame.forget()
            self.toggle_button.configure(text='﹀')


if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(width=800, height=600)
    root.maxsize(width=1000, height=800)
   
    left = Frame(root, borderwidth=2, relief="solid")
    right = Frame(root, borderwidth=2, relief="solid")
    
    container = Frame(left, borderwidth=2, relief="solid", bg='white')
    box1 = Frame(right, borderwidth=2, relief="solid", bg='white')

    #t = ToggledFrame(root, text='Rotate', relief="raised", borderwidth=1)
    t = ToggledFrame(container, text='Search Objects', relief="raised", borderwidth=1)
    t.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    select_lbl=ttk.Label(t.sub_frame, text='Select Databases').grid(row=0,column=0,padx=5, pady=5, sticky=W)
    #select_lbl.pack(side="left", fill="x", expand=1)
    comboDb = ttk.Combobox(t.sub_frame, 
                            values=[
                                    "A00_NORMAP", 
                                    "A00_OECD_MEI",
                                    "A00_OECD_OUTLOOK",
                                    "A02_BEF",
                                    "A03_TRDGD",
                                    "A06_AKU"]).grid(row=0,column=1, sticky=W)
    
    
    lbl_tom=ttk.Label(t.sub_frame, text='').grid(row=1,column=1)
    #lbl.pack(side="left", fill="x", expand=1)
    lbl=ttk.Label(t.sub_frame, text='Object Name/wildcard/alias').grid(row=2,column=1, sticky=W)
   
    ttk.Entry(t.sub_frame, font=20,width=13).grid(row=3,column=1, sticky=W)
    button = ttk.Button(t.sub_frame, text='Search').grid(row=3,column=2, padx=10, pady=10,sticky=W)
    #button.pack(side="right", fill="x", expand=1)691451

    lbl_tom=ttk.Label(t.sub_frame, text='').grid(row=4,column=1)
    select_lbl=ttk.Label(t.sub_frame, text='Select Chart Type').grid(row=5,column=0, padx=5, pady=5,sticky=W)

    comboChart = ttk.Combobox(t.sub_frame, 
                            values=[
                                    "line", 
                                    "bar",
                                    "column",
                                    "area",
                                    "scatter"]).grid(row=5,column=1, sticky=W)
    
    button = ttk.Button(t.sub_frame, text='View Graph').grid(row=6,column=0, columnspan=2, padx=5, pady=10,sticky=W)
    button = ttk.Button(t.sub_frame, text='View Series Values').grid(row=6,column=1, padx=5, pady=5, sticky=S)
    button = ttk.Button(t.sub_frame, text='View Series Details').grid(row=7,column=0, padx=5, pady=5, sticky=W)
    button = ttk.Button(t.sub_frame, text='Reset All').grid(row=7,column=1, padx=5, pady=5, sticky=S)
    t.sub_frame.pack(padx=5, pady=5, side=tk.LEFT)
    
    #t2 = ToggledFrame(root, text='Resize', relief="raised", borderwidth=1)
    t2 = ToggledFrame(container, text='Search By Description', relief="raised", borderwidth=1)
    t2.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    ttk.Label(t2.sub_frame, text='Description String').grid(row=0, column=0, sticky=W)
    ttk.Entry(t2.sub_frame, font=40).grid(row=0,column=1, padx=5, pady=5,sticky=W)
    button = ttk.Button(t2.sub_frame, text='Search').grid(row=0,column=2, padx=10, pady=10,sticky=W)
    #for i in range(10):
       # ttk.Label(t2.sub_frame, text='Test' + str(i)).pack()
    
    mydate = StringVar()
    #t3 = ToggledFrame(root, text='Fooo', relief="raised", borderwidth=1)
    t3 = ToggledFrame(container, text='Search by Date Range', relief="raised", borderwidth=1)
    t3.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

   # for i in range(10):
       # ttk.Label(t3.sub_frame, text='Bar' + str(i)).pack()
       
    lbl_tom=ttk.Label(t3.sub_frame, text='Start Date').grid(row=0,column=0,padx=5,sticky=W)
    ttk.Entry(t3.sub_frame, font=40,width=10).grid(row=1,column=0, padx=5, pady=5,sticky=W)
    lbl_tom=ttk.Label(t3.sub_frame, text = 'End Date').grid(row=2,column=0, padx=5,sticky=W)
    ttk.Entry(t3.sub_frame, font=40, width=10,textvariable=mydate).grid(row=3,column=0, padx=5, pady=5,sticky=W)
    button = ttk.Button(t3.sub_frame, text='Apply').grid(row=4,column=0, padx=5, pady=5,sticky=W)
    button = ttk.Button(t3.sub_frame, text='Reset').grid(row=4,column=1, sticky=W)
    
    t4 = ToggledFrame(container, text='Time Scaling', relief="raised", borderwidth=1)
    t4.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    #for i in range(10):
        #ttk.Label(t4.sub_frame, text='Bar' + str(i)).pack()
    lbl_tom=ttk.Label(t4.sub_frame, text='Select Frequency').grid(row=0,column=0,padx=5,pady=5,sticky=W)
    comboFreq = ttk.Combobox(t4.sub_frame, 
                            values=[
                                    "Annual", 
                                    "Weekly",
                                    "Monthly",
                                    "Daily",
                                    "Business",
                                    "Quarterly"]).grid(row=1,column=0, padx=5,pady=5, sticky=W)
    button = ttk.Button(t4.sub_frame, text='Apply').grid(row=2,column=0, padx=5, pady=5,sticky=W)
    button = ttk.Button(t4.sub_frame, text='Reset').grid(row=2,column=1, sticky=W)

    t5 = ToggledFrame(container, text='Analytics', relief="raised", borderwidth=1)
    t5.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    #for i in range(10):
        #ttk.Label(t5.sub_frame, text='Bar' + str(i)).pack()
    lbl_tom=ttk.Label(t5.sub_frame, text='Analytics').grid(row=0,column=0,padx=5,pady=5,sticky=W)
    comboAna = ttk.Combobox(t5.sub_frame, 
                            values=[
                                    "Abs", 
                                    "Annpct",
                                    "Atan",
                                    "Cave",
                                    "Cmax",
                                    "Cmin",
                                    "Cos",
                                    "Csum",
                                    "Diff",
                                    "Lave",
                                    "Lmax",
                                    "Lmin",
                                    "Log",
                                    "log10",
                                    "Lsum",
                                    "Mavec",
                                    "Mmax",
                                    "Mmedian",
                                    "Mmin",
                                    "Msum",
                                    "Mvar",
                                    "Pct",
                                    "Round",
                                    "Sannpct",
                                    "Skift",
                                    "Sign",
                                    "Sin",
                                    "Sqrt",
                                    "Trunc",
                                    "Ytypct"]).grid(row=1,column=0, padx=5,pady=5, sticky=W)
    button = ttk.Button(t5.sub_frame, text='Reset').grid(row=1,column=1, padx=5, pady=5,sticky=W)

    t6 = ToggledFrame(container, text='Base Year', relief="raised", borderwidth=1)
    t6.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    lbl_tom=ttk.Label(t6.sub_frame, text='Select Base Year').grid(row=0,column=0,padx=5,pady=5,sticky=W)
    comboAna = ttk.Combobox(t6.sub_frame, 
                            values=[
                                    "2000", 
                                    "2001",
                                    "2002",
                                    "2003",
                                    "2004",
                                    "2005",
                                    "2006",
                                    "2007",
                                    "2008",
                                    "2009",
                                    "2010",
                                    "2011",
                                    "2012",
                                    "2013",
                                    "2014",
                                    "2015",
                                    "2016",
                                    "2017",
                                    "2018",
                                    "2019",
                                    "2020"]).grid(row=1,column=0, padx=5,pady=5, sticky=W)
                                    
    tab_parent = ttk.Notebook(box1)

    tab1 = ttk.Frame(tab_parent)
    tab2 = ttk.Frame(tab_parent)
    tab3 = ttk.Frame(tab_parent)
    tab4 = ttk.Frame(tab_parent)

    tab_parent.add(tab1, text="Series List")
    tab_parent.add(tab2, text="Graph")
    tab_parent.add(tab3, text="Sereis Values")
    tab_parent.add(tab4, text="Series Details")
    
    
    tab_parent.pack(expand=1, fill="both")
    
    left.pack(side="left", expand=True, fill="both")
    right.pack(side="right", expand=True, fill="both")
    container.pack(expand=True, fill="both", padx=5, pady=5)
    box1.pack(expand=True, fill="both", padx=10, pady=10)
  
    root.mainloop()