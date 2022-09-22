postgresql = {
    'host': 'localhost',
    'user': 'postgres',
    'password': '',
    'db': 'harmonic'
}

postgresql_test = {
    'host': 'localhost:5431',
    'user': 'cours',
    'password': 'db',
    'db': 'demo_harmonic'
}

postgresql_string = "postgresql://{}:{}@{}/{}".format(postgresql['user'], postgresql['password'], postgresql['host'], postgresql['db'])
postgresql_string_test = "postgresql://{}:{}@{}/{}".format(postgresql_test['user'], postgresql_test['password'], postgresql_test['host'], postgresql_test['db'])
