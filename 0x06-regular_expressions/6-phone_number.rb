#!/usr/bin/env ruby
# a regular expression that matches 10 digit phone number

puts ARGV[0].scan(/^\d{10}$/).join
