#client config
exec { 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/school" >> /.ssh/config':
        path    => '/bin/'
}
