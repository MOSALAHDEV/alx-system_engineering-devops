# this script increases Nginx's ability to handle traffic

exec { 'fix_nginx':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => ['/usr/local/bin', '/bin'],
}

exec { 'restart_nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/',
}
