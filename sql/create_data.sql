--
-- Crea tabla `datos`
--

CREATE TABLE `datos` (
  `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `fecha` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `temperatura` decimal(10,2),
  `humedad` decimal(10,2)
);
