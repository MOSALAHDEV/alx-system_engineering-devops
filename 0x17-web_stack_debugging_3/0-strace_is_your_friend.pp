# fix Apache 500 error by ensuring index.php has correct content

file { '/var/www/html/index.php':
  ensure  => file,
  content => "<?php phpinfo(); ?>\n",
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

service { 'apache2':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  subscribe  => [File['/var/www/html/index.php']],
}
