
ssl_rt_by_trial <-
  read.csv("/Volumes/data/projects/blast/data_summaries/blast_online_child/breakdown/rt_by_trial/blast_ssl_rt_by_trial.csv")

loop_index = 0
hit_trial_count <- list()
id <- list()
for (i in unique(ssl_rt_by_trial$id)) {
  loop_index = loop_index + 1
  current_id_data <- ssl_rt_by_trial[which(ssl_rt_by_trial$id == i),]
  hit_trial_count[loop_index] <- length(which(current_id_data$reaction_time != ""))
  id[loop_index] <- i
}

hit_trial_number <- do.call(rbind, hit_trial_count)
part_id <- do.call(rbind, id)

ssl_rt_hit_trial_count <- cbind(part_id, hit_trial_number)
colnames(ssl_rt_hit_trial_count) <- c("part_id", "hit_trial_number")
ssl_rt_hit_trial_count <- data.frame(ssl_rt_hit_trial_count)
ssl_rt_hit_trial_count$hit_trial_number <- 
  as.numeric(as.character(ssl_rt_hit_trial_count$hit_trial_number))

write.csv(ssl_rt_hit_trial_count, "ssl_rt_hit_trial_count.csv")


tsl_rt_by_trial <-
read.csv("/Volumes/data/projects/blast/data_summaries/blast_online_child/breakdown/rt_by_trial/blast_tsl_rt_by_trial.csv")

loop_index = 0
hit_trial_count <- list()
id <- list()

for (i in unique(tsl_rt_by_trial$id)) {
  loop_index = loop_index + 1
  current_id_data <- tsl_rt_by_trial[which(tsl_rt_by_trial$id == i),]
  hit_trial_count[loop_index] <- length(which(current_id_data$reaction_time != ""))
  id[loop_index] <- i
}

hit_trial_number <- do.call(rbind, hit_trial_count)
part_id <- do.call(rbind, id)

tsl_rt_hit_trial_count <- cbind(part_id, hit_trial_number)
colnames(tsl_rt_hit_trial_count) <- c("part_id", "hit_trial_number")
tsl_rt_hit_trial_count <- data.frame(tsl_rt_hit_trial_count)
tsl_rt_hit_trial_count$hit_trial_number <- 
  as.numeric(as.character(tsl_rt_hit_trial_count$hit_trial_number))

write.csv(tsl_rt_hit_trial_count, "tsl_rt_hit_trial_count.csv")

