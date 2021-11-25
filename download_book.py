import requests

image_url = ''
for i in range(2, 638):

    img_data = requests.get(
        'https://www.profil-klett.hr/datoteke/ucenje-na-daljinu/matematika_ok/files/large/{}.jpg?1585942736'.format(i)).content
    with open('knjiga/{}.jpg'.format(i), 'wb') as handler:
        handler.write(img_data)
