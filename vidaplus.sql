CREATE DATABASE  IF NOT EXISTS `vidaplus` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `vidaplus`;
-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: vidaplus
-- ------------------------------------------------------
-- Server version	8.0.43

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
-- Table structure for table `alergias`
--

DROP TABLE IF EXISTS `alergias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alergias` (
  `idPaciente` int NOT NULL,
  `penicilina` tinyint(1) DEFAULT NULL,
  `amoxicilina` tinyint(1) DEFAULT NULL,
  `ibuprofeno` tinyint(1) DEFAULT NULL,
  `dipirona` tinyint(1) DEFAULT NULL,
  `extra1` varchar(20) DEFAULT NULL,
  `extra2` varchar(20) DEFAULT NULL,
  `extra3` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`idPaciente`),
  CONSTRAINT `alergias_ibfk_1` FOREIGN KEY (`idPaciente`) REFERENCES `paciente` (`pacienteId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alergias`
--

LOCK TABLES `alergias` WRITE;
/*!40000 ALTER TABLE `alergias` DISABLE KEYS */;
INSERT INTO `alergias` VALUES (1,NULL,1,NULL,NULL,'Amendoim','Corinthians',NULL),(3,0,0,0,0,'Camarão','',''),(4,0,0,0,0,'','',''),(7,0,0,0,0,'','','');
/*!40000 ALTER TABLE `alergias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `condicoes`
--

DROP TABLE IF EXISTS `condicoes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `condicoes` (
  `idPaciente` int NOT NULL,
  `pressaoAlta` tinyint(1) DEFAULT NULL,
  `diabetes` tinyint(1) DEFAULT NULL,
  `asma` tinyint(1) DEFAULT NULL,
  `eplepsia` tinyint(1) DEFAULT NULL,
  `HIV` tinyint(1) DEFAULT NULL,
  `gastrite` tinyint(1) DEFAULT NULL,
  `extra1` varchar(20) DEFAULT NULL,
  `extra2` varchar(20) DEFAULT NULL,
  `extra3` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`idPaciente`),
  CONSTRAINT `condicoes_ibfk_1` FOREIGN KEY (`idPaciente`) REFERENCES `paciente` (`pacienteId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `condicoes`
--

LOCK TABLES `condicoes` WRITE;
/*!40000 ALTER TABLE `condicoes` DISABLE KEYS */;
INSERT INTO `condicoes` VALUES (1,1,NULL,NULL,NULL,NULL,1,NULL,NULL,NULL),(3,0,1,0,NULL,0,0,'','',''),(4,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(7,0,0,0,NULL,0,0,'','','');
/*!40000 ALTER TABLE `condicoes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `consulta`
--

DROP TABLE IF EXISTS `consulta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `consulta` (
  `consultaId` int NOT NULL AUTO_INCREMENT,
  `pacienteId` int NOT NULL,
  `profissionalId` int NOT NULL,
  `motivo` varchar(50) DEFAULT NULL,
  `dataConsulta` datetime DEFAULT NULL,
  `observacoes` varchar(100) DEFAULT NULL,
  `chave` int DEFAULT NULL,
  `diagnostico` varchar(100) DEFAULT NULL,
  `idLocal` int DEFAULT NULL,
  `statusConsulta` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`consultaId`),
  KEY `pacienteId` (`pacienteId`),
  KEY `profissionalId` (`profissionalId`),
  KEY `fk_consulta_local` (`idLocal`),
  CONSTRAINT `consulta_ibfk_1` FOREIGN KEY (`pacienteId`) REFERENCES `paciente` (`pacienteId`),
  CONSTRAINT `consulta_ibfk_2` FOREIGN KEY (`profissionalId`) REFERENCES `profissional` (`profissionalId`),
  CONSTRAINT `fk_consulta_local` FOREIGN KEY (`idLocal`) REFERENCES `locais` (`localId`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consulta`
--

LOCK TABLES `consulta` WRITE;
/*!40000 ALTER TABLE `consulta` DISABLE KEYS */;
INSERT INTO `consulta` VALUES (10,1,1,NULL,'2025-11-04 13:30:00',NULL,597231,'Teste de diagnostico consulta 10, Joao',NULL,'Finalizada'),(11,3,1,'Dores de Cabeça Constante','2025-11-04 13:00:00','Alérgica a consultas médicas',187526,'enchaqueca',NULL,'Finalizada'),(12,2,16,'Mal estar constante','2025-10-12 09:30:00','',358741,NULL,NULL,'Finalizada'),(13,4,16,'Joelho Doendo','2025-10-10 09:00:00','',475225,NULL,NULL,'Finalizada'),(14,1,16,'Dores no Braço','2025-10-11 11:00:00','',313037,NULL,NULL,'Finalizada'),(15,1,1,'Dores no Braço','2025-10-14 09:30:00','',NULL,NULL,2,'Pendente'),(16,6,16,'Consulta de Rotina','2025-10-22 12:30:00','',NULL,NULL,2,'Pendente'),(17,7,17,'Teste','2025-10-18 11:00:00','Val e sergio',656199,'teste 2',NULL,'Pendente'),(18,1,17,'teste','2025-10-17 16:00:00','jm',NULL,NULL,2,'Pendente'),(19,4,17,'Teste','2025-10-19 13:00:00','',NULL,NULL,2,'Finalizada'),(20,1,17,'Dores no Braço','2025-10-18 10:00:00','dasd',715050,'teste 6',NULL,'Finalizada');
/*!40000 ALTER TABLE `consulta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `leito`
--

DROP TABLE IF EXISTS `leito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `leito` (
  `id` int NOT NULL AUTO_INCREMENT,
  `numero` int NOT NULL,
  `idUnidade` int NOT NULL,
  `tipo` varchar(20) DEFAULT NULL,
  `statusLeito` varchar(20) DEFAULT NULL,
  `observacoes` varchar(10000) DEFAULT NULL,
  `idPaciente` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_leitos_locais` (`idUnidade`),
  KEY `fk_leito_paciente` (`idPaciente`),
  CONSTRAINT `fk_leito_paciente` FOREIGN KEY (`idPaciente`) REFERENCES `paciente` (`pacienteId`),
  CONSTRAINT `fk_leitos_locais` FOREIGN KEY (`idUnidade`) REFERENCES `locais` (`localId`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leito`
--

LOCK TABLES `leito` WRITE;
/*!40000 ALTER TABLE `leito` DISABLE KEYS */;
INSERT INTO `leito` VALUES (6,1,2,'Enfermaria','indisponivel','   Paciente já fez exames, está aguardando próximas etapas.\r\n\r\nAguardando transfusão.\r\n\r\nTransfusão feita, aguardando alta.\r\n\r\nAlta registrada para dia 22/10',1),(7,2,2,'Enfermaria','disponivel',NULL,NULL),(8,3,2,'UTI','disponivel',NULL,NULL),(9,4,2,'Enfermaria','disponivel',NULL,NULL),(10,1,4,'UTI','disponivel',NULL,NULL);
/*!40000 ALTER TABLE `leito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locais`
--

DROP TABLE IF EXISTS `locais`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `locais` (
  `localId` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(60) DEFAULT NULL,
  `endereco` varchar(50) DEFAULT NULL,
  `tipo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`localId`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locais`
--

LOCK TABLES `locais` WRITE;
/*!40000 ALTER TABLE `locais` DISABLE KEYS */;
INSERT INTO `locais` VALUES (1,'Clinica Jovem','Clinica','Rua Jovem, 78'),(2,'Hospital Beneficente','Hospital','Avenida Tiradentes, 1092'),(3,'Clinica 2','Clinica','Rua clinica'),(4,'Hospital quatro','Hospital','Avenida Hospital');
/*!40000 ALTER TABLE `locais` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paciente`
--

DROP TABLE IF EXISTS `paciente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paciente` (
  `pacienteId` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) DEFAULT NULL,
  `dataNasc` date DEFAULT NULL,
  `cpf` varchar(11) DEFAULT NULL,
  `endereco` varchar(50) DEFAULT NULL,
  `telefone` varchar(11) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pacienteId`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paciente`
--

LOCK TABLES `paciente` WRITE;
/*!40000 ALTER TABLE `paciente` DISABLE KEYS */;
INSERT INTO `paciente` VALUES (1,'João Mário Bulla Oliveira',NULL,'10037121936','Viela Bristol, 907','44998773734','jmbullaoliveira@gmail.com'),(2,'Carlos Almeida','1995-05-06','35671264865','Rua','44998752635',NULL),(3,'Bárbara Vitorino','2001-08-30','12345678910','Rua Santa Se, 287','44998342181',NULL),(4,'Sidney Araujo','1978-11-06','22244477769','Rua Milano','44997852423',NULL),(5,'Josimar Lopes','1989-06-08','11122233344','Rua Milano','45987589324',NULL),(6,'Jaqueline Oliveira','1987-06-04','45678912354','Rua Panama, 898','44975316254','jaqueline@gmail.com'),(7,'Sergio Augusto','1985-04-25','58763254821','Rua 1 ','44987125946','sergio@gmail.com');
/*!40000 ALTER TABLE `paciente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profissional`
--

DROP TABLE IF EXISTS `profissional`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profissional` (
  `profissionalId` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `dataNasc` date DEFAULT NULL,
  `crm` varchar(7) DEFAULT NULL,
  `telefone` varchar(11) DEFAULT NULL,
  `cargo` varchar(15) DEFAULT NULL,
  `cpf` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`profissionalId`),
  UNIQUE KEY `cpf` (`cpf`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profissional`
--

LOCK TABLES `profissional` WRITE;
/*!40000 ALTER TABLE `profissional` DISABLE KEYS */;
INSERT INTO `profissional` VALUES (1,'Jose Ferreira','jose.ferreira@gmail.com','1982-02-06','1111111','44997514852','Médico','06478521696'),(16,'Gustavo Henrique Lacerda','gustavolac@outlook.com','1989-04-26','2222222','44987521463','Médico','07521564396'),(17,'Valdenice Correa','val_correa1@gmail.com',NULL,'1354867','44987652315','Médico','84695875825');
/*!40000 ALTER TABLE `profissional` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prontuario`
--

DROP TABLE IF EXISTS `prontuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prontuario` (
  `idPaciente` int NOT NULL,
  `peso` double NOT NULL,
  `altura` double NOT NULL,
  `observacoes` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idPaciente`),
  CONSTRAINT `prontuario_ibfk_1` FOREIGN KEY (`idPaciente`) REFERENCES `paciente` (`pacienteId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prontuario`
--

LOCK TABLES `prontuario` WRITE;
/*!40000 ALTER TABLE `prontuario` DISABLE KEYS */;
INSERT INTO `prontuario` VALUES (1,85.8,1.75,'Acima do peso'),(3,65,1.55,'Consulta 11'),(4,100,1.98,''),(7,98,1.87,'');
/*!40000 ALTER TABLE `prontuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `receita`
--

DROP TABLE IF EXISTS `receita`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `receita` (
  `id` int NOT NULL,
  `descricao` varchar(100) DEFAULT NULL,
  `data_emissao` date DEFAULT NULL,
  `id_paciente` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_paciente` (`id_paciente`),
  CONSTRAINT `receita_ibfk_1` FOREIGN KEY (`id`) REFERENCES `consulta` (`consultaId`),
  CONSTRAINT `receita_ibfk_2` FOREIGN KEY (`id_paciente`) REFERENCES `paciente` (`pacienteId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receita`
--

LOCK TABLES `receita` WRITE;
/*!40000 ALTER TABLE `receita` DISABLE KEYS */;
INSERT INTO `receita` VALUES (10,'Nimesulida 10 dias','2025-10-13',1),(11,'dipirona 5 dias','2025-10-13',3),(17,'teset rece','2025-10-16',7),(19,NULL,'2025-10-17',4),(20,'Teste 6','2025-10-17',1);
/*!40000 ALTER TABLE `receita` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suprimentos`
--

DROP TABLE IF EXISTS `suprimentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suprimentos` (
  `unidadeId` int NOT NULL,
  `soro` int DEFAULT NULL,
  `gaze` int DEFAULT NULL,
  `alcool` int DEFAULT NULL,
  `medicamento` int DEFAULT NULL,
  PRIMARY KEY (`unidadeId`),
  CONSTRAINT `suprimentos_ibfk_1` FOREIGN KEY (`unidadeId`) REFERENCES `locais` (`localId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suprimentos`
--

LOCK TABLES `suprimentos` WRITE;
/*!40000 ALTER TABLE `suprimentos` DISABLE KEYS */;
INSERT INTO `suprimentos` VALUES (1,0,0,0,0),(2,12,12,12,12),(3,3,0,0,0),(4,0,0,0,0);
/*!40000 ALTER TABLE `suprimentos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unidade`
--

DROP TABLE IF EXISTS `unidade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `unidade` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unidade`
--

LOCK TABLES `unidade` WRITE;
/*!40000 ALTER TABLE `unidade` DISABLE KEYS */;
/*!40000 ALTER TABLE `unidade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `userId` int NOT NULL AUTO_INCREMENT,
  `nomeUsuario` varchar(100) DEFAULT NULL,
  `senha` varchar(162) DEFAULT NULL,
  `isAdmin` tinyint(1) NOT NULL,
  `email` varchar(50) NOT NULL,
  `tipoUsuario` varchar(20) DEFAULT NULL,
  `idPaciente` int DEFAULT NULL,
  `idProfissional` int DEFAULT NULL,
  PRIMARY KEY (`userId`),
  KEY `idPaciente` (`idPaciente`),
  KEY `idProfissional` (`idProfissional`),
  CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`idPaciente`) REFERENCES `paciente` (`pacienteId`),
  CONSTRAINT `usuario_ibfk_2` FOREIGN KEY (`idProfissional`) REFERENCES `profissional` (`profissionalId`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'admin','scrypt:32768:8:1$Nu4hprlXfMTj9y0Q$a0b1f7d57cd0b74420fc325b737e84d612301165a8cf00371a5148ea337569ce96c13e9aeae33e0fd953d425a370c6daf8a49f95ae8886562d9e3b5a1a5f1db6',1,'jmbullaoliveira@gmail.com',NULL,NULL,NULL),(3,'gustavo.lacerda','scrypt:32768:8:1$EjvLSWvhfczSNyh2$0d67ce4c1af7d0653d2fb11c7e529c9f453f595fcaa1eb6f45524588c5089f3ad1d294aa09106dc5e7dfa29f807c6e9ef84ee18fb0ba281f11442fa2ef0545b0',0,'gustavolac@outlook.com','profissional',NULL,16),(4,'joão.oliveira','scrypt:32768:8:1$mDPTedOE70Ot0FS4$06d7a3021c76f79e8ff750fa39434312f02bfa452e23199441d058ec563eb140aa3c366b869e6e1bf5cb90d9fc422b31a5b71904d98cff9dc51645bae4bccd16',0,'jmbullaoliveira@gmail.com','paciente',1,NULL),(5,'carlos.almeida','35671264865',0,'carl.alm@gmail.com','paciente',2,NULL),(6,'bárbara.vitorino','12345678910',0,'barbvit@gmail.com','paciente',3,NULL),(7,'sidney.araujo','22244477769',0,'sidneyaraujo@gmail.com','paciente',4,NULL),(8,'jose.ferreira','scrypt:32768:8:1$gwbkWRUuo9U0x3HV$ab8c365db0edaa392c6aed92805b3f5534a2d36f9665dbdde0657df0398e8b54ee8f354b6fe369b2e86ed64f37c58a77369b8bc3ce697212e093d489da483cbb',0,'jose.ferreira@gmail.com','profissional',NULL,1),(9,'josimar.lopes','scrypt:32768:8:1$Kcz3cJoiVUzcAm3a$5e939f655336b841b5bbb1fc873e6191c49edb1a866854ab5f661fe8b1ba70e3542984c2ef07223e5f25dde37c16fe35cf84d73d2126495242b78023aae86f19',0,'josimarl@gmail.com','paciente',5,NULL),(10,'jaqueline.oliveira','scrypt:32768:8:1$yPkhd0CtZnS3U8Hf$c896876f5e9441184927b40c72011c520f20a40ca6d000914052779abe640422ca45651d1e0340a12383513f4a107cfade3bfaa28e6ebc55d474f06816913410',0,'jaqueline@gmail.com','paciente',6,NULL),(11,'sergio.augusto','scrypt:32768:8:1$jNIR4yk2pObxYtgB$74f31b8a257a5e078e2f447773e6f0dcef44ad017b71379a519cce9f465dcaa2cda7c8c04f63008a075c73f122c123d6cb5febb8806e680bd339eb0e0fdb04b4',0,'sergio@gmail.com','paciente',7,NULL),(12,'valdenice.correa','scrypt:32768:8:1$HZG2mxqhAk3oO0W3$111e2baeb5badd1b51cbd0708d3d55b1fc8417cdeaace77c1233601ad12a004dfa0159e0e5833fcac0601a04fd7d7baee64b198a5c4af482b5d6f4f52a53d390',0,'val_correa@gmail.com','profissional',NULL,17);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-17 20:09:59
