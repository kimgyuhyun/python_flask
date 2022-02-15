from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(
    os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\x1f\x104$\x8dB\x18\xdf=Y\xd7\xbe\xaf\xde\xc1\x8d'
