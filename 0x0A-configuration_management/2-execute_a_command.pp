# Executing command using puppet
exec { 'kill_kill_me_know':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/usr/sbin'],
}
