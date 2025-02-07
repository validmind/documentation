# Breaking changes and deprecations

This guide walks you through how to add a breaking change or deprecation to our `~/releases/breaking-changes/breaking-changes.qmd` history.

## Before you begin

In order to get Quarto display the neat interactive table in our HTML output, you need to have R and some dependencies installed in your environment.

### Install R

- **Download and install R** from the Comprehensive R Archive Network: [CRAN](https://cran.r-project.org/index.html)
    - If you're using VS Code, you may also want to install the following extensions: [R](https://marketplace.visualstudio.com/items?itemName=REditorSupport.r), [R Extension Pack](https://marketplace.visualstudio.com/items?itemName=Ikuyadeu.r-pack)
- **Open up an R terminal.** In VS Code you can press `CTRL/CMD + SHIFT + P` to open up the command palette, then type in and select `R: Create R Terminal`.

### Install R dependencies

In the R terminal, run:

```bash
install.packages("DT")
install.packages("readr")
install.packages("lubridate")
```

These are the packages used to generate cool interactive tables from the yearly CSVs:

- **[DataTables](https://rstudio.github.io/DT/)** — Displays a R data object as an HTML table.
- **[readr](https://readr.tidyverse.org/)** — Parses the yearly `.csv` files for the table.
- **[lubridate](https://lubridate.tidyverse.org/)** — Parses and reformats the ISO 8601 date in the CSV into the Mon DD, YYYY format in the output.

## Creating entries

### Add a year

If you're adding the first entry for that year, you'll need to add that year to the history section first:

#### Create the yearly CSV

Make a copy of `~/releases/breaking-changes/year.csv` in the `~/releases/breaking-changes/history/` directory. For example:

> `~/releases/breaking-changes/year.csv` > `~/releases/breaking-changes/history/2025.csv`

#### Insert CSV as table

1. In `~/releases/breaking-changes/breaking-changes.qmd` under `<!-- CURRENT YEAR START -->`, insert the new year `h3` header. For example:

    ```markdown
    ### 2025
    ```

2. Then under that header, call the functions to display the interactive table for that year under a fenced `{r}` code block. For example:

    ```R
        ```{r}
        ## Render 2025.csv
        my_data_2025 <- read_csv_data(2025)
        my_data_2025 <- convert_markdown_links(my_data_2025)
        my_data_2025 <- format_dates_in_data(my_data_2025)
        render_table(my_data_2025)
        ```
    ```

    Replace the year with the actual year you're intending to display.

### Add an entry

#### Create collateral

#### Enter an entry

