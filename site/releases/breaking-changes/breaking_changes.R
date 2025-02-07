# Load necessary libraries with output messages supressed
suppressPackageStartupMessages(library(DT))
suppressPackageStartupMessages(library(readr))
suppressPackageStartupMessages(library(stringr))
suppressPackageStartupMessages(library(lubridate))

# Read CSV while preserving column names and treating all text as characters
read_csv_data <- function(year) {
  file_name <- paste0(year, ".csv")
  data <- read.csv(file_name, check.names = FALSE, stringsAsFactors = FALSE)
  return(data)
}

# Cnvert Markdown-style links to proper HTML
convert_markdown_links <- function(data) {
  data[] <- lapply(data, function(column) {
    column <- str_replace_all(column, "\\[(.*?)\\]\\((.*?)\\)", "<a href='\\2'>\\1</a>")
    return(column)
  })
  return(data)
}

# Reformat ISO dates to Mon DD, YYYY
format_date <- function(date_column) {
  parsed_dates <- ymd(date_column)
  formatted_dates <- format(parsed_dates, "%b %d, %Y")
  return(formatted_dates)
}

# Apply date formatting to `Date announced` and `Date of removal` columns
format_dates_in_data <- function(data) {
  if ("Date announced" %in% names(data)) {
    data[["Date announced"]] <- format_date(data[["Date announced"]])
  }
  if ("Date of removal" %in% names(data)) {
    data[["Date of removal"]] <- paste0(
      "<span style='color: #92130cff;'>", format_date(data[["Date of removal"]]), "</span>"
    )
  }
  return(data)
}

# Render an interactive searchable and filterable table
render_table <- function(data) {
  datatable(
    data,
    options = list(
      pageLength = 10, # Define default length of entries
      dom = 'fltpi', # Table display options: Search/filter, length menu, the table istself, pagination, table info
      initComplete = JS( # Filter `Product area`, `Version`, & `Type` using JavaScript
        "function(settings, json) {
          [1, 2, 3].forEach(function(index) {
            var column = this.api().column(index);
            var header = $(column.header()); // Keep original header text
            var select = $('<br><select><option value=\"\">All</option></select>')
              .appendTo(header) // Append instead of replacing
              .on('change', function() {
                var val = $.fn.dataTable.util.escapeRegex($(this).val());
                column.search(val ? '^' + val + '$' : '', true, false).draw();
              });
            column.data().unique().sort().each(function(d, j) {
              select.append('<option value=\"'+d+'\">'+d+'</option>')
            });
          }.bind(this));
        }"
      )
    ),
    escape = FALSE, # Allow HTML rendering
    rownames = FALSE # Disable row numbering
  )
}