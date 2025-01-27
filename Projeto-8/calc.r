library(ggplot2)
library(dplyr)

head(mtcars)
summary(mt)cars

ggplot2(mtcars, aes(x = wt, y = mpg)) + 
    geom_point() +
    labs(title = "Relação entre Peso e Eficiência de Combustível",
        x = "Peso (1000 lbs)",
        y = "Eficiência de Combustível (mpg)"
    )


cor(mtcars$mpg, mtcars$wt)

mtcars %>% 
    group_by(cyl) %>% 
    summarise(mpg_mean = mean(mpg))

ggsave("grafico_peso_vs_mpg.png")
write.csv(summary(mtcars), "resumo_mtcars.csv")
