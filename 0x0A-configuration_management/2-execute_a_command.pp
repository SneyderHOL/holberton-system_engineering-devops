#create a manifest that kills a process named killmenow
exec { 'pkill -f ./killmenow':
  path     => '/usr/bin:/usr/sbin:/bin',
  command  => 'pkill -f ./killmenow',
  provider => 'shell',
}
