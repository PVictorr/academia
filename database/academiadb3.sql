-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema academiadb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema academiadb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `academiadb` DEFAULT CHARACTER SET utf8 ;
USE `academiadb` ;

-- -----------------------------------------------------
-- Table `academiadb`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `academiadb`.`Usuario` (
  `codigous` BIGINT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(200) NOT NULL,
  `sobrenome` VARCHAR(200) NOT NULL,
  `email` VARCHAR(200) NOT NULL,
  `senha` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`codigous`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `academiadb`.`Avaliacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `academiadb`.`Avaliacao` (
  `codigoav` BIGINT NOT NULL,
  `peso` VARCHAR(45) NULL,
  `altura` VARCHAR(45) NULL,
  `braco` VARCHAR(45) NULL,
  `ombro` VARCHAR(45) NULL,
  `peito` VARCHAR(45) NULL,
  `cintura` VARCHAR(45) NULL,
  `quadril` VARCHAR(45) NULL,
  `abdominal` VARCHAR(45) NULL,
  `coxaMedial` VARCHAR(45) NULL,
  `panturrilha` VARCHAR(45) NULL,
  `Usuario_codigous` BIGINT NOT NULL,
  PRIMARY KEY (`codigoav`),
  INDEX `fk_Avaliacao_Usuario1_idx` (`Usuario_codigous` ASC),
  CONSTRAINT `fk_Avaliacao_Usuario1`
    FOREIGN KEY (`Usuario_codigous`)
    REFERENCES `academiadb`.`Usuario` (`codigous`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `academiadb`.`Rotina`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `academiadb`.`Rotina` (
  `codigorot` BIGINT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(500) NOT NULL,
  `objetivo` VARCHAR(500) NOT NULL,
  `dia1` BIGINT NULL,
  `dia2` BIGINT NULL,
  `dia3` BIGINT NULL,
  `dia4` BIGINT NULL,
  `dia5` BIGINT NULL,
  `dia6` BIGINT NULL,
  `dia7` BIGINT NULL,
  `Usuario_codigous` BIGINT NOT NULL,
  PRIMARY KEY (`codigorot`),
  INDEX `fk_Rotina_Usuario1_idx` (`Usuario_codigous` ASC),
  CONSTRAINT `fk_Rotina_Usuario1`
    FOREIGN KEY (`Usuario_codigous`)
    REFERENCES `academiadb`.`Usuario` (`codigous`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `academiadb`.`Treino`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `academiadb`.`Treino` (
  `codigotr` BIGINT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(200) NOT NULL,
  `descricao` VARCHAR(500) NOT NULL,
  PRIMARY KEY (`codigotr`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `academiadb`.`Exercicios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `academiadb`.`Exercicios` (
  `codigoex` BIGINT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(200) NOT NULL,
  `descricao` VARCHAR(500) NOT NULL,
  `equipamento` VARCHAR(100) NOT NULL,
  `tp_treino` VARCHAR(100) NOT NULL,
  `video` VARCHAR(5000) NOT NULL,
  PRIMARY KEY (`codigoex`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `academiadb`.`Treino_has_Exercicios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `academiadb`.`Treino_has_Exercicios` (
  `Treino_codigotr` BIGINT NOT NULL,
  `Exercicios_codigoex` BIGINT NOT NULL,
  `carga` BIGINT NOT NULL,
  `series` BIGINT NOT NULL,
  `repeticoes` BIGINT NOT NULL,
  PRIMARY KEY (`Treino_codigotr`, `Exercicios_codigoex`),
  INDEX `fk_Treino_has_Exercicios_Exercicios1_idx` (`Exercicios_codigoex` ASC),
  INDEX `fk_Treino_has_Exercicios_Treino_idx` (`Treino_codigotr` ASC),
  CONSTRAINT `fk_Treino_has_Exercicios_Treino`
    FOREIGN KEY (`Treino_codigotr`)
    REFERENCES `academiadb`.`Treino` (`codigotr`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Treino_has_Exercicios_Exercicios1`
    FOREIGN KEY (`Exercicios_codigoex`)
    REFERENCES `academiadb`.`Exercicios` (`codigoex`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
