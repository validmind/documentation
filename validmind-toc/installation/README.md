# User guide

## Installation




### Uninstalling the extension

In your VS Code terminal:

```bash
code --uninstall-extension validbeck.validmind-toc
```

#### Clear cached extension settings (optional)

Via the terminal:

1. Navigate to your VS Code extension directory:

```bash
cd ~/.vscode/extensions
```

2. Retrieve a list of your extension directories and note the folder name for the extension's version:

```bash
ls -d */
```

3. Remove the cached folder, e.g:

```bash
rm -rf validbeck.validmind-toc-1.0.0/
```

## Settings

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

## Generating table of contents


### Update table of contents

### Remove table of contents