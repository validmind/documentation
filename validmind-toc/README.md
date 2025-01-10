# ValidMind Jupyter Notebooks — Table of Contents


## Installation


## User guide

### Settings

#### Global settings

Key|Expected Values|Default|Description
:---|:---:|:---:|:---
`validmind.tableOfContents.tableHeader`|`string`|`## Contents`|Defines the heading for the table of contents cell.
`validmind.tableOfContents.minHeaderLevel`|`1-6`|`1`|Defines the minimum level of notebook headers to be collected in the table of contents.
`validmind.tableOfContents.maxHeaderLevel`|`1-6`|`6`|Defines the maximum level of notebook headers to be collected in the table of contents.

#### Notebook level settings

Override the global settings for a specific notebook in the table of contents cell that gets generated within `vm-toc-notebook-config`.

Key|Expected Values|Default|Description
:---|:---:|:---:|:---
`numbering`|`boolean`|`false`|Enumerate the generated table of contents.
`anchor`|`boolean`|`true`|Table of contents is generated as a set of links to the page anchors.
`flat`|`boolean`|`false`|Flat table of contents without intendentions and list markers. Looks better when used with `numbering` enabled.
`minLevel`|`1-6`|`1`|Defines the minimum level of notebook headers to be collected in the table of contents.
`maxLevel`|`1-6`|`6`|Defines the maximum level of notebook headers to be collected in the table of contents.

## Making changes to the extension

### Before you begin

Make sure you're in the `documentation` repo in the `validmind-toc` directory:

```bash
cd validmind-toc
```

The first time you'll need to install the dependencies required for you to work on the extension:

```bash
npm install
```

### Updating the version

### Packaging the extension


