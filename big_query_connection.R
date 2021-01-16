
install.packages("bigrquery")
library(bigrquery)
project <- "chrome-plateau-112111" # put your project ID here
sql <- "SELECT * FROM [chrome-plateau-112111:65114006.delivery_dates] LIMIT 1000"
delivery_dates <- query_exec(sql, project = project)
