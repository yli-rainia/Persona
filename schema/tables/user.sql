CREATE TABLE `user` (
  `id` int(11) NOT NULL auto_increment,
  `flags` int(11) NOT NULL default '0',
  `email` varchar(255) collate utf8_unicode_ci default NULL,
  `time_last_login` int(11) default NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci
