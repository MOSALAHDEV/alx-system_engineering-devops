# This script increase nginx ability to handle traffic
{ 'fix_nginx':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin:/bin/',
}

# restart nginx

exec { 'restart_nginx':
  command => '/bin/systemctl restart nginx',
  path    => '/usr/local/bin:/bin/',
}

