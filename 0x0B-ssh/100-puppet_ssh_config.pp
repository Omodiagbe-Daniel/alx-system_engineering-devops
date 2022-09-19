# client configuration
exec { 'ssh client config':
  command => 'echo PasswordAuthentication no >> /etc/ssh/ssh_config',
  path    => '/usr/bin'
}
exec { 'ssh client con':
  command => 'echo ~/.ssh/school ~/.ssh/config',
  path    => '/usr/bin'
}
