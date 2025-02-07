# Breaking changes and deprecations

This guide walks you through how to add a breaking change or deprecation to our [~/releases/breaking-changes/breaking-changes.qmd](breaking-changes.qmd) history.

## Before you begin

In order to get Quarto display the neat interactive table in our HTML output, you need to have R and some dependencies installed in your environment.

### Install R

1. **Download and install R** from the Comprehensive R Archive Network: [CRAN](https://cran.r-project.org/index.html)
    - If you're using VS Code, you may also want to install the following extensions: [R](https://marketplace.visualstudio.com/items?itemName=REditorSupport.r), [R Extension Pack](https://marketplace.visualstudio.com/items?itemName=Ikuyadeu.r-pack)
2. **Open up an R terminal.** In VS Code you can press `CTRL/CMD + SHIFT + P` to open up the command palette, then type in and select `R: Create R Terminal`.

### Install R dependencies

In the R terminal, run:

```bash
install.packages("DT")
install.packages("readr")
install.packages("stringr")
install.packages("lubridate")
```

These are the packages used to generate cool interactive tables from the yearly CSVs:

- **[DataTables](https://rstudio.github.io/DT/)** — Displays a R data object as an HTML table.
- **[readr](https://readr.tidyverse.org/)** — Parses the yearly `.csv` files for the table.
- **[stringr](https://readr.tidyverse.org/)** — Parses markdown links in the `.csv` and turns them into HTML for the output table so they can be displayed properly.
- **[lubridate](https://lubridate.tidyverse.org/)** — Parses and reformats the ISO 8601 date in the CSV into the Mon DD, YYYY format in the output table.

## Creating entries

### Add a year

If you're adding the first entry for that year, you'll need to add that year to the history section first:

#### Create the yearly CSV

Make a copy of `~/releases/breaking-changes/year.csv` in the `~/releases/breaking-changes/history/` directory. For example:

> `~/releases/breaking-changes/year.csv` > `~/releases/breaking-changes/history/2025.csv`

> [!CAUTION]
> Due to the way DataTables processes the input, there needs to be an empty row/line break at the end of the sheet.

#### Insert CSV as table

1. In `~/releases/breaking-changes/breaking-changes.qmd` under `<!-- CURRENT YEAR START -->`, insert the new year `h3` header. For example:

    ```markdown
    ### 2025
    ```

2. Then under that header, call the functions to display the interactive table for that year under a named and fenced `{r}` code block. For example:

    ```R
        ```{r 2025}
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

You'll need the links for the release notes and any blog posts associated with the breaking change or deprecation to include in the table, so make sure those are published that first unless you want to fill them in at a later date.

#### Enter an entry

Open up the `.csv` for the year you want to update and create a new entry under the header row with the following information:

| Column name | Content | Example |
|---|---|---|
| Change | Name of the feature being broken or deprecated | `Standard inputs are deprecated` |
| Product area | Applicable variable for the ValidMind Library or ValidMind Platform | `{{< var validmind.developer >}} `|
| Version | Associated library or platform version attached to the announcement prefaced by a `v` (Linked to release tags) | `v1.25.3` |
| Type | Whether it's a breaking change or deprecation | `Deprecation` |
| Date announced | ISO 8601 date of announcement | `2024-01-26` |
| Release notes | Markdown format **HTML** link to the associated release notes enclosed by `""` | `"[Read](/releases/2024/2024-jan-26/highlights.html#standard-inputs-are-deprecated)"` |
| Blog post | Markdown format link to the associated blog post enclosed by `""` | `"[Read](https://validmind.com/blog/)"` |
| Date of removal | ISO 8601 date of removal | `2024-01-26` |

> [!NOTE]
> You can refer to the **[example `.csv`](example.csv)** for formatting guidance.
>
> If you're using VS Code, [Excel Viewer](https://marketplace.visualstudio.com/items?itemName=GrapeCity.gc-excelviewer) is a great extension to make editing `.csv` files more accessible.

