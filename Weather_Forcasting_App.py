from tkinter import *
import requests
import datetime
import Shadow
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
        self.window.geometry("1500x750")
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
        # Unfortunetely I didn't find a way to do it easier and I had to intialize the one by one
        self.frame_hourly_info_1 = Frame()
        self.frame_hourly_info_1.config(highlightthickness=0, bg=NAVY_BLUE)
        self.frame_hourly_info_2 = Frame()
        self.frame_hourly_info_2.config(highlightthickness=0, bg=NAVY_BLUE)
        self.frame_hourly_info_3 = Frame()
        self.frame_hourly_info_3.config(highlightthickness=0, bg=NAVY_BLUE)
        self.frame_hourly_info_4 = Frame()
        self.frame_hourly_info_4.config(highlightthickness=0, bg=NAVY_BLUE)
        self.frame_hourly_info_5 = Frame()
        self.frame_hourly_info_5.config(highlightthickness=0, bg=NAVY_BLUE)
        self.frame_hourly_info_6 = Frame()
        self.frame_hourly_info_6.config(highlightthickness=0, bg=NAVY_BLUE)
        self.frame_hourly_info_7 = Frame()
        self.frame_hourly_info_7.config(highlightthickness=0, bg=NAVY_BLUE)
        self.frame_hourly_info_8 = Frame()
        self.frame_hourly_info_8.config(highlightthickness=0, bg=NAVY_BLUE)
        self.frame_hourly_info_9 = Frame()
        self.frame_hourly_info_9.config(highlightthickness=0, bg=NAVY_BLUE)
        self.frame_hourly_info_10 = Frame()
        self.frame_hourly_info_10.config(highlightthickness=0, bg=NAVY_BLUE)
        self.frame_hourly_info_11 = Frame()
        self.frame_hourly_info_11.config(highlightthickness=0, bg=NAVY_BLUE)
        self.frame_hourly_info_12 = Frame()
        self.frame_hourly_info_12.config(highlightthickness=0, bg=NAVY_BLUE)
        self.frame_hourly_info_13 = Frame()
        self.frame_hourly_info_13.config(highlightthickness=0, bg=NAVY_BLUE)
        self.frame_hourly_info_14 = Frame()
        self.frame_hourly_info_14.config(highlightthickness=0, bg=NAVY_BLUE)
        self.frame_hourly_info_15 = Frame()
        self.frame_hourly_info_15.config(highlightthickness=0, bg=NAVY_BLUE)
        self.frame_hourly_info_16 = Frame()
        self.frame_hourly_info_16.config(highlightthickness=0, bg=NAVY_BLUE)
        self.frame_hourly_info_17 = Frame()
        self.frame_hourly_info_17.config(highlightthickness=0, bg=NAVY_BLUE)
        self.frame_hourly_info_18 = Frame()
        self.frame_hourly_info_18.config(highlightthickness=0, bg=NAVY_BLUE)
        self.frame_hourly_info_19 = Frame()
        self.frame_hourly_info_19.config(highlightthickness=0, bg=NAVY_BLUE)
        self.frame_hourly_info_20 = Frame()
        self.frame_hourly_info_20.config(highlightthickness=0, bg=NAVY_BLUE)
        self.frame_hourly_info_21 = Frame()
        self.frame_hourly_info_21.config(highlightthickness=0, bg=NAVY_BLUE)
        self.frame_hourly_info_22 = Frame()
        self.frame_hourly_info_22.config(highlightthickness=0, bg=NAVY_BLUE)
        self.frame_hourly_info_23 = Frame()
        self.frame_hourly_info_23.config(highlightthickness=0, bg=NAVY_BLUE)
        self.frame_hourly_info_24 = Frame()
        self.frame_hourly_info_24.config(highlightthickness=0, bg=NAVY_BLUE)

        # Canvas
        # if the image format was jpg you have to set it like this with the commented package above
        # img = ImageTk.PhotoImage(Image.open("Pictures\\pic_no2.jpg"))
        img = PhotoImage(file="Pictures\\pic_no3.png")
        self.canvas = Canvas(width=1500, height=300)
        self.canvas.config(highlightthickness=0)
        self.canvas.create_image(750, 135, image=img)
        self.canvas.grid(column=0, row=0, columnspan=11)
        # main forecast
        self.canvas_icon = Canvas(self.frame_today_info, width=100, height=100)
        icon_img = PhotoImage(file=f"Icons\\{self.datas['current']['weather'][0]['icon']}@2x.png")
        # print(f"{self.datas['current']['weather'][0]['icon']}@2x.png")
        self.canvas_icon.create_image(50, 50, image=icon_img)
        self.canvas_icon.config(bg=NAVY_BLUE, highlightthickness=0)
        # hourly forecast
        img_hourly_1 = PhotoImage(file=f"Icons\\{self.datas['hourly'][0]['weather'][0]['icon']}@2x.png")
        self.canvas_icon_hourly_1 = Canvas(self.frame_hourly_info_1, width=100, height=100)
        self.canvas_icon_hourly_1.create_image(50, 50, image=img_hourly_1)
        self.canvas_icon_hourly_1.config(bg=NAVY_BLUE, highlightthickness=0)

        img_hourly_2 = PhotoImage(file=f"Icons\\{self.datas['hourly'][1]['weather'][0]['icon']}@2x.png")
        self.canvas_icon_hourly_2 = Canvas(self.frame_hourly_info_2, width=100, height=100)
        self.canvas_icon_hourly_2.create_image(50, 50, image=img_hourly_2)
        self.canvas_icon_hourly_2.config(bg=NAVY_BLUE, highlightthickness=0)

        img_hourly_3 = PhotoImage(file=f"Icons\\{self.datas['hourly'][2]['weather'][0]['icon']}@2x.png")
        self.canvas_icon_hourly_3 = Canvas(self.frame_hourly_info_3, width=100, height=100)
        self.canvas_icon_hourly_3.create_image(50, 50, image=img_hourly_3)
        self.canvas_icon_hourly_3.config(bg=NAVY_BLUE, highlightthickness=0)

        img_hourly_4 = PhotoImage(file=f"Icons\\{self.datas['hourly'][3]['weather'][0]['icon']}@2x.png")
        self.canvas_icon_hourly_4 = Canvas(self.frame_hourly_info_4, width=100, height=100)
        self.canvas_icon_hourly_4.create_image(50, 50, image=img_hourly_4)
        self.canvas_icon_hourly_4.config(bg=NAVY_BLUE, highlightthickness=0)

        img_hourly_5 = PhotoImage(file=f"Icons\\{self.datas['hourly'][4]['weather'][0]['icon']}@2x.png")
        self.canvas_icon_hourly_5 = Canvas(self.frame_hourly_info_5, width=100, height=100)
        self.canvas_icon_hourly_5.create_image(50, 50, image=img_hourly_5)
        self.canvas_icon_hourly_5.config(bg=NAVY_BLUE, highlightthickness=0)

        img_hourly_6 = PhotoImage(file=f"Icons\\{self.datas['hourly'][5]['weather'][0]['icon']}@2x.png")
        self.canvas_icon_hourly_6 = Canvas(self.frame_hourly_info_6, width=100, height=100)
        self.canvas_icon_hourly_6.create_image(50, 50, image=img_hourly_6)
        self.canvas_icon_hourly_6.config(bg=NAVY_BLUE, highlightthickness=0)

        img_hourly_7 = PhotoImage(file=f"Icons\\{self.datas['hourly'][6]['weather'][0]['icon']}@2x.png")
        self.canvas_icon_hourly_7 = Canvas(self.frame_hourly_info_7, width=100, height=100)
        self.canvas_icon_hourly_7.create_image(50, 50, image=img_hourly_7)
        self.canvas_icon_hourly_7.config(bg=NAVY_BLUE, highlightthickness=0)

        img_hourly_8 = PhotoImage(file=f"Icons\\{self.datas['hourly'][7]['weather'][0]['icon']}@2x.png")
        self.canvas_icon_hourly_8 = Canvas(self.frame_hourly_info_8, width=100, height=100)
        self.canvas_icon_hourly_8.create_image(50, 50, image=img_hourly_8)
        self.canvas_icon_hourly_8.config(bg=NAVY_BLUE, highlightthickness=0)

        img_hourly_9 = PhotoImage(file=f"Icons\\{self.datas['hourly'][8]['weather'][0]['icon']}@2x.png")
        self.canvas_icon_hourly_9 = Canvas(self.frame_hourly_info_9, width=100, height=100)
        self.canvas_icon_hourly_9.create_image(50, 50, image=img_hourly_9)
        self.canvas_icon_hourly_9.config(bg=NAVY_BLUE, highlightthickness=0)

        img_hourly_10 = PhotoImage(file=f"Icons\\{self.datas['hourly'][9]['weather'][0]['icon']}@2x.png")
        self.canvas_icon_hourly_10 = Canvas(self.frame_hourly_info_10, width=100, height=100)
        self.canvas_icon_hourly_10.create_image(50, 50, image=img_hourly_10)
        self.canvas_icon_hourly_10.config(bg=NAVY_BLUE, highlightthickness=0)

        img_hourly_11 = PhotoImage(file=f"Icons\\{self.datas['hourly'][10]['weather'][0]['icon']}@2x.png")
        self.canvas_icon_hourly_11 = Canvas(self.frame_hourly_info_11, width=100, height=100)
        self.canvas_icon_hourly_11.create_image(50, 50, image=img_hourly_11)
        self.canvas_icon_hourly_11.config(bg=NAVY_BLUE, highlightthickness=0)

        img_hourly_12 = PhotoImage(file=f"Icons\\{self.datas['hourly'][11]['weather'][0]['icon']}@2x.png")
        self.canvas_icon_hourly_12 = Canvas(self.frame_hourly_info_12, width=100, height=100)
        self.canvas_icon_hourly_12.create_image(50, 50, image=img_hourly_12)
        self.canvas_icon_hourly_12.config(bg=NAVY_BLUE, highlightthickness=0)

        img_hourly_13 = PhotoImage(file=f"Icons\\{self.datas['hourly'][12]['weather'][0]['icon']}@2x.png")
        self.canvas_icon_hourly_13 = Canvas(self.frame_hourly_info_13, width=100, height=100)
        self.canvas_icon_hourly_13.create_image(50, 50, image=img_hourly_13)
        self.canvas_icon_hourly_13.config(bg=NAVY_BLUE, highlightthickness=0)

        img_hourly_1 = PhotoImage(file=f"Icons\\{self.datas['hourly'][0]['weather'][0]['icon']}@2x.png")
        self.canvas_icon_hourly_1 = Canvas(self.frame_hourly_info_1, width=100, height=100)
        self.canvas_icon_hourly_1.create_image(50, 50, image=img_hourly_1)
        self.canvas_icon_hourly_1.config(bg=NAVY_BLUE, highlightthickness=0)

        img_hourly_14 = PhotoImage(file=f"Icons\\{self.datas['hourly'][13]['weather'][0]['icon']}@2x.png")
        self.canvas_icon_hourly_14 = Canvas(self.frame_hourly_info_14, width=100, height=100)
        self.canvas_icon_hourly_14.create_image(50, 50, image=img_hourly_14)
        self.canvas_icon_hourly_14.config(bg=NAVY_BLUE, highlightthickness=0)

        img_hourly_15 = PhotoImage(file=f"Icons\\{self.datas['hourly'][14]['weather'][0]['icon']}@2x.png")
        self.canvas_icon_hourly_15 = Canvas(self.frame_hourly_info_15, width=100, height=100)
        self.canvas_icon_hourly_15.create_image(50, 50, image=img_hourly_15)
        self.canvas_icon_hourly_15.config(bg=NAVY_BLUE, highlightthickness=0)

        img_hourly_16 = PhotoImage(file=f"Icons\\{self.datas['hourly'][15]['weather'][0]['icon']}@2x.png")
        self.canvas_icon_hourly_16 = Canvas(self.frame_hourly_info_16, width=100, height=100)
        self.canvas_icon_hourly_16.create_image(50, 50, image=img_hourly_16)
        self.canvas_icon_hourly_16.config(bg=NAVY_BLUE, highlightthickness=0)

        img_hourly_17 = PhotoImage(file=f"Icons\\{self.datas['hourly'][16]['weather'][0]['icon']}@2x.png")
        self.canvas_icon_hourly_17 = Canvas(self.frame_hourly_info_17, width=100, height=100)
        self.canvas_icon_hourly_17.create_image(50, 50, image=img_hourly_17)
        self.canvas_icon_hourly_17.config(bg=NAVY_BLUE, highlightthickness=0)

        img_hourly_18 = PhotoImage(file=f"Icons\\{self.datas['hourly'][17]['weather'][0]['icon']}@2x.png")
        self.canvas_icon_hourly_18 = Canvas(self.frame_hourly_info_18, width=100, height=100)
        self.canvas_icon_hourly_18.create_image(50, 50, image=img_hourly_18)
        self.canvas_icon_hourly_18.config(bg=NAVY_BLUE, highlightthickness=0)

        img_hourly_19 = PhotoImage(file=f"Icons\\{self.datas['hourly'][18]['weather'][0]['icon']}@2x.png")
        self.canvas_icon_hourly_19 = Canvas(self.frame_hourly_info_19, width=100, height=100)
        self.canvas_icon_hourly_19.create_image(50, 50, image=img_hourly_19)
        self.canvas_icon_hourly_19.config(bg=NAVY_BLUE, highlightthickness=0)

        img_hourly_20 = PhotoImage(file=f"Icons\\{self.datas['hourly'][19]['weather'][0]['icon']}@2x.png")
        self.canvas_icon_hourly_20 = Canvas(self.frame_hourly_info_20, width=100, height=100)
        self.canvas_icon_hourly_20.create_image(50, 50, image=img_hourly_20)
        self.canvas_icon_hourly_20.config(bg=NAVY_BLUE, highlightthickness=0)

        img_hourly_21 = PhotoImage(file=f"Icons\\{self.datas['hourly'][20]['weather'][0]['icon']}@2x.png")
        self.canvas_icon_hourly_21 = Canvas(self.frame_hourly_info_21, width=100, height=100)
        self.canvas_icon_hourly_21.create_image(50, 50, image=img_hourly_21)
        self.canvas_icon_hourly_21.config(bg=NAVY_BLUE, highlightthickness=0)

        img_hourly_22 = PhotoImage(file=f"Icons\\{self.datas['hourly'][21]['weather'][0]['icon']}@2x.png")
        self.canvas_icon_hourly_22 = Canvas(self.frame_hourly_info_22, width=100, height=100)
        self.canvas_icon_hourly_22.create_image(50, 50, image=img_hourly_22)
        self.canvas_icon_hourly_22.config(bg=NAVY_BLUE, highlightthickness=0)

        img_hourly_23 = PhotoImage(file=f"Icons\\{self.datas['hourly'][22]['weather'][0]['icon']}@2x.png")
        self.canvas_icon_hourly_23 = Canvas(self.frame_hourly_info_23, width=100, height=100)
        self.canvas_icon_hourly_23.create_image(50, 50, image=img_hourly_23)
        self.canvas_icon_hourly_23.config(bg=NAVY_BLUE, highlightthickness=0)

        img_hourly_24 = PhotoImage(file=f"Icons\\{self.datas['hourly'][23]['weather'][0]['icon']}@2x.png")
        self.canvas_icon_hourly_24 = Canvas(self.frame_hourly_info_24, width=100, height=100)
        self.canvas_icon_hourly_24.create_image(50, 50, image=img_hourly_24)
        self.canvas_icon_hourly_24.config(bg=NAVY_BLUE, highlightthickness=0)


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
        dt = datetime.datetime.fromtimestamp(self.datas['current']['dt']).strftime("%A, %B %d, %Y")

        self.canvas_icon.grid(column=0, row=0, sticky='w')
        # Labels
        self.label_main = Label(self.frame_today_info, text=text, font=("nk57-monospace", "13", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_main.grid(column=0, row=1, sticky='w')
        self.label_temp = Label(self.frame_today_info, text="Temp : " + str(temp)[0:4] + "  feels like " + str(temp_feel)[0:4], font=("nk57-monospace", "11", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_temp.grid(column=0, row=2, sticky='w')
        self.label_description = Label(self.frame_today_info, text=text_description, font=("nk57-monospace", "11", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_description.grid(column=0, row=3, sticky='w')
        self.label_humidity = Label(self.frame_today_info, text="Humidity : " + str(humidity) + " %", font=("nk57-monospace", "11", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_humidity.grid(column=0, row=4, sticky='w')
        self.label_wind_speed = Label(self.frame_today_info, text="Wind Speed : " + str(wind_speed) + " m/s", font=("nk57-monospace", "11", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_wind_speed.grid(column=0, row=5, sticky='w')
        self.label_uvi = Label(self.frame_today_info, text="UVI : " + str(uvi) + " index", font=("nk57-monospace", "11", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_uvi.grid(column=0, row=6, sticky='w')

        self.frame_today_info.grid(column=0, row=1, sticky="w", padx=40, pady=20, columnspan=3, rowspan=3)

        # hourly Labels
        # hourly times
        self.label_time_1 = Label(self.frame_hourly_info_1,
            text=datetime.datetime.fromtimestamp(self.datas['hourly'][0]['dt']).strftime("%I:%M:%S"), font=("nk57-monospace", "8", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_time_2 = Label(self.frame_hourly_info_2,
            text=datetime.datetime.fromtimestamp(self.datas['hourly'][1]['dt']).strftime("%I:%M:%S"), font=("nk57-monospace", "8", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_time_3 = Label(self.frame_hourly_info_3,
            text=datetime.datetime.fromtimestamp(self.datas['hourly'][2]['dt']).strftime("%I:%M:%S"), font=("nk57-monospace", "8", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_time_4 = Label(self.frame_hourly_info_4,
            text=datetime.datetime.fromtimestamp(self.datas['hourly'][3]['dt']).strftime("%I:%M:%S"), font=("nk57-monospace", "8", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_time_5 = Label(self.frame_hourly_info_5,
            text=datetime.datetime.fromtimestamp(self.datas['hourly'][4]['dt']).strftime("%I:%M:%S"), font=("nk57-monospace", "8", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_time_6 = Label(self.frame_hourly_info_6,
            text=datetime.datetime.fromtimestamp(self.datas['hourly'][5]['dt']).strftime("%I:%M:%S"), font=("nk57-monospace", "8", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_time_7 = Label(self.frame_hourly_info_7,
            text=datetime.datetime.fromtimestamp(self.datas['hourly'][6]['dt']).strftime("%I:%M:%S"), font=("nk57-monospace", "8", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_time_8 = Label(self.frame_hourly_info_8,
            text=datetime.datetime.fromtimestamp(self.datas['hourly'][7]['dt']).strftime("%I:%M:%S"), font=("nk57-monospace", "8", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_time_9 = Label(self.frame_hourly_info_9,
            text=datetime.datetime.fromtimestamp(self.datas['hourly'][8]['dt']).strftime("%I:%M:%S"), font=("nk57-monospace", "8", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_time_10 = Label(self.frame_hourly_info_10,
            text=datetime.datetime.fromtimestamp(self.datas['hourly'][9]['dt']).strftime("%I:%M:%S"), font=("nk57-monospace", "8", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_time_11 = Label(self.frame_hourly_info_11,
            text=datetime.datetime.fromtimestamp(self.datas['hourly'][10]['dt']).strftime("%I:%M:%S"), font=("nk57-monospace", "8", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_time_12 = Label(self.frame_hourly_info_12,
            text=datetime.datetime.fromtimestamp(self.datas['hourly'][11]['dt']).strftime("%I:%M:%S"), font=("nk57-monospace", "8", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_time_13 = Label(self.frame_hourly_info_13,
            text=datetime.datetime.fromtimestamp(self.datas['hourly'][12]['dt']).strftime("%I:%M:%S"), font=("nk57-monospace", "8", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_time_14 = Label(self.frame_hourly_info_14,
            text=datetime.datetime.fromtimestamp(self.datas['hourly'][13]['dt']).strftime("%I:%M:%S"), font=("nk57-monospace", "8", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_time_15 = Label(self.frame_hourly_info_15,
            text=datetime.datetime.fromtimestamp(self.datas['hourly'][14]['dt']).strftime("%I:%M:%S"), font=("nk57-monospace", "8", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_time_16 = Label(self.frame_hourly_info_16,
            text=datetime.datetime.fromtimestamp(self.datas['hourly'][15]['dt']).strftime("%I:%M:%S"), font=("nk57-monospace", "8", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_time_17 = Label(self.frame_hourly_info_17,
            text=datetime.datetime.fromtimestamp(self.datas['hourly'][16]['dt']).strftime("%I:%M:%S"), font=("nk57-monospace", "8", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_time_18 = Label(self.frame_hourly_info_18,
            text=datetime.datetime.fromtimestamp(self.datas['hourly'][17]['dt']).strftime("%I:%M:%S"), font=("nk57-monospace", "8", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_time_19 = Label(self.frame_hourly_info_19,
            text=datetime.datetime.fromtimestamp(self.datas['hourly'][18]['dt']).strftime("%I:%M:%S"), font=("nk57-monospace", "8", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_time_20 = Label(self.frame_hourly_info_20,
            text=datetime.datetime.fromtimestamp(self.datas['hourly'][19]['dt']).strftime("%I:%M:%S"), font=("nk57-monospace", "8", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_time_21 = Label(self.frame_hourly_info_21,
            text=datetime.datetime.fromtimestamp(self.datas['hourly'][20]['dt']).strftime("%I:%M:%S"), font=("nk57-monospace", "8", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_time_22 = Label(self.frame_hourly_info_22,
            text=datetime.datetime.fromtimestamp(self.datas['hourly'][21]['dt']).strftime("%I:%M:%S"), font=("nk57-monospace", "8", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_time_23 = Label(self.frame_hourly_info_23,
            text=datetime.datetime.fromtimestamp(self.datas['hourly'][22]['dt']).strftime("%I:%M:%S"), font=("nk57-monospace", "8", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        self.label_time_24 = Label(self.frame_hourly_info_24,
            text=datetime.datetime.fromtimestamp(self.datas['hourly'][23]['dt']).strftime("%I:%M:%S"), font=("nk57-monospace", "8", "normal"),
                                fg="white", bg=NAVY_BLUE, highlightthickness=0)
        # hourly temp
        self.label_temp_1 = Label(self.frame_hourly_info_1,
                                  text="temp : " + str(self.datas['hourly'][0]['temp'])[0:4] + " / feels like " + str(
                                      self.datas['hourly'][0]['feels_like'])[0:4],
                                  font=("nk57-monospace", "8", "normal"),
                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                  )
        self.label_temp_2 = Label(self.frame_hourly_info_2,
                                  text="temp : " + str(self.datas['hourly'][1]['temp'])[0:4] + " / feels like " + str(
                                      self.datas['hourly'][1]['feels_like'])[0:4],
                                  font=("nk57-monospace", "8", "normal"),
                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                  )
        self.label_temp_3 = Label(self.frame_hourly_info_3,
                                  text="temp : " + str(self.datas['hourly'][2]['temp'])[0:4] + " / feels like " + str(
                                      self.datas['hourly'][2]['feels_like'])[0:4],
                                  font=("nk57-monospace", "8", "normal"),
                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                  )
        self.label_temp_4 = Label(self.frame_hourly_info_4,
                                  text="temp : " + str(self.datas['hourly'][3]['temp'])[0:4] + " / feels like " + str(
                                      self.datas['hourly'][3]['feels_like'])[0:4],
                                  font=("nk57-monospace", "8", "normal"),
                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                  )
        self.label_temp_5 = Label(self.frame_hourly_info_5,
                                  text="temp : " + str(self.datas['hourly'][4]['temp'])[0:4] + " / feels like " + str(
                                      self.datas['hourly'][4]['feels_like'])[0:4],
                                  font=("nk57-monospace", "8", "normal"),
                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                  )
        self.label_temp_6 = Label(self.frame_hourly_info_6,
                                  text="temp : " + str(self.datas['hourly'][5]['temp'])[0:4] + " / feels like " + str(
                                      self.datas['hourly'][5]['feels_like'])[0:4],
                                  font=("nk57-monospace", "8", "normal"),
                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                  )
        self.label_temp_7 = Label(self.frame_hourly_info_7,
                                  text="temp : " + str({self.datas['hourly'][6]['temp']})[0:4] + " / feels like " + str(
                                      self.datas['hourly'][6]['feels_like'])[0:4],
                                  font=("nk57-monospace", "8", "normal"),
                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                  )
        self.label_temp_8 = Label(self.frame_hourly_info_8,
                                  text="temp : " + str(self.datas['hourly'][7]['temp'])[0:4] + " / feels like " + str(
                                      self.datas['hourly'][7]['feels_like'])[0:4],
                                  font=("nk57-monospace", "8", "normal"),
                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                  )
        self.label_temp_9 = Label(self.frame_hourly_info_9,
                                  text="temp : " + str(self.datas['hourly'][8]['temp'])[0:4] + " / feels like " + str(
                                      self.datas['hourly'][8]['feels_like'])[0:4],
                                  font=("nk57-monospace", "8", "normal"),
                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                  )
        self.label_temp_10 = Label(self.frame_hourly_info_10,
                                  text="temp : " + str(self.datas['hourly'][9]['temp'])[0:4] + " / feels like " + str(
                                      self.datas['hourly'][9]['feels_like'])[0:4],
                                  font=("nk57-monospace", "8", "normal"),
                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                  )
        self.label_temp_11 = Label(self.frame_hourly_info_11,
                                  text="temp : " + str(self.datas['hourly'][10]['temp'])[0:4] + " / feels like " + str(
                                      self.datas['hourly'][10]['feels_like'])[0:4],
                                  font=("nk57-monospace", "8", "normal"),
                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                  )
        self.label_temp_12 = Label(self.frame_hourly_info_12,
                                  text="temp : " + str(self.datas['hourly'][11]['temp'])[0:4] + " / feels like " + str(
                                      self.datas['hourly'][11]['feels_like'])[0:4],
                                  font=("nk57-monospace", "8", "normal"),
                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                  )
        self.label_temp_13 = Label(self.frame_hourly_info_13,
                                  text="temp : " + str(self.datas['hourly'][12]['temp'])[0:4] + " / feels like " + str(
                                      self.datas['hourly'][12]['feels_like'])[0:4],
                                  font=("nk57-monospace", "8", "normal"),
                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                  )
        self.label_temp_14 = Label(self.frame_hourly_info_14,
                                  text="temp : " + str(self.datas['hourly'][13]['temp'])[0:4] + " / feels like " + str(
                                      self.datas['hourly'][13]['feels_like'])[0:4],
                                  font=("nk57-monospace", "8", "normal"),
                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                  )
        self.label_temp_15 = Label(self.frame_hourly_info_15,
                                  text="temp : " + str(self.datas['hourly'][14]['temp'])[0:4] + " / feels like " + str(
                                      self.datas['hourly'][14]['feels_like'])[0:4],
                                  font=("nk57-monospace", "8", "normal"),
                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                  )
        self.label_temp_16 = Label(self.frame_hourly_info_16,
                                  text="temp : " + str(self.datas['hourly'][15]['temp'])[0:4] + " / feels like " + str(
                                      self.datas['hourly'][15]['feels_like'])[0:4],
                                  font=("nk57-monospace", "8", "normal"),
                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                  )
        self.label_temp_17 = Label(self.frame_hourly_info_17,
                                  text="temp : " + str(self.datas['hourly'][16]['temp'])[0:4] + " / feels like " + str(
                                      self.datas['hourly'][16]['feels_like'])[0:4],
                                  font=("nk57-monospace", "8", "normal"),
                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                  )
        self.label_temp_18 = Label(self.frame_hourly_info_18,
                                  text="temp : " + str(self.datas['hourly'][17]['temp'])[0:4] + " / feels like " + str(
                                      self.datas['hourly'][17]['feels_like'])[0:4],
                                  font=("nk57-monospace", "8", "normal"),
                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                  )
        self.label_temp_19 = Label(self.frame_hourly_info_19,
                                  text="temp : " + str(self.datas['hourly'][18]['temp'])[0:4] + " / feels like " + str(
                                      self.datas['hourly'][18]['feels_like'])[0:4],
                                  font=("nk57-monospace", "8", "normal"),
                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                  )
        self.label_temp_20 = Label(self.frame_hourly_info_20,
                                  text="temp : " + str(self.datas['hourly'][19]['temp'])[0:4] + " / feels like " + str(
                                      self.datas['hourly'][19]['feels_like'])[0:4],
                                  font=("nk57-monospace", "8", "normal"),
                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                  )
        self.label_temp_21 = Label(self.frame_hourly_info_21,
                                  text="temp : " + str(self.datas['hourly'][20]['temp'])[0:4] + " / feels like " + str(
                                      self.datas['hourly'][20]['feels_like'])[0:4],
                                  font=("nk57-monospace", "8", "normal"),
                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                  )
        self.label_temp_22 = Label(self.frame_hourly_info_22,
                                  text="temp : " + str(self.datas['hourly'][21]['temp'])[0:4] + " / feels like " + str(
                                      self.datas['hourly'][21]['feels_like'])[0:4],
                                  font=("nk57-monospace", "8", "normal"),
                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                  )
        self.label_temp_23 = Label(self.frame_hourly_info_23,
                                  text="temp : " + str(self.datas['hourly'][22]['temp'])[0:4] + " / feels like " + str(
                                      self.datas['hourly'][22]['feels_like'])[0:4],
                                  font=("nk57-monospace", "8", "normal"),
                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                  )
        self.label_temp_24 = Label(self.frame_hourly_info_24,
                                  text="temp : " + str(self.datas['hourly'][23]['temp'])[0:4] + " / feels like " + str(
                                      self.datas['hourly'][23]['feels_like'])[0:4],
                                  font=("nk57-monospace", "8", "normal"),
                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                  )
        # hourly main weather
        self.label_weather_main_1 = Label(self.frame_hourly_info_1,
                                                 text=self.datas['hourly'][0]['weather'][0]['main'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_main_2 = Label(self.frame_hourly_info_2,
                                                 text=self.datas['hourly'][1]['weather'][0]['main'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_main_3 = Label(self.frame_hourly_info_3,
                                                 text=self.datas['hourly'][2]['weather'][0]['main'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_main_4 = Label(self.frame_hourly_info_4,
                                                 text=self.datas['hourly'][3]['weather'][0]['main'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_main_5 = Label(self.frame_hourly_info_5,
                                                 text=self.datas['hourly'][4]['weather'][0]['main'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_main_6 = Label(self.frame_hourly_info_6,
                                                 text=self.datas['hourly'][5]['weather'][0]['main'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_main_7 = Label(self.frame_hourly_info_7,
                                                 text=self.datas['hourly'][6]['weather'][0]['main'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_main_8 = Label(self.frame_hourly_info_8,
                                                 text=self.datas['hourly'][7]['weather'][0]['main'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_main_9 = Label(self.frame_hourly_info_9,
                                                 text=self.datas['hourly'][8]['weather'][0]['main'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_main_10 = Label(self.frame_hourly_info_10,
                                                 text=self.datas['hourly'][9]['weather'][0]['main'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_main_11 = Label(self.frame_hourly_info_11,
                                                 text=self.datas['hourly'][10]['weather'][0]['main'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_main_12 = Label(self.frame_hourly_info_12,
                                                 text=self.datas['hourly'][11]['weather'][0]['main'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_main_13 = Label(self.frame_hourly_info_13,
                                                 text=self.datas['hourly'][12]['weather'][0]['main'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_main_14 = Label(self.frame_hourly_info_14,
                                                 text=self.datas['hourly'][13]['weather'][0]['main'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_main_15 = Label(self.frame_hourly_info_15,
                                                 text=self.datas['hourly'][14]['weather'][0]['main'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_main_16 = Label(self.frame_hourly_info_16,
                                                 text=self.datas['hourly'][15]['weather'][0]['main'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_main_17 = Label(self.frame_hourly_info_17,
                                                 text=self.datas['hourly'][16]['weather'][0]['main'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_main_18 = Label(self.frame_hourly_info_18,
                                                 text=self.datas['hourly'][17]['weather'][0]['main'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_main_19 = Label(self.frame_hourly_info_19,
                                                 text=self.datas['hourly'][18]['weather'][0]['main'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_main_20 = Label(self.frame_hourly_info_20,
                                                 text=self.datas['hourly'][19]['weather'][0]['main'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_main_21 = Label(self.frame_hourly_info_21,
                                                 text=self.datas['hourly'][20]['weather'][0]['main'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_main_22 = Label(self.frame_hourly_info_22,
                                                 text=self.datas['hourly'][21]['weather'][0]['main'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_main_23 = Label(self.frame_hourly_info_23,
                                                 text=self.datas['hourly'][22]['weather'][0]['main'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_main_24 = Label(self.frame_hourly_info_24,
                                                  text=self.datas['hourly'][23]['weather'][0]['main'],
                                                  font=("nk57-monospace", "8", "normal"),
                                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                  )

        # hourly weather description
        self.label_weather_description_1 = Label(self.frame_hourly_info_1,
                                                 text=
                                                      self.datas['hourly'][0]['weather'][0]['description'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_description_2 = Label(self.frame_hourly_info_2,
                                                 text=
                                                      self.datas['hourly'][1]['weather'][0]['description'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_description_3 = Label(self.frame_hourly_info_3,
                                                 text=
                                                      self.datas['hourly'][2]['weather'][0]['description'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_description_4 = Label(self.frame_hourly_info_4,
                                                 text=
                                                      self.datas['hourly'][3]['weather'][0]['description'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_description_5 = Label(self.frame_hourly_info_5,
                                                 text=
                                                      self.datas['hourly'][4]['weather'][0]['description'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_description_6 = Label(self.frame_hourly_info_6,
                                                 text=
                                                      self.datas['hourly'][5]['weather'][0]['description'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_description_7 = Label(self.frame_hourly_info_7,
                                                 text=
                                                      self.datas['hourly'][6]['weather'][0]['description'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_description_8 = Label(self.frame_hourly_info_8,
                                                 text=
                                                      self.datas['hourly'][7]['weather'][0]['description'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_description_9 = Label(self.frame_hourly_info_9,
                                                 text=
                                                      self.datas['hourly'][8]['weather'][0]['description'],
                                                 font=("nk57-monospace", "8", "normal"),
                                                 fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                 )
        self.label_weather_description_10 = Label(self.frame_hourly_info_10,
                                                  text=
                                                       self.datas['hourly'][9]['weather'][0]['description'],
                                                  font=("nk57-monospace", "8", "normal"),
                                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                  )
        self.label_weather_description_11 = Label(self.frame_hourly_info_11,
                                                  text=
                                                       self.datas['hourly'][10]['weather'][0]['description'],
                                                  font=("nk57-monospace", "8", "normal"),
                                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                  )
        self.label_weather_description_12 = Label(self.frame_hourly_info_12,
                                                  text=
                                                       self.datas['hourly'][11]['weather'][0]['description'],
                                                  font=("nk57-monospace", "8", "normal"),
                                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                  )
        self.label_weather_description_13 = Label(self.frame_hourly_info_13,
                                                  text=
                                                       self.datas['hourly'][12]['weather'][0]['description'],
                                                  font=("nk57-monospace", "8", "normal"),
                                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                  )
        self.label_weather_description_14 = Label(self.frame_hourly_info_14,
                                                  text=
                                                       self.datas['hourly'][13]['weather'][0]['description'],
                                                  font=("nk57-monospace", "8", "normal"),
                                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                  )
        self.label_weather_description_15 = Label(self.frame_hourly_info_15,
                                                  text=
                                                       self.datas['hourly'][14]['weather'][0]['description'],
                                                  font=("nk57-monospace", "8", "normal"),
                                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                  )
        self.label_weather_description_16 = Label(self.frame_hourly_info_16,
                                                  text=
                                                       self.datas['hourly'][15]['weather'][0]['description'],
                                                  font=("nk57-monospace", "8", "normal"),
                                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                  )
        self.label_weather_description_17 = Label(self.frame_hourly_info_17,
                                                  text=
                                                       self.datas['hourly'][16]['weather'][0]['description'],
                                                  font=("nk57-monospace", "8", "normal"),
                                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                  )
        self.label_weather_description_18 = Label(self.frame_hourly_info_18,
                                                  text=
                                                       self.datas['hourly'][17]['weather'][0]['description'],
                                                  font=("nk57-monospace", "8", "normal"),
                                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                  )
        self.label_weather_description_19 = Label(self.frame_hourly_info_19,
                                                  text=
                                                       self.datas['hourly'][18]['weather'][0]['description'],
                                                  font=("nk57-monospace", "8", "normal"),
                                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                  )
        self.label_weather_description_20 = Label(self.frame_hourly_info_20,
                                                  text=
                                                       self.datas['hourly'][19]['weather'][0]['description'],
                                                  font=("nk57-monospace", "8", "normal"),
                                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                  )
        self.label_weather_description_21 = Label(self.frame_hourly_info_21,
                                                  text=
                                                       self.datas['hourly'][20]['weather'][0]['description'],
                                                  font=("nk57-monospace", "8", "normal"),
                                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                  )
        self.label_weather_description_22 = Label(self.frame_hourly_info_22,
                                                  text=
                                                       self.datas['hourly'][21]['weather'][0]['description'],
                                                  font=("nk57-monospace", "8", "normal"),
                                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                  )
        self.label_weather_description_23 = Label(self.frame_hourly_info_23,
                                                  text=
                                                       self.datas['hourly'][22]['weather'][0]['description'],
                                                  font=("nk57-monospace", "8", "normal"),
                                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                  )
        self.label_weather_description_24 = Label(self.frame_hourly_info_24,
                                                  text=
                                                       self.datas['hourly'][23]['weather'][0]['description'],
                                                  font=("nk57-monospace", "8", "normal"),
                                                  fg="white", bg=NAVY_BLUE, highlightthickness=0
                                                  )




        self.canvas.create_text(85, 100, text="Karaj", font=MONOFONT, fill="white")
        self.canvas.create_text(235, 220, text=f"sunrise : {sunrise} AM / sunset : {sunset} PM", font=MONOFONT_NK57, fill="white")
        self.canvas.create_text(160, 180, text=dt, font=MONOFONT_NK57, fill="white")

        # Giving position to widgets
        self.canvas_icon_hourly_1.grid(column=0, row=0, sticky="w")
        self.label_time_1.grid(column=0, row=1, sticky="w")
        self.label_temp_1.grid(column=0, row=2, sticky="w")
        self.label_weather_main_1.grid(column=0, row=3, sticky="w")
        self.label_weather_description_1.grid(column=0, row=4, sticky="w")

        self.canvas_icon_hourly_2.grid(column=0, row=0, sticky="w")
        self.label_time_2.grid(column=0, row=1, sticky="w")
        self.label_temp_2.grid(column=0, row=2, sticky="w")
        self.label_weather_main_2.grid(column=0, row=3, sticky="w")
        self.label_weather_description_2.grid(column=0, row=4, sticky="w")

        self.canvas_icon_hourly_3.grid(column=0, row=0, sticky="w")
        self.label_time_3.grid(column=0, row=1, sticky="w")
        self.label_temp_3.grid(column=0, row=2, sticky="w")
        self.label_weather_main_3.grid(column=0, row=3, sticky="w")
        self.label_weather_description_3.grid(column=0, row=4, sticky="w")

        self.canvas_icon_hourly_4.grid(column=0, row=0, sticky="w")
        self.label_time_4.grid(column=0, row=1, sticky="w")
        self.label_temp_4.grid(column=0, row=2, sticky="w")
        self.label_weather_main_4.grid(column=0, row=3, sticky="w")
        self.label_weather_description_4.grid(column=0, row=4, sticky="w")

        self.canvas_icon_hourly_5.grid(column=0, row=0, sticky="w")
        self.label_time_5.grid(column=0, row=1, sticky="w")
        self.label_temp_5.grid(column=0, row=2, sticky="w")
        self.label_weather_main_5.grid(column=0, row=3, sticky="w")
        self.label_weather_description_5.grid(column=0, row=4, sticky="w")

        self.canvas_icon_hourly_6.grid(column=0, row=0, sticky="w")
        self.label_time_6.grid(column=0, row=1, sticky="w")
        self.label_temp_6.grid(column=0, row=2, sticky="w")
        self.label_weather_main_6.grid(column=0, row=3, sticky="w")
        self.label_weather_description_6.grid(column=0, row=4, sticky="w")

        self.canvas_icon_hourly_7.grid(column=0, row=0, sticky="w")
        self.label_time_7.grid(column=0, row=1, sticky="w")
        self.label_temp_7.grid(column=0, row=2, sticky="w")
        self.label_weather_main_7.grid(column=0, row=3, sticky="w")
        self.label_weather_description_7.grid(column=0, row=4, sticky="w")

        self.canvas_icon_hourly_8.grid(column=0, row=0, sticky="w")
        self.label_time_8.grid(column=0, row=1, sticky="w")
        self.label_temp_8.grid(column=0, row=2, sticky="w")
        self.label_weather_main_8.grid(column=0, row=3, sticky="w")
        self.label_weather_description_8.grid(column=0, row=4, sticky="w")

        self.canvas_icon_hourly_9.grid(column=0, row=0, sticky="w")
        self.label_time_9.grid(column=0, row=1, sticky="w")
        self.label_temp_9.grid(column=0, row=2, sticky="w")
        self.label_weather_main_9.grid(column=0, row=3, sticky="w")
        self.label_weather_description_9.grid(column=0, row=4, sticky="w")

        self.canvas_icon_hourly_10.grid(column=0, row=0, sticky="w")
        self.label_time_10.grid(column=0, row=1, sticky="w")
        self.label_temp_10.grid(column=0, row=2, sticky="w")
        self.label_weather_main_10.grid(column=0, row=3, sticky="w")
        self.label_weather_description_10.grid(column=0, row=4, sticky="w")

        self.canvas_icon_hourly_11.grid(column=0, row=0, sticky="w")
        self.label_time_11.grid(column=0, row=1, sticky="w")
        self.label_temp_11.grid(column=0, row=2, sticky="w")
        self.label_weather_main_11.grid(column=0, row=3, sticky="w")
        self.label_weather_description_11.grid(column=0, row=4, sticky="w")

        self.canvas_icon_hourly_12.grid(column=0, row=0, sticky="w")
        self.label_time_12.grid(column=0, row=1, sticky="w")
        self.label_temp_12.grid(column=0, row=2, sticky="w")
        self.label_weather_main_12.grid(column=0, row=3, sticky="w")
        self.label_weather_description_12.grid(column=0, row=4, sticky="w")

        self.canvas_icon_hourly_13.grid(column=0, row=0, sticky="w")
        self.label_time_13.grid(column=0, row=1, sticky="w")
        self.label_temp_13.grid(column=0, row=2, sticky="w")
        self.label_weather_main_13.grid(column=0, row=3, sticky="w")
        self.label_weather_description_13.grid(column=0, row=4, sticky="w")

        self.canvas_icon_hourly_14.grid(column=0, row=0, sticky="w")
        self.label_time_14.grid(column=0, row=1, sticky="w")
        self.label_temp_14.grid(column=0, row=2, sticky="w")
        self.label_weather_main_14.grid(column=0, row=3, sticky="w")
        self.label_weather_description_14.grid(column=0, row=4, sticky="w")

        self.canvas_icon_hourly_15.grid(column=0, row=0, sticky="w")
        self.label_time_15.grid(column=0, row=1, sticky="w")
        self.label_temp_15.grid(column=0, row=2, sticky="w")
        self.label_weather_main_15.grid(column=0, row=3, sticky="w")
        self.label_weather_description_15.grid(column=0, row=4, sticky="w")

        self.canvas_icon_hourly_16.grid(column=0, row=0, sticky="w")
        self.label_time_16.grid(column=0, row=1, sticky="w")
        self.label_temp_16.grid(column=0, row=2, sticky="w")
        self.label_weather_main_16.grid(column=0, row=3, sticky="w")
        self.label_weather_description_16.grid(column=0, row=4, sticky="w")

        self.canvas_icon_hourly_17.grid(column=0, row=0, sticky="w")
        self.label_time_17.grid(column=0, row=1, sticky="w")
        self.label_temp_17.grid(column=0, row=2, sticky="w")
        self.label_weather_main_17.grid(column=0, row=3, sticky="w")
        self.label_weather_description_17.grid(column=0, row=4, sticky="w")

        self.canvas_icon_hourly_18.grid(column=0, row=0, sticky="w")
        self.label_time_18.grid(column=0, row=1, sticky="w")
        self.label_temp_18.grid(column=0, row=2, sticky="w")
        self.label_weather_main_18.grid(column=0, row=3, sticky="w")
        self.label_weather_description_18.grid(column=0, row=4, sticky="w")

        self.canvas_icon_hourly_19.grid(column=0, row=0, sticky="w")
        self.label_time_19.grid(column=0, row=1, sticky="w")
        self.label_temp_19.grid(column=0, row=2, sticky="w")
        self.label_weather_main_19.grid(column=0, row=3, sticky="w")
        self.label_weather_description_19.grid(column=0, row=4, sticky="w")

        self.canvas_icon_hourly_20.grid(column=0, row=0, sticky="w")
        self.label_time_20.grid(column=0, row=1, sticky="w")
        self.label_temp_20.grid(column=0, row=2, sticky="w")
        self.label_weather_main_20.grid(column=0, row=3, sticky="w")
        self.label_weather_description_20.grid(column=0, row=4, sticky="w")

        self.canvas_icon_hourly_21.grid(column=0, row=0, sticky="w")
        self.label_time_21.grid(column=0, row=1, sticky="w")
        self.label_temp_21.grid(column=0, row=2, sticky="w")
        self.label_weather_main_21.grid(column=0, row=3, sticky="w")
        self.label_weather_description_21.grid(column=0, row=4, sticky="w")

        self.canvas_icon_hourly_22.grid(column=0, row=0, sticky="w")
        self.label_time_22.grid(column=0, row=1, sticky="w")
        self.label_temp_22.grid(column=0, row=2, sticky="w")
        self.label_weather_main_22.grid(column=0, row=3, sticky="w")
        self.label_weather_description_22.grid(column=0, row=4, sticky="w")

        self.canvas_icon_hourly_23.grid(column=0, row=0, sticky="w")
        self.label_time_23.grid(column=0, row=1, sticky="w")
        self.label_temp_23.grid(column=0, row=2, sticky="w")
        self.label_weather_main_23.grid(column=0, row=3, sticky="w")
        self.label_weather_description_23.grid(column=0, row=4, sticky="w")

        self.canvas_icon_hourly_24.grid(column=0, row=0, sticky="w")
        self.label_time_24.grid(column=0, row=1, sticky="w")
        self.label_temp_24.grid(column=0, row=2, sticky="w")
        self.label_weather_main_24.grid(column=0, row=3, sticky="w")
        self.label_weather_description_24.grid(column=0, row=4, sticky="w")

        # Giving position to frames
        self.frame_hourly_info_1.grid(column=4, row=1, sticky="w", padx=3, pady=4)
        self.frame_hourly_info_2.grid(column=5, row=1, sticky="w", padx=3, pady=4)
        self.frame_hourly_info_3.grid(column=6, row=1, sticky="w", padx=3, pady=4)
        self.frame_hourly_info_4.grid(column=7, row=1, sticky="w", padx=3, pady=4)
        self.frame_hourly_info_5.grid(column=8, row=1, sticky="w", padx=3, pady=4)
        self.frame_hourly_info_6.grid(column=9, row=1, sticky="w", padx=3, pady=4)
        self.frame_hourly_info_7.grid(column=4, row=2, sticky="w", padx=3, pady=4)
        self.frame_hourly_info_8.grid(column=5, row=2, sticky="w", padx=3, pady=4)
        self.frame_hourly_info_9.grid(column=6, row=2, sticky="w", padx=3, pady=4)
        self.frame_hourly_info_10.grid(column=7, row=2, sticky="w", padx=3, pady=4)
        self.frame_hourly_info_11.grid(column=8, row=2, sticky="w", padx=3, pady=4)
        self.frame_hourly_info_12.grid(column=9, row=2, sticky="w", padx=3, pady=4)











        self.window.mainloop()





Weather()
