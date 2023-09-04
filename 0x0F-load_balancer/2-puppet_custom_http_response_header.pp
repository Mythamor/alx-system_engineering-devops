# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Create an HTML file with "Hello World!" content
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

# Define a custom fact to retrieve the hostname
$custom_hostname = $facts['hostname']

# Configure Nginx to add the custom header
file { '/etc/nginx/conf.d/custom-header.conf':
  ensure  => file,
  content => "add_header X-Served-By $custom_hostname always;",
  require => Package['nginx'],
}

# Restart Nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/conf.d/custom-header.conf'],
}

# Apply the Nginx configuration
exec { 'nginx-config-test':
  command => '/usr/sbin/nginx -t',
  refreshonly => true,
  subscribe   => [
    File['/etc/nginx/conf.d/custom-header.conf'],
    Service['nginx'],
  ],
}

# Notify the Nginx service restart
Exec['nginx-config-test'] -> Service['nginx']
