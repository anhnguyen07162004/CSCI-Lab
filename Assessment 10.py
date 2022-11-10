# Anh Nguyen
# CSCI 102 - Section B
# Assessment 10
# References: https://www.youtube.com/watch?v=q5uM4VKywbA
# Time: 2 hours

import csv
info_line = ["Depth", "Start Depth", "End Depth", "Difference in Depth", "Formation", "Age of Formation"]
age = ""

with open("formations.csv", "r") as formations:
  formations_reader = csv.reader(formations, delimiter = ",")
  
  next(formations_reader)

  with open("formations_parsed.csv", "w") as parse:
    parse_writer = csv.writer(parse, delimiter = ",")

    parse_writer.writerow(info_line)

    for row in formations_reader:
      depth_range = row[0]
      depth_range_list = depth_range.split("-")
      start_depth = float(depth_range_list[0])
      end_depth = float(depth_range_list[1])
      depth_diff = round((end_depth - start_depth), 2)
      form = row[1]

      if start_depth < 700:
        age = "Paleocene"
      else:
        age = "Cretaceous"
      
      parse_writer.writerow([depth_range] + [start_depth] + [end_depth] + [f'{depth_diff:.2f}'] + [form] + [age])
      
# with open("formations_parsed.csv", "r") as test:
#   contents = test.read()
#   print(contents)
