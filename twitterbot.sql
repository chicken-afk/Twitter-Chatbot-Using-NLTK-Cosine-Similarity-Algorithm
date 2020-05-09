-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 09, 2020 at 08:47 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `twitter_bot`
--

-- --------------------------------------------------------

--
-- Table structure for table `data_set`
--

CREATE TABLE `data_set` (
  `id_data_set` int(11) NOT NULL,
  `questions` text NOT NULL,
  `answers` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `data_set`
--

INSERT INTO `data_set` (`id_data_set`, `questions`, `answers`) VALUES
(1, 'apa saja syarat buat akta kelahiran', 'Syarat pencatatan kelahiran :\r\n\r\nSurat keterangan lahir dari dokter/bidan/penolong kelahiran\r\nFotokopi Akta Nikah/Kutipan Akta Perkawinan orangtua (dilegalisir)\r\nFotokopi KK dan KTP-el orangtua\r\nFotokopi KTP-el 2 (dua) orang saksi\r\nPencatatan kelahiran tidak dipungut biaya\r\nSurat kuasa di atas materai cukup bagi yang dikuasakan, dilampiri fotokopi KTP-el penerima kuasa\r\nUntuk orang asing, ditambah :\r\nFotokopi Surat Keterangan Tempat Tinggal (SKTT) orangtua bagi pemegang Izin Tinggal Terbatas (ITAS)\r\nFotokopi paspor (dilegalisir)'),
(2, 'apa saja syarat buat akta kawin nikah', '1. Syarat umum:\r\n\r\nSurat keterangan telah terjadinya perkawinan dari pemuka agama/pendeta atau surat perkawinan penghayat kepercayaan yang ditandatangani oleh pemuka penghayat kepercayaan\r\nFormulir Pencatatan Perkawinan\r\nFotokopi Kutipan Akta Kelahiran suami dan istri (dilegalisir)\r\nFotokopi KK dan KTP-el suami dan istri\r\nPas foto berdampingan suami dan istri 4 x 6 sebanyak 4 (empat) lembar\r\nFotokopi KTP-el 2 (dua) orang saksi\r\nUntuk orang asing, ditambah :\r\n\r\nFotokopi Surat Keterangan Tempat Tinggal (SKTT) suami atau istri pemegang Izin Tinggal Terbatas (ITAS)\r\nFotokopi paspor suami atau istri (dilegalisir)\r\nSurat Keterangan/izin dari perwakilan negara yang bersangkutan bagi suami atau istri\r\nBagi perkawinan antar orang asing membawa kelengkapan dari kedutaan besar yang bersangkutan\r\n2. Syarat khusus:\r\n\r\nKutipan Akta Perceraian bagi yang telah bercerai\r\nFotokopi Kutipan Akta Kematian bagi yang pernah kawin, yang salah satu pihak telah meninggal dunia\r\nKutipan Akta Kelahiran anak yang akan disahkan dalam perkawinan (apabila sudah mempunyai anak)\r\nBagi anggota TNI atau POLRI harus melampirkan izin dari komandan\r\nPencatatan perkawinan tidak dipungut biaya, selama belum melewati batas waktu pelaporan (60 hari)\r\nPencatatan perkawinan yang melampaui 60 hari sejak tanggal perkawinan dikenakan sanksi administrasi keterlambatan sebesar Rp. 000,-\r\nSurat kuasa di atas materai cukup bagi yang dikuasakan, dilampiri fotokopi KTP-el penerima kuasa'),
(3, 'apa saja syarat buat akta cerai', 'Syarat Pencatatan Perceraian:\r\n\r\nKutipan Akta Perkawinan yang bersangkutan\r\nSalinan Putusan Pengadilan Negeri mengenai perceraian, yang telah memperoleh kekuatan hukum tetap\r\nFormulir Pencatatan Perceraian\r\nFotokopi KK dan KTP-el yang bersangkutan\r\nSurat kuasa di atas materai cukup bagi yang dikuasakan, dilampiri fotokopi KTP-el penerima kuasa\r\nPencatatan perceraian GRATIS, selama belum melampaui batas waktu pelaporan (60 hari)\r\nPencatatan perceraian yang melampaui batas waktu 60 hari sejak putusan pengadilan memperoleh kekuatan hukum tetap, dikenakan administrasi keterlambatan sebesar Rp. 000,-\r\nUntuk orang asing, ditambah :\r\nFotokopi Surat Keterangan Tempat Tinggal (SKTT) suami atau istri pemegang Izin Tinggal Terbatas (ITAS)\r\nFotokopi paspor suami atau istri (dilegalisir)'),
(4, 'apa saja membuat Persyaratan Akta Kematian', 'Syarat Pencatatan Kematian:\r\n\r\nSurat keterangan kematian dari dokter/paramedis\r\nSurat Keterangan Kematian dari Desa\r\nKK dan KTP-el yang meninggal atau ahli waris\r\nFotokopi kutipan akta kelahiran yang meninggal (jika ada)\r\nFotokopi KTP-el 2 (dua) orang saksi\r\nSurat kuasa di atas materai cukup bagi yang dikuasakan, dilampiri fotokopi KTP-el penerima kuasa\r\nPencatatan kematian tidak dipungut biaya, selama belum melewati batas waktu pelaporan (30 hari)\r\nPencatatan kematian yang melampaui 30 hari sejak tanggal kematian dikenakan sanksi administrasi keterlambatan sebesar Rp. 000,-\r\nUntuk orang asing, ditambah:\r\nFotokopi Surat Keterangan Tempat Tinggal (SKTT) bagi pemegang Izin Tinggal Terbatas (ITAS)\r\nFotokopi paspor (dilegalisir)'),
(5, 'Jadwal Jam Pelayanan Dinas Kependudukan dan Pencatatan Sipil Kabupaten Sleman', 'Senin – Kamis\r\n08.00 s.d 15.00 WIB\r\n\r\nJum’at\r\n08.00 s.d 14.00 WIB');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `data_set`
--
ALTER TABLE `data_set`
  ADD PRIMARY KEY (`id_data_set`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `data_set`
--
ALTER TABLE `data_set`
  MODIFY `id_data_set` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
