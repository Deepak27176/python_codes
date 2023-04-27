import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_color = data[data["Primary Fur Color"] == "Gray"]
gray_count = len(gray_color)
black_count = len(data[data["Primary Fur Color"] == "Black"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

new_dict = {
    "colour": ['Gray', 'Black', 'Red'],
    "count": [gray_count, black_count, red_count]


}
new_data_frame = pandas.DataFrame(new_dict)
print(new_data_frame)
# new_data_frame.to_csv("colour_count.csv")
