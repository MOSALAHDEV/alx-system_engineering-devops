# puppet script to correct typo in a file

$file = '/var/www/html/wp-settings.php'

exec { 'fix_wp_settings':
  command => "sed -i 's/phpp/php/g' ${file}",
  onlyif  => "grep -q 'phpp' ${file}",
  path    => ["/bin", "/usr/bin", "/sbin", "/usr/sbin"],
}

