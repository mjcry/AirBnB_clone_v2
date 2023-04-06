# Install Nginx
class { 'nginx':
  ensure => 'installed',
}

# Create web_static directories
file { '/data':
  ensure => 'directory',
}

file { '/data/web_static':
  ensure => 'directory',
}

file { '/data/web_static/releases':
  ensure => 'directory',
}

file { '/data/web_static/shared':
  ensure => 'directory',
}

# Create a symbolic link to /data/web_static/releases/test
file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test',
  require => [
    File['/data/web_static'],
    File['/data/web_static/releases'],
    File['/data/web_static/shared'],
  ],
}

# Create a test HTML file
file { '/data/web_static/releases/test/index.html':
  content => '<html><head></head><body>Holberton School</body></html>',
  require => File['/data/web_static/releases/test'],
}

# Update Nginx configuration
file { '/etc/nginx/sites-available/default':
  content => "
server {
    listen 80;
    listen [::]:80 default_server;
    server_name _;

    location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html;
    }
}
  ",
  notify => Service['nginx'],
}

# Reload Nginx
service { 'nginx':
  ensure => 'running',
  enable => true,
  require => [
    File['/etc/nginx/sites-available/default'],
  ],
  subscribe => [
    File['/etc/nginx/sites-available/default'],
  ],
}

