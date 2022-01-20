from tkinter import *
import requests
import datetime
# from PIL import ImageTk, Image

ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
KEY = "58cd189feef4d9f808fc5630caf130a1"


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
        self.window.config(highlightthickness=0, bg="black")

        # Frames
        # Daily Forecast
        self.frame_today = Frame()
        self.frame_1 = Frame()
        self.frame_2 = Frame()
        self.frame_3 = Frame()
        self.frame_4 = Frame()
        self.frame_5 = Frame()
        self.frame_6 = Frame()
        self.frame_7 = Frame()
        # Main Page
        self.frame_today_info = Frame()
        self.frame_today_info.config(highlightthickness=0, bg="black")
        self.frame_hourly_1 = Frame()
        self.frame_hourly_2 = Frame()
        self.frame_hourly_3 = Frame()
        self.frame_hourly_4 = Frame()

        # Canvas
        # img = ImageTk.PhotoImage(Image.open("Pictures\\pic_no2.jpg"))
        img = PhotoImage(file="Pictures\\pic_no2.png")
        self.canvas = Canvas(width=1500, height=250)
        self.canvas.create_image(750, 0, image=img)
        self.canvas.pack()
        self.canvas_icon = Canvas(width=100, height=100)
        icon_img = PhotoImage(file=f"Icons\\{self.datas['current']['weather'][0]['icon']}@2x.png")
        print(f"{self.datas['current']['weather'][0]['icon']}@2x.png")
        self.canvas_icon.create_image(50, 50, image=icon_img)
        self.canvas_icon.config(bg="black", highlightthickness=0)

        # Labels
        self.label_city_name = Label(text="Karaj")
        temp = str(self.datas['current']['temp'] - 273)
        temp_feel = str(self.datas['current']['feels_like'] - 273)
        self.label_temp = Label(text=f"{temp} / feels {temp_feel}")
        sunrise = datetime.datetime.fromtimestamp(self.datas['current']['sunrise']).strftime("%I:%M:%S")
        sunset = datetime.datetime.fromtimestamp(self.datas['current']['sunset']).strftime("%I:%M:%S")
        self.sun_rise_set = Label(text=f"sunrise : {sunrise} / sunset : {sunset}")
        text = self.datas['current']['weather'][0]['main']
        self.label_weather = Label(self.frame_today_info, text=text)
        text_description = self.datas['current']['weather'][0]['description']
        self.label_description = Label(text=text_description)


        self.canvas.create_text(50, 50, text="Karaj")







        self.window.mainloop()


Weather()
