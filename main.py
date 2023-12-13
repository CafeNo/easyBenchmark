from tkinter import *
import tkinter as tk
import cpu_benchmark
import disk_benchmark
import memory_benchmark

cpu_score = 0
cpu_runtime = 0
memory_score = 0
memory_runtime = 0
disk_score = 0
disk_runtime = 0
total_score = 0

window = tk.Tk()
window.geometry('900x200')
window.resizable(0,0)
window.title("CN210_Final")

label1 = tk.Label(master=window,  text=f"COMPUTER BENCHMARK", font=("Sukhumvit Set",20)).pack()
label2 = tk.Label(master=window,  text=f"BY ขอจบ 4 ปีได้ไหม", font=("Sukhumvit Set",17)).pack()
frame = tk.Frame(master=window, width=225, height=80, relief=tk.RAISED)
frame.pack(fill=tk.BOTH, pady=5)
frame.columnconfigure(3, weight=1)
frame.rowconfigure(0, weight=1)

def on_run_cpu():
    global cpu_score
    cpu_score = cpu_benchmark.cpu_benchmark()

def on_run_memory():
    global memory_score 
    memory_score = memory_benchmark.memory_benchmark()

def on_run_disk():
    global disk_score
    global total_score
    disk_score = disk_benchmark.disk_benchmark()
    total_score = (cpu_score + memory_score + disk_score) / 3

def on_result():
    window = tk.Tk()
    window.geometry('900x500')
    window.resizable(0,0)
    window.title("CN210_Final")

    label1 = tk.Label(master=window,  text=f"COMPUTER BENCHMARK", font=("Sukhumvit Set",20)).pack()
    label2 = tk.Label(master=window,  text=f"BY ขอจบ 4 ปีได้ไหม", font=("Sukhumvit Set",17)).pack()
    frame = tk.Frame(master=window, width=225, height=80, relief=tk.RAISED)
    frame.pack(fill=tk.BOTH, pady=5)
    frame.columnconfigure(3, weight=1)
    frame.rowconfigure(0, weight=1)

    box1 = tk.Label(master=window, text=f"CPU Score: {cpu_score}.").pack(pady=5)
    box2 = tk.Label(master=window, text=f"\nMemory Score: {memory_score}.").pack(pady=5)
    box3 = tk.Label(master=window, text=f"\nDisk Score: {disk_score}.").pack(pady=5)
    box4 = tk.Label(master=window, text=f"\nTotal Score: {total_score}").pack(pady=5)


button1 = tk.Button(frame,width=30, height=7 , text=f"CPU")
button1.grid(column=1, row=0)
button2 = tk.Button(frame,width=30, height=7 , text=f"MEMORY")
button2.grid(column=2, row=0)
button3 = tk.Button(frame,width=30, height=7 , text=f"DISK")
button3.grid(column=3, row=0)
button4 = tk.Button(frame,width=30, height=7 , text=f"RESULT")
button4.grid(column=4, row=0)

button1.config(command=on_run_cpu)
button2.config(command=on_run_memory)
button3.config(command=on_run_disk)
button4.config(command=on_result)

window.mainloop()
