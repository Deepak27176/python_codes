# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     lis = []
#     flag =0
#     for row in data:
#         print(row)
#         if flag > 0:
#             lis.append(int(row[1]))
#         flag += 1
#     print(lis)
import pandas
data = pandas.read_csv("weather_data.csv")
# temp_dict = data.to_dict()  # to convert data_frame to dictionary
# print(temp_dict)
# temp_list = data["temp"].to_list()  # to convert series to list
# print(sum(temp_list)/len(temp_list))
# print(data["temp"].max())
# To print row
# #print(data[data.day == "Monday"])
# create your data_frame data in dictionary
new_dict = {
    "students": ["shyam", "singh", "Roy"],
    "scores": [67, 78, 63]
}
data_frame = pandas.DataFrame(new_dict)
print(data_frame)
# convert data frame to csv file
data_frame.to_csv("new_data.csv")
