# This enables user holberton login and open files without errors.

exec { 'increasing-hard-file-limit-for-holberton-user':
  command => "sed -i "/^holberton hard/s/5/50000/' /etc/security/limits.conf",
  path	=> '/usr/local/bin/:/bin/'
}

exec { 'increasing-hard-file-limit-for-holberton-user':
  command => 'sed -i "/^holberton soft/s/4/50000/' /etc/security/limits.conf',
  path  => '/usr/local/bin/:/bin/'
}
