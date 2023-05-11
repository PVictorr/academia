-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Exercicios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Exercicios` (
  `codigoex` BIGINT NOT NULL,
  `nome` VARCHAR(200) NOT NULL,
  `descricao` VARCHAR(1000) NOT NULL,
  PRIMARY KEY (`codigoex`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Usuario` (
  `codigous` BIGINT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(200) NOT NULL,
  `email` VARCHAR(200) NOT NULL,
  `senha` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`codigous`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Rotina`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Rotina` (
  `codigorot` BIGINT NOT NULL,
  `objetivo` VARCHAR(1000) NOT NULL,
  `semana` VARCHAR(200) NOT NULL,
  `Usuario_codigous` BIGINT NOT NULL,
  PRIMARY KEY (`codigorot`, `Usuario_codigous`),
  INDEX `fk_Rotina_Usuario1_idx` (`Usuario_codigous` ASC),
  CONSTRAINT `fk_Rotina_Usuario1`
    FOREIGN KEY (`Usuario_codigous`)
    REFERENCES `mydb`.`Usuario` (`codigous`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Treino`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Treino` (
  `codigotr` BIGINT NOT NULL,
  `nome` VARCHAR(200) NOT NULL,
  `dia` VARCHAR(200) NOT NULL,
  `Rotina_codigorot` BIGINT NOT NULL,
  PRIMARY KEY (`codigotr`, `Rotina_codigorot`),
  INDEX `fk_Treino_Rotina1_idx` (`Rotina_codigorot` ASC),
  CONSTRAINT `fk_Treino_Rotina1`
    FOREIGN KEY (`Rotina_codigorot`)
    REFERENCES `mydb`.`Rotina` (`codigorot`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Treino_has_Exercicios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Treino_has_Exercicios` (
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
    REFERENCES `mydb`.`Treino` (`codigotr`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Treino_has_Exercicios_Exercicios1`
    FOREIGN KEY (`Exercicios_codigoex`)
    REFERENCES `mydb`.`Exercicios` (`codigoex`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Avaliacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Avaliacao` (
  `codigoav` INT NOT NULL,
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
  PRIMARY KEY (`codigoav`, `Usuario_codigous`),
  INDEX `fk_Avaliacao_Usuario1_idx` (`Usuario_codigous` ASC),
  CONSTRAINT `fk_Avaliacao_Usuario1`
    FOREIGN KEY (`Usuario_codigous`)
    REFERENCES `mydb`.`Usuario` (`codigous`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
