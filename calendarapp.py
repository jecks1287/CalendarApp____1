import calendar
import datetime
import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
class CalendarApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Календарь")
        self.current_date = datetime.date.today()
        self.calendar_frame = tk.Frame(self.window)
        self.calendar_frame.pack(pady=1)
        self.calendar = Calendar(self.calendar_frame, selectmode="day", date_pattern="dd/MM/yyyy")
        self.calendar.pack()
        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=1)
        self.select_button = tk.Button(button_frame, text="Выбрать дату", command=self.select_date)
        self.select_button.pack(side=tk.LEFT, padx=1)
        self.prev_button = tk.Button(button_frame, text="<< Предыдущий месяц", command=self.prev_month)
        self.prev_button.pack(side=tk.LEFT, padx=1)
        self.next_button = tk.Button(button_frame, text="Следующий месяц >>", command=self.next_month)
        self.next_button.pack(side=tk.RIGHT, padx=1)
        self.selected_date = None
        self.window.mainloop()
    def select_date(self):
        # Выбор даты из календаря
        selected_date_str = self.calendar.get_date()
        selected_date = datetime.datetime.strptime(selected_date_str, "%d/%m/%Y").date()
        if selected_date < self.current_date:
            messagebox.showwarning("Ошибка", "Невозможно добавить событие для прошедшей даты.")
            return
        self.selected_date = selected_date
        # Отображение выбранной даты в консоли
        print(f"Выбранная дата: {self.selected_date}")
        # Запросить текстовое сообщение у пользователя
        event_text = input("Введите текстовое сообщение:")
        if event_text is not None and event_text.strip() != "":
            # Здесь можно добавить логику для создания события на выбранную дату и с указанным сообщением
            print(f"Добавлено событие на {self.selected_date}: {event_text}")
        else:
            messagebox.showwarning("Ошибка", "Неверное сообщение. Событие не добавлено.")
    def prev_month(self):
        # Переключение на предыдущий месяц
        if self.current_date.month == 1:
            self.current_date = self.current_date.replace(year=self.current_date.year - 1, month=12)
        else:
            self.current_date = self.current_date.replace(month=self.current_date.month - 1)
        self.show_calendar()
    def next_month(self):
        # Переключение на следующий месяц
        if self.current_date.month == 12:
            self.current_date = self.current_date.replace(year=self.current_date.year + 1, month=1)
        else:
            self.current_date = self.current_date.replace(month=self.current_date.month + 1)
        self.show_calendar()
    def show_calendar(self):
        # Отображение календаря
        year = self.current_date.year
        month = self.current_date.month
        day = self.current_date.day
        self.calendar.selection_set(datetime.datetime(year, month, day))
if __name__ == '__main__':
    app = CalendarApp()
    
