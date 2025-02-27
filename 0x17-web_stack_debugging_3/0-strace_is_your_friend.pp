# fix  errors

exec{'fix-apache':
  command => 'sed -i s/phpp/php/g /var/www/html/web-settings.php',
  path    => ['/bin', '/usr/bin', '/usr/local/bin'],
}
