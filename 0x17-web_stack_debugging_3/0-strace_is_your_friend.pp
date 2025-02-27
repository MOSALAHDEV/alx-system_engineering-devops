# fix errors

file { '/var/www/html/web-settings.php':
  ensure  => 'file',
  content => 'initial content here',
  mode    => '0644',
  owner   => 'www-data',
  group   => 'www-data',
}
exec { 'fix-apache':
  command => 'sed -i s/phpp/php/g /var/www/html/web-settings.php',
  path    => '/bin:/usr/bin:/usr/local/bin',
}
