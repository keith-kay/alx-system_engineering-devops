#!/usr/bin/env bash
# using puppet to make changes to our configuration file

file { 'etc/ssh/ssh_config':
	ensure => present,

content =>"

	#SSH Client configuration
	host*
	IdentityFile /root/alx-system_engineering-devops/0x0B-ssh/.ssh/school
	PasswordAuthentication no
"}
