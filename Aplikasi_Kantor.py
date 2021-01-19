import tkinter as Tk
import tkinter.font as font
import calendar
import time

def MyCalc(source, side):
    sObj = Tk.Frame(source, borderwidth=4, bd=4, bg='powder blue')
    sObj.pack(side=side, expand=Tk.YES, fill=Tk.BOTH)
    return sObj


def tombol(source, side, text, command=None, bg='powder blue'):
    sObj = Tk.Button(source, text=text, command=command, bg=bg)
    sObj.pack(side=side, expand=Tk.YES, fill=Tk.BOTH)
    return sObj


# nama class dibuat dengan camelcase
# TEMPLATE
class Kalkulator(Tk.Toplevel):
    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        # resolusi
        # self.geometry("400x300")
        # Judul window
        self.title("Kalkulator")
        self. kembali()
        self.frame()
        self.option_add('*Font', 'arial 20 bold')


        display = Tk.StringVar()
        Tk.Entry(self, relief=Tk.FLAT, textvariable=display, bd=30, bg='blue').pack(side=Tk.TOP, expand=Tk.YES, fill=Tk.BOTH)

        for TombAngka in ('789', '456', '123', '0.+', '/*-'):
            fNum = MyCalc(self, Tk.TOP)
            for isdm in TombAngka:
                tombol(fNum, Tk.LEFT, isdm, lambda sObj=display, q=isdm: sObj.set(sObj.get() + q))

        for TombolC in (['C']):
            ers = MyCalc(self, Tk.RIGHT)
            for ichar in TombolC:
                tombol(ers, Tk.RIGHT, ichar, lambda sObj=display, q=ichar: sObj.set(''), bg='red')

        SamaDengan = MyCalc(self, Tk.LEFT)
        for sd in '=':
            if sd == '=':
                TombolSama = tombol(SamaDengan, Tk.LEFT, sd)
                TombolSama.bind('<ButtonRelease-1>', lambda e, s=self, sObj=display: s.hitung(sObj), '+')
            else:
                TombolSama = tombol(SamaDengan, Tk.LEFT, sd,
                                    lambda sObj=display, s=' %s ' % sd: sObj.set(sObj.get() + s))

    def hitung(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set('ERROR')

    # tombol tutup
    def kembali(self):
        self.btnkembali = Tk.Button(self, text="Close", command=self.tutup)
        # koordinat tombol tutup iso diatur sesuai selera,,
        self.btnkembali.place(x=0, y=5)

    # ojo di otak atik sek bagiak iki
    def tutup(self):
        self.destroy()
        self.original_frame.show()


class Kalender(Tk.Toplevel):
    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.frame()
        self.title("Kalender Covid-19")
        Tk.year = 2021
        myCal = calendar.calendar(Tk.year)
        cal_year = Tk.Label(self, text=myCal, font="Consolas 10 bold")
        cal_year.pack()
        self.kembali()

    # tombol tutup
    def kembali(self):
        self.btnkembali = Tk.Button(self, text="Close", command=self.tutup)
        # koordinat tombol tutup iso diatur sesuai selera,,
        self.btnkembali.place(x=0, y=5)

    # ojo di otak atik sek bagiak iki
    def tutup(self):
        self.destroy()
        self.original_frame.show()

class Stopwatch(Tk.Toplevel):
    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.frame()
        self.title("Stopwatch")
        self.kembali()
        self._start = 0.0
        self.waktuSekarang = 0.0
        self.sedangBerjalan = False
        self.waktuString = Tk.StringVar()
        self.textStart = Tk.StringVar()
        self.textStart.set('Start')
        self.configure(background='light blue')
        self.buatTeks()
        self.buatTombol()

    def buatTeks(self):
        self.teks = Tk.Label(self, textvariable=self.waktuString, font="Verdana 19 bold", bg='light blue', fg='blue')
        self.aturWaktu(self.waktuSekarang)
        self.teks.grid(row=0, column=0)

    def perbarui(self):
        self.waktuSekarang = time.time() - self._start
        self.aturWaktu(self.waktuSekarang)
        self._timer = self.after(50, self.perbarui)

    def aturWaktu(self, waktu):
        menit = int(waktu / 60)
        detik = int(waktu - menit * 60.0)
        jam = int((waktu - menit * 60.0 - detik) * 100)
        self.waktuString.set('%02d:%02d:%02d' % (menit, detik, jam))

    def Start(self):
        if not self.sedangBerjalan and (self.textStart.get() == 'Start' or self.textStart.get() == 'Resume'):
            self.textStart.set('Pause')
            self._start = time.time() - self.waktuSekarang
            self.perbarui()
            self.sedangBerjalan = True
        elif self.sedangBerjalan and self.textStart.get() == 'Pause':
            self.textStart.set('Resume')
            self.pause()

    def pause(self):
        if self.sedangBerjalan:
            self.after_cancel(self._timer)
            self.waktuSekarang = time.time() - self._start
            self.aturWaktu(self.waktuSekarang)
            self.sedangBerjalan = False

    def buatTombol(self):
        Tk.Button(textvariable=self.textStart, command=self.Start).place(x=2, y=1)


    # tombol tutup
    def kembali(self):
        self.btnkembali = Tk.Button(self, text="Close", command=self.tutup)
        # koordinat tombol tutup iso diatur sesuai selera,,
        self.btnkembali.place(x=0, y=5)

    # ojo di otak atik sek bagiak iki
    def tutup(self):
        self.destroy()
        self.original_frame.show()


class Notepad(Tk.Toplevel):
    def __init__(self, original):
        Tk.Frame.__init__(self, original)
        self.frm = Tk.Frame(original)
        self.title('Notepad')
        self.kembali()
        self.frm.pack(fill=X)
        self.layoutKolom = Tk.Frame(root)
        self.buatJudul()
        self.kembali()
        self.title('Notepad')
        self.buatTombol()
        self.kolomTeksUtama()
        self.settext(text='', file=file)
        self.kolomTeks.config(font=('DejaVu Sans Mono', 10))
        self.indeks = 1.0
        self.buatCari()
        self.path = ''

    def buatTombol(self):
        Tk.Button(self.frm, text='Open', relief='flat', command=self.bukaFile).pack(side=Tk.LEFT)
        Tk.Button(self.frm, text='Simpan', relief='flat', command=self.perintahSimpan).pack(side=Tk.LEFT)
        Tk.Button(self.frm, text='Copy', relief='flat', command=self.perintahCopy).pack(side=Tk.LEFT)
        Tk.Button(self.frm, text='Cut', relief='flat', command=self.perintahCut).pack(side=Tk.LEFT)
        Tk.Button(self.frm, text='Paste', relief='flat', command=self.perintahPaste).pack(side=Tk.LEFT)
        Tk.Button(self.frm, text='Cari', relief='flat', command=self.perintahFind).pack(side=Tk.LEFT)
        Tk.Button(self.frm, text='Keluar', relief='flat', command=self.perintahKeluar).pack(side=Tk.LEFT)

    def kolomTeksUtama(self):
        scroll = Tk.Scrollbar(self)
        kolomTeks = Tk.Text(self, relief=Tk.SUNKEN)
        scroll.config(command=kolomTeks.yview)
        kolomTeks.config(yscrollcommand=scroll.set)
        scroll.pack(side=Tk.RIGHT, fill=Tk.Y)
        kolomTeks.pack(side=Tk.LEFT, expand=Tk.YES, fill=Tk.BOTH)
        self.kolomTeks = kolomTeks
        self.pack(expand=Tk.YES, fill=Tk.BOTH)

    def perintahSimpan(self):
        print(self.path)
        if self.path:
            alltext = self.gettext()
            open(self.path, 'w').write(alltext)
            messagebox.showinfo('Berhasil', 'Selamat File telah tersimpan ! ')
        else:
            tipeFile = [('Text file', '*.txt'), ('Python file', '*asdf.py'), ('All files', '.*')]
            filename = asksaveasfilename(filetypes=(tipeFile), initialfile=self.kolomJudul.get())
            if filename:
                alltext = self.gettext()
                open(filename, 'w').write(alltext)
                self.path = filename

    def perintahCopy(self):
        try:
            text = self.kolomTeks.get(SEL_FIRST, SEL_LAST)
            self.clipboard_clear()
            self.clipboard_append(text)
            self.kolomTeks.selection_clear()
        except:
            pass

    def perintahCut(self):
        try:
            text = self.kolomTeks.get(SEL_FIRST, SEL_LAST)
            self.kolomTeks.delete(SEL_FIRST, SEL_LAST)
            self.clipboard_clear()
            self.clipboard_append(text)
        except:
            pass

    def perintahPaste(self):
        try:
            text = self.selection_get(selection='CLIPBOARD')
            self.kolomTeks.insert(Tk.INSERT, text)
        except TclError:
            pass

    def perintahFind(self):
        target = self.kolomCari.get()
        if target:
            self.indeks = self.kolomTeks.search(target, str(float(self.indeks) + 0.1), stopindex=Tk.END)
            if self.indeks:
                pastit = self.indeks + ('+%dc' % len(target))
                self.kolomTeks.tag_remove(Tk.SEL, '1.0', Tk.END)
                self.kolomTeks.tag_add(SEL, self.indeks, pastit)
                self.kolomTeks.mark_set(Tk.INSERT, pastit)
                self.kolomTeks.see(Tk.INSERT)
                self.kolomTeks.focus()
            else:
                self.indeks = '0.9'

    def perintahKeluar(self):
        ans = askokcancel('Keluar', "anda yakin ingin keluar?")
        if ans: Frame.quit(self)

    def settext(self, text='', file=None):
        if file:
            text = open(file, 'r').read()
        self.kolomTeks.delete('1.0', Tk.END)
        self.kolomTeks.insert('1.0', text)
        self.kolomTeks.mark_set(Tk.INSERT, '1.0')
        self.kolomTeks.focus()

    def gettext(self):
        return self.kolomTeks.get('1.0', Tk.END + '-1c')

    def buatJudul(self):
        self.layoutKolom.pack(fill=Tk.BOTH, expand=1, padx=17, pady=5)
        judul = Tk.Label(self.layoutKolom, text="Judul : ")
        judul.pack(side="left")
        self.kolomJudul = Entry(self.layoutKolom)
        self.kolomJudul.pack(side="left")

    def buatCari(self):
        Button(self.frm, text='Cari', command=self.perintahFind).pack(side="right")
        self.kolomCari = Tk.Entry(self.frm)
        self.kolomCari.pack(side="right")

    def bukaFile(self):
        extensiFile = [('All files', '*'), ('Text files', '*.txt'), ('Python files', '*.py')]
        buka = filedialog.askopenfilename(filetypes=extensiFile)
        if buka != '':
            text = self.readFile(buka)
            if text:
                self.path = buka
                nama = os.path.basename(buka)
                self.kolomJudul.delete(0, Tk.END)
                self.kolomJudul.insert(Tk.END, nama)
                self.kolomTeks.delete('0.1', Tk.END)
                self.kolomTeks.insert(Tk.END, text)

    def readFile(self, filename):
        try:
            f = open(filename, "r")
            text = f.read()
            return text
        except:
            messagebox.showerror("Error!!", "Maaf file tidak dapat dibuka ! :) \nsabar ya..")
            return None

    # tombol tutup
    def kembali(self):
        self.btnkembali = Tk.Button(self, text="Close", command=self.tutup)
        # koordinat tombol tutup iso diatur sesuai selera,,
        self.btnkembali.place(x=0, y=5)

    # ojo di otak atik sek bagiak iki
    def tutup(self):
        self.destroy()
        self.original_frame.show()

class Coba(Tk.Toplevel):
    def __init__(self, original):
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("400x300")
        self.title("MAAF APLIKASI MASIH DALAM TAHAP PRODUKSI")

        btn = Tk.Button(self, text="MMAAF APLIKASI MASIH DALAM TAHAP PRODUKSI", command=self.onClose)
        btn.pack()

    def onClose(self):
        self.destroy()
        self.original_frame.show()


# sek bagian iki,sek tak tandai ojo diotakatik,tak gawene ben apik sek
class MainApp(object):
    def __init__(self, parent):
        self.root = parent
        self.root.title("Menu Utama")
        self.frame = Tk.Frame(parent)
        self.frame.pack()
        self.tulisanJudul()
        self.panelmenu()
        self.keterangan()

    def hide(self):
        self.root.withdraw()

    def show(self):
        self.root.update()
        self.root.deiconify()

    #     iki bagian tambah aplikasi,hubungane karo fungsi panel menu .cocokloginen dewe
    def openkalkulator(self):
        self.hide()
        # iki panggil class aplikasi
        subFrame = Kalkulator(self)

    def openkalender(self):
        self.hide()
        subFrame = Kalender(self)

    def opennotepad(self):
        self.hide()
        subFrame = Notepad(self)

    def openstopwatch(self):
        self.hide()
        subFrame = Stopwatch(self)

    def appbelumrilis(self):
        self.hide()
        subFrame = Coba(self)

    def tulisanJudul(self):
        FontJudul = font.Font(size=16, weight='bold')
        self.teksJudul = Tk.Label(text="Selamat Datang di ONE FOR ALL Aplikasi Kantor")
        self.teksJudul['font'] = FontJudul
        self.teksJudul.place(x=100, y=10)

    #     iki oleh mbok edit nek rep tambah aplikasi
    def panelmenu(self):
        #Open Aplikasi Kalkulator
        self.kalkulator = Tk.Button(self.root, text="Kalkulator", command=self.openkalkulator)
        self.kalkulator.place(x=80, y=60)
        #Open Aplikasi Kalender
        self.Kalender = Tk.Button(self.root, text="Kalender", command=self.openkalender)
        self.Kalender.place(x=180, y=60)
        #Open Aplikasi Notepad
        self.Notepad = Tk.Button(self.root, text="Notepad", command=self.appbelumrilis)
        self.Notepad.place(x=280, y=60)
        #Open Aplikasi Stopwatch
        self.app1 = Tk.Button(self.root, text="Stopwatch", command=self.openstopwatch)
        self.app1.place(x=380, y=60)

    def keterangan(self):
        FontlabelInput = font.Font(size=12, weight='bold')
        FontlabelKet = font.Font(size=11)
        self.KetJudulapp1 = Tk.Label(text="Kalkulator")
        self.KetJudulapp1['font'] = FontlabelInput
        self.KetJudulapp1.place(x=25, y=100)
        self.Ketapp1 = Tk.Label(text="Sudah bosan dengan perhitungan manual? Menggunakan kalkulator solusinya!")
        self.Ketapp1['font'] = FontlabelKet
        self.Ketapp1.place(x=25, y=120)

        #         ####APP2
        self.KetJudulapp2 = Tk.Label(text="Kalender")
        self.KetJudulapp2['font'] = FontlabelInput
        self.KetJudulapp2.place(x=25, y=150)
        self.Ketapp2 = Tk.Label(text="Lengkapi hari anda dengan kalender masehi,jadi engga binggung kapan libur deh :D")
        self.Ketapp2['font'] = FontlabelKet
        self.Ketapp2.place(x=25, y=170)

        #         ####APP3
        self.KetJudulapp3 = Tk.Label(text="Notepad")
        self.KetJudulapp3['font'] = FontlabelInput
        self.KetJudulapp3.place(x=25, y=200)
        self.Ketapp3 = Tk.Label(text="Curahkan kegalauan anda dengan Notepad, Bisa untuk menghilangkan Mantan :D")
        self.Ketapp3['font'] = FontlabelKet
        self.Ketapp3.place(x=25, y=220)

        #         ####APP4
        self.KetJudulapp4 = Tk.Label(text="Stopwatch")
        self.KetJudulapp4['font'] = FontlabelInput
        self.KetJudulapp4.place(x=25, y=250)
        self.Ketapp4 = Tk.Label(text="Menghitung kembali waktu anda saat melakukan aktifitas kerja")
        self.Ketapp4['font'] = FontlabelKet
        self.Ketapp4.place(x=25, y=270)


if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("800x600")
    app = MainApp(root)
    root.mainloop()


#Kelompok
#Abi Fadri Untoro (19.83.0366)
#Alief Rizky Adriansyah (19.83.0366)