import json

personal_data = {}
with open('./config.json', 'r') as f:
    personal_data = json.load(f)

coefs = [   len(personal_data['name']),
            len(personal_data['surname']),
            len(personal_data['patronymic'])]
