for i in range(1, 13):
    print("No. {0:2} squared is {1:3}, and cubed is {2:4}"
          .format(i, i ** 2, i ** 3))

print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3}, and cubed is {2:>4}"
          .format(i, i ** 2, i ** 3))

print()

print("Pi is approximately {:>60.20}".format(22 / 7))
print("Pi is approximately {:>60.20f}".format(22 / 7))
print("Pi is approximately {:12f}".format(22 / 7))
print("Pi is approximately {:12.50f}".format(22 / 7))
print("Pi is approximately {:52.50f}".format(22 / 7))
print("Pi is approximately {:62.50f}".format(22 / 7))
print("Pi is approximately {:<60.50f}".format(22 / 7))
print("Pi is approximately {:<60.54f}".format(22 / 7))

print("This is a test to see if {0:3.10f} looks anything like {0:20.10f} looks".format(5 / 4))

print()