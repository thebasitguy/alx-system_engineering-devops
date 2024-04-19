# Ensures pip3 is installed
package { 'pip3':
  ensure   => installed,
  provider => 'pip3',
}

# Installs Flask
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
