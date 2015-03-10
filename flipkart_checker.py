import urllib2
import re
import subprocess
# URL to the product
flipkart_url = 'http://www.flipkart.com/cooler-master-notepal-l1-cooling-pad/p/itmdyh7fzpggufdc?pid=ACCDYH7DHYZYDQMH&srno=b_1&offer=DOTDOnCoolingPads_Mar10.&ref=f3f70743-9f5c-4c8c-afe4-42a9d57d0274'
flipkart_fetch = urllib2.urlopen(flipkart_url).read()
# the magic line (change this accordingly :) )
product = re.findall('Notify me when this product is in stock', flipkart_fetch);
# message to print 
if len(product) == 0: 
   message = "your product is back in stock at Flipkart "
   subprocess.Popen(['notify-send', message])
else:
# this line only prints in terminal
   print 'Your product is not available '
