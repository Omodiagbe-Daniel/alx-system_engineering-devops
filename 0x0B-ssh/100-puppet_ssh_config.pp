#client config
exec { 'echo "PasswordAuthentication no" >> /etc/ssh/ssh_config',
  path => 'usr/bin'
}
exec { 'echo "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
  path => '/usr/bin'
}
