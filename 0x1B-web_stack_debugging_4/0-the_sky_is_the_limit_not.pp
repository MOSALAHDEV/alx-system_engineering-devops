# This script increase nginx ability to handle traffic
{ 'fix_nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx && sudo service nginx restart',
  path    => '/usr/local/bin:/bin/',
}
