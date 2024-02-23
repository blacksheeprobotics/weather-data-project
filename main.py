# with open("weather_data.csv", mode="r") as data:
#     weather_data = data.readlines()
#
# print(weather_data)

# import csv
import pandas

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] == "temp":
#             # temperatures.append("temp")
#             pass
#         else:
#             temperatures.append(int(row[1]))
#
# print(temperatures)

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

data_dict = data.to_dict()
temperature_list = data["temp"].to_list()
total_temp = sum(temperature_list)
temperature_list_length = len(temperature_list)
average_temp = total_temp / temperature_list_length

average_via_pandas = data["temp"].mean()
max_temperature = data["temp"].max()

print(data["temp"].to_list())
print(f"The average temperature is: {average_temp}")
print(f"The average temperature (via pandas) is {average_via_pandas}")
print(f"The maximum temperature is: {max_temperature}")
print(data.condition)
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday)
monday_fahrenheit = (monday.temp[0] * 9/5.0) + 32
print(monday_fahrenheit)

#create dataframe
data2_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data2 = pandas.DataFrame(data2_dict)
print(data2)

data2.to_csv("new_data.csv")
