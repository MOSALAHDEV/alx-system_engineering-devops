# Fix Apache 500 error
file { '/var/www/html/index.php':
  ensure => file,
  content => '<?php phpinfo(); ?>\n',
  owner => 'www-data',
  group => 'www-data',
  mode => '0644',
}
exec { 'restart_apache2':
  command => '/bin/systemctl restart apache2',
  path    => ['/bin', '/usr/bin'],
  onlyif  => '/bin/systemctl is-active apache2',
}

