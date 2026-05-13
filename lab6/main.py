import tkinter as tk
from calc_package.area import calc_area
from calc_package.heat import calc_heat
from calc_package.models import get_multiplier
from export.to_doc import save_to_doc

def calculate():
    length = float(entry_length.get())
    width = float(entry_width.get())
    room_type = var.get()

    area = calc_area(length, width)
    heat = calc_heat(area) * get_multiplier(room_type)

    result_label.config(text=f"Площадь: {area:.2f} м²\nМощность: {heat:.2f} Вт")

    global last_area, last_heat
    last_area, last_heat = area, heat

def save_doc():
    save_to_doc(last_area, last_heat)


root = tk.Tk()
root.title("Расчёт помещения")

tk.Label(root, text="Длина").pack()
entry_length = tk.Entry(root)
entry_length.pack()

tk.Label(root, text="Ширина").pack()
entry_width = tk.Entry(root)
entry_width.pack()

var = tk.StringVar(value="Комната")
tk.OptionMenu(root, var, "Комната", "Квартира", "Дом").pack()

tk.Button(root, text="Рассчитать", command=calculate).pack()

result_label = tk.Label(root, text="")
result_label.pack()

tk.Button(root, text="Сохранить в DOC", command=save_doc).pack()

root.mainloop()
