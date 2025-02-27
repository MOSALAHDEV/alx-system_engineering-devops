# Fix Apache 500 error
file { '/var/www/html/index.php':
  ensure  => file,
  content => '<?php phpinfo(); ?>\n',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}
exec { 'apache2':
  ensure    => running,
  enable    => true,
  harestart => true,
  subscribe => File['/var/www/html/index.php'],
}
