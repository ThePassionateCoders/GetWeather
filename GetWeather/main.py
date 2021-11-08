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
data = [

	{
		'Version': 1, 
		'Key': '202396', 
		'Type': 'City', 
		'Rank': 11, 
		'LocalizedName': 'Delhi', 
		'Country': {'ID': 'IN', 'LocalizedName': 'India'}, 
		'AdministrativeArea': {'ID': 'DL', 'LocalizedName': 'Delhi'}
	},

	{
		'Version': 1, 
		'Key': '65329', 
		'Type': 'City', 
		'Rank': 45, 
		'LocalizedName': 'Delhi', 
		'Country': {'ID': 'CN', 'LocalizedName': 'China'}, 
		'AdministrativeArea': {'ID': 'QH', 'LocalizedName': 'Qinghai'}
	},

	{
		'Version': 1, 
		'Key': '893482', 
		'Type': 'City', 
		'Rank': 45, 
		'LocalizedName': 'Delhi Cantonment', 
		'Country': {'ID': 'IN', 'LocalizedName': 'India'}, 
		'AdministrativeArea': {'ID': 'DL', 'LocalizedName': 'Delhi'}
	},

	{
		'Version': 1, 
		'Key': '2155308', 
		'Type': 'City', 
		'Rank': 65, 
		'LocalizedName': 'Delhi', 
		'Country': {'ID': 'US', 'LocalizedName': 'United States'}, 
		'AdministrativeArea': {'ID': 'CA', 'LocalizedName': 'California'}
	}, 

	{
		'Version': 1, 
		'Key': '1122380', 
		'Type': 'City', 
		'Rank': 75, 
		'LocalizedName': 'Delhi Settlement', 
		'Country': {'ID': 'TT', 'LocalizedName': 'Trinidad and Tobago'}, 
		'AdministrativeArea': {'ID': 'SIP', 'LocalizedName': 'Siparia'}
	},

	{
		'Version': 1, 
		'Key': '2190984', 
		'Type': 'City', 
		'Rank': 75, 
		'LocalizedName': 'Delhi Hills', 
		'Country': {'ID': 'US', 'LocalizedName': 'United States'}, 
		'AdministrativeArea': {'ID': 'OH', 'LocalizedName': 'Ohio'}
	}, 

	{
		'Version': 1, 
		'Key': '2204223', 
		'Type': 'City', 
		'Rank': 85, 
		'LocalizedName': 'Delhi', 
		'Country': {'ID': 'US', 'LocalizedName': 'United States'}, 
		'AdministrativeArea': {'ID': 'IA', 'LocalizedName': 'Iowa'}
	},

	{
		'Version': 1, 
		'Key': '333472', 
		'Type': 'City', 
		'Rank': 85, 
		'LocalizedName': 'Delhi', 
		'Country': {'ID': 'US', 'LocalizedName': 'United States'}, 
		'AdministrativeArea': {'ID': 'LA', 'LocalizedName': 'Louisiana'}
	}, 

	{
		'Version': 1, 
		'Key': '2247464', 
		'Type': 'City', 
		'Rank': 85, 
		'LocalizedName': 'Delhi', 
		'Country': {'ID': 'US', 'LocalizedName': 'United States'}, 
		'AdministrativeArea': {'ID': 'MN', 'LocalizedName': 'Minnesota'}
	}, 

	{
		'Version': 1, 
		'Key': '334629', 
		'Type': 'City', 
		'Rank': 85, 
		'LocalizedName': 'Delhi', 
		'Country': {'ID': 'US', 'LocalizedName': 'United States'}, 
		'AdministrativeArea': {'ID': 'NY', 'LocalizedName': 'New York'}
	}

]

