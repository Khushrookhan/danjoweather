from django.shortcuts import render

def home(request):
	import json
	import requests

	if request.method == "POST":
		zipcode = request.POST['zipcode']
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=A29E2683-AFA1-4C01-92A6-A2269D777CD3")
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..." 

		if api[0]['Category']['Name'] =="Good":
	 		Category_description = "(0-50) Air quality is considered satisfactory, and air pollution poses little or n risk."
	 		Category_color = "good"
	 	elif if api[0]['Category']['Name'] =="Moderate":
	 		Category_description = "(50-100) Air quality is acceptable ;however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
	 		Category_color = "Moderate"
	 	elif if api[0]['Category']['Name'] =="Unhealthy for sensitive groups":
	 		Category_description = "(100-150) Although general public is not going to be affected at this AQI range ,people with lung disease,older adults and cildren are at high risk from the presence of particles in the air."
	 		Category_color = "Unhealthy for sensitive groups"
	 	elif if api[0]['Category']['Name'] =="Unhealthy":
	 		Category_description = "(150-200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
	 		Category_color = "Unhealthy"
	 	elif if api[0]['Category']['Name'] =="Very unhealthy":
	 		Category_description = "(200-300) Health alert: everyone may experience serious health effects".
	 		Category_color = "Very unhealthy"
	 	elif if api[0]['Category']['Name'] =="Hazardous":
	 		Category_description = "(301-500)Health warning of emergency conditions."
	 		Category_color = "Hazardous" 	
	 	{ endif }		
			
		return render (request, 'home.html', {
			'api': api,
			'Category_description': Category_description,
			'Category_color' = Category_color
			})
		
	else:

        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=A29E2683-AFA1-4C01-92A6-A2269D777CD3")
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..." 

		if api[0]['Category']['Name'] =="Good":
	 		Category_description = "(0-50) Air quality is considered satisfactory, and air pollution poses little or n risk."
	 		Category_color = "good"
	 	elif if api[0]['Category']['Name'] =="Moderate":
	 		Category_description = "(50-100) Air quality is acceptable ;however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
	 		Category_color = "Moderate"
	 	elif if api[0]['Category']['Name'] =="Unhealthy for sensitive groups":
	 		Category_description = "(100-150) Although general public is not going to be affected at this AQI range ,people with lung disease,older adults and cildren are at high risk from the presence of particles in the air."
	 		Category_color = "Unhealthy for sensitive groups"
	 	elif if api[0]['Category']['Name'] =="Unhealthy":
	 		Category_description = "(150-200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
	 		Category_color = "Unhealthy"
	 	elif if api[0]['Category']['Name'] =="Very unhealthy":
	 		Category_description = "(200-300) Health alert: everyone may experience serious health effects".
	 		Category_color = "Very unhealthy"
	 	elif if api[0]['Category']['Name'] =="Hazardous":
	 		Category_description = "(301-500)Health warning of emergency conditions."
	 		Category_color = "Hazardous" 	
	 	{ endif }		
			
		return render (request, 'home.html', {
			'api': api,
			'Category_description': Category_description,
			'Category_color' = Category_color
			})

def about(request):
	return render (request, 'about.html', {})	



