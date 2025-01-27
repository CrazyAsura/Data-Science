library(ggplot2)
library(dplyr)
library(caret)
library(broom)

data(iris)
str(iris)
summary(iris)

ggplot(iris, aes(x = Petal.Length, y = Sepal.Length)) +
    geom_point(aes(color = Species), size = 3) +
    labs(title = "Relação entre Comprimento da Pétala e Comprimento da Sépala",
       x = "Comprimento da Pétala",
       y = "Comprimento da Sépala") +
    theme_minimal()

set.seed(123)

trainIndex <- createDataPartition(iris$Sepal.Length, p = 0.8, list = FALSE)
trainData <- iris[trainIndex]
testData <- iris[-trainIndex]

modelo <- lm(Sepal.Length ~ Petal.Length + Petal.Width + Sepal.Width, data = trainData)

summary(modelo)

previsoes <- predict(modelo, newdata = testData)

resultados <- data.frame(Real = testData$Sepal.Length, Previsto = previsoes)
print(resultados)

mae <- mean(abs(resultados$Real - resultados$Previsto))
print(paste("Erro Médio Absoluto (MAE):", round(mae, 2)))

ggplot(resultados, aes(x = Real, y = Previsto)) +
  geom_point(aes(color = "Predições"), size = 3) +
  geom_abline(intercept = 0, slope = 1, color = "red", linetype = "dashed") +  # Linha de identidade
  labs(title = "Valores Reais vs. Previsões",
       x = "Valores Reais de Sepal.Length",
       y = "Previsões de Sepal.Length") +
  theme_minimal()
