CREATE LOGIN readOnlyUser WITH PASSWORD = 'password';
CREATE LOGIN developerUser WITH PASSWORD = 'password';
CREATE LOGIN adminUser WITH PASSWORD = 'password';

CREATE USER readOnlyUser FOR LOGIN readOnlyUser;
CREATE USER developerUser FOR LOGIN developerUser;
CREATE USER adminUser FOR LOGIN adminUser;