CREATE TABLE `archive_item` (
  `id` int(11) NOT NULL auto_increment,
  `flags` int(11) NOT NULL default '0',
  `s3_key` varchar(255) collate utf8_unicode_ci default NULL,
  `md5` varchar(255) collate utf8_unicode_ci default NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci
