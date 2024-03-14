import tkinter as tk
from tkinter import messagebox

# Коэффициенты пересчета
conversion_factors = {
    "Грамм": 1,
    "Фунт": 0.00220462,
    "Унция": 0.035274,
    "Килограмм": 0.001
}

def convert():
    try:
        value = float(entry.get())
        unit = unit_var.get()
        result_unit = result_unit_var.get()
        
        result = value * conversion_factors[result_unit]  # Измененная формула
        result_text.set(f"{value} {unit} = {result:.7f} {result_unit}")  # Изменение формата вывода

    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите числовое значение.")

# Создание окна
window = tk.Tk()
window.title("Конвертер единиц измерения")
window.geometry("550x200")

# Создание элементов управления
instruction_label = tk.Label(window, text="Введите число для конвертации:")
instruction_label.place(x=50, y=20)

entry = tk.Entry(window)
entry.place(x=50, y=50)

unit_var = tk.StringVar(window)
unit_var.set("Грамм")
unit_dropdown = tk.OptionMenu(window, unit_var, *conversion_factors.keys())
unit_dropdown.place(x=250, y=50)

result_unit_var = tk.StringVar(window)
result_unit_var.set("Фунт")
result_unit_dropdown = tk.OptionMenu(window, result_unit_var, *conversion_factors.keys())
result_unit_dropdown.place(x=400, y=50)

convert_button = tk.Button(window, text="Конвертировать", command=convert)
convert_button.place(x=50, y=100)

result_text = tk.StringVar(window)
result_label = tk.Label(window, textvariable=result_text, justify=tk.LEFT)
result_label.place(x=50, y=150)

# Запуск основного цикла обработки событий
window.mainloop()
