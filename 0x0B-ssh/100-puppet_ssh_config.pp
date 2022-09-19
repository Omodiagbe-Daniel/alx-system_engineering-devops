# client configuration
exec { 'ssh client config':
  command => 'echo "PasswordAuthentication no" >> /etc/ssh/ssh_config',
  path    => '/usr/bin'
}
exec { 'ssh client':
  command => 'echo "~/.ssh/school" >> /etc/ssh/ssh_config',
  path    => '/usr/bin'
}
