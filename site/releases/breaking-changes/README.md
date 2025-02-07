# Breaking changes and deprecations

This guide walks you through how to add a breaking change or deprecation to our `releases/breaking-changes/breaking-changes.qmd` history.

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

#### Create the yearly CSV

#### Insert CSV as table

### Add an entry

#### Create collateral

#### Enter an entry

