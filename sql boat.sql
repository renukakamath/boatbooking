/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - online_boat_reservation
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`online_boat_reservation` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `online_boat_reservation`;

/*Table structure for table `boat` */

DROP TABLE IF EXISTS `boat`;

CREATE TABLE `boat` (
  `boat_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(100) DEFAULT NULL,
  `subcategory_id` int(100) DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL,
  `image` varchar(1000) DEFAULT NULL,
  `duration` varchar(100) DEFAULT NULL,
  `bstatus` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`boat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `boat` */

insert  into `boat`(`boat_id`,`category_id`,`subcategory_id`,`price`,`image`,`duration`,`bstatus`) values 
(1,1,1,'5001','static/imageed46044d-220b-4572-a6f1-20f3f8e50f2adownload (2).jfif','dhgfj1','1'),
(2,1,1,'2001','static/imaged89c963f-7d28-4577-87ca-e28609e0e65310855406.jpg','1','1');

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `boat_id` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL,
  `hours` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`booking_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `booking` */

insert  into `booking`(`booking_id`,`boat_id`,`customer_id`,`price`,`hours`,`date`,`status`) values 
(1,1,1,'10002','2','2023-02-19','paid'),
(2,1,1,'5001','1','2023-01-29','paid'),
(3,2,1,'4002','2','2023-01-21','paid'),
(4,2,1,'2001','1','2023-01-25','paid'),
(5,1,1,'10002','2','2023-01-20','paid'),
(6,2,1,'4002','2','2023-01-27','paid'),
(7,1,1,'10002','2','2023-03-03','paid'),
(8,1,1,'10002','2','2023-02-23','paid'),
(9,1,1,'10002','2','2023-03-09','paid');

/*Table structure for table `card` */

DROP TABLE IF EXISTS `card`;

CREATE TABLE `card` (
  `card_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `card_no` varchar(100) DEFAULT NULL,
  `card_name` varchar(100) DEFAULT NULL,
  `expiry_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`card_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `card` */

insert  into `card`(`card_id`,`customer_id`,`card_no`,`card_name`,`expiry_date`) values 
(1,1,'1234567890123456','hai','2023-12'),
(2,1,'1234567890234567','wefghju','2023-12'),
(3,1,'1234567890566123','ai','2023-11');

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(100) DEFAULT NULL,
  `cat_decription` varchar(100) DEFAULT NULL,
  `status` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`category_id`,`category_name`,`cat_decription`,`status`) values 
(1,'ucat','asdfgmn,','1');

/*Table structure for table `customer` */

DROP TABLE IF EXISTS `customer`;

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `customer_fname` varchar(100) DEFAULT NULL,
  `customer_lname` varchar(100) DEFAULT NULL,
  `customer_houser_name` varchar(100) DEFAULT NULL,
  `customer_dist` varchar(100) DEFAULT NULL,
  `customer_pincode` varchar(100) DEFAULT NULL,
  `customer_phone` varchar(100) DEFAULT NULL,
  `customer_status` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `customer` */

insert  into `customer`(`customer_id`,`username`,`customer_fname`,`customer_lname`,`customer_houser_name`,`customer_dist`,`customer_pincode`,`customer_phone`,`customer_status`) values 
(1,'user@gmail.com','user1','qwerty1',' house Karanakodam Thammanam','Ernakulam1','682032','2345678907',0);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `username` varchar(100) NOT NULL,
  `password` varchar(100) DEFAULT NULL,
  `user_type` varchar(100) DEFAULT NULL,
  `status` varchar(4) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`username`,`password`,`user_type`,`status`) values 
('user@gmail.com','user','customer','1'),
('admin@gmail.com','admin','admin','1'),
('hai@gmail.com','hai','staff','1');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`booking_id`,`amount`,`date`) values 
(1,5,'5001','2023-01-05'),
(2,6,'2001','2023-02-19'),
(3,7,'5001','2023-02-19'),
(4,7,'5001','2023-02-19'),
(5,8,'5001','2023-02-19'),
(6,8,'5001','2023-02-19'),
(7,9,'5001','2023-02-19');

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `rating_id` int(11) NOT NULL AUTO_INCREMENT,
  `boat_id` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `rated` varchar(100) DEFAULT NULL,
  `review` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`rating_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

insert  into `rating`(`rating_id`,`boat_id`,`customer_id`,`rated`,`review`) values 
(1,1,1,'2','ok');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `staff_fname` varchar(100) DEFAULT NULL,
  `staff_lname` varchar(100) DEFAULT NULL,
  `staff_dob` varchar(100) DEFAULT NULL,
  `staff_house_no` varchar(100) DEFAULT NULL,
  `staff_house_name` varchar(100) DEFAULT NULL,
  `staff_dist` varchar(100) DEFAULT NULL,
  `staff_pincode` varchar(100) DEFAULT NULL,
  `staff_gender` varchar(100) DEFAULT NULL,
  `staff_phone` varchar(100) DEFAULT NULL,
  `staff_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`username`,`staff_fname`,`staff_lname`,`staff_dob`,`staff_house_no`,`staff_house_name`,`staff_dist`,`staff_pincode`,`staff_gender`,`staff_phone`,`staff_status`) values 
(1,'hai@gmail.com','user1','qwerty1','2023-01-15','15671','Thusiprambil1 house Karanakodam Thammanam','fdfsf11','682032','male','0987654321','0');

/*Table structure for table `subcategory` */

DROP TABLE IF EXISTS `subcategory`;

CREATE TABLE `subcategory` (
  `subcategory_id` int(11) NOT NULL AUTO_INCREMENT,
  `subcategory_name` varchar(100) DEFAULT NULL,
  `sub_status` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`subcategory_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `subcategory` */

insert  into `subcategory`(`subcategory_id`,`subcategory_name`,`sub_status`) values 
(1,'sub1','1');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
