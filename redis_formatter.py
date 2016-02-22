from walrus import *
import csv

database = Database()
ac = database.autocomplete()

with open('countries.csv', 'rb') as csvfile:
    country_reader = csv.reader(csvfile, delimiter=',')
    ctr = 0
    for row in country_reader:
        if ctr > 0:
            country = row[0]
            city = row[1]
            props = []
            for x in row[2:]:
                if x == "None":
                    props.append(None)
                else:
                    props.append(float(x))
            ac.store(obj_id=ctr, title=city, data={'country': country, 'city': city, 'props': props})
        ctr += 1

# ac.store(
#     obj_id = 1,
#     title = "emre",
#     data = {
#         'image': "SAKSO",
#         'title': "KOKARCA",
#         'intval': 5.5
#     }
#     )

# ac.store(
#     obj_id = 2,
#     title = "emre",
#     data = {
#         'image': "DKsodks",
#         'title': "POKMPA",
#     }
#     )


#print list(ac.search("emre"))