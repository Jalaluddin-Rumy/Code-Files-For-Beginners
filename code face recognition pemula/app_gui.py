import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

#Init
window = tk.Tk()
window.configure(bg="white")
window.geometry("500x300")
window.resizable(False,False)
window.title("Face Recognition")
#Variable & fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()
def tombol_click():
    #print(NAMA_BELAKANG.get())#.get() mrpkn string far biar mudah diolah.
    '''fungsi ini akan di panggil oleh tombol'''
    pesan = f"Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Ganteng"
    showinfo(title="Whazzup!",message=pesan)
#frame input
input_frame = ttk.Frame(window)
#penempatan Grid, Pack, Place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

#komponen-komponen GUI
#1. Label nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan :")
nama_depan_label.pack(padx=10, fill="x",expand=True)
#2. entry nama depan
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, fill="x",expand=True)

#3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame,text="Nama belakang :")
nama_belakang_label.pack(padx=10, fill="x",expand=True)
#4. entry nama belakaeng
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_depan_entry.pack(padx=10, fill="x",expand=True)

#5. Tombol
tombol_Tekan = ttk.Button(input_frame,text="Tekan!",command=tombol_click)
tombol_Tekan.pack(fill='x',expand=True,padx=10,pady=10)

#mainloop window
window.mainloop()