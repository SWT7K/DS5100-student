#0

abalone_data <- read.csv(url("https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"), header = FALSE)
abalone_data

#1

x<-nrow(abalone_data)
print(x)

#2

max_rings <- max(abalone_data$V9)
print(max_rings)

#3

library(tidyverse)
abalone_data %>%
  filter(V1 == "I") %>% nrow

#4

abalone_data %>%
  filter(V1 == "I"| V1 == "M") %>% nrow

#5

table(abalone_data$V1)

#6

library(dplyr)
grouped_data <- abalone_data %>% 
  group_by(V1) %>%
  summarise(mean_shell = mean(V2))

print(grouped_data$mean_shell)

#7

V2_median <- abalone_data %>%
  filter(V1 == "M") %>%
  summarise(filtered_median = median(V2))
V2_median$filtered_median

