from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import NoTransition
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import ThreeLineAvatarIconListItem
from kivymd.uix.button import MDFlatButton
from kivymd.toast import toast
import requests

# delhi key = "202396"
 
class City():

  text = "Delhi"
  secondary_text = "India"
  tertiary_text = "202396"

  current = {
    "WeatherText": "",
    "WeatherIcon": "",
    "DateTime": "22/22/22 22:22:22+05:30",
    "Temperature": "",
    "RealFeelTemperature": "",
    "DewPoint": "",
    "CloudCover": "",
    "RelativeHumidity": "",
    "IndoorRelativeHumidity": "",
    "Wind": "",
    "WindGust": "",
    "UVIndex": "",
    "Visibility": "",
    "Pressure": "",
    "Precipitation": "",
    "SunRise": "",
    "SunSet": "",
    "MoonRise": "",
    "MoonSet": ""
  }

  forecast = {
  	"Date": "",
  	"WeatherText": "",
  	"MinTemp": "",
  	"MaxTemp": "",
  	"MinRealFeel": "",
  	"MaxRealFeel": "",
  	"HrsOfSun": "",
  	"AirQuality": "",
  	"UVIndex": ""
  }

  day_forecast = {
  	"Icon": "",
  	"Text": "",
  	"PrecpProb": "",
  	"ThunderProb": "",
  	"RainProb": "",
  	"SnowProb": "",
  	"IceProb": "",
  	"CloudCover": "",
  	"Wind": "",
  	"WindGust": ""
  }

  night_forecast = {
  	"Icon": "",
  	"Text": "",
  	"PrecpProb": "",
  	"ThunderProb": "",
  	"RainProb": "",
  	"SnowProb": "",
  	"IceProb": "",
  	"CloudCover": "",
  	"Wind": "",
  	"WindGust": ""
  }

class ConfirmCity(ThreeLineAvatarIconListItem):
	divider = None
	check = ObjectProperty(None)

class GetWeather(MDApp):
	api_key = "wIbO7AmIwOQLzaXAq5XY73kxXsjHhaVO"
	dialog = None
	selected_city = City()

	def build(self):
		return Builder.load_file("design.kv")

	def call_api(self, api):
		try:
			toast("SEARCHING...")
			data = requests.get(api)
			if data.status_code != 200:
				raise ValueError
			return data.json()
		except:
			toast("Error!!!")

	def searched(self, searched_text):
		
		if len(searched_text) == 0:
			toast("Enter something first")
				
		else:
			searched_cities = self.call_api(f"http://dataservice.accuweather.com/locations/v1/cities/autocomplete?apikey={self.api_key}&q={searched_text}")
			if not searched_cities :
				return
			list_cities = []
			for i in range(len(searched_cities)):
				list_cities.append(
					ConfirmCity(
						text = searched_cities[i]["LocalizedName"],
						secondary_text = searched_cities[i]["Country"]["LocalizedName"],
						tertiary_text = searched_cities[i]["Key"],
						)
					)

			list_cities[0].check.active = True
			self.selected_city.text = list_cities[0].text
			self.selected_city.secondary_text = list_cities[0].secondary_text
			self.selected_city.tertiary_text = list_cities[0].tertiary_text
			print(self.selected_city.text)

			if not self.dialog:
				self.dialog = MDDialog(
					title = "Select Your City",
					type = "confirmation",
					items = list_cities,
					auto_dismiss = False,
					size_hint = (.9, .5),
					buttons = [MDFlatButton(text = "Ok", on_release = self.update_main_screen_data),],
					)
				self.dialog.open()

	def close_dialog(self, *args):
		if self.dialog:
			self.dialog.dismiss()
			self.dialog = None

	def select_city(self, instance_check, city_item):
		instance_check.active = True
		self.selected_city.text = city_item.text
		self.selected_city.secondary_text = city_item.secondary_text
		self.selected_city.tertiary_text = city_item.tertiary_text
		print(self.selected_city.text)

		check_list = instance_check.get_widgets(instance_check.group)
		for check in check_list:
			if check != instance_check:
				check.active = False

	def update_main_screen_data(self, *args):
		self.close_dialog()

		# current_data = self.call_api(f"http://dataservice.accuweather.com/currentconditions/v1/{self.selected_city.tertiary_text}?apikey={self.api_key}&details=true")
		# forecast_data = self.call_api(f"http://dataservice.accuweather.com/forecasts/v1/daily/1day/{self.selected_city.tertiary_text}?apikey={self.api_key}&details=true&metric=true")
		# if not current_data or not forecast_data:
		# 	return



if __name__ == "__main__":
	GetWeather().run()
