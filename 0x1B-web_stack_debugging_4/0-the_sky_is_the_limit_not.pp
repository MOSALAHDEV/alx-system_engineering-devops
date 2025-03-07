# This script increase nginx ability to handle traffic

exec { 'fix_nginx':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx && systemctl restart nginx',
  path    => '/usr/local/bin:/usr/bin:/bin',
  unless  => 'grep -q "4096" /etc/default/nginx',
}

