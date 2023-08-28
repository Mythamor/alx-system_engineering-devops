#!/usr/bin/env bash

# Install nginx with Puppet

# nginx_config.pp

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Configure Nginx site for redirection
file { '/etc/nginx/sites-available/redirect_config':
  ensure  => 'present',
  content => "
server {
    listen 80;
    server_name _;

    location /redirect_me {
        return 301 http://example.com/destination_page;
    }

    # Add your other server configurations here if needed
}
  ",
  require => Package['nginx'],
}

# Create symbolic link for the site
file { '/etc/nginx/sites-enabled/redirect_config':
  ensure => 'link',
  target => '/etc/nginx/sites-available/redirect_config',
  require => File['/etc/nginx/sites-available/redirect_config'],
}

# Create the custom 404.html page
file { '/usr/share/nginx/html/404.html':
  ensure => 'present',
  content => "Ceci n'est pas une page\n",
  require => Package['nginx'],
}

# Configure Nginx to return 404 error with custom page
file { '/etc/nginx/sites-available/404_config':
  ensure  => 'present',
  content => "
server {
    listen 80;
    server_name _;

    location / {
        return 404 /404.html;
    }

    error_page 404 /404.html;
    location = /404.html {
        root /usr/share/nginx/html;
        internal;
    }

    # Add your other server configurations here if needed
}
  ",
  require => Package['nginx'],
}

# Create symbolic link for the 404 site
file { '/etc/nginx/sites-enabled/404_config':
  ensure => 'link',
  target => '/etc/nginx/sites-available/404_config',
  require => File['/etc/nginx/sites-available/404_config'],
}

# Ensure Nginx is running and enabled at boot
service { 'nginx':
  ensure => 'running',
  enable => true,
  require => [File['/etc/nginx/sites-enabled/redirect_config'], File['/etc/nginx/sites-enabled/404_config']],
}

