from tkinter import *
import requests
import datetime
import ScrollBar
from tkinter import ttk

# from PIL import ImageTk, Image

ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
KEY = "58cd189feef4d9f808fc5630caf130a1"

# Fonts
MONTERY = ("MontereyFLF", "15", "normal")
NOVA = ("NovaMono", "20", "normal")
MONOFONT = ("MONOFONT", "25", "bold")
MONOFONT_NK57 = ("nk57-monospace", "14", "normal")

# Colors
NAVY_BLUE = "#1A374D"
BLUE = "#406882"
CAYN = "#7CD1B8"


class Weather:
    def __init__(self):
        self.city = "Karaj"
        self.weather = {
            "lat": 35.807580,
            "lon": 50.987420,
            "appid": KEY
        }
        self.response = requests.get(ENDPOINT, params=self.weather)
        self.response.raise_for_status()
        self.datas = self.response.json()

        # UI
        self.window = Tk()
        self.window.title("Weather App")
        self.window.geometry("1500x780")
        self.window.config(highlightthickness=0, bg=NAVY_BLUE)

        # Frames
        # Daily Forecast
        # self.frame_today = Frame()
        # self.frame_1 = Frame()
        # self.frame_2 = Frame()
        # self.frame_3 = Frame()
        # self.frame_4 = Frame()
        # self.frame_5 = Frame()
        # self.frame_6 = Frame()
        # self.frame_7 = Frame()
        # Main Page
        self.frame_today_info = Frame()
        self.frame_today_info.config(highlightthickness=0, bg=NAVY_BLUE)
        # Hourly Forcast

        self.frames_hourly = []
        for i in range(48):
            a = Frame(highlightthickness=0, bg=NAVY_BLUE, name=f"frame_hourly_{i}")
            self.frames_hourly.append(a)

        # Canvas
        # if the image format was jpg you have to set it like this with the commented package above
        # img = ImageTk.PhotoImage(Image.open("Pictures\\pic_no2.jpg"))
        img = PhotoImage(file="Pictures\\pic_no3.png")
        self.canvas = Canvas(width=1500, height=300)
        self.canvas.config(highlightthickness=0)
        self.canvas.create_image(750, 135, image=img)
        self.canvas.grid(column=0, row=0, columnspan=12)
        # # main forecast
        self.canvas_icon = Canvas(self.frame_today_info, width=100, height=100)
        self.icon_img = PhotoImage(file=f"Icons\\{self.datas['current']['weather'][0]['icon']}@2x.png")
        # print(f"{self.datas['current']['weather'][0]['icon']}@2x.png")
        self.canvas_icon_main = self.canvas_icon.create_image(50, 50, image=self.icon_img)
        self.canvas_icon.config(bg=NAVY_BLUE, highlightthickness=0)
        # # hourly forecast
        self.images = []
        for i in range(48):
            a = PhotoImage(file=f"Icons\\{self.datas['hourly'][i]['weather'][0]['icon']}@2x.png", name=f"img_{i}")
            self.images.append(a)
        self.canvases = []
        for i in range(48):
            a = Canvas(self.frames_hourly[i], width=100, height=100, name=f"hourly_canvas_{i}")
            a.create_image(50, 50, image=self.images[i])
            a.config(bg=NAVY_BLUE, highlightthickness=0)
            self.canvases.append(a)

        # Getting datas
        temp = str(self.datas['current']['temp'] - 273)
        temp_feel = str(self.datas['current']['feels_like'] - 273)
        sunrise = datetime.datetime.fromtimestamp(self.datas['current']['sunrise']).strftime("%I:%M:%S")
        sunset = datetime.datetime.fromtimestamp(self.datas['current']['sunset']).strftime("%I:%M:%S")
        text = self.datas['current']['weather'][0]['main']
        text_description = self.datas['current']['weather'][0]['description']
        wind_speed = self.datas['current']['wind_speed']
        uvi = self.datas['current']['uvi']
        humidity = self.datas['current']['humidity']
        self.dt = datetime.datetime.fromtimestamp(self.datas['current']['dt']).strftime("%A, %B %d, %Y  %I:%M:%S")

        self.canvas_icon.grid(column=0, row=0, sticky='w')
        # Labels
        # Main labels
        self.label_main = Label(self.frame_today_info, text=text, font=("nk57-monospace", "13", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_main.grid(column=0, row=1, sticky='w')
        self.label_temp = Label(self.frame_today_info,
                                text="Temp : " + str(temp)[0:5] + "  feels like " + str(temp_feel)[0:5],
                                font=("nk57-monospace", "13", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_temp.grid(column=0, row=2, sticky='w')
        self.label_description = Label(self.frame_today_info, text=text_description,
                                       font=("nk57-monospace", "13", "normal"),
                                       fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_description.grid(column=0, row=3, sticky='w')
        self.label_humidity = Label(self.frame_today_info, text="Humidity : " + str(humidity) + " %",
                                    font=("nk57-monospace", "13", "normal"),
                                    fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_humidity.grid(column=0, row=4, sticky='w')
        self.label_wind_speed = Label(self.frame_today_info, text="Wind Speed : " + str(wind_speed) + " m/s",
                                      font=("nk57-monospace", "13", "normal"),
                                      fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_wind_speed.grid(column=0, row=5, sticky='w')
        self.label_uvi = Label(self.frame_today_info, text="UVI : " + str(uvi) + " index",
                               font=("nk57-monospace", "13", "normal"),
                               fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_uvi.grid(column=0, row=6, sticky='w')

        self.frame_today_info.grid(column=0, row=1, sticky="w", padx=40, pady=20, columnspan=3, rowspan=2)

        # hourly Labels
        # hourly times
        self.hourly_time_labels = []
        for i in range(48):
            a = Label(self.frames_hourly[i],
                      text=datetime.datetime.fromtimestamp(self.datas['hourly'][i]['dt']).strftime("%I:%M:%S"),
                      font=("nk57-monospace", "8", "normal"),
                      fg="white", bg=NAVY_BLUE, highlightthickness=0, name=f"label_time_{i}")
            self.hourly_time_labels.append(a)

        # hourly temp
        self.hourly_temp_labels = []
        for i in range(48):
            a = Label(self.frames_hourly[i],
                      text="temp : " + str(self.datas['hourly'][i]['temp'] - 273)[0:5] + " / feels like " + str(
                          self.datas['hourly'][i]['feels_like'] - 273)[0:5],
                      font=("nk57-monospace", "8", "normal"),
                      fg="white", bg=NAVY_BLUE, highlightthickness=0, name=f"label_temp_{i}")
            self.hourly_temp_labels.append(a)

        # hourly main weather
        self.hourly_main_label = []
        for i in range(48):
            a = Label(self.frames_hourly[i], text=self.datas['hourly'][i]['weather'][0]['main'],
                      font=("nk57-monospace", "8", "normal"),
                      fg="white", bg=NAVY_BLUE, highlightthickness=0, name=f"label_main_{i}")
            self.hourly_main_label.append(a)

        # hourly weather description
        self.hourly_label_description = []
        for i in range(48):
            a = Label(self.frames_hourly[i], text=
            self.datas['hourly'][i]['weather'][0]['description'],
                      font=("nk57-monospace", "8", "normal"),
                      fg="white", bg=NAVY_BLUE, highlightthickness=0, name=f"label_desvription_{i}")
            self.hourly_label_description.append(a)

        self.city_text = self.canvas.create_text(85, 100, text="Karaj", font=MONOFONT, fill="white")
        self.sun_rise_set_text = self.canvas.create_text(235, 220,
                                                         text=f"sunrise : {sunrise} AM / sunset : {sunset} PM",
                                                         font=MONOFONT_NK57,
                                                         fill="white")
        self.date_text = self.canvas.create_text(200, 180, text=self.dt, font=MONOFONT_NK57, fill="white")

        # Button Labels
        self.more = Label(text="more...",font=("nk57-monospace", "8", "normal"),
                      fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.more.grid(column=10, row=4)
        self.more.bind("<Button-1>", self.more_information)

        # Buttons
        self.refresh_button = Button(text="Refresh", bg=BLUE, fg="white", font=MONOFONT_NK57, command=self.update_thread)
        self.refresh_button.grid(column=0, row=3, columnspan=3)

        # Giving position to widgets
        for i in range(48):
            self.canvases[i].grid(column=0, row=0, sticky="w")
            self.hourly_time_labels[i].grid(column=0, row=1, sticky="w")
            self.hourly_temp_labels[i].grid(column=0, row=2, sticky="w")
            self.hourly_main_label[i].grid(column=0, row=3, sticky="w")
            self.hourly_label_description[i].grid(column=0, row=4, sticky="w")

        # Giving position to frames
        for i in range(6):
            self.frames_hourly[i].grid(column=4 + i, row=1, sticky="w", padx=3, pady=4)
        for i in range(6, 12):
            self.frames_hourly[i].grid(column=4 + i - 6, row=2, sticky="w", padx=3, pady=4)

        # self.update_thread()
        self.clock_thread()

        self.window.mainloop()

    def update_thread(self):
        import threading
        t = threading.Thread(target=self.update)
        t.setDaemon(True)
        t.start()

    def update(self):
        self.response = requests.get(ENDPOINT, params=self.weather)
        self.response.raise_for_status()
        self.datas = self.response.json()
        # Update Hourly Informations
        self.images.clear()
        for i in range(48):
            self.canvases[i].grid_forget()
        self.canvases.clear()
        for i in range(48):
            self.hourly_time_labels[i]["text"] = datetime.datetime.fromtimestamp(
                self.datas['hourly'][i]['dt']).strftime("%I:%M:%S")
            self.hourly_temp_labels[i]["text"] = "temp : " + str(self.datas['hourly'][i]['temp'] - 273)[
                                                             0:5] + " / feels like " + str(
                self.datas['hourly'][i]['feels_like'] - 273)[0:5]
            self.hourly_main_label[i]["text"] = self.datas['hourly'][i]['weather'][0]['main']
            self.hourly_label_description[i]["text"] = self.datas['hourly'][i]['weather'][0]['description']
            self.images.append(
                PhotoImage(file=f"Icons\\{self.datas['hourly'][i]['weather'][0]['icon']}@2x.png", name=f"img_{i}"))
            a = Canvas(self.frames_hourly[i], width=100, height=100, name=f"hourly_canvas_{i}")
            a.create_image(50, 50, image=self.images[i])
            a.config(bg=NAVY_BLUE, highlightthickness=0)
            self.canvases.append(a)

        for i in range(48):
            self.canvases[i].grid(column=0, row=0, sticky="w")

        # Update Main Informations
        self.label_main["text"] = self.datas['current']['weather'][0]['main']
        self.label_temp["text"] = "Temp : " + str(str(self.datas['current']['temp'] - 273))[
                                              0:5] + "  feels like " + str(
            str(self.datas['current']['feels_like'] - 273))[0:5]
        self.label_humidity["text"] = "Humidity : " + str(self.datas['current']['humidity']) + " %"
        self.label_wind_speed["text"] = "Wind Speed : " + str(self.datas['current']['wind_speed']) + " m/s"
        self.label_uvi["text"] = "UVI : " + str(self.datas['current']['uvi']) + " index"
        self.icon_image = PhotoImage(file=f"Icons\\{self.datas['current']['weather'][0]['icon']}@2x.png")
        self.canvas_icon.itemconfig(self.canvas_icon_main, image=self.icon_image)

        self.dt = datetime.datetime.fromtimestamp(self.datas['current']['dt']).strftime("%A, %B %d, %Y  %I:%M:%S")
        self.canvas.itemconfig(self.date_text, text=self.dt)
        sunrise = datetime.datetime.fromtimestamp(self.datas['current']['sunrise']).strftime("%I:%M:%S")
        sunset = datetime.datetime.fromtimestamp(self.datas['current']['sunset']).strftime("%I:%M:%S")
        self.canvas.itemconfig(self.sun_rise_set_text, text=f"sunrise : {sunrise} AM / sunset : {sunset} PM")

        self.window.update()

    def clock_thread(self):
        import threading
        f = threading.Thread(target=self.clock)
        f.setDaemon(True)
        f.start()

    def clock(self):
        import time
        while True:
            time.sleep(1)
            num = self.dt.find("2022") + 5
            self.dt = self.dt[0:num] + datetime.datetime.now().strftime("%I:%M:%S")
            self.canvas.itemconfig(self.date_text, text=self.dt)
            self.window.update()

    def more_information(self, event):
        print("here")


Weather()
