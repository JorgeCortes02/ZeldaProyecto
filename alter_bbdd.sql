
USE ZeldaBBDD;


ALTER TABLE game
modify COLUMN game_id int UNSIGNED AUTO_INCREMENT,
add primary key(game_id),
MODIFY COLUMN user_name VARCHAR(50) NOT NULL,
MODIFY COLUMN hearts_remaining INT NOT NULL,
MODIFY COLUMN blood_moon_countdown INT NOT NULL,
MODIFY COLUMN blood_moon_appearances INT NOT NULL,
MODIFY COLUMN region VARCHAR(20) not null,
ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
ADD COLUMN created_by VARCHAR(50),
ADD COLUMN updated_by VARCHAR(50);



ALTER TABLE game_food
modify game_id int unsigned not null,
modify food_name varchar(15) not null,
modify quanntity_remaining int not null,
ADD FOREIGN KEY fk_game_food_game_id (game_id) REFERENCES game(game_id) ON UPDATE CASCADE ON DELETE CASCADE,
ADD PRIMARY KEY (game_id, food_name),
ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
ADD COLUMN created_by VARCHAR(50),
ADD COLUMN updated_by VARCHAR(50);



ALTER TABLE game_weapons
modify game_id int unsigned not null,
modify equiped BOOLEAN DEFAULT FALSE,
modify weapon_name varchar(15) not null,
modify lives_remaining int not null,
ADD FOREIGN KEY fk_game_weapons_game_id (game_id) REFERENCES game(game_id) ON UPDATE CASCADE ON DELETE CASCADE,
ADD PRIMARY KEY (game_id, weapon_name),
ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
ADD COLUMN created_by VARCHAR(50),
ADD COLUMN updated_by VARCHAR(50);
;

Alter table game_enemies

modify game_id int unsigned not null,
ADD FOREIGN KEY fk_game_enemies_game_id (game_id) REFERENCES game(game_id) ON UPDATE CASCADE ON DELETE CASCADE,
modify region varchar(20) not null,
modify num int not null,
modify xpos int not null,
modify ypos int not null,
modify lives_remaining int not null,
ADD PRIMARY KEY(game_id , region, num),
ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
ADD COLUMN created_by VARCHAR(50),
ADD COLUMN updated_by VARCHAR(50);
;


Alter table game_sactuaries_opened

modify game_id int unsigned not null,
ADD FOREIGN KEY fk_game_sactuaries_game_id (game_id) REFERENCES game(game_id) ON UPDATE CASCADE ON DELETE CASCADE,
modify region varchar(20) not null,
modify num int not null,
modify ypos int not null,
modify xpos int not null,
ADD PRIMARY KEY(game_id , region, num),
ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
ADD COLUMN created_by VARCHAR(50),
ADD COLUMN updated_by VARCHAR(50);
;

Alter table game_chests_opened

modify game_id int unsigned not null,
ADD FOREIGN KEY fk_game_chests_game_id (game_id) REFERENCES game(game_id) ON UPDATE CASCADE ON DELETE CASCADE,
modify region varchar(20) not null,
modify num int not null,
add PRIMARY KEY(game_id , region, num),
modify xpos int not null,
modify ypos int not null,
modify lives_remaining int not null,
ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
ADD COLUMN created_by VARCHAR(50),
ADD COLUMN updated_by VARCHAR(50);


