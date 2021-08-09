#!/usr/bin/env Rscript

require(tidyverse)
require(data.table)

df_raw <- data.frame(data.table::fread(
    "../molecule_moa.tsv.gz",
    sep = "\t"
))
df_raw$target_hits <- grepl("ENSG", df_raw$targets)

df_number_targets <- df_raw %>%
    dplyr::select(
        id,
        targets,
        target_hits
    ) %>%
    unique() %>%
    dplyr::group_by(
        id
    ) %>%
    dplyr::summarize(
        n_targets = sum(target_hits)
    )

# Plot
plt <- ggplot2::ggplot(
    df_number_targets,
    ggplot2::aes(x = n_targets)
)
plt <- plt + ggplot2::theme_bw(base_size = 12)
plt <- plt + ggplot2::geom_histogram(bins = 100)
plt <- plt + ggplot2::scale_fill_brewer(palette = "Dark2")
plt <- plt + ggplot2::labs(
    x = "Number of gene targets",
    y = "Count",
    title = "All ChEMBL molecules"
)
plt1 <- plt

# Plot2
plt <- ggplot2::ggplot(
    subset(df_number_targets, n_targets > 0),
    ggplot2::aes(x = n_targets)
)
plt <- plt + ggplot2::theme_bw(base_size = 12)
plt <- plt + ggplot2::geom_histogram(bins = 100)
plt <- plt + ggplot2::scale_fill_brewer(palette = "Dark2")
plt <- plt + ggplot2::labs(
    x = "Number of gene targets",
    y = "Count",
    title = "ChEMBL molecules with >= 1 gene target"
)
plt2 <- plt


pdf(file = paste0("distribution-n_targets", ".pdf"),
    height = 5,
    width = 5
)
    print(plt1)
    print(plt2)
dev.off()
