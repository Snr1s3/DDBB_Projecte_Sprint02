-- Crear Usuaris
CREATE USER 'readOnlyUser' IDENTIFIED BY 'password';
CREATE USER 'developerUser' IDENTIFIED BY 'password';
CREATE USER 'adminUser' IDENTIFIED BY 'password';

-- DOnar permisos
GRANT SELECT ON DDBBPROJ.* TO 'readOnlyUser';
GRANT SELECT, INSERT, UPDATE, DELETE ON DDBBPROJ.* TO 'developerUser';
GRANT ALL PRIVILEGES ON DDBBPROJ.* TO 'adminUser';

-- Actualitzar permisos
FLUSH PRIVILEGES;