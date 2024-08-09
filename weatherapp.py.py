import tkinter as tk
import requests

# Directly define the API key here
OPENWEATHER_APIKEY = "24b97bb0e0cbdf1a03da4f1cc979e102"

def getWeather():
    city = textField.get()
    apiUrl = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APIKEY}"
    
    try:
        json_data = requests.get(apiUrl).json()
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)  
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        # rain= json_data['rain']['1h']
        sea_level = json_data['main']['sea_level']

        final_info = condition + "\n" + str(temp) + "°C" 
        final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sea level:" + str(sea_level)
        label1.config(text=final_info)
        label2.config(text=final_data)

    except Exception as e:
        label1.config(text="Error")
        label2.config(text="Could not retrieve data")

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

smallText = ("poppins", 15, "bold")
largeText = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width=20, font=largeText)
submitButton = tk.Button(canvas, text="Get Result", command=getWeather)
textField.pack(pady=20)
submitButton.pack(pady=15)

textField.focus()

label1 = tk.Label(canvas, font=largeText)
label1.pack()
label2 = tk.Label(canvas, font=smallText)
label2.pack()

canvas.mainloop()
