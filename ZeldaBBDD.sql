
CREATE DATABASE ZeldaBBDD CHARACTER SET utf8mb4;
USE ZeldaBBDD;


Create table game(
game_id int, 
user_name varchar(50) ,
date_started date ,
hearts_remaining int,
blood_moon_countdown int,
blood_moon_appearances int,
region varchar(20)

);

Create table game_food(

game_id int,
food_name varchar(15),
quanntity_remaining int

);


Create table game_weapons(

game_id int,
weapon_name varchar(15),
equiped boolean,
lives_remaining int 

);

Create table game_enemies(

game_id int,
region varchar(20),
num int,
xpos int,
ypos int,
lives_remaining int

);

Create table game_sactuaries_opened(

game_id int,
region varchar(20),
num int,
xpos int,
ypos int,
lives_remaining int

);

Create table game_chests_opened(

game_id int,
region varchar(20),
num int,
xpos int,
ypos int,
lives_remaining int 

);


