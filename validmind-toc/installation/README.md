# User guide

> `validmind-toc-1.0.0.vsix` is the latest version as of January 10th, 2024.

Once the extension is enabled, to generate a table of contents for the first time:

1. Select the cell that will live **below** the table of contents cell.
2. From the horizontal ellipsis menu in the top-right hand corner of the notebook, select `+ ValidMind table of contents`.

| Command | Functionality | 
|---|---|
| `+ ValidMind table of contents` | Adds or updates a table of contents. Once generated, you can override global settings with [`vm-toc-notebook-config`](#notebook-level-settings). | 
| `- ValidMind table of contents` | Removes the table of contents and associated page anchors. |

## Installation

1. Make sure you're in the `validmind-toc` directory in the `documentation` repo:

```bash
cd validmind-toc
```

2. Install the extension version you'd like to use, e.g:

```bash
code --install-extension installation/validmind-toc-1.0.0.vsix
```

<details>
  <summary><b>Uninstalling the extension</b><br><br></summary>

In your VS Code terminal:

```bash
code --uninstall-extension validbeck.validmind-toc
```

Optionally, you can clear cached extension settings via the terminal:

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
</details>

## Settings

### Global settings

These are the expected ValidMind defaults; you should not need to adjust these.

Key|Expected Values|Default|Description
:---|:---:|:---:|:---
`validmind.tableOfContents.tableHeader`|`string`|`## Contents`|Defines the heading for the table of contents cell.
`validmind.tableOfContents.minHeaderLevel`|`1-6`|`2`|Defines the minimum level of notebook headers to be collected in the table of contents. `2` will leave the title of the notebook out as it is an `h1` header.
`validmind.tableOfContents.maxHeaderLevel`|`1-6`|`4`|Defines the maximum level of notebook headers to be collected in the table of contents.

### Notebook level settings

Override the global settings for a specific notebook in the table of contents cell that gets generated within `vm-toc-notebook-config`. Defaults are set to ValidMind conventions.

Key|Expected Values|Default|Description
:---|:---:|:---:|:---
`numbering`|`boolean`|`false`|Enumerate the generated table of contents.
`anchor`|`boolean`|`true`|Table of contents is generated as a set of links to the page anchors.
`flat`|`boolean`|`false`|Flat table of contents without intendentions and list markers. Looks better when used with `numbering` enabled.
`minLevel`|`1-6`|`2`|Defines the minimum level of notebook headers to be collected in the table of contents. `2` will leave the title of the notebook out as it is an `h1` header.
`maxLevel`|`1-6`|`4`|Defines the maximum level of notebook headers to be collected in the table of contents.