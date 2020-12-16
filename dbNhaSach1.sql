-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: dbnhasach1
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bill`
--

DROP TABLE IF EXISTS `bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bill` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created_date` datetime DEFAULT NULL,
  `total` float DEFAULT NULL,
  `customer_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `bill_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill`
--

LOCK TABLES `bill` WRITE;
/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bill_detail`
--

DROP TABLE IF EXISTS `bill_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bill_detail` (
  `bill_id` int NOT NULL,
  `book_id` int NOT NULL,
  `quantity` int DEFAULT NULL,
  `price` float DEFAULT NULL,
  PRIMARY KEY (`bill_id`,`book_id`),
  KEY `book_id` (`book_id`),
  CONSTRAINT `bill_detail_ibfk_1` FOREIGN KEY (`bill_id`) REFERENCES `bill` (`id`),
  CONSTRAINT `bill_detail_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `book` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill_detail`
--

LOCK TABLES `bill_detail` WRITE;
/*!40000 ALTER TABLE `bill_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `bill_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `description` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `price` float DEFAULT NULL,
  `image` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `typeofBook_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `author` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `publishingYear` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES (1,'Doraemon','Truyện hoạt hình, hài hước',20000,'images/doraemon.png','Truyện Tranh','Fujiko Fujio',1969),(2,'Goblin','Ngôn tình Hàn Quốc',100000,'images/goblin.png','Truyện Ngôn Tình','Kim Eun-sook',2016),(3,'Hoa học trò','Tạp chí thiếu niên',15000,'images/hoahoctro.png','Tạp chí','Báo Sinh Viên Việt Nam',1991),(4,'Báo bóng đá','Tin tức thể thao đa dạng',5000,'images/baosoccer.png','Báo','Liên đoàn Bóng Đá Việt Nam',2007),(5,'Sách giáo khoa Lớp 12','Đa dạng các môn học của khối 12',192000,'images/SGK12.png','Sách Giáo Khoa','Nhà xuất bản Giáo Dục Việt Nam',2020),(6,'Conan','Truyện trinh thám',50000,'images/conan.png','Truyện Tranh','Aoyama Gosho',1994),(7,'Tuổi trẻ đáng giá bao nhiêu','Chia sẻ những kỹ năng, tâm sự bình dị mang đến những tư tưởng tích cực đến các bạn trẻ trước khi bước vào đời của Rosie Nguyễn',75000,'images/tuoitre.png','Sách kỹ năng, tản văn','Rosie Nguyễn',2016);
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coupon`
--

DROP TABLE IF EXISTS `coupon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coupon` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created_date` datetime DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `coupon_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coupon`
--

LOCK TABLES `coupon` WRITE;
/*!40000 ALTER TABLE `coupon` DISABLE KEYS */;
/*!40000 ALTER TABLE `coupon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coupon_detail`
--

DROP TABLE IF EXISTS `coupon_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coupon_detail` (
  `coupon_id` int NOT NULL,
  `book_id` int NOT NULL,
  `quantity` int DEFAULT NULL,
  PRIMARY KEY (`coupon_id`,`book_id`),
  KEY `book_id` (`book_id`),
  CONSTRAINT `coupon_detail_ibfk_1` FOREIGN KEY (`coupon_id`) REFERENCES `coupon` (`id`),
  CONSTRAINT `coupon_detail_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `book` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coupon_detail`
--

LOCK TABLES `coupon_detail` WRITE;
/*!40000 ALTER TABLE `coupon_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `coupon_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `username` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `gender` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `avatar` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `phone` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `user_role` enum('USER','ADMIN') COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  CONSTRAINT `customer_chk_1` CHECK ((`active` in (0,1)))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Nguyễn Bảo Long','1851050083long@ou.edu.vn','user1','e10adc3949ba59abbe56e057f20f883e','male','images/upload/anh4.png','0937752035',1,'USER');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dept_detail_report`
--

DROP TABLE IF EXISTS `dept_detail_report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dept_detail_report` (
  `dept_id` int NOT NULL,
  `customer_id` int NOT NULL,
  `money_before` float DEFAULT NULL,
  `money_after` float DEFAULT NULL,
  `arises` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`dept_id`,`customer_id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `dept_detail_report_ibfk_1` FOREIGN KEY (`dept_id`) REFERENCES `dept_report` (`id`),
  CONSTRAINT `dept_detail_report_ibfk_2` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dept_detail_report`
--

LOCK TABLES `dept_detail_report` WRITE;
/*!40000 ALTER TABLE `dept_detail_report` DISABLE KEYS */;
/*!40000 ALTER TABLE `dept_detail_report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dept_report`
--

DROP TABLE IF EXISTS `dept_report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dept_report` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dept_report`
--

LOCK TABLES `dept_report` WRITE;
/*!40000 ALTER TABLE `dept_report` DISABLE KEYS */;
/*!40000 ALTER TABLE `dept_report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory_detail_report`
--

DROP TABLE IF EXISTS `inventory_detail_report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory_detail_report` (
  `inventory_id` int NOT NULL,
  `book_id` int NOT NULL,
  `quantity_before` int DEFAULT NULL,
  `quantity_after` int DEFAULT NULL,
  `arises` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`inventory_id`,`book_id`),
  KEY `book_id` (`book_id`),
  CONSTRAINT `inventory_detail_report_ibfk_1` FOREIGN KEY (`inventory_id`) REFERENCES `inventory_report` (`id`),
  CONSTRAINT `inventory_detail_report_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `book` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory_detail_report`
--

LOCK TABLES `inventory_detail_report` WRITE;
/*!40000 ALTER TABLE `inventory_detail_report` DISABLE KEYS */;
/*!40000 ALTER TABLE `inventory_detail_report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory_report`
--

DROP TABLE IF EXISTS `inventory_report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory_report` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory_report`
--

LOCK TABLES `inventory_report` WRITE;
/*!40000 ALTER TABLE `inventory_report` DISABLE KEYS */;
/*!40000 ALTER TABLE `inventory_report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `receipt`
--

DROP TABLE IF EXISTS `receipt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `receipt` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created_date` datetime DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `receipt_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receipt`
--

LOCK TABLES `receipt` WRITE;
/*!40000 ALTER TABLE `receipt` DISABLE KEYS */;
INSERT INTO `receipt` VALUES (1,'2020-12-16 13:15:28',1);
/*!40000 ALTER TABLE `receipt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `receipt_detail`
--

DROP TABLE IF EXISTS `receipt_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `receipt_detail` (
  `receipt_id` int NOT NULL,
  `book_id` int NOT NULL,
  `quantity` int DEFAULT NULL,
  `price` float DEFAULT NULL,
  PRIMARY KEY (`receipt_id`,`book_id`),
  KEY `book_id` (`book_id`),
  CONSTRAINT `receipt_detail_ibfk_1` FOREIGN KEY (`receipt_id`) REFERENCES `receipt` (`id`),
  CONSTRAINT `receipt_detail_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `book` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receipt_detail`
--

LOCK TABLES `receipt_detail` WRITE;
/*!40000 ALTER TABLE `receipt_detail` DISABLE KEYS */;
INSERT INTO `receipt_detail` VALUES (1,1,1,20000),(1,2,1,100000),(1,3,1,15000),(1,4,1,5000),(1,5,1,192000),(1,6,1,50000),(1,7,1,75000);
/*!40000 ALTER TABLE `receipt_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `username` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `gender` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `avatar` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `user_role` enum('USER','ADMIN') COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  CONSTRAINT `user_chk_1` CHECK ((`active` in (0,1)))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Nguyễn Bảo Long','1851050083long@ou.edu.vn','user1','e10adc3949ba59abbe56e057f20f883e','male','images/upload/anh4.png',1,'USER'),(2,'Quản Trị Viên','admin@ou.edu.vn','admin','e10adc3949ba59abbe56e057f20f883e','male',NULL,NULL,'ADMIN');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-16 13:42:53
