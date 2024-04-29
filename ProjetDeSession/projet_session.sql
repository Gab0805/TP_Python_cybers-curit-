-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : lun. 29 avr. 2024 à 22:30
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `projet_session`
--

-- --------------------------------------------------------

--
-- Structure de la table `paiement`
--

CREATE TABLE `paiement` (
  `ID` int(3) NOT NULL,
  `nom_complet` varchar(60) NOT NULL,
  `telephone` varchar(16) NOT NULL,
  `email` varchar(40) NOT NULL,
  `carte_credit` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `paiement`
--

INSERT INTO `paiement` (`ID`, `nom_complet`, `telephone`, `email`, `carte_credit`) VALUES
(1, 'doudou', '418-555-7575', 'doudou@music.ca', '1111 1111 1111 1111'),
(2, 'moussa', '819-222-1010', 'moussac@foot.ca', '1212 2323 5555 9898');

-- --------------------------------------------------------

--
-- Structure de la table `reservations`
--

CREATE TABLE `reservations` (
  `ID` int(100) NOT NULL,
  `nom` varchar(60) NOT NULL,
  `place` int(5) NOT NULL,
  `status` varchar(30) NOT NULL,
  `event` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `reservations`
--

INSERT INTO `reservations` (`ID`, `nom`, `place`, `status`, `event`) VALUES
(1, 'anta', 10, 'confirmé', 'festival jazz'),
(2, 'dia', 55, 'en attente', 'cirque soleil');

-- --------------------------------------------------------

--
-- Structure de la table `table_evenements`
--

CREATE TABLE `table_evenements` (
  `ID` int(2) NOT NULL,
  `nom` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `emplacement` varchar(40) NOT NULL,
  `prix` int(50) NOT NULL,
  `images` varchar(50) NOT NULL,
  `description` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `table_evenements`
--

INSERT INTO `table_evenements` (`ID`, `nom`, `date`, `emplacement`, `prix`, `images`, `description`) VALUES
(1, 'festival Jazz', '2024-06-05', 'saint louis', 10, '', 'à découvrir'),
(2, 'fete de la musique', '2024-05-15', 'un peu partout en ville', 0, '', 'c\'est gratuit. faut en profiter');

-- --------------------------------------------------------

--
-- Structure de la table `table_usagers`
--

CREATE TABLE `table_usagers` (
  `ID` int(50) NOT NULL,
  `nom_complet` varchar(70) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(60) NOT NULL,
  `email` varchar(60) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `table_usagers`
--

INSERT INTO `table_usagers` (`ID`, `nom_complet`, `username`, `password`, `email`, `status`) VALUES
(0, 'vincent paul', 'vince', '1234$paul', 'vincent.paul@cybersec.ca', 'client'),
(0, 'adan corban', 'adam', 'ad@n$1425', 'adan@festival.com', 'agent');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `paiement`
--
ALTER TABLE `paiement`
  ADD PRIMARY KEY (`ID`);

--
-- Index pour la table `reservations`
--
ALTER TABLE `reservations`
  ADD PRIMARY KEY (`ID`);

--
-- Index pour la table `table_evenements`
--
ALTER TABLE `table_evenements`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `paiement`
--
ALTER TABLE `paiement`
  MODIFY `ID` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `reservations`
--
ALTER TABLE `reservations`
  MODIFY `ID` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `table_evenements`
--
ALTER TABLE `table_evenements`
  MODIFY `ID` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
