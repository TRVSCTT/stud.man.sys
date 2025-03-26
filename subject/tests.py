from django.test import TestCase

# Create your tests here.
x = 1
y = 2
if x > y:
    try:
        x*y
    except ValueError:
        print('there is a problem guy')
else:
    print('try go')