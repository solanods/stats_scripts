#MINIMUM SIZE OF A SAMPLE
print('MINIMUM SIZE OF A PROPORTIONAL STRATIFIED RANDOM SAMPLE')

N = int(input('POPULATION SIZE (N):  '))
E0 = float(input('TOLERABLE SAMPLE ERROR %  '))
print('------------------------------------------------------------------------')
print('------------------------------------------------VARIABLES---------------')
print('------------------------------------------------------------------------')
E0 = E0/100
n0 = 1/(E0*E0)
n = (N*n0)/(N+n0)
x = n/N
print('Population size --------------------------------N =',N)
print('Tolerable sample error--------------------------E0 = ',E0)
print('First approach----------------------------------n0 = {:.2f}'.format(n0))
print('Sample size ------------------------------------n = {:.2f}'.format(n))
print('Sample estimator -------------------------------x = {:.5f}'.format(x))

