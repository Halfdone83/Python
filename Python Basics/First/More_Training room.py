w = float(input()) * 100
h = float(input()) * 100

path = 100

work_station_h = 70
work_station_w = 120

working_stations_h = (h - path) // work_station_h
working_stations_w = w // work_station_w


total_work_stations = working_stations_h * working_stations_w - 3

print(total_work_stations)
