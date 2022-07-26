#!/usr/bin/env ruby
# a regular expression that matches exactly a string
# starts with h and ends with n
# it must have a single character in between

puts ARGV[0].scan(/^h[A-Za-z0-9]n$/).join