current = ["""
  {
    "LocalObservationDateTime": "2021-11-06T20:00:00+05:30",
    "EpochTime": 1636209000,
    "WeatherText": "Hazy clouds",
    "WeatherIcon": 37,
    "HasPrecipitation": false,
    "PrecipitationType": null,
    "IsDayTime": false,
    "Temperature": {
      "Metric": {
        "Value": 19.7,
        "Unit": "C",
        "UnitType": 17
      },
      "Imperial": {
        "Value": 67,
        "Unit": "F",
        "UnitType": 18
      }
    },
    "RealFeelTemperature": {
      "Metric": {
        "Value": 17.7,
        "Unit": "C",
        "UnitType": 17
      },
      "Imperial": {
        "Value": 64,
        "Unit": "F",
        "UnitType": 18
      }
    },
    "RealFeelTemperatureShade": {
      "Metric": {
        "Value": 17.7,
        "Unit": "C",
        "UnitType": 17
      },
      "Imperial": {
        "Value": 64,
        "Unit": "F",
        "UnitType": 18
      }
    },
    "RelativeHumidity": 54,
    "IndoorRelativeHumidity": 53,
    "DewPoint": {
      "Metric": {
        "Value": 10.2,
        "Unit": "C",
        "UnitType": 17
      },
      "Imperial": {
        "Value": 50,
        "Unit": "F",
        "UnitType": 18
      }
    },
    "Wind": {
      "Direction": {
        "Degrees": 293,
        "Localized": "WNW",
        "English": "WNW"
      },
      "Speed": {
        "Metric": {
          "Value": 10.9,
          "Unit": "km/h",
          "UnitType": 7
        },
        "Imperial": {
          "Value": 6.8,
          "Unit": "mi/h",
          "UnitType": 9
        }
      }
    },
    "WindGust": {
      "Speed": {
        "Metric": {
          "Value": 22,
          "Unit": "km/h",
          "UnitType": 7
        },
        "Imperial": {
          "Value": 13.7,
          "Unit": "mi/h",
          "UnitType": 9
        }
      }
    },
    "UVIndex": 0,
    "UVIndexText": "Low",
    "Visibility": {
      "Metric": {
        "Value": 2.8,
        "Unit": "km",
        "UnitType": 6
      },
      "Imperial": {
        "Value": 2,
        "Unit": "mi",
        "UnitType": 2
      }
    },
    "ObstructionsToVisibility": "",
    "CloudCover": 75,
    "Ceiling": {
      "Metric": {
        "Value": 12192,
        "Unit": "m",
        "UnitType": 5
      },
      "Imperial": {
        "Value": 40000,
        "Unit": "ft",
        "UnitType": 0
      }
    },
    "Pressure": {
      "Metric": {
        "Value": 1011,
        "Unit": "mb",
        "UnitType": 14
      },
      "Imperial": {
        "Value": 29.85,
        "Unit": "inHg",
        "UnitType": 12
      }
    },
    "PressureTendency": {
      "LocalizedText": "Steady",
      "Code": "S"
    },
    "Past24HourTemperatureDeparture": {
      "Metric": {
        "Value": -1.6,
        "Unit": "C",
        "UnitType": 17
      },
      "Imperial": {
        "Value": -3,
        "Unit": "F",
        "UnitType": 18
      }
    },
    "ApparentTemperature": {
      "Metric": {
        "Value": 19.4,
        "Unit": "C",
        "UnitType": 17
      },
      "Imperial": {
        "Value": 67,
        "Unit": "F",
        "UnitType": 18
      }
    },
    "WindChillTemperature": {
      "Metric": {
        "Value": 19.4,
        "Unit": "C",
        "UnitType": 17
      },
      "Imperial": {
        "Value": 67,
        "Unit": "F",
        "UnitType": 18
      }
    },
    "WetBulbTemperature": {
      "Metric": {
        "Value": 14.1,
        "Unit": "C",
        "UnitType": 17
      },
      "Imperial": {
        "Value": 57,
        "Unit": "F",
        "UnitType": 18
      }
    },
    "Precip1hr": {
      "Metric": {
        "Value": 0,
        "Unit": "mm",
        "UnitType": 3
      },
      "Imperial": {
        "Value": 0,
        "Unit": "in",
        "UnitType": 1
      }
    },
    "PrecipitationSummary": {
      "Precipitation": {
        "Metric": {
          "Value": 0,
          "Unit": "mm",
          "UnitType": 3
        },
        "Imperial": {
          "Value": 0,
          "Unit": "in",
          "UnitType": 1
        }
      },
      "PastHour": {
        "Metric": {
          "Value": 0,
          "Unit": "mm",
          "UnitType": 3
        },
        "Imperial": {
          "Value": 0,
          "Unit": "in",
          "UnitType": 1
        }
      },
      "Past3Hours": {
        "Metric": {
          "Value": 0,
          "Unit": "mm",
          "UnitType": 3
        },
        "Imperial": {
          "Value": 0,
          "Unit": "in",
          "UnitType": 1
        }
      },
      "Past6Hours": {
        "Metric": {
          "Value": 0,
          "Unit": "mm",
          "UnitType": 3
        },
        "Imperial": {
          "Value": 0,
          "Unit": "in",
          "UnitType": 1
        }
      },
      "Past9Hours": {
        "Metric": {
          "Value": 0,
          "Unit": "mm",
          "UnitType": 3
        },
        "Imperial": {
          "Value": 0,
          "Unit": "in",
          "UnitType": 1
        }
      },
      "Past12Hours": {
        "Metric": {
          "Value": 0,
          "Unit": "mm",
          "UnitType": 3
        },
        "Imperial": {
          "Value": 0,
          "Unit": "in",
          "UnitType": 1
        }
      },
      "Past18Hours": {
        "Metric": {
          "Value": 0,
          "Unit": "mm",
          "UnitType": 3
        },
        "Imperial": {
          "Value": 0,
          "Unit": "in",
          "UnitType": 1
        }
      },
      "Past24Hours": {
        "Metric": {
          "Value": 0,
          "Unit": "mm",
          "UnitType": 3
        },
        "Imperial": {
          "Value": 0,
          "Unit": "in",
          "UnitType": 1
        }
      }
    },
    "TemperatureSummary": {
      "Past6HourRange": {
        "Minimum": {
          "Metric": {
            "Value": 19.7,
            "Unit": "C",
            "UnitType": 17
          },
          "Imperial": {
            "Value": 67,
            "Unit": "F",
            "UnitType": 18
          }
        },
        "Maximum": {
          "Metric": {
            "Value": 26.8,
            "Unit": "C",
            "UnitType": 17
          },
          "Imperial": {
            "Value": 80,
            "Unit": "F",
            "UnitType": 18
          }
        }
      },
      "Past12HourRange": {
        "Minimum": {
          "Metric": {
            "Value": 16.4,
            "Unit": "C",
            "UnitType": 17
          },
          "Imperial": {
            "Value": 61,
            "Unit": "F",
            "UnitType": 18
          }
        },
        "Maximum": {
          "Metric": {
            "Value": 26.8,
            "Unit": "C",
            "UnitType": 17
          },
          "Imperial": {
            "Value": 80,
            "Unit": "F",
            "UnitType": 18
          }
        }
      },
      "Past24HourRange": {
        "Minimum": {
          "Metric": {
            "Value": 13.1,
            "Unit": "C",
            "UnitType": 17
          },
          "Imperial": {
            "Value": 56,
            "Unit": "F",
            "UnitType": 18
          }
        },
        "Maximum": {
          "Metric": {
            "Value": 26.8,
            "Unit": "C",
            "UnitType": 17
          },
          "Imperial": {
            "Value": 80,
            "Unit": "F",
            "UnitType": 18
          }
        }
      }
    },
    "MobileLink": "http://www.accuweather.com/en/in/delhi/202396/current-weather/202396?lang=en-us",
    "Link": "http://www.accuweather.com/en/in/delhi/202396/current-weather/202396?lang=en-us"
  }
"""]
 
