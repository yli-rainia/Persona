CREATE TABLE `bookmark` (
  `id` int(11) NOT NULL auto_increment,
  `flags` int(11) NOT NULL default '0',
  `url` varchar(255) collate utf8_unicode_ci default NULL,
  `title` varchar(255) collate utf8_unicode_ci default NULL,
  `user_id` int(11) default NULL,
  `lft` int(11) default NULL,
  `rgt` int(11) default NULL,
  `visits` int(11) NOT NULL default '0',
  `archive_id` int(11) default NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci
