SCHEMA_SQL = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS worker(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    role TEXT NOT NULL CHECK(role IN ('keeper', 'cleaner', 'admin')),
    notes TEXT,
    phone_number TEXT,
    created_at TEXT NOT NULL,
);


CREATE TABLE IF NOT EXISTS exhibit(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    size_sqm REAL,
    condition TEXT,
    location TEXT NOT NULL,
    created_at TEXT NOT NULL,
);

CREATE TABLE IF NOT EXISTS animal(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    sex TEXT NOT NULL CHECK(sex IN ('male', 'female', 'unknown')) DEFAULT 'unknown',
    date_of_birth TEXT,
    intake_date TEXT,
    description TEXT,
    weight_kg REAL,
    height_cm REAL,
    is_healthy INTEGER NOT NULL DEFAULT 1,
    exhibit_id INTEGER NOT NULL,
    FOREIGN KEY (exhibit_id) REFERENCES exhibit(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS animal_image(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    animal_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    caption TEXT,
    created_at TEXT NOT NULL,
    FOREIGN KEY (animal_id) REFERENCES animal(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS keeper_exhibit(
    keeper_id INTEGER NOT NULL,
    exhibit_id INTEGER NOT NULL,
    assigned_since TEXT,
    PRIMARY KEY (keeper_id, exhibit_id),
    FOREIGN KEY (keeper_id) REFERENCES worker(id) ON DELETE CASCADE,
    FOREIGN KEY (exhibit_id) REFERENCES exhibit(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS food_inventory(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    quantity REAL NOT NULL,
    unit TEXT NOT NULL CHECK(unit IN ('kg', 'g', 'l', 'ml', 'pieces')),
    type TEXT,
    notes TEXT,
    vendor TEXT,
    purchase_price_per_unit REAL,
    created_at TEXT NOT NULL,
);
"""