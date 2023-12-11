CREATE TABLE IF NOT EXISTS profesor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dni CHAR(9) NOT NULL UNIQUE CHECK (dni REGEXP '^[0-9]{8}[A-Za-z]$'),
    nombre VARCHAR(20) NOT NULL,
    direccion VARCHAR(35) NOT NULL,
    telefono CHAR(9) NOT NULL CHECK (telefono REGEXP '^[0-9]{9}$')
);
CREATE TABLE IF NOT EXISTS alumno(
    num_expediente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    apellidos VARCHAR(35) NOT NULL,
    telefono CHAR(9) NOT NULL CHECK (telefono REGEXP '^[0-9]{9}$'),
    direccion VARCHAR(35) NOT NULL,
    fecha_nac DATE CHECK (fecha_nac IS NULL OR STR_TO_DATE(fecha_nac, '%Y-%m-%d') IS NOT NULL),
    CONSTRAINT uk_nombre_apellidos UNIQUE (nombre, apellidos)
);
CREATE TABLE IF NOT EXISTS curso(
    cod_curso INT AUTO_INCREMENT PRIMARY KEY,
    id_profesor INT,
    nombre VARCHAR(20) NOT NULL UNIQUE,
    descripcion VARCHAR(50) NOT NULL,
    CONSTRAINT fk_curso_profesor FOREIGN KEY (id_profesor) REFERENCES profesor(id) ON UPDATE CASCADE
);
CREATE TABLE IF NOT EXISTS alumno_curso(
    num_exp_alu INT,
    cod_curso INT,
    CONSTRAINT pk_alumno_curso PRIMARY KEY(num_exp_alu, cod_curso),
    CONSTRAINT fk_alumno_curso_alumno FOREIGN KEY (num_exp_alu) REFERENCES alumno(num_expediente) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_alumno_curso_curso FOREIGN KEY (cod_curso) REFERENCES curso(cod_curso) ON DELETE CASCADE ON UPDATE CASCADE

);