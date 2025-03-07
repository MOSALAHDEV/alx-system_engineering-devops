# enable holberton user limit

exec { 'enable_holberton_hard_limit':
  command => 'sed -i "/holberton hard/s/5/5000/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin/',
}
exec { 'enable_holberton_soft_limit':
  command => 'sed -i "/holberton soft/s/4/5000/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin/',
}
