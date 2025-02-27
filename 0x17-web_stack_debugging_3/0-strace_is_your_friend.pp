# Fix Apache 500 error

package { ['apache2', 'php', 'php-mysql']:
  ensure => installed,
}

file { '/var/www/html/index.php':
  ensure  => file,
  content => "<?php phpinfo(); ?>\n",
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

file { '/var/www/html':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  recurse => true,
}

service { 'apache2':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  subscribe  => [File['/var/www/html/index.php'], Package['php-mysql']],
}

