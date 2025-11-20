from flask import request, jsonify, abort
from database import db
from models import Artist, Album, Genre, Track


def _get_or_404(model, object_id: int):
    obj = model.query.get(object_id)
    if obj is None:
        abort(404, description=f"{model.__name__} with id {object_id} not found")
    return obj


def register_routes(app):
    # ---- Artists ----
    @app.route("/api/artists", methods=["GET"])
    def list_artists():
        artists = Artist.query.order_by(Artist.id).all()
        return jsonify([a.to_dict() for a in artists])

    @app.route("/api/artists/<int:artist_id>", methods=["GET"])
    def get_artist(artist_id: int):
        artist = _get_or_404(Artist, artist_id)
        return jsonify(artist.to_dict())

    @app.route("/api/artists", methods=["POST"])
    def create_artist():
        data = request.get_json(silent=True) or {}
        name = data.get("name")
        if not name:
            abort(400, description="Field 'name' is required")

        artist = Artist(name=name)
        db.session.add(artist)
        db.session.commit()
        return jsonify(artist.to_dict()), 201

    @app.route("/api/artists/<int:artist_id>", methods=["PUT"])
    def update_artist(artist_id: int):
        artist = _get_or_404(Artist, artist_id)
        data = request.get_json(silent=True) or {}
        name = data.get("name")
        if not name:
            abort(400, description="Field 'name' is required")

        artist.name = name
        db.session.commit()
        return jsonify(artist.to_dict())

    @app.route("/api/artists/<int:artist_id>", methods=["DELETE"])
    def delete_artist(artist_id: int):
        artist = _get_or_404(Artist, artist_id)
        db.session.delete(artist)
        db.session.commit()
        return "", 204

    # ---- Albums ----
    @app.route("/api/albums", methods=["GET"])
    def list_albums():
        albums = Album.query.order_by(Album.id).all()
        return jsonify([a.to_dict() for a in albums])

    @app.route("/api/albums/<int:album_id>", methods=["GET"])
    def get_album(album_id: int):
        album = _get_or_404(Album, album_id)
        return jsonify(album.to_dict())

    @app.route("/api/albums", methods=["POST"])
    def create_album():
        data = request.get_json(silent=True) or {}
        title = data.get("title")
        artist_id = data.get("artist_id")

        if not title or artist_id is None:
            abort(400, description="Fields 'title' and 'artist_id' are required")

        # ensure artist exists
        _get_or_404(Artist, artist_id)

        album = Album(title=title, artist_id=artist_id)
        db.session.add(album)
        db.session.commit()
        return jsonify(album.to_dict()), 201

    @app.route("/api/albums/<int:album_id>", methods=["PUT"])
    def update_album(album_id: int):
        album = _get_or_404(Album, album_id)
        data = request.get_json(silent=True) or {}
        title = data.get("title")
        artist_id = data.get("artist_id")

        if not title or artist_id is None:
            abort(400, description="Fields 'title' and 'artist_id' are required")

        _get_or_404(Artist, artist_id)

        album.title = title
        album.artist_id = artist_id
        db.session.commit()
        return jsonify(album.to_dict())

    @app.route("/api/albums/<int:album_id>", methods=["DELETE"])
    def delete_album(album_id: int):
        album = _get_or_404(Album, album_id)
        db.session.delete(album)
        db.session.commit()
        return "", 204

    # ---- Genres ----
    @app.route("/api/genres", methods=["GET"])
    def list_genres():
        genres = Genre.query.order_by(Genre.id).all()
        return jsonify([g.to_dict() for g in genres])

    @app.route("/api/genres/<int:genre_id>", methods=["GET"])
    def get_genre(genre_id: int):
        genre = _get_or_404(Genre, genre_id)
        return jsonify(genre.to_dict())

    @app.route("/api/genres", methods=["POST"])
    def create_genre():
        data = request.get_json(silent=True) or {}
        name = data.get("name")
        if not name:
            abort(400, description="Field 'name' is required")

        genre = Genre(name=name)
        db.session.add(genre)
        db.session.commit()
        return jsonify(genre.to_dict()), 201

    @app.route("/api/genres/<int:genre_id>", methods=["PUT"])
    def update_genre(genre_id: int):
        genre = _get_or_404(Genre, genre_id)
        data = request.get_json(silent=True) or {}
        name = data.get("name")
        if not name:
            abort(400, description="Field 'name' is required")

        genre.name = name
        db.session.commit()
        return jsonify(genre.to_dict())

    @app.route("/api/genres/<int:genre_id>", methods=["DELETE"])
    def delete_genre(genre_id: int):
        genre = _get_or_404(Genre, genre_id)
        db.session.delete(genre)
        db.session.commit()
        return "", 204

    # ---- Tracks ----
    @app.route("/api/tracks", methods=["GET"])
    def list_tracks():
        tracks = Track.query.order_by(Track.id).all()
        return jsonify([t.to_dict() for t in tracks])

    @app.route("/api/tracks/<int:track_id>", methods=["GET"])
    def get_track(track_id: int):
        track = _get_or_404(Track, track_id)
        return jsonify(track.to_dict())

    @app.route("/api/tracks", methods=["POST"])
    def create_track():
        data = request.get_json(silent=True) or {}

        required_fields = ["name", "album_id", "genre_id",
                           "milliseconds", "bytes", "unit_price"]
        missing = [f for f in required_fields if f not in data]
        if missing:
            abort(400, description=f"Missing fields: {', '.join(missing)}")

        # ensure referenced records exist
        _get_or_404(Album, data["album_id"])
        _get_or_404(Genre, data["genre_id"])

        track = Track(
            name=data["name"],
            album_id=data["album_id"],
            genre_id=data["genre_id"],
            composer=data.get("composer"),
            milliseconds=data["milliseconds"],
            bytes=data["bytes"],
            unit_price=data["unit_price"],
        )
        db.session.add(track)
        db.session.commit()
        return jsonify(track.to_dict()), 201

    @app.route("/api/tracks/<int:track_id>", methods=["PUT"])
    def update_track(track_id: int):
        track = _get_or_404(Track, track_id)
        data = request.get_json(silent=True) or {}

        required_fields = ["name", "album_id", "genre_id",
                           "milliseconds", "bytes", "unit_price"]
        missing = [f for f in required_fields if f not in data]
        if missing:
            abort(400, description=f"Missing fields: {', '.join(missing)}")

        _get_or_404(Album, data["album_id"])
        _get_or_404(Genre, data["genre_id"])

        track.name = data["name"]
        track.album_id = data["album_id"]
        track.genre_id = data["genre_id"]
        track.composer = data.get("composer")
        track.milliseconds = data["milliseconds"]
        track.bytes = data["bytes"]
        track.unit_price = data["unit_price"]

        db.session.commit()
        return jsonify(track.to_dict())

    @app.route("/api/tracks/<int:track_id>", methods=["DELETE"])
    def delete_track(track_id: int):
        track = _get_or_404(Track, track_id)
        db.session.delete(track)
        db.session.commit()
        return "", 204
