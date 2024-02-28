from faker import Faker


faker = Faker(locale='pt_BR')
faker2 = Faker(locale='es_AR')

Faker.seed(0)

print(faker.name())
print(faker.name())
print(faker.name())
print(faker.name())

print(faker.email())
print(faker.password())
print(faker.address())
print(faker.credit_card_number())
print(faker.phone_number())
print(faker.company())
print(faker.date())
print(faker.cpf())


print(faker2.last_name())
print(faker2.email())
print(faker2.password())
print(faker2.url())
print(faker2.license_plate())
