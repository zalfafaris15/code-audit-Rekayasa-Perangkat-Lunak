# aplikasi manajemen nilai mahasiswa
# dibuat oleh mahasiswa

d = []

def f(n, v, t):
    # fungsi untuk tambah data
    x = {"nm": n, "val": v, "tp": t}
    d.append(x)
    return x

def g():
    # print semua
    for i in d:
        print(i["nm"], i["val"], i["tp"])

def h(n):
    tot = 0
    c = 0
    for i in d:
        if i["nm"] == n:
            tot = tot + i["val"]
            c = c + 1
    if c == 0:
        return 0
    a = tot / c
    return a

def calc(n):
    a = h(n)
    # cek grade
    if a >= 85:
        g2 = "A"
    elif a >= 70:
        g2 = "B"
    elif a >= 60:
        g2 = "C"
    elif a >= 50:
        g2 = "D"
    else:
        g2 = "E"
    print(n + " rata-rata: " + str(a) + " grade: " + g2)

def proc():
    # proses semua mahasiswa
    nm_list = []
    for i in d:
        if i["nm"] not in nm_list:
            nm_list.append(i["nm"])
    for n in nm_list:
        calc(n)

# main
f("Budi", 80, "UTS")
f("Budi", 90, "UAS")
f("Budi", 75, "Tugas")
f("Siti", 60, "UTS")
f("Siti", 70, "UAS")
f("Siti", 55, "Tugas")
g()
proc()
