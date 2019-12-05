## ---- vot_graph ----
values <- sample(0:60, 15, replace = TRUE)
stripchart(values,
           method = "jitter",
           main = "Tokens of /ɡ/ and /k/",
           xlab = "Voice onset time (ms)",
           xlim = c(0, 60))
abline(v = 30)
text(15, 1.3, "/ɡ/")
text(45, 1.3, "/k/")
