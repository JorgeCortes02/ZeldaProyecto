CREATE DATABASE ZeldaBBDD CHARACTER SET utf8mb4;
USE ZeldaBBDD;


Create table game(
game_id int unsigned auto_increment primary key, 
user_name varchar(50) not null,
date_started date not null,
hearts_remaining int not null ,
blood_moon_countdown int not null,
blood_moon_appearances int not null,
region varchar(20)

);

Create table game_food(

game_id int unsigned not null,
FOREIGN KEY GAMEID(game_id)  REFERENCES game(game_id) 
ON UPDATE CASCADE
ON DELETE CASCADE,
food_name varchar(15) not null,
PRIMARY KEY(game_id , food_name),
quanntity_remaining int not null

);

Create table game_weapons(

game_id int unsigned not null,
FOREIGN KEY GAMEID(game_id)  REFERENCES game(game_id) 
ON UPDATE CASCADE
ON DELETE CASCADE,
weapon_name varchar(15) not null,
PRIMARY KEY(game_id , weapon_name),
equiped boolean default false,
lives_remaining int not null

);

Create table game_enemies(

game_id int unsigned not null,
FOREIGN KEY GAMEID(game_id)  REFERENCES game(game_id) 
ON UPDATE CASCADE
ON DELETE CASCADE,
region varchar(20) not null,
num int not null,
PRIMARY KEY(game_id , region, num),
xpos int not null,
ypos int not null,
lives_remaining int not null

);

Create table game_sactuaries_opened(

game_id int unsigned not null,
FOREIGN KEY GAMEID(game_id)  REFERENCES game(game_id) 
ON UPDATE CASCADE
ON DELETE CASCADE,
region varchar(20) not null,
num int not null,
PRIMARY KEY(game_id , region, num),
xpos int not null,
ypos int not null,
lives_remaining int not null

);

Create table game_chests_opened(

game_id int unsigned not null,
FOREIGN KEY GAMEID(game_id)  REFERENCES game(game_id) 
ON UPDATE CASCADE
ON DELETE CASCADE,
region varchar(20) not null,
num int not null,
PRIMARY KEY(game_id , region, num),
xpos int not null,
ypos int not null,
lives_remaining int not null

);




