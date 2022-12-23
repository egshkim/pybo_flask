from config.default import *
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xda\xf1\x03\xbem\x9a\x99\x9e\xaf\xb5,\xd7:\xee\xbd\xf7'
