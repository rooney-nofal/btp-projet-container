-- Initialize InfraMusicStore database (schema + sample data)

CREATE DATABASE IF NOT EXISTS infra_music_store;
USE infra_music_store;

-- Artists
CREATE TABLE IF NOT EXISTS artists (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(120) NOT NULL
);

-- Albums
CREATE TABLE IF NOT EXISTS albums (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(160) NOT NULL,
    artist_id INT NOT NULL,
    CONSTRAINT fk_albums_artists
        FOREIGN KEY (artist_id)
        REFERENCES artists(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Genres
CREATE TABLE IF NOT EXISTS genres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(120) NOT NULL
);

-- Tracks
CREATE TABLE IF NOT EXISTS tracks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    album_id INT NOT NULL,
    genre_id INT NOT NULL,
    composer VARCHAR(220),
    milliseconds INT NOT NULL,
    bytes INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    CONSTRAINT fk_tracks_albums
        FOREIGN KEY (album_id)
        REFERENCES albums(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_tracks_genres
        FOREIGN KEY (genre_id)
        REFERENCES genres(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

-- Sample data (20+ rows across 4 tables)

INSERT INTO artists (name) VALUES
('Lunar Echo'),
('Digital Sunset'),
('Neon Horizon'),
('Analog Dreams'),
('Infra Beats');

INSERT INTO genres (name) VALUES
('Rock'),
('Pop'),
('Jazz'),
('Electronic'),
('Classical'),
('Hip-Hop');

INSERT INTO albums (title, artist_id) VALUES
('Midnight City Lights', 1),
('Golden Hour Reflections', 2),
('Skyline Stories', 3),
('Tape Machine Memories', 4),
('Infra Sessions Vol. 1', 5),
('Infra Sessions Vol. 2', 5);

INSERT INTO tracks
(name, album_id, genre_id, composer, milliseconds, bytes, unit_price)
VALUES
('Neon Streets', 1, 4, 'Lunar Echo', 210000, 4000000, 0.99),
('Night Drive', 1, 4, 'Lunar Echo', 195000, 3800000, 0.99),
('Sunset Radio', 2, 2, 'Digital Sunset', 180000, 3600000, 0.99),
('Burning Skies', 2, 1, 'Digital Sunset', 205000, 3950000, 0.99),
('Skyline Prelude', 3, 3, 'Neon Horizon', 175000, 3500000, 0.99),
('City Birds', 3, 3, 'Neon Horizon', 220000, 4200000, 0.99),
('Lo-Fi Station', 4, 4, 'Analog Dreams', 200000, 3900000, 0.99),
('Cassette Love', 4, 2, 'Analog Dreams', 230000, 4300000, 0.99),
('Infra Intro', 5, 4, 'Infra Beats', 120000, 2500000, 0.99),
('Bassline Circuit', 5, 4, 'Infra Beats', 210000, 4100000, 0.99),
('Hi-Hat Galaxy', 5, 4, 'Infra Beats', 190000, 3700000, 0.99),
('Analog Soul', 4, 3, 'Analog Dreams', 240000, 4400000, 1.29),
('Morning Skyline', 2, 2, 'Digital Sunset', 185000, 3600000, 0.99),
('Classical Echo', 3, 5, 'Neon Horizon', 260000, 4800000, 1.49),
('Jazz Corner', 3, 3, 'Neon Horizon', 230000, 4500000, 1.29),
('Street Poetry', 6, 6, 'Infra Beats', 200000, 3900000, 0.99),
('Metro Lines', 6, 4, 'Infra Beats', 210000, 3950000, 0.99),
('Digital Moon', 1, 4, 'Lunar Echo', 215000, 4050000, 0.99),
('Golden Tape', 4, 2, 'Analog Dreams', 225000, 4200000, 0.99),
('Final Horizon', 1, 1, 'Lunar Echo', 250000, 4600000, 1.29);
