from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    type_of_user = db.Column(db.String(30), nullable=False)
    # is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "type_of_user": self.type_of_user
            # do not serialize the password, its a security breach
        }
    
    @classmethod
    def create(cls, name, email, password, type_of_user):
        instance = cls(
            name=name,
            email=email,
            password=password,
            type_of_user=type_of_user
        )
        if isinstance(instance, cls):
            return instance
        else:
            return None
    
    @classmethod
    def login(cls, email, password):
        user = cls.query.filter_by(
            email=email
        ).one_or_none()
        if (not isinstance(user, cls)):
            return user
        if user.password == password:
            return user
        else:
            return False

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(30))
    local_name = db.Column(db.String(50))
    type_of_event = db.Column(db.String(50))
    description = db.Column(db.String(120))
    place = db.Column(db.String(30))
    date = db.Column(db.String(30))
    schedule = db.Column(db.String(30))
    age = db.Column(db.String(10))
    parking = db.Column(db.String(10))
    number = db.Column(db.String(30))
    capacity = db.Column(db.String(30))
    photo = db.Column(db.String(30))
    location = db.Column(db.String(30))
    cover = db.Column(db.String(30))

    def serialize(self):
            return {
                "id": self.id,
                "event_name": self.event_name,
                "local_name": self.local_name,
                "type_of_event": self.type_of_event,
                "description":self.description,
                "place":self.place,
                "date":self.date,
                "schedule":self.schedule,
                "age":self.age,
                "parking":self.parking,
                "number":self.number,
                "capacity":self.capacity,
                "photo":self.photo,
                "location":self.location,
                "cover":self.cover
            }

    @classmethod
    def create_event(cls, event_name, local_name, type_of_event, description, place, date, schedule, age, parking, number, capacity, photo, location, cover):
        event = cls(
            event_name=event_name,
            local_name=local_name,
            type_of_event=type_of_event,
            description=description,
            place=place,
            date=date,
            schedule=schedule,
            age=age,
            parking=parking,
            number=number,
            capacity=capacity,
            photo=photo,
            location=location,
            cover=cover
        )
        if isinstance(event, cls):
            return event
        else:
            return None

