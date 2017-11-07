import csv
import random
from faker import Faker

fake = Faker()

with open('some.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for _ in range(200):
        writer.writerow([str(random.randrange(0.0,20.0,1)) + random.choice(['.99', '.89'])])
        # writer.writerow([fake.street_name()])


# fake.street_name()
# fake.country()
# fake.city()

# Artist
# SongTitle
# 'AlbumTitle': 'TestyTestersTestyTests',
#                 'Genre' : 'Classical',
#                 'Price' : str(random.randrange(0.0,20.0,1)) + random.choice(['.99', '.89']),
#                 'CriticRating' :