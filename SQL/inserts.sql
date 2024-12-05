
INSERT INTO `users` (`name`, `surname`, `username`, `DNI`, `password`, `email`,`groups`) VALUES
('John', 'Doe', 'johndoe', '12345678A', 'password1', 'johndoe@example.com', 'DAM2A'),
('Jane', 'Doe', 'janedoe', '87654321B', 'password2', 'janedoe@example.com', 'DAM2A'),
('Alice', 'Smith', 'alicesmith', '11223344C', 'password3', 'alicesmith@example.com', 'DAM2B'),
('Bob', 'Johnson', 'bobjohnson', '44332211D', 'password4', 'bobjohnson@example.com', 'DAM2A'),
('Charlie', 'Brown', 'charliebrown', '55667788E', 'password5', 'charliebrown@example.com', 'DAM2B'),
('David', 'Wilson', 'davidwilson', '99887766F', 'password6', 'davidwilson@example.com', 'DAM2B'),
('Eva', 'Davis', 'evadavis', '66554433G', 'password7', 'evadavis@example.com', 'DAM2A'),
('Frank', 'Miller', 'frankmiller', '33445566H', 'password8', 'frankmiller@example.com', 'DAM2B'),
('Grace', 'Lee', 'gracelee', '77889900I', 'password9', 'gracelee@example.com', 'DAM2A'),
('Hannah', 'Taylor', 'hannahtaylor', '99001122J', 'password10', 'hannahtaylor@example.com', 'DAM2B');

INSERT INTO `rooms` (`name`, `description`, `building_name`, `created_at`, `updated_at`) VALUES
('Room A', 'Description for Room A', 'Building 1', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Room B', 'Description for Room B', 'Building 1', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Room C', 'Description for Room C', 'Building 2', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Room D', 'Description for Room D', 'Building 2', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Room E', 'Description for Room E', 'Building 3', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Room F', 'Description for Room F', 'Building 3', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Room G', 'Description for Room G', 'Building 4', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Room H', 'Description for Room H', 'Building 4', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Room I', 'Description for Room I', 'Building 5', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Room J', 'Description for Room J', 'Building 5', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO `access` (`user_id`, `room_id`, `entry_time`, `exit_time`, `entry_date`, `exit_date`, `created_at`, `updated_at`) VALUES
(1, 1, '08:00:00', '10:00:00', '2023-11-11', '2023-11-11', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(2, 1, '09:00:00', '11:00:00', '2023-11-11', '2023-11-11', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(3, 1, '10:00:00', '12:00:00', '2023-11-11', '2023-11-11', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(1, 4, '11:00:00', '13:00:00', '2023-11-11', '2023-11-11', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(1, 5, '12:00:00', '14:00:00', '2023-11-11', '2023-11-11', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(1, 6, '13:00:00', '15:00:00', '2023-11-11', '2023-11-11', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(1, 7, '14:00:00', '16:00:00', '2023-11-11', '2023-11-11', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(1, 8, '15:00:00', '17:00:00', '2023-11-11', '2023-11-11', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(1, 9, '16:00:00', '18:00:00', '2023-11-11', '2023-11-11', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(1, 10, '17:00:00', '19:00:00', '2023-11-11', '2023-11-11', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);