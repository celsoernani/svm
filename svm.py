
from sklearn import svm

x = [[0,0],[1,1]] ##matriz de treino
y = [0,1]  ## classe esperada
clf = svm.SVC() ##criando classificador SVM
clf.fit(x,y) ##treinando classificador
classe = clf.predict([[2., 2.]]) ##previsão

print(classe)
