from sqlalchemy import Column, Integer, String
from .. import db

class LoginUser(db.Model):
    __tablename__ = "LoginUser"
    id = Column(Integer, primary_key=True)
    _username = Column(String, nullable=False)
    _password = Column(String, nullable=False)
    _state = Column(String, nullable = False)

    def __init__(self, username, password, state):
        self._username = username
        self._password = password
        self._state = state
    
    def __repr__(self):
        return "id= '%s', username='%s', password='%s', state= '%s'" % (self.id, self.username, self.password, self.state)
    @property    
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        self._password = value
    
    @property
    def state(self):
        return self._state 
    
    @state.setter
    def state(self, value):
        self._state = value

    def to_dict(self):
        return {"id": self.id, "username": self.username, "password": self.password, "state": self.state}
    
def initLoginUser():
    db.session.commit()