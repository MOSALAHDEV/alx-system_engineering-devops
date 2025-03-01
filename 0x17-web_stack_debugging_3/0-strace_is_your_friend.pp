# puppet script to correct typo in a file

$file = '/var/www/html/wp-settings.php'

edit {
  command => 'sed -i "s/phpp/php/g" $file',
  path    => ['/bin', '/usr/bin'],
}

