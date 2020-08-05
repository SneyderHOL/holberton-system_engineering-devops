#create a SSH configuration file using puppet
exec { 'adding lines to ssh_config file':
  path     => '/etc/ssh/',
  command  => 'echo -e "\nIdentityFile ~/.ssh/holberton\nPasswordAuthentication no\n" >> ssh_config',
  provider => 'shell',
}
