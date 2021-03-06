import tkinter
from tkinter import *
import requests
import datetime
from tkinter import ttk

# from PIL import ImageTk, Image

ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
GEOCODING_ENDPOINT = "https://api.opencagedata.com/geocode/v1/json"
KEY = "YOUR KEY"
GEOCODING_KEY = "YOUR KEY"

# Fonts
MONTERY = ("MontereyFLF", "15", "normal")
NOVA = ("NovaMono", "20", "normal")
MONOFONT = ("MONOFONT", "25", "bold")
MONOFONT_NK57 = ("nk57-monospace", "14", "normal")
VONIQUE = ("Vonique 64", "40", "bold")

# Colors
NAVY_BLUE = "#1A374D"
BLUE = "#406882"
CAYN = "#7CD1B8"


class Weather:
    def __init__(self):

        self.city = "Karaj"
        self.city_temp = ""
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
        self.frames_daily = []
        for i in range(8):
            a = Frame(highlightthickness=0, bg=NAVY_BLUE, name=f"frame_daily_{i}")
            self.frames_daily.append(a)
        # Main Page
        self.frame_today_info = Frame()
        self.frame_today_info.config(highlightthickness=0, bg=NAVY_BLUE)
        # Hourly Forcast

        self.frames_hourly = []
        for i in range(48):
            a = Frame(highlightthickness=0, bg=NAVY_BLUE, name=f"frame_hourly_{i}")
            self.frames_hourly.append(a)
        # Frame for Labels
        self.label_button_frame = Frame(bg=NAVY_BLUE, highlightthickness=0)
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

        self.canvas_icon.grid(column=1, row=0, sticky='w')
        # Labels
        # Main labels
        self.label_main = Label(self.frame_today_info, text=text, font=("nk57-monospace", "13", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_main.grid(column=1, row=1, sticky='w')
        self.label_description = Label(self.frame_today_info, text=text_description,
                                       font=("nk57-monospace", "13", "normal"),
                                       fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_description.grid(column=1, row=2, sticky='w')
        self.label_temp = Label(self.frame_today_info,
                                text="Temp : " + str(temp)[0:5] + "  feels like " + str(temp_feel)[0:5],
                                font=("nk57-monospace", "13", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_temp.grid(column=1, row=3, sticky='w')
        self.label_humidity = Label(self.frame_today_info, text="Humidity : " + str(humidity) + " %",
                                    font=("nk57-monospace", "13", "normal"),
                                    fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_humidity.grid(column=1, row=4, sticky='w')
        self.label_wind_speed = Label(self.frame_today_info, text="Wind Speed : " + str(wind_speed) + " m/s",
                                      font=("nk57-monospace", "13", "normal"),
                                      fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_wind_speed.grid(column=1, row=5, sticky='w')
        self.label_uvi = Label(self.frame_today_info, text="UVI : " + str(uvi) + " index",
                               font=("nk57-monospace", "13", "normal"),
                               fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_uvi.grid(column=1, row=6, sticky='w')
        self.canvas_main_icon = Canvas(self.frame_today_info, width=30, height=30)
        self.canvas_des_icon = Canvas(self.frame_today_info, width=30, height=30)
        self.canvas_wind_icon = Canvas(self.frame_today_info, width=30, height=30)
        self.canvas_humidity_icon = Canvas(self.frame_today_info, width=30, height=30)
        self.canvas_uvi_icon = Canvas(self.frame_today_info, width=30, height=30)
        self.canvas_sun_icon = Canvas(self.frame_today_info, width=30, height=30)
        self.canvas_temp_icon = Canvas(self.frame_today_info, width=30, height=30)
        self.canvas_main_icon.grid(column=0, row=1, sticky="w")
        self.canvas_des_icon.grid(column=0, row=2, sticky="w")
        self.canvas_temp_icon.grid(column=0, row=3, sticky="w")
        self.canvas_humidity_icon.grid(column=0, row=4, sticky="w")
        self.canvas_wind_icon.grid(column=0, row=5, sticky="w")
        self.canvas_uvi_icon.grid(column=0, row=6, sticky="w")
        self.canvas_main_icon.config(bg=NAVY_BLUE, highlightthickness=0)
        self.canvas_des_icon.config(bg=NAVY_BLUE, highlightthickness=0)
        self.canvas_temp_icon.config(bg=NAVY_BLUE, highlightthickness=0)
        self.canvas_uvi_icon.config(bg=NAVY_BLUE, highlightthickness=0)
        self.canvas_humidity_icon.config(bg=NAVY_BLUE, highlightthickness=0)
        self.canvas_sun_icon.config(bg=NAVY_BLUE, highlightthickness=0)
        self.canvas_wind_icon.config(bg=NAVY_BLUE, highlightthickness=0)
        self.img_main_icon = PhotoImage(file="Icons\\main.png")
        self.img_moon_icon = PhotoImage(file="Icons\\moon3.png")
        self.img_sun_icon = PhotoImage(file="Icons\\sun.png")
        self.img_time_icon = PhotoImage(file="Icons\\time.png")
        self.img_cloud_icon = PhotoImage(file="Icons\\cloud.png")
        self.img_moon_icon = PhotoImage(file="Icons\\moon3.png")
        self.img_uvi_icon = PhotoImage(file="Icons\\uvi.png")
        self.img_wind_icon = PhotoImage(file="Icons\\wind_speed2.png")
        self.img_humidity_icon = PhotoImage(file="Icons\\humidity.png")
        self.img_temp_icon = PhotoImage(file="Icons\\temp2.png")
        self.img_calender_icon = PhotoImage(file="Icons\\calender.png")
        self.canvas_main_icon.create_image(15, 15, image=self.img_main_icon)
        self.canvas_des_icon.create_image(15, 15, image=self.img_main_icon)
        self.canvas_temp_icon.create_image(15, 15, image=self.img_temp_icon)
        self.canvas_wind_icon.create_image(15, 15, image=self.img_wind_icon)
        self.canvas_uvi_icon.create_image(15, 15, image=self.img_uvi_icon)
        self.canvas_humidity_icon.create_image(15, 15, image=self.img_humidity_icon)

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

        self.city_text = self.canvas.create_text(45, 100, text=self.city, font=MONOFONT, fill="white", anchor="nw")
        self.sun_rise_set_text = self.canvas.create_text(45, 220,
                                                         text=f"sunrise : {sunrise} AM / sunset : {sunset} PM",
                                                         font=MONOFONT_NK57,
                                                         fill="white", anchor="nw")
        self.date_text = self.canvas.create_text(45, 180, text=self.dt, font=MONOFONT_NK57, fill="white", anchor="nw")

        # Button Labels
        self.more = Label(text="more...", font=("nk57-monospace", "8", "normal"),
                          fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.more.grid(column=10, row=4)
        self.more.bind("<Button-1>", self.more_information)
        self.home_page = Label(text="Home", font=("nk57-monospace", "8", "normal"),
                               fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.daily_page = self.canvas.create_text(70, 30, text="Daily", font=("nk57-monospace", "10", "normal"),
                                                  fill="white")
        self.home_page_canvas = self.canvas.create_text(210, 30, text="Refresh",
                                                        font=("nk57-monospace", "10", "normal"),
                                                        fill="white")
        self.hourly_page = self.canvas.create_text(140, 30, text="Hourly", font=("nk57-monospace", "10", "normal"),
                                                   fill="white")
        self.canvas.tag_bind(self.daily_page, "<Button-1>", self.daily_clicked)
        self.canvas.tag_bind(self.home_page_canvas, "<Button-1>", self.update_thread)
        self.canvas.tag_bind(self.hourly_page, "<Button-1>", self.more_information)

        self.home_label = Label(self.label_button_frame, text="Home", font=("nk57-monospace", "15", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.next_label = Label(self.label_button_frame, text="Next", font=("nk57-monospace", "15", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.previous_label = Label(self.label_button_frame, text="Previous", font=("nk57-monospace", "15", "normal"),
                                    fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.back_label = Label(text="Back", font=("nk57-monospace", "15", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.home_label.bind("<Button-1>", self.home_clicked)
        self.next_label.bind("<Button-1>", self.next_clicked)
        self.previous_label.bind("<Button-1>", self.previous_clicked)
        self.back_label.bind("<Button-1>", self.back_clicked)

        # Labels
        self.today_label = Label(text="Today", font=("nk57-monospace", "20", "bold"),
                                 fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.tomorrow_label = Label(text="Tomorrow", font=("nk57-monospace", "20", "bold"),
                                    fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.daily_text = Label(text="Daily", font=("nk57-monospace", "35", "bold"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)

        # Entry
        self.searchbox = Entry(width=20)
        self.searchbox.config(highlightbackground=BLUE)
        self.searchbox.insert(0, "Search")
        self.searchbox['state'] = "disable"
        self.searchbox.bind("<Button-1>", self.enable)
        self.searchbox.bind("<KeyRelease>", self.disable)
        self.searchbox.bind("<Return>", self.search_city)

        # Button_label
        self.search_img = PhotoImage(file="Icons\\search.png")
        self.search_lbl = Label(image=self.search_img, bg=NAVY_BLUE, highlightthickness=0)
        self.search_lbl.bind("<Button-1>", self.search_city)

        self.canvas.create_window(1300, 175, window=self.searchbox, anchor="nw")
        self.canvas.create_window(1280, 175, window=self.search_lbl, anchor="nw")
        self.canvas.create_text(650, 40, text="Weather", anchor="nw", fill="#007ba7", font=VONIQUE)

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

        # Setting the Daily frames
        self.dt_daily = []
        for i in range(8):
            a = Label(self.frames_daily[i],
                      text=datetime.datetime.fromtimestamp(self.datas['daily'][i]['dt']).strftime("%A"),
                      font=("nk57-monospace", "13", "bold"),
                      fg="white", bg=NAVY_BLUE, highlightthickness=0, name=f"dt_daily_{i}")
            self.dt_daily.append(a)
        self.dt_daily[0]["text"] = "Today"
        self.sunrise_daily = []
        for i in range(8):
            a = Label(self.frames_daily[i], text="sunrise : " + str(
                datetime.datetime.fromtimestamp(self.datas['daily'][i]['sunrise']).strftime("%I:%M:%S")),
                      font=("nk57-monospace", "11", "normal"),
                      fg="white", bg=NAVY_BLUE, highlightthickness=0, name=f"sunrise_daily_{i}")
            self.sunrise_daily.append(a)
        self.sunset_daily = []
        for i in range(8):
            a = Label(self.frames_daily[i], text="sunset : " + str(
                datetime.datetime.fromtimestamp(self.datas['daily'][i]['sunset']).strftime("%I:%M:%S")),
                      font=("nk57-monospace", "11", "normal"),
                      fg="white", bg=NAVY_BLUE, highlightthickness=0, name=f"sunset_daily_{i}")
            self.sunset_daily.append(a)
        self.moonrise_daily = []
        for i in range(8):
            a = Label(self.frames_daily[i], text="moonrise : " + str(
                datetime.datetime.fromtimestamp(self.datas['daily'][i]['moonrise']).strftime("%I:%M:%S")),
                      font=("nk57-monospace", "11", "normal"),
                      fg="white", bg=NAVY_BLUE, highlightthickness=0, name=f"moonrise_daily_{i}")
            self.moonrise_daily.append(a)
        self.moonset_daily = []
        for i in range(8):
            a = Label(self.frames_daily[i], text="moonset : " + str(
                datetime.datetime.fromtimestamp(self.datas['daily'][i]['moonset']).strftime("%I:%M:%S")),
                      font=("nk57-monospace", "11", "normal"),
                      fg="white", bg=NAVY_BLUE, highlightthickness=0, name=f"moonset_daily_{i}")
            self.moonset_daily.append(a)
        self.temp_daily = []
        for i in range(8):
            a = Label(self.frames_daily[i], text="min : " + str(self.datas['daily'][i]['temp']['min'] - 273)[0:5] +
                                                 "/ max : " + str(self.datas['daily'][i]['temp']['max'] - 273)[0:5],
                      font=("nk57-monospace", "11", "normal"),
                      fg="white", bg=NAVY_BLUE, highlightthickness=0, name=f"temp_daily_{i}")
            self.temp_daily.append(a)
        self.main_daily = []
        for i in range(8):
            a = Label(self.frames_daily[i], text=self.datas['daily'][i]['weather'][0]['main'],
                      font=("nk57-monospace", "11", "normal"),
                      fg="white", bg=NAVY_BLUE, highlightthickness=0, name=f"main_daily_{i}")
            self.main_daily.append(a)
        self.description_daily = []
        for i in range(8):
            a = Label(self.frames_daily[i], text=self.datas['daily'][i]['weather'][0]['description'],
                      font=("nk57-monospace", "11", "normal"),
                      fg="white", bg=NAVY_BLUE, highlightthickness=0, name=f"description_daily_{i}")
            self.description_daily.append(a)
        self.icon_images_daily = []
        for i in range(8):
            a = PhotoImage(file=f"Icons\\{self.datas['daily'][i]['weather'][0]['icon']}@2x.png", name=f"icon_daily_{i}")
            self.icon_images_daily.append(a)
        self.canvases_daily = []
        for i in range(8):
            a = Canvas(self.frames_daily[i], width=100, height=100, name=f"daily_canvas_{i}")
            a.create_image(50, 50, image=self.icon_images_daily[i])
            a.config(bg=NAVY_BLUE, highlightthickness=0)
            self.canvases_daily.append(a)
        self.clouds_daily = []
        for i in range(8):
            a = Label(self.frames_daily[i], text="Clouds : " + str(self.datas['daily'][i]['clouds']) + " %",
                      font=("nk57-monospace", "11", "normal"),
                      fg="white", bg=NAVY_BLUE, highlightthickness=0, name=f"clouds_daily_{i}")
            self.clouds_daily.append(a)
        self.uvi_daily = []
        for i in range(8):
            a = Label(self.frames_daily[i], text="UVI : " + str(self.datas['daily'][i]['uvi']) + " index",
                      font=("nk57-monospace", "11", "normal"),
                      fg="white", bg=NAVY_BLUE, highlightthickness=0, name=f"uvi_daily_{i}")
            self.uvi_daily.append(a)
        self.humidity_daily = []
        for i in range(8):
            a = Label(self.frames_daily[i], text="humidity : " + str(self.datas['daily'][i]['humidity']) + " %",
                      font=("nk57-monospace", "11", "normal"),
                      fg="white", bg=NAVY_BLUE, highlightthickness=0, name=f"humidity_daily_{i}")
            self.humidity_daily.append(a)
        self.wind_speed_daily = []
        for i in range(8):
            a = Label(self.frames_daily[i], text="wind speed : " + str(self.datas['daily'][i]['wind_speed']) + " m/s",
                      font=("nk57-monospace", "11", "normal"),
                      fg="white", bg=NAVY_BLUE, highlightthickness=0, name=f"wind_speed_daily_{i}")
            self.wind_speed_daily.append(a)
        self.canvas_dt_daily = []
        for i in range(8):
            a = Canvas(self.frames_daily[i], width=30, height=30, name=f"canvas_dt_{i}")
            a.config(highlightthickness=0, bg=NAVY_BLUE)
            a.create_image(15, 15, image=self.img_calender_icon)
            self.canvas_dt_daily.append(a)
        self.canvas_main_daily = []
        for i in range(8):
            a = Canvas(self.frames_daily[i], width=30, height=30, name=f"canvas_main_{i}")
            a.config(highlightthickness=0, bg=NAVY_BLUE)
            a.create_image(15, 15, image=self.img_main_icon)
            self.canvas_main_daily.append(a)
        self.canvas_des_daily = []
        for i in range(8):
            a = Canvas(self.frames_daily[i], width=30, height=30, name=f"canvas_description_{i}")
            a.config(highlightthickness=0, bg=NAVY_BLUE)
            a.create_image(15, 15, image=self.img_main_icon)
            self.canvas_des_daily.append(a)
        self.canvas_sunrise_daily = []
        for i in range(8):
            a = Canvas(self.frames_daily[i], width=30, height=30, name=f"canvas_sunrise_{i}")
            a.config(highlightthickness=0, bg=NAVY_BLUE)
            a.create_image(15, 15, image=self.img_sun_icon)
            self.canvas_sunrise_daily.append(a)
        self.canvas_sunset_daily = []
        for i in range(8):
            a = Canvas(self.frames_daily[i], width=30, height=30, name=f"canvas_sunset_{i}")
            a.config(highlightthickness=0, bg=NAVY_BLUE)
            a.create_image(15, 15, image=self.img_sun_icon)
            self.canvas_sunset_daily.append(a)
        self.canvas_moonrise_daily = []
        for i in range(8):
            a = Canvas(self.frames_daily[i], width=30, height=30, name=f"canvas_moonrise_{i}")
            a.config(highlightthickness=0, bg=NAVY_BLUE)
            a.create_image(15, 15, image=self.img_moon_icon)
            self.canvas_moonrise_daily.append(a)
        self.canvas_moonset_daily = []
        for i in range(8):
            a = Canvas(self.frames_daily[i], width=30, height=30, name=f"canvas_moonset_{i}")
            a.config(highlightthickness=0, bg=NAVY_BLUE)
            a.create_image(15, 15, image=self.img_moon_icon)
            self.canvas_moonset_daily.append(a)
        self.canvas_clouds_daily = []
        for i in range(8):
            a = Canvas(self.frames_daily[i], width=30, height=30, name=f"canvas_clouds_{i}")
            a.config(highlightthickness=0, bg=NAVY_BLUE)
            a.create_image(15, 15, image=self.img_cloud_icon)
            self.canvas_clouds_daily.append(a)
        self.canvas_uvi_daily = []
        for i in range(8):
            a = Canvas(self.frames_daily[i], width=30, height=30, name=f"canvas_uvi_{i}")
            a.config(highlightthickness=0, bg=NAVY_BLUE)
            a.create_image(15, 15, image=self.img_uvi_icon)
            self.canvas_uvi_daily.append(a)
        self.canvas_wind_daily = []
        for i in range(8):
            a = Canvas(self.frames_daily[i], width=30, height=30, name=f"canvas_wind_{i}")
            a.config(highlightthickness=0, bg=NAVY_BLUE)
            a.create_image(15, 15, image=self.img_wind_icon)
            self.canvas_wind_daily.append(a)
        self.canvas_humidity_daily = []
        for i in range(8):
            a = Canvas(self.frames_daily[i], width=30, height=30, name=f"canvas_humidity_{i}")
            a.config(highlightthickness=0, bg=NAVY_BLUE)
            a.create_image(15, 15, image=self.img_humidity_icon)
            self.canvas_humidity_daily.append(a)
        self.canvas_temp_daily = []
        for i in range(8):
            a = Canvas(self.frames_daily[i], width=30, height=30, name=f"canvas_temp_{i}")
            a.config(highlightthickness=0, bg=NAVY_BLUE)
            a.create_image(15, 15, image=self.img_temp_icon)
            self.canvas_temp_daily.append(a)
        # Giving position to daily widgets
        for i in range(8):
            self.canvases_daily[i].grid(column=0, row=0, columnspan=2)
            self.dt_daily[i].grid(column=1, row=1, sticky="w")
            self.canvas_dt_daily[i].grid(column=0, row=1, sticky="w")
            self.main_daily[i].grid(column=1, row=2, sticky="w")
            self.canvas_main_daily[i].grid(column=0, row=2, sticky="w")
            self.description_daily[i].grid(column=1, row=3, sticky="w")
            self.canvas_des_daily[i].grid(column=0, row=3, sticky="w")
            self.temp_daily[i].grid(column=1, row=4, sticky="w")
            self.canvas_temp_daily[i].grid(column=0, row=4, sticky="w")
            self.sunrise_daily[i].grid(column=1, row=5, sticky="w")
            self.canvas_sunrise_daily[i].grid(column=0, row=5, sticky="w")
            self.sunset_daily[i].grid(column=1, row=6, sticky="w")
            self.canvas_sunset_daily[i].grid(column=0, row=6, sticky="w")
            self.moonrise_daily[i].grid(column=1, row=7, sticky="w")
            self.canvas_moonrise_daily[i].grid(column=0, row=7, sticky="w")
            self.moonset_daily[i].grid(column=1, row=8, sticky="w")
            self.canvas_moonset_daily[i].grid(column=0, row=8, sticky="w")
            self.clouds_daily[i].grid(column=1, row=9, sticky="w")
            self.canvas_clouds_daily[i].grid(column=0, row=9, sticky="w")
            self.uvi_daily[i].grid(column=1, row=10, sticky="w")
            self.canvas_uvi_daily[i].grid(column=0, row=10, sticky="w")
            self.humidity_daily[i].grid(column=1, row=11, sticky="w")
            self.canvas_humidity_daily[i].grid(column=0, row=11, sticky="w")
            self.wind_speed_daily[i].grid(column=1, row=12, sticky="w")
            self.canvas_wind_daily[i].grid(column=0, row=12, sticky="w")

        # Labels for daily page
        self.next_lbl_daily = Label(text="Next",
                                    font=("nk57-monospace", "15", "normal"),
                                    fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.next_lbl_daily.bind("<Button-1>", self.next_daily)
        self.previous_lbl_daily = Label(text="Previous",
                                        font=("nk57-monospace", "15", "normal"),
                                        fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.previous_lbl_daily.bind("<Button-1>", self.previous_daily)

        self.clock_thread()

        self.window.mainloop()

    def next_daily(self, event):
        # Forgetting
        for i in range(4):
            self.frames_daily[i].grid_forget()
        self.next_lbl_daily.grid_forget()
        # Setting
        # Giving position to frames
        for i in range(4, 8):
            self.frames_daily[i].grid(column=i - 4, row=1, padx=80, pady=60)
        self.previous_lbl_daily.grid(column=3, row=2, padx=20, pady=15)

    def previous_daily(self, event):
        # Forgetting
        for i in range(4, 8):
            self.frames_daily[i].grid_forget()
        self.previous_lbl_daily.grid_forget()
        # Setting
        self.next_lbl_daily.grid(column=3, row=2, padx=20, pady=15)
        for i in range(4):
            self.frames_daily[i].grid(column=i, row=1, padx=80, pady=60)

    def daily_clicked(self, event):
        # Forgetting
        self.canvas.grid_forget()
        self.frame_today_info.grid_forget()
        for i in range(12):
            self.frames_hourly[i].grid_forget()
        self.more.grid_forget()
        # Setting
        # Giving position to frames
        for i in range(4):
            self.frames_daily[i].grid(column=i, row=1, padx=80, pady=60)
        self.daily_text.grid(column=1, row=0, padx=20, pady=15, columnspan=2)
        self.back_label.grid(column=0, row=2, padx=20, pady=15)
        self.next_lbl_daily.grid(column=3, row=2, padx=20, pady=15)

    def search_city(self, event):
        response = requests.get(GEOCODING_ENDPOINT, params={'q': self.searchbox.get(), 'key': GEOCODING_KEY})
        response.raise_for_status()
        ans: dict = response.json()
        lat = ans['results'][0]['geometry']['lat']
        lon = ans['results'][0]['geometry']['lng']
        self.weather['lat'] = lat
        self.weather['lon'] = lon
        self.city = self.searchbox.get()
        self.canvas.itemconfig(self.city_text, text=self.city)
        self.update_thread(1)
        self.searchbox.delete(0, END)
        self.searchbox.insert(0, "Search")
        self.searchbox['state'] = "disable"

    def enable(self, event):
        self.searchbox['state'] = "normal"
        self.searchbox.delete(0, END)

    def disable(self, event):
        if len(self.searchbox.get()) == 0:
            self.city_temp = self.searchbox.get()
            self.searchbox.insert(0, "Search")
            self.searchbox['state'] = "disable"

    def update_thread(self, event):
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

        # Update Daily informations
        self.icon_images_daily.clear()
        for i in range(8):
            self.canvases_daily[i].grid_forget()
        self.canvases_daily.clear()
        for i in range(8):
            self.dt_daily[i]['text'] = datetime.datetime.fromtimestamp(self.datas['daily'][i]['dt']).strftime("%A")
            self.sunrise_daily[i]['text'] = "sunrise : " + str(
                datetime.datetime.fromtimestamp(self.datas['daily'][i]['sunrise']).strftime("%I:%M:%S"))
            self.sunset_daily[i]['text'] = "sunset : " + str(
                datetime.datetime.fromtimestamp(self.datas['daily'][i]['sunset']).strftime("%I:%M:%S"))
            self.moonrise_daily[i]['text'] = "moonrise : " + str(
                datetime.datetime.fromtimestamp(self.datas['daily'][i]['moonrise']).strftime("%I:%M:%S"))
            self.moonset_daily[i]['text'] = "moonset : " + str(
                datetime.datetime.fromtimestamp(self.datas['daily'][i]['moonset']).strftime("%I:%M:%S"))
            self.temp_daily[i]['text'] = "min : " + str(self.datas['daily'][i]['temp']['min'] - 273)[
                                                    0:5] + "/ max : " + str(
                self.datas['daily'][i]['temp']['max'] - 273)[0:5]
            self.main_daily[i]['text'] = self.datas['daily'][i]['weather'][0]['main']
            self.description_daily[i]['text'] = self.datas['daily'][i]['weather'][0]['description']
            self.clouds_daily[i]['text'] = "Clouds : " + str(self.datas['daily'][i]['clouds']) + " %"
            self.uvi_daily[i]['text'] = "UVI : " + str(self.datas['daily'][i]['uvi']) + " index"
            self.humidity_daily[i]['text'] = "humidity : " + str(self.datas['daily'][i]['humidity']) + " %"
            self.wind_speed_daily[i]['text'] = "wind speed : " + str(self.datas['daily'][i]['wind_speed']) + " m/s"
            self.icon_images_daily.append(
                PhotoImage(file=f"Icons\\{self.datas['daily'][i]['weather'][0]['icon']}@2x.png",
                           name=f"icon_daily_{i}"))
        self.dt_daily[0]['text'] = "Today"
        for i in range(8):
            a = Canvas(self.frames_daily[i], width=100, height=100, name=f"daily_canvas_{i}")
            a.create_image(50, 50, image=self.icon_images_daily[i])
            a.config(bg=NAVY_BLUE, highlightthickness=0)
            self.canvases_daily.append(a)
        for i in range(8):
            self.canvases_daily[i].grid(column=0, row=0)

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
            self.dt = datetime.datetime.fromtimestamp(time.mktime((datetime.datetime.strptime(self.dt,
                                                                                              "%A, %B %d, %Y %I:%M:%S") + datetime.timedelta(
                seconds=1)).timetuple())).strftime("%A, %B %d, %Y %I:%M:%S")
            self.canvas.itemconfig(self.date_text, text=self.dt)
            self.window.update()

    def more_information(self, event):
        # Forgetting
        self.canvas.grid_forget()
        self.frame_today_info.grid_forget()
        for i in range(12):
            self.frames_hourly[i].grid_forget()
        self.more.grid_forget()
        # Setting
        for i in range(6):
            self.frames_hourly[i].grid(column=1 + i, row=0, padx=25, pady=5)
        for i in range(6, 12):
            self.frames_hourly[i].grid(column=1 + i - 6, row=1, padx=25, pady=5)
        for i in range(12, 18):
            self.frames_hourly[i].grid(column=1 + i - 12, row=2, padx=25, pady=5)
        for i in range(18, 24):
            self.frames_hourly[i].grid(column=1 + i - 18, row=3, padx=25, pady=5)
        self.today_label.grid(column=0, row=0, pady=25)
        self.home_label.grid(column=0, row=0, pady=10, sticky="w")
        self.next_label.grid(column=0, row=1, pady=10, sticky="w")
        self.label_button_frame.grid(column=0, row=3, padx=100)

    def back_clicked(self, event):
        # Forgetting
        for i in range(4):
            self.frames_daily[i].grid_forget()
        self.next_lbl_daily.grid_forget()
        self.previous_lbl_daily.grid_forget()
        for i in range(4, 8):
            self.frames_daily[i].grid_forget()
        self.daily_text.grid_forget()
        self.back_label.grid_forget()
        # Setting
        # frames
        for i in range(6):
            self.frames_hourly[i].grid(column=4 + i, row=1, sticky="w", padx=3, pady=4)
        for i in range(6, 12):
            self.frames_hourly[i].grid(column=4 + i - 6, row=2, sticky="w", padx=3, pady=4)
        # Other widgets
        self.more.grid(column=10, row=4)
        self.canvas.grid(column=0, row=0, columnspan=12)
        self.frame_today_info.grid(column=0, row=1, sticky="w", padx=40, pady=20, columnspan=3, rowspan=2)

    def next_clicked(self, event):
        # Forgetting
        for i in range(24):
            self.frames_hourly[i].grid_forget()
        self.today_label.grid_forget()
        self.next_label.grid_forget()
        # Setting
        for i in range(24, 30):
            self.frames_hourly[i].grid(column=1 + i - 24, row=0, padx=25, pady=5)
        for i in range(30, 36):
            self.frames_hourly[i].grid(column=1 + i - 30, row=1, padx=25, pady=5)
        for i in range(36, 42):
            self.frames_hourly[i].grid(column=1 + i - 36, row=2, padx=25, pady=5)
        for i in range(42, 48):
            self.frames_hourly[i].grid(column=1 + i - 42, row=3, padx=25, pady=5)
        self.previous_label.grid(column=0, row=1, pady=10, sticky="w")
        self.tomorrow_label.grid(column=0, row=0, pady=25)

    def home_clicked(self, event):
        # Forgetting
        try:
            self.today_label.grid_forget()
            for i in range(24):
                self.frames_hourly[i].grid_forget()
        except:
            pass
        try:
            self.tomorrow_label.grid_forget()
            for i in range(24, 48):
                self.frames_hourly[i].grid_forget()
        except:
            pass
        self.label_button_frame.grid_forget()
        # Setting
        # frames
        for i in range(6):
            self.frames_hourly[i].grid(column=4 + i, row=1, sticky="w", padx=3, pady=4)
        for i in range(6, 12):
            self.frames_hourly[i].grid(column=4 + i - 6, row=2, sticky="w", padx=3, pady=4)
        # Other widgets
        self.more.grid(column=10, row=4)
        self.canvas.grid(column=0, row=0, columnspan=12)
        self.frame_today_info.grid(column=0, row=1, sticky="w", padx=40, pady=20, columnspan=3, rowspan=2)

    def previous_clicked(self, event):
        # Forgetting
        for i in range(24, 48):
            self.frames_hourly[i].grid_forget()
        self.tomorrow_label.grid_forget()
        self.previous_label.grid_forget()
        # Setting
        for i in range(6):
            self.frames_hourly[i].grid(column=1 + i, row=0, padx=25, pady=5)
        for i in range(6, 12):
            self.frames_hourly[i].grid(column=1 + i - 6, row=1, padx=25, pady=5)
        for i in range(12, 18):
            self.frames_hourly[i].grid(column=1 + i - 12, row=2, padx=25, pady=5)
        for i in range(18, 24):
            self.frames_hourly[i].grid(column=1 + i - 18, row=3, padx=25, pady=5)
        self.today_label.grid(column=0, row=0, pady=25)
        self.next_label.grid(column=0, row=1, pady=10, sticky="w")


Weather()
