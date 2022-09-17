# Using Puppet, install flask from pip3
exec { 'flask installation':
  command => '/bin/sudo pip3 install flask==2.1.0',
  path    => '.'
}
