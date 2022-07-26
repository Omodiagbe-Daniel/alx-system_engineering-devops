#!/usr/bin/env ruby
# a regular expression that matches school
name=$1
puts ARGV[0].scan(/School/).join
