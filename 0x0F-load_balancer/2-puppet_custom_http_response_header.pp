# Puppet manifest to configure Nginx with a custom HTTP response header X-Served-By

package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => File['/etc/nginx/nginx.conf'],
}

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  require => Package['nginx'],
  content => template('nginx/nginx.conf.erb'),
}

# Template file nginx.conf.erb should include:
# add_header X-Served-By $hostname always; inside the http block
# You can also use file_line if you want to avoid templates.

file_line { 'add_custom_header':
  path  => '/etc/nginx/nginx.conf',
  line  => '    add_header X-Served-By $hostname always;',
  match => 'add_header X-Served-By',
  after => 'http {',
  require => Package['nginx'],
  notify  => Service['nginx'],
}
