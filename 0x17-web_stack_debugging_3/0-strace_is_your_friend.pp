# puppet script to correct typo in a file

$file = '/var/www/html/wp-settings.php'

exec { 'fix_wp_settings':
  command => "sed -i 's/phpp/php/g' ${file}",
  onlyif  => "grep -q 'phpp' ${file}",
  path    => ['/bin', '/usr/bin'],
}

service { 'apache2':
  ensure   => running,
  enable   => true,
  provider => 'init',
}
