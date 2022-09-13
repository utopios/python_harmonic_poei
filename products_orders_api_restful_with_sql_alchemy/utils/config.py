postgresql = {
    'host': 'localhost',
    'user': 'cours',
    'password': 'db',
    'db': 'harmonic'
}

postgresql_string = "postgresql://{}:{}@{}/{}".format(postgresql['user'], postgresql['password'], postgresql['host'], postgresql['db'])
