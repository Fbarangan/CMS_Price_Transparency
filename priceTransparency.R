library(dplyr)
setwd("C:/Users/felix/OneDrive/Documents/SQL/Price_transparency/CMS_Price_Transparency")

data <- read.csv("ColumnSelected.csv")
head(data)

# rename columns
 PT_Columns <- data %>%
     rename(Plans = Plan.s.)

head(PT_Columns)
  
# Aggregate similar plans
group_PT_Columns <- PT_Columns %>%
  group_by(Code_type, Code, Procedure_Description, NDC, Rev_Code
           ,Plans, IP_Price, OP_Price) %>%
  summarize(IP = mean(IP,na.rm = TRUE),
            OP = mean(OP, na.rm = TRUE)
  )

head(group_PT_Columns)

write.csv(group_PT_Columns, "PT_Grouped.csv", row.names = FALSE)
