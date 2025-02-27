# Fix Apache 500 error
package { ['apache2', 'php', 'php-mysql']:
  ensure  => installed,
}

file { '/var/www/html/index.php':
  ensure  => file,
  content => '<?php phpinfo(); ?>\n',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}
file { '/var/www/html/index.html':
  ensure  => file,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  recurse => true,
}
exec { 'apache2':
  ensure    => running,
  enable    => true,
  harestart => true,
  subscribe => File['/var/www/html/index.php'], package['php-mysql'],
}
