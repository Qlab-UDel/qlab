# 0. Clean up data (no duplicates, etc)
# 1. Make sure matched
# 2. Test same/ different effect (aov)
# 3. Are all 3 correlated with vocab? (hope ll and lv will be more correlated)
# 4. Plot again in ggplots --> use scripts from zhenghan
# 5. t-tests to show that there was learning in each condition
# 6. Abstract (move off of github)



install.packages("plotly")
library(plotly)

task <- c("ll", "lv", "vl", "vv")
random <- c(1.173, 1.112, 1.202, 1.14)
structured <- c(1.013, -1.254, -2.554, -2.376)
data <- data.frame(task, random, structured)


p <- plot_ly(data, x = ~task, y = ~random, type = 'bar', name = 'random', color =I("rgba(160,190,156,1)")) %>%
  add_trace(y = ~structured, name = 'structured', color =I("rgba(51,113,74,1)")) %>%
  layout(yaxis = list(title = 'Mean RT Slope'), barmode = 'group')


task <- c("letter", "image")
same <- c(0.583, 0.635)
different <- c(0.609, 0.661)
data <- data.frame(task, same, different)


q <- plot_ly(data, x = ~task, y = ~same, type = 'bar', name = 'same', color =I("rgba(109,138,135,1)")) %>%
  add_trace(y = ~different, name = 'different', color =I("rgba(47,92,91,1)")) %>%
  layout(yaxis = list(title = 'Mean Accuracy'), barmode = 'group')


task <- c("ll", "lv", "vv", "vl")
structured <- c(462.512, 460.18, 487.465, 461.908)
random <- c(488.224, 513.437, 525.127, 503.218)
data <- data.frame(task, structured, random)

k <- plot_ly(data, x = ~task, y = ~random, type = 'bar', name = 'random', color =I("rgba(160,190,156,1)")) %>%
  add_trace(y = ~structured, name = 'structured', color =I("rgba(51,113,74,1)")) %>%
  layout(yaxis = list(title = 'Mean RT'), barmode = 'group')




# TO DO: for mean RT, only plot from 300 up

# TO DO: look at Zhenghan's ggplot commands to plot bar graphs w data points