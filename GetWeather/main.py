from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import NoTransition
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import ThreeLineAvatarIconListItem
from kivymd.uix.button import MDFlatButton
from kivymd.toast import toast
from kivy.clock import Clock
import requests
 
class City():

  text = "Delhi"
  secondary_text = "India"
  tertiary_text = "202396"

  current = {
    "WeatherText": "",
    "WeatherIcon": "",
    "DateTime": "",
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
	api_keys = [] #Write your api keys here in this list
	dialog = None
	selected_city = City()

	def build(self):
		self.icon = "assets/icon.png"
		return Builder.load_file("design.kv")

	def on_start(self):
		self.update_main_screen_data()

	def about_developer(self):
		self.root.ids.nav_drawer.set_state('close')
		MDDialog(text="This app is developed by Hammad Ali using kivy module and accuweather api.").open()

	def change_theme(self, btn):
		if self.theme_cls.theme_style == "Light":
			self.theme_cls.theme_style = "Dark"
			btn.text = "Light Theme"
		else:
			self.theme_cls.theme_style = "Light"
			btn.text = "Dark Theme"

	def change_color(self, btn):
		self.theme_cls.primary_palette = btn.text

	def call_api(self, api):
		try:
			for i in range(len(self.api_keys)):
				api_to_use = api.replace("api_key_here", self.api_keys[i])
				data = requests.get(api_to_use)
				if data.status_code != 503:
					break
			if data.status_code != 200:
				raise ValueError
			return data.json()
		except Exception as e:
			toast("Error!!!")

	def searched(self, searched_text, *largs):
		if len(searched_text) == 0:
			toast("Enter something first")
				
		else:
			searched_cities = self.call_api(f"http://dataservice.accuweather.com/locations/v1/cities/autocomplete?apikey=api_key_here&q={searched_text}")
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

			if not self.dialog:
				self.dialog = MDDialog(
					title = "Select Your City",
					type = "confirmation",
					items = list_cities,
					auto_dismiss = False,
					size_hint = (.9, .5),
					buttons = [MDFlatButton(text = "Ok", on_release = lambda btn: Clock.schedule_once(self.update_main_screen_data, 1), ripple_scale= 2),],
					)
				self.dialog.open()

	def select_city(self, instance_check, city_item):
		instance_check.active = True
		self.selected_city.text = city_item.text
		self.selected_city.secondary_text = city_item.secondary_text
		self.selected_city.tertiary_text = city_item.tertiary_text

		check_list = instance_check.get_widgets(instance_check.group)
		for check in check_list:
			if check != instance_check:
				check.active = False

	def update_main_screen_data(self, *args):
		if self.dialog:
			self.dialog.dismiss()
			self.dialog = None

		current_data = self.call_api(f"http://dataservice.accuweather.com/currentconditions/v1/{self.selected_city.tertiary_text}?apikey=api_key_here&details=true")
		forecast_data = self.call_api(f"http://dataservice.accuweather.com/forecasts/v1/daily/1day/{self.selected_city.tertiary_text}?apikey=api_key_here&details=true&metric=true")
		if not current_data or not forecast_data:
			return

		self.selected_city.current['WeatherText'] = str(current_data[0]['WeatherText'])
		self.selected_city.current['WeatherIcon'] = str(current_data[0]['WeatherIcon']) if current_data[0]['WeatherIcon']>=10 else "0"+str(current_data[0]['WeatherIcon'])
		self.selected_city.current['Temperature'] = str(current_data[0]['Temperature']['Metric']['Value'])
		self.selected_city.current['DateTime'] = str(current_data[0]['LocalObservationDateTime'].replace('T', ' '))
		self.selected_city.current['RealFeelTemperature'] = str(current_data[0]['RealFeelTemperature']['Metric']['Value'])
		self.selected_city.current['DewPoint'] = str(current_data[0]['DewPoint']['Metric']['Value'])
		self.selected_city.current['CloudCover'] = str(current_data[0]['CloudCover'])
		self.selected_city.current['RelativeHumidity'] = str(current_data[0]['RelativeHumidity'])
		self.selected_city.current['IndoorRelativeHumidity'] = str(current_data[0]['IndoorRelativeHumidity'])
		self.selected_city.current['Wind'] = f"{current_data[0]['Wind']['Direction']['Localized']} {current_data[0]['Wind']['Speed']['Metric']['Value']}"
		self.selected_city.current['WindGust'] = str(current_data[0]['WindGust']['Speed']['Metric']['Value'])
		self.selected_city.current['UVIndex'] = str(current_data[0]['UVIndexText'])
		self.selected_city.current['Visibility'] = str(current_data[0]['Visibility']['Metric']['Value'])
		self.selected_city.current['Pressure'] = str(current_data[0]['Pressure']['Metric']['Value'])
		self.selected_city.current['Precipitation'] = str(current_data[0]['PrecipitationSummary']['Precipitation']['Metric']['Value'])

		self.selected_city.current['SunRise'] = str(forecast_data['DailyForecasts'][0]['Sun']['Rise'].split('T')[1][:8])
		self.selected_city.current['SunSet'] = str(forecast_data['DailyForecasts'][0]['Sun']['Set'].split('T')[1][:8])
		self.selected_city.current['MoonRise'] = str(forecast_data['DailyForecasts'][0]['Moon']['Rise'].split('T')[1][:8])
		self.selected_city.current['MoonSet'] = str(forecast_data['DailyForecasts'][0]['Moon']['Rise'].split('T')[1][:8])
		
		self.selected_city.forecast['Date'] = str(forecast_data['Headline']['EffectiveDate'].split('T')[0])
		self.selected_city.forecast['WeatherText'] = str(forecast_data['Headline']['Text'])
		self.selected_city.forecast['MinTemp'] = str(forecast_data['DailyForecasts'][0]['Temperature']['Minimum']['Value'])
		self.selected_city.forecast['MaxTemp'] = str(forecast_data['DailyForecasts'][0]['Temperature']['Maximum']['Value'])
		self.selected_city.forecast['MinRealFeel'] = str(forecast_data['DailyForecasts'][0]['RealFeelTemperature']['Minimum']['Value'])
		self.selected_city.forecast['MaxRealFeel'] = str(forecast_data['DailyForecasts'][0]['RealFeelTemperature']['Maximum']['Value'])
		self.selected_city.forecast['HrsOfSun'] = str(forecast_data['DailyForecasts'][0]['HoursOfSun'])
		self.selected_city.forecast['AirQuality'] = str(forecast_data['DailyForecasts'][0]['AirAndPollen'][0]['Category'])
		self.selected_city.forecast['UVIndex'] = str(forecast_data['DailyForecasts'][0]['AirAndPollen'][-1]['Category'])
		
		self.selected_city.day_forecast['Icon'] = str(forecast_data['DailyForecasts'][0]['Day']['Icon']) if forecast_data['DailyForecasts'][0]['Day']['Icon'] >= 10 else '0'+str(forecast_data['DailyForecasts'][0]['Day']['Icon'])
		self.selected_city.day_forecast['Text'] = str(forecast_data['DailyForecasts'][0]['Day']['IconPhrase'])
		self.selected_city.day_forecast['PrecpProb'] = str(forecast_data['DailyForecasts'][0]['Day']['PrecipitationProbability'])
		self.selected_city.day_forecast['ThunderProb'] = str(forecast_data['DailyForecasts'][0]['Day']['ThunderstormProbability'])
		self.selected_city.day_forecast['RainProb'] = str(forecast_data['DailyForecasts'][0]['Day']['RainProbability'])
		self.selected_city.day_forecast['SnowProb'] = str(forecast_data['DailyForecasts'][0]['Day']['SnowProbability'])
		self.selected_city.day_forecast['IceProb'] = str(forecast_data['DailyForecasts'][0]['Day']['IceProbability'])
		self.selected_city.day_forecast['CloudCover'] = str(forecast_data['DailyForecasts'][0]['Day']['CloudCover'])
		self.selected_city.day_forecast['Wind'] = f"{forecast_data['DailyForecasts'][0]['Day']['Wind']['Direction']['Localized']} {forecast_data['DailyForecasts'][0]['Day']['Wind']['Speed']['Value']}"
		self.selected_city.day_forecast['WindGust'] = str(forecast_data['DailyForecasts'][0]['Day']['WindGust']['Speed']['Value'])

		self.selected_city.night_forecast['Icon'] = str(forecast_data['DailyForecasts'][0]['Night']['Icon']) if forecast_data['DailyForecasts'][0]['Night']['Icon'] >= 10 else '0'+str(forecast_data['DailyForecasts'][0]['Night']['Icon'])
		self.selected_city.night_forecast['Text'] = str(forecast_data['DailyForecasts'][0]['Night']['IconPhrase'])
		self.selected_city.night_forecast['PrecpProb'] = str(forecast_data['DailyForecasts'][0]['Night']['PrecipitationProbability'])
		self.selected_city.night_forecast['ThunderProb'] = str(forecast_data['DailyForecasts'][0]['Night']['ThunderstormProbability'])
		self.selected_city.night_forecast['RainProb'] = str(forecast_data['DailyForecasts'][0]['Night']['RainProbability'])
		self.selected_city.night_forecast['SnowProb'] = str(forecast_data['DailyForecasts'][0]['Night']['SnowProbability'])
		self.selected_city.night_forecast['IceProb'] = str(forecast_data['DailyForecasts'][0]['Night']['IceProbability'])
		self.selected_city.night_forecast['CloudCover'] = str(forecast_data['DailyForecasts'][0]['Night']['CloudCover'])
		self.selected_city.night_forecast['Wind'] = f"{forecast_data['DailyForecasts'][0]['Night']['Wind']['Direction']['Localized']} {forecast_data['DailyForecasts'][0]['Day']['Wind']['Speed']['Value']}"
		self.selected_city.night_forecast['WindGust'] = str(forecast_data['DailyForecasts'][0]['Night']['WindGust']['Speed']['Value'])

		self.root.ids.city_info.text = f"{self.selected_city.text}, {self.selected_city.secondary_text}"
		self.root.ids.current_weather_text.text = self.selected_city.current['WeatherText']
		self.root.ids.current_weather_icon.source = f"https://developer.accuweather.com/sites/default/files/{self.selected_city.current['WeatherIcon']}-s.png"
		self.root.ids.current_temp.text = f"{self.selected_city.current['Temperature']} \u00B0C"
		self.root.ids.current_datetime.text = self.selected_city.current['DateTime']
		self.root.ids.current_real_feel_temp.text = f"{self.selected_city.current['RealFeelTemperature']} \u00B0C"
		self.root.ids.current_dew_point.text = f"{self.selected_city.current['DewPoint']} \u00B0C"
		self.root.ids.current_cloud_cover.text = f"{self.selected_city.current['CloudCover']} %"
		self.root.ids.current_relative_humidity.text = f"{self.selected_city.current['RelativeHumidity']} %"
		self.root.ids.current_indoor_relative_humidity.text = f"{self.selected_city.current['IndoorRelativeHumidity']} %"
		self.root.ids.current_wind.text = f"{self.selected_city.current['Wind']} km/hr"
		self.root.ids.current_wind_gust.text =  f"{self.selected_city.current['WindGust']} km/hr"
		self.root.ids.current_uv_index.text = self.selected_city.current['UVIndex']
		self.root.ids.current_visibility.text = f"{self.selected_city.current['Visibility']} km"
		self.root.ids.current_pressure.text = f"{self.selected_city.current['Pressure']} mb"
		self.root.ids.current_precipitation.text = f"{self.selected_city.current['Precipitation']} mm"
		self.root.ids.current_date.text = self.selected_city.current['DateTime'].split()[0]
		self.root.ids.sun.text = f"Rise:{self.selected_city.current['SunRise']}\nSet:{self.selected_city.current['SunSet']}\n{self.selected_city.current['DateTime'].split()[1][-6:]}"
		self.root.ids.moon.text = f"Rise:{self.selected_city.current['MoonRise']}\nSet:{self.selected_city.current['MoonSet']}\n{self.selected_city.current['DateTime'].split()[1][-6:]}"
		self.root.ids.forecast_date.text = self.selected_city.forecast['Date']
		self.root.ids.forecast_weather_text.text = self.selected_city.forecast['WeatherText']
		self.root.ids.forecast_min_temp.text = f"{self.selected_city.forecast['MinTemp']} \u00B0C"
		self.root.ids.forecast_max_temp.text = f"{self.selected_city.forecast['MaxTemp']} \u00B0C"
		self.root.ids.forecast_min_real_feel.text = f"{self.selected_city.forecast['MinRealFeel']} \u00B0C"
		self.root.ids.forecast_max_real_feel.text = f"{self.selected_city.forecast['MaxRealFeel']} \u00B0C"
		self.root.ids.forecast_hrs_of_sun.text = self.selected_city.forecast['HrsOfSun']
		self.root.ids.forecast_air_quality.text = self.selected_city.forecast['AirQuality']
		self.root.ids.forecast_uv_index.text = self.selected_city.forecast['UVIndex']
		self.root.ids.day_forecast_date.text = self.selected_city.forecast['Date']
		self.root.ids.day_forecast_icon.source = f"https://developer.accuweather.com/sites/default/files/{self.selected_city.day_forecast['Icon']}-s.png"
		self.root.ids.day_forecast_text.text = self.selected_city.day_forecast['Text']
		self.root.ids.day_forecast_precp_prob.text = f"{self.selected_city.day_forecast['PrecpProb']} %"
		self.root.ids.day_forecast_thunder_prob.text = f"{self.selected_city.day_forecast['ThunderProb']} %"
		self.root.ids.day_forecast_rain_prob.text = f"{self.selected_city.day_forecast['RainProb']} %"
		self.root.ids.day_forecast_snow_prob.text = f"{self.selected_city.day_forecast['SnowProb']} %"
		self.root.ids.day_forecast_ice_prob.text = f"{self.selected_city.day_forecast['IceProb']} %"
		self.root.ids.day_forecast_cloud_cover.text = f"{self.selected_city.day_forecast['CloudCover']} %"
		self.root.ids.day_forecast_wind.text = f"{self.selected_city.day_forecast['Wind']} km/hr"
		self.root.ids.day_forecast_wind_gust.text = f"{self.selected_city.day_forecast['WindGust']} km/hr"
		self.root.ids.night_forecast_date.text = self.selected_city.forecast['Date']
		self.root.ids.night_forecast_icon.source = f"https://developer.accuweather.com/sites/default/files/{self.selected_city.night_forecast['Icon']}-s.png"
		self.root.ids.night_forecast_text.text = self.selected_city.night_forecast['Text']
		self.root.ids.night_forecast_precp_prob.text = f"{self.selected_city.night_forecast['PrecpProb']} %"
		self.root.ids.night_forecast_thunder_prob.text = f"{self.selected_city.night_forecast['ThunderProb']} %"
		self.root.ids.night_forecast_rain_prob.text = f"{self.selected_city.night_forecast['RainProb']} %"
		self.root.ids.night_forecast_snow_prob.text = f"{self.selected_city.night_forecast['SnowProb']} %"
		self.root.ids.night_forecast_ice_prob.text = f"{self.selected_city.night_forecast['IceProb']} %"
		self.root.ids.night_forecast_cloud_cover.text = f"{self.selected_city.night_forecast['CloudCover']} %"
		self.root.ids.night_forecast_wind.text = f"{self.selected_city.night_forecast['Wind']} km/hr"
		self.root.ids.night_forecast_wind_gust.text = f"{self.selected_city.night_forecast['WindGust']} km/hr"




if __name__ == "__main__":
	GetWeather().run()
