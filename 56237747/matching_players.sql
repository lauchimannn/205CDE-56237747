-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2021-04-11 07:05:17
-- 伺服器版本： 10.4.14-MariaDB
-- PHP 版本： 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `matching_players`
--

-- --------------------------------------------------------

--
-- 資料表結構 `contact_us`
--

CREATE TABLE `contact_us` (
  `case_id` int(10) NOT NULL,
  `player_id` int(5) NOT NULL,
  `name` varchar(30) NOT NULL,
  `email` varchar(40) NOT NULL,
  `subject` text NOT NULL,
  `status` enum('waiting','solved','denied') NOT NULL,
  `createdSince` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `contact_us`
--

INSERT INTO `contact_us` (`case_id`, `player_id`, `name`, `email`, `subject`, `status`, `createdSince`) VALUES
(1, 0, 'Lau Chi Man', 'bjenny@gmail.com', 'as', 'waiting', '2021-03-28 13:47:54'),
(2, 0, 'Lau Chi Man', 'bjenny@gmail.com', 'ppo', 'waiting', '2021-03-28 13:49:33'),
(3, 0, 'Lau Chi Man', 'bjenny@gmail.com', 'hi im good', 'waiting', '2021-04-02 14:16:23'),
(4, 0, 'Lau Chi Man', 'bjenny@gmail.com', 'hi', 'waiting', '2021-04-02 14:16:30'),
(5, 0, 'Lau Chi Man', 'bjenny@gmail.com', 'asdjasfafasf', 'waiting', '2021-04-04 15:05:13'),
(6, 0, 'Lau Chi Man', 'bjenny@gmail.com', 'alkjfklajfkldaklfdkfdfdfdf\r\n', 'waiting', '2021-04-04 22:16:09'),
(7, 0, 'aa', 'aa@a', 'abc', 'waiting', '2021-04-06 16:40:57'),
(8, 0, '劉智敏', 'a@a', 'gg', 'waiting', '2021-04-06 16:45:42'),
(9, 0, 's p a c e', 'space@a.a', '   s   spaceeeee       spsps', 'waiting', '2021-04-07 14:56:40'),
(10, 1, 'player one', 'player01@email.com', 'player01', 'waiting', '2021-04-11 03:13:11'),
(11, 1, 'player one', 'player01@email.com', 'player01 again', 'waiting', '2021-04-11 03:21:57'),
(12, 0, 'testing', 'testing@testing.com', 'testing', 'waiting', '2021-04-11 05:22:38'),
(13, 1, 'player one', 'player01@email.com', 'player01 testing here', 'waiting', '2021-04-11 05:44:43');

-- --------------------------------------------------------

--
-- 資料表結構 `game`
--

CREATE TABLE `game` (
  `game_id` int(10) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `game`
--

INSERT INTO `game` (`game_id`, `name`) VALUES
(1, 'Apex'),
(2, 'Barotrauma'),
(3, 'Counter-Strike: Global Offensive'),
(4, 'Dead by Daylight'),
(5, 'Don\'t Starve Together'),
(6, 'Overwatch'),
(7, 'PLAYERUNKNOWN\'S BATTLEGROUNDS'),
(8, 'Raft'),
(9, 'Terraria'),
(10, 'Tom Clancy\'s Rainbow Six® Siege');

-- --------------------------------------------------------

--
-- 資料表結構 `player`
--

CREATE TABLE `player` (
  `player_id` int(5) NOT NULL,
  `room_id` int(10) NOT NULL,
  `name` varchar(30) NOT NULL,
  `username` varchar(20) NOT NULL,
  `pw` varchar(20) NOT NULL,
  `language` enum('Arabic','Bengali','Chinese','Cantonese','English','Hindi','Japanese','Portuguese','Russian','Spanish') NOT NULL,
  `gender` enum('F','M','other','secret') NOT NULL,
  `email` varchar(40) NOT NULL,
  `status` enum('verifying','verified') NOT NULL,
  `createdSince` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `player`
--

INSERT INTO `player` (`player_id`, `room_id`, `name`, `username`, `pw`, `language`, `gender`, `email`, `status`, `createdSince`) VALUES
(1, 1, 'player one', 'player01', 'player01', 'Cantonese', 'F', 'player01@email.com', 'verified', '2021-03-25 01:19:48'),
(2, 0, 'verify email', 'verifyemail', 'verifyemail', 'Japanese', 'M', 'verifyemail@email.com', 'verifying', '2021-04-06 15:55:15'),
(3, 0, 'player three', 'player03', 'player03', 'Arabic', 'M', 'user@a', 'verified', '2021-04-09 13:28:35'),
(4, 4, 'player four', 'player04', 'player04', 'Chinese', 'other', 'player02@a.a', 'verified', '2021-04-09 14:10:04'),
(5, 3, 'player five', 'player05', 'player05', 'Russian', 'secret', 'player03@a', 'verified', '2021-04-09 22:14:12'),
(6, 1, 'player six', 'player06', 'player06', 'Arabic', 'other', 'ihavenoroom@a', 'verified', '2021-04-09 22:40:59'),
(7, 1, 'player seven', 'player07', 'player07', 'Chinese', 'other', 'testing@a', 'verified', '2021-04-09 22:48:06'),
(8, 0, 'player eight', 'player08', 'player08', 'Spanish', 'F', 'testing2@a', 'verifying', '2021-04-09 22:48:58'),
(9, 0, 'testing one', 'testing1', 'testing1', 'Cantonese', 'other', 'testing1@testing.com', 'verifying', '2021-04-11 05:38:16');

-- --------------------------------------------------------

--
-- 資料表結構 `room`
--

CREATE TABLE `room` (
  `room_id` int(10) NOT NULL,
  `host_username` varchar(20) NOT NULL,
  `title` varchar(30) NOT NULL,
  `game` enum('Apex','Barotrauma','Counter-Strike: Global Offensive','Dead by Daylight','Dont Starve Together','Overwatch','PLAYERUNKNOWNS BATTLEGROUNDS','Raft','Terraria','Tom Clancys Rainbow Six Siege') NOT NULL,
  `language` enum('Arabic','Bengali','Chinese','Cantonese','English','Hindi','Japanese','Portuguese','Russian','Spanish') NOT NULL,
  `joinedPlayer` int(3) NOT NULL,
  `maxPlayer` int(3) NOT NULL,
  `createdSince` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `room`
--

INSERT INTO `room` (`room_id`, `host_username`, `title`, `game`, `language`, `joinedPlayer`, `maxPlayer`, `createdSince`) VALUES
(1, 'player01', 'testing here', 'Barotrauma', 'Cantonese', 3, 3, '2021-04-11 06:13:49'),
(3, 'player05', 'iam new', 'Terraria', 'Cantonese', 1, 3, '2021-04-11 01:25:37'),
(4, 'player04', 'hi guys', 'Tom Clancys Rainbow Six Siege', 'Arabic', 1, 10, '2021-04-09 23:14:45');

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `contact_us`
--
ALTER TABLE `contact_us`
  ADD PRIMARY KEY (`case_id`);

--
-- 資料表索引 `game`
--
ALTER TABLE `game`
  ADD PRIMARY KEY (`game_id`);

--
-- 資料表索引 `player`
--
ALTER TABLE `player`
  ADD PRIMARY KEY (`player_id`);

--
-- 資料表索引 `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`room_id`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `contact_us`
--
ALTER TABLE `contact_us`
  MODIFY `case_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `game`
--
ALTER TABLE `game`
  MODIFY `game_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `player`
--
ALTER TABLE `player`
  MODIFY `player_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `room`
--
ALTER TABLE `room`
  MODIFY `room_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
