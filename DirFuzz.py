#!/usr/bin/python3

import requests
host = input("Host: ")
file = open("opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-meduim.txt",'r')
outfile = open("{}_dir_fuzzing_outfile.txt".format(host),'w')

extensions = ['html','html5','php','jpg','jpeg','png','txt']
directories = []
successfull = []

for dir in file:
  for ext in extensions:
    response = requests.get("{}/{}.{}".format(host,dir,ext))
    if 200 == response.status_code:
      print("{}: {}.{}".format(response.status_code,dir,ext))
      successful_dir = "{}.{}".format(dir,ext)
      successful.append(successful_dir)
for success in successful:
  print("Status of 200 on: {}".format(success))
  outfile.write("200: {}".format(success))
  
