library(rpart)         # Para criar o modelo de árvore de decisão
library(caret)         # Para avaliar o modelo
library(rpart.plot)    # Para visualizar a árvore de decisão

data(iris)  # Carregar o conjunto de dados 'iris'
str(iris)   # Estrutura do conjunto de dados
summary(iris)  # Estatísticas resumidas

set.seed(123)
trainIndex <- createDataPartition(iris$Species, p = 0.7, list = FALSE)
trainData <- iris[trainIndex, ]
testData <- iris[-trainIndex, ]

modelo_arvore <- rpart(Species ~ Sepal.Length + Sepal.Width + Petal.Length + Petal.Width,
                       data = trainData, method = "class")

summary(modelo_arvore)

rpart.plot(modelo_arvore)

previsoes <- predict(modelo_arvore, newdata = testData, type = "class")

confusionMatrix(previsoes, testData$Species)
