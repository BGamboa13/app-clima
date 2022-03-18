import tkinter as tk
from tkinter import messagebox
import requests
import PIL.Image, PIL.ImageTk

class ClimaApp(tk.Tk):
    def __init__(self,):
         super().__init__()

         self.inicializar_gui()
         self.API_OPEN_WEATHER_MAP = 'ede128f1fcdce9db572a4e0545b2ff25'
         self.URL_OPEN_WEATHER_MAP = 'https://api.openweathermap.org/data/2.5/weather'

    def inicializar_gui(self):
        self.title("Estado del clima")

        canvas = tk.Canvas(self, width=500, height=600)
        canvas.pack()

        img_landscape = PIL.Image.open("day_landscape_by_sergio9929-dbcjfsz.png")
        img_landscape = PIL.ImageTk.PhotoImage(img_landscape)
        lbl_landscape = tk.Label(self, image=img_landscape)
        lbl_landscape.image = img_landscape
        lbl_landscape.place(relx=0, rely=0, relwidth="1", relheight="1")

        frm_componentes = tk.Frame(self, bg="white", bd=5)
        frm_componentes.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

        self.txt_ciudad = tk.Entry(frm_componentes, font=("Arial", 12))
        self.txt_ciudad.place(relx=0, rely=0, relwidth=0.65, relheight=1)

        btn_buscar = tk.Button(frm_componentes, fg="white", bg="#2D3142", text="Buscar", font=("Arial", 12), command=self.buscar_ciudad)
        btn_buscar.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

        frm_resultados = tk.Frame(self, bg="white", bd=5)
        frm_resultados.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

        self.lbl_resultado = tk.Label(frm_resultados, text="", font=("Arial", 12))
        self.lbl_resultado.place(relx=0, rely=0, relwidth=1, relheight=1)

    def buscar_ciudad(self):
        ciudad = self.txt_ciudad.get().strip()

        if len(ciudad) == 0:
            messagebox.showerror("Error", "Debe ingresar una ciudad")
            return

        params = {'q': ciudad, 'appid': self.API_OPEN_WEATHER_MAP, 'units': 'metric'}
        response = requests.get(self.URL_OPEN_WEATHER_MAP,params)
        data = response.json()

        self.lbl_resultado['text'] = self.obtener_resultado(data)

    def obtener_resultado(self, data):
        if data['cod'] == 200:
            ciudad = data['name']
            temperatura = data['main']['temp']
            resultado = "La temperatura de {} es de {} grados".format(ciudad, temperatura)
        else:
            resultado = "No se pudo determinar el clima de la ciudad"

        return resultado

def main():
    app = ClimaApp()
    app.mainloop()

if __name__ == '__main__':
    main()