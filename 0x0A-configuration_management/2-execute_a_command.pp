# Using Puppet, create a manifest that kills a process named killmenow

exec { 'kill me now':
  command => 'pkill killmenow',
  path    => '/usr/bin';
}
