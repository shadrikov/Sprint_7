from faker import Faker

fake = Faker('ru_RU')

def courier_login_generator():
    generated_login = fake.user_name()
    return generated_login

def courier_passw_generator():
    generated_password = fake.password(special_chars=False)
    return generated_password

def courier_name_generator():
    generated_name = fake.first_name()
    return generated_name

def order_data_generator(color):
    generated_order_data = {
        'firstName': fake.first_name(),
        'lastName': fake.last_name(),
        'address': fake.address(),
        'metroStation': fake.random_int(max=20),
        'phone': fake.phone_number(),
        'rentTime': fake.random_int(max=20),
        'deliveryDate': '2026-12-12',
        'comment': fake.text(max_nb_chars=20),
        'color': color
    }
    return generated_order_data