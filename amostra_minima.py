#TAMANHO MÍNIMO DE UMA AMOSTRA
print('TAMANHO MÍNIMO DE UMA AMOSTRA ALEATÓRIA ESTRATIFICADA PROPORCIONAL')

N = int(input('TAMANHO DA POPULAÇÃO (N):  '))
E0 = float(input('ERRO AMOSTRAL TOLERÁVEL EM %  '))
print('------------------------------------------------------------------------')
print('------------------------------------------------VARIÁVEIS---------------')
print('------------------------------------------------------------------------')
E0 = E0/100
n0 = 1/(E0*E0)
n = (N*n0)/(N+n0)
x = n/N
print('Tamanho da população ---------------------------N =',N)
print('Erro amostral tolerável-------------------------E0 = ',E0)
print('Amostra Ideal (1ª aproximação)------------------n0 = {:.2f}'.format(n0))
print('Tamanho da Amostra -----------------------------n = {:.2f}'.format(n))
print('Estimador da Amostra ---------------------------x = {:.5f}'.format(x))

