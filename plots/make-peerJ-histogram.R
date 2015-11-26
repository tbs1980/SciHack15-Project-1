setwd("/home/ross/suppdata/manualpeerj")
install.packages("ggplot2")
library(ggplot2)

install.packages("rcrossref")
library(rcrossref)
zz <- cr_journals(issn="2167-8359", works=TRUE, filter=c(from_pub_date='2010-01-01'))
#write.csv(zz,file="outout.csv")

chol <- read.table(url("http://assets.datacamp.com/blog_assets/chol.txt"), header = TRUE)
# Take the dataset "chol" to be plotted, pass the "AGE" column from the "chol" dataset as values on the x-axis and compute a histogram of this
ggplot(data=chol, aes(chol$AGE)) + geom_histogram()
filetypes <- read.table('sortedextensions.txt')
filetypes
summary(filetypes, maxsum=40)
filetypes <- within(filetypes, 
                   V1 <- factor(V1, 
                                      levels=names(sort(table(V1), 
                                                        decreasing=TRUE))))
ggplot(data=filetypes, aes(filetypes$V1)) + geom_histogram() + coord_cartesian(ylim=c(0, 700)) + theme(panel.background = element_blank()) +
  scale_y_continuous(breaks=seq(0, 700, 100)) +
  ylab("Number of Files") +
  xlab("File Extension")

getwd()