class DefaultCity():

  text = ""
  secondary_text = ""
  tertiary_text = ""
  current = {
    "WeatherText": "",
    "WeatherIcon": "",
    "DateTime": "",
    "Temperature": "",
    "RealFeelTemperature": "",
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

class ConfirmCity(ThreeLineAvatarIconListItem):
	divider = None
	check = ObjectProperty(None)

class GetWeather(MDApp):
	api_key = "wIbO7AmIwOQLzaXAq5XY73kxXsjHhaVO"
	dialog = None
	searched_cities = []
	selected_city = DefaultCity()
	current_data =  current



	def build(self):
		return Builder.load_file("design.kv")

	def call_api(self, api):
		try:
			toast("SEARCHING...")
			# data = requests.get(api)
			# if data.status_code != 200:
				# raise ValueError
			return data #data.json()
		except:
			toast("Error!!!")

	def searched(self, searched_text):
		
		if len(searched_text) == 0:
			toast("Enter something first")
				
		else:
			self.searched_cities = self.call_api(f"http://dataservice.accuweather.com/locations/v1/cities/autocomplete?apikey={self.api_key}&q={searched_text}")

			list_cities = []
			for i in range(len(self.searched_cities)):
				list_cities.append(
					ConfirmCity(
						text = self.searched_cities[i]["LocalizedName"],
						secondary_text = self.searched_cities[i]["Country"]["LocalizedName"],
						tertiary_text = self.searched_cities[i]["Key"],
						)
					)

			list_cities[0].check.active = True
			self.selected_city = list_cities[0]

			if not self.dialog:
				self.dialog = MDDialog(
					title = "Select Your City",
					type = "confirmation",
					items = list_cities,
					auto_dismiss = False,
					size_hint = (.9, .5),
					buttons = [
						MDFlatButton(text = "Cancel", on_release = self.close_dialog), 
						MDFlatButton(text = "Ok", on_release = self.update_main_screen_data),
						],
					)
				self.dialog.open()

	def close_dialog(self, *args):
		self.dialog.dismiss()
		self.dialog = None
		if len(args)!=0:
			if args[0].text == "Cancel":
				self.selected_city = None

	def select_city(self, instance_check, city):
		self.selected_city = city
		instance_check.active = True
		check_list = instance_check.get_widgets(instance_check.group)

		for check in check_list:
			if check != instance_check:
				check.active = False

	def update_main_screen_data(self, *args):
		app_ids = self.root.ids
		if self.dialog:
			self.close_dialog()
		app_ids.city_info.text = self.selected_city.text+", "+self.selected_city.secondary_text




if __name__ == "__main__":
	GetWeather().run()
