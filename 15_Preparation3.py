"""
Question : Create a program that gives weather advice based on:

· Temperature:
  · Below 0°C: "Extreme cold warning"
  · 0-10°C: "Cold weather"
  · 11-25°C: "Pleasant weather"
  · Above 25°C: "Warm weather"
· Rain: If raining, add " - Bring umbrella"
· Wind: If wind speed > 30 km/h, add " - Windy conditions"

"""

weather = float(input("Enter Temprature of weather e.g 5 : "))

if weather < 0 :
    print("Extreme cold warning");
elif 0 <= weather <= 10 :
    print("Cold weather")
elif 11 <= weather <= 25 :
    print("Pleasant weather");
else :
    print("warm weather");

rain = input("Is it raining ? if raning type Yes and if not type No : ").strip().capitalize();
if rain == "Yes" :
    print("Bring umbrella")
else :
    print("don't bring umberlla")

wind = int(input("Enter Wind speed in km/h e.g 5 : "));
if wind > 30 :
    print("Windy Conditions")
else :
    print("Not Windy Condition it's normal !")