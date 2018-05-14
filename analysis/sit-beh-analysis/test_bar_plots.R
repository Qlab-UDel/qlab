# TO DO: Change to ggplot to include beeswarm



# ************ PLOT MEAN ACCURACY BY TASK AND GROUP ************ 

task <- c("letter", "image")
same <- c(0.587, 0.597)
different <- c(0.641, 0.681)
data <- data.frame(task, same, different)


accuracy_plot <- plot_ly(data, x = ~task, y = ~same, type = 'bar', name = 'same', color =I("rgba(109,138,135,1)")) %>%
  add_trace(y = ~different, name = 'different', color =I("rgba(47,92,91,1)")) %>%
  layout(yaxis = list(title = 'Mean Accuracy'), barmode = 'group')



# ************ PLOT MEAN RT SLOPE BY TASK AND GROUP ************ 

task <- c("ll", "lv", "vl", "vv")
random <- c(2.849, 1.131, 1.303, 1.232)
structured <- c(1.522, -1.482, -3.061, -1.928)
data <- data.frame(task, random, structured)


rt_slope_plot <- plot_ly(data, x = ~task, y = ~random, type = 'bar', name = 'random', color =I("rgba(160,190,156,1)")) %>%
  add_trace(y = ~structured, name = 'structured', color =I("rgba(51,113,74,1)")) %>%
  layout(yaxis = list(title = 'Mean RT Slope'), barmode = 'group')



# ************ PLOT MEAN RT BY TASK AND GROUP ************ 

task <- c("ll", "lv", "vv", "vl")
structured <- c(463.007, 459.541, 458.223, 483.574)
random <- c(442.966, 508.564, 502.304, 521.621)
data <- data.frame(task, structured, random)

mean_rt_plot <- plot_ly(data, x = ~task, y = ~random, type = 'bar', name = 'random', color =I("rgba(160,190,156,1)")) %>%
  add_trace(y = ~structured, name = 'structured', color =I("rgba(51,113,74,1)")) %>%
  layout(yaxis = list(title = 'Mean RT', range = c(300,525)), barmode = 'group')





