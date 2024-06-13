SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `recognizer`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `dosen`
--

CREATE TABLE `dosen` (
  `id` int(11) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `nidn` bigint(12) NOT NULL,
  `waktu` timestamp NOT NULL DEFAULT current_timestamp(),
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `pengunjung`
--

CREATE TABLE `pengunjung` (
  `id_pengunjung` int(11) NOT NULL,
  `nm_lengkap` varchar(50) NOT NULL,
  `nim_nidn` bigint(20) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `pengunjung`
--

INSERT INTO `pengunjung` (`id_pengunjung`, `nm_lengkap`, `nim_nidn`, `status`) VALUES
(1, 'Andi Riyansah', 0609108802, 'dosen'),
(2, 'Bagus Satrio WP', 1027118801,'dosen'),
(3, 'Imam Much Ibnu Subroto', 0613037301, 'dosen'),
(4, 'Ahmad Jalaluddin', 32601700004, 'dosen');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `kedatangan`
--
ALTER TABLE `dosen`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `pengunjung`
--
ALTER TABLE `pengunjung`
  ADD PRIMARY KEY (`id_pengunjung`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `kedatangan`
--
ALTER TABLE `dosen `
  MODIFY `id_dosen` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `pengunjung`
--
ALTER TABLE `pengunjung`
  MODIFY `id_pengunjung` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;