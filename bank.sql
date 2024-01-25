-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 03, 2023 at 06:26 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bank`
--

-- --------------------------------------------------------

--
-- Table structure for table `account_opening`
--

CREATE TABLE `account_opening` (
  `Account Number` varchar(15) NOT NULL,
  `New Password` varbinary(15) NOT NULL,
  `Full Name` varchar(20) NOT NULL,
  `Address` varchar(20) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `Mobile` bigint(12) NOT NULL,
  `Email` varchar(25) NOT NULL,
  `Country` varchar(10) NOT NULL,
  `State` varchar(20) NOT NULL,
  `City` varchar(15) NOT NULL,
  `Zipcode` int(10) NOT NULL,
  `Balance` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `account_summary`
--

CREATE TABLE `account_summary` (
  `Account Number` varchar(15) NOT NULL,
  `Transaction` varchar(10) NOT NULL,
  `Date` date NOT NULL,
  `Action` varchar(15) NOT NULL,
  `Balance` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `credit`
--

CREATE TABLE `credit` (
  `Account Number` varchar(15) NOT NULL,
  `Pin` varchar(10) NOT NULL,
  `Withdraw Amount` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `deposite`
--

CREATE TABLE `deposite` (
  `Account Number` varchar(15) NOT NULL,
  `Pin` varchar(10) NOT NULL,
  `Depositing Amount` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `document_verification`
--

CREATE TABLE `document_verification` (
  `Hight School Roll` int(10) NOT NULL,
  `Hight School Marks` int(3) NOT NULL,
  `Hight School Percent` int(5) NOT NULL,
  `Secondary School Roll` int(10) NOT NULL,
  `Secondary School Marks` int(3) NOT NULL,
  `Secondary School Percent` int(5) NOT NULL,
  `Aadhar Number` varchar(15) NOT NULL,
  `Pan Number` int(10) NOT NULL,
  `Father Aadhar Number` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `nominee_details`
--

CREATE TABLE `nominee_details` (
  `Name` varchar(20) NOT NULL,
  `Age` varchar(3) NOT NULL,
  `Account Number` varchar(15) NOT NULL,
  `IFSC Code` varchar(15) NOT NULL,
  `Branch` varchar(20) NOT NULL,
  `Area` varchar(10) NOT NULL,
  `Relation` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `transfer`
--

CREATE TABLE `transfer` (
  `Account Number` varchar(15) NOT NULL,
  `Pin` varchar(10) NOT NULL,
  `Transfer Amount` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account_opening`
--
ALTER TABLE `account_opening`
  ADD PRIMARY KEY (`Account Number`);

--
-- Indexes for table `account_summary`
--
ALTER TABLE `account_summary`
  ADD PRIMARY KEY (`Account Number`);

--
-- Indexes for table `document_verification`
--
ALTER TABLE `document_verification`
  ADD PRIMARY KEY (`Aadhar Number`);

--
-- Indexes for table `nominee_details`
--
ALTER TABLE `nominee_details`
  ADD PRIMARY KEY (`Account Number`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
