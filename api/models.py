from database import db



class Artist(db.Model):
    __tablename__ = "artists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    albums = db.relationship(
        "Album",
        back_populates="artist",
        cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }


class Album(db.Model):
    __tablename__ = "albums"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(160), nullable=False)
    artist_id = db.Column(
        db.Integer,
        db.ForeignKey("artists.id"),
        nullable=False
    )

    artist = db.relationship("Artist", back_populates="albums")
    tracks = db.relationship(
        "Track",
        back_populates="album",
        cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "artist_id": self.artist_id,
        }


class Genre(db.Model):
    __tablename__ = "genres"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    tracks = db.relationship("Track", back_populates="genre")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }


class Track(db.Model):
    __tablename__ = "tracks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)

    album_id = db.Column(
        db.Integer,
        db.ForeignKey("albums.id"),
        nullable=False
    )
    genre_id = db.Column(
        db.Integer,
        db.ForeignKey("genres.id"),
        nullable=False
    )

    composer = db.Column(db.String(220), nullable=True)
    milliseconds = db.Column(db.Integer, nullable=False)
    bytes = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Numeric(10, 2), nullable=False)

    album = db.relationship("Album", back_populates="tracks")
    genre = db.relationship("Genre", back_populates="tracks")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "album_id": self.album_id,
            "genre_id": self.genre_id,
            "composer": self.composer,
            "milliseconds": self.milliseconds,
            "bytes": self.bytes,
            "unit_price": float(self.unit_price),
        }
