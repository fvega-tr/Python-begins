t = ( 0, 4, 132.42222, 10000, 12345.67)
#print ("#day"+ "{:0>2d}".format(t[0]) + ", ex" + "{:0>2d}".format(t[1]) + " : " + "{:.2f}".format(t[2]), end = '')
#print (",", "{:.2e}".format(t[3]) + ", " + "{:.2e}".format(t[4]))
print("day_%02d, ex_%02d  :  %.2f, %.2e, %.2e" % (t[0], t[1], t[2], t[3], t[4]))