# User guide

Once the extension is installed and enabled, to generate a table of contents for the first time:

1. Select the cell that will live **below** the table of contents cell.
2. From the horizontal ellipsis menu in the top-right hand corner of the notebook, select `+ Table of contents`.

| Command | Functionality | 
|---|---|
| `+ Table of contents` | Adds or updates a table of contents. Once generated, you can override global settings with [`jn-toc-notebook-config`](#notebook-level-settings). | 
| `- Table of contents` | Removes the table of contents and associated page anchors. |

## Installation

> Refer to the releases for the available/latest versions: https://github.com/validbeck/jupyter-notebook-toc/releases

1. Download the extension version you'd like to use.

2. Follow the [VS Code instructions on how to install from a `.vsix` file](https://code.visualstudio.com/docs/editor/extension-marketplace#_install-from-a-vsix), e.g.: 

```bash
code --install-extension jn-toc-1.0.0.vsix
```

<details>
  <summary><b>Uninstalling the extension</b><br><br></summary>

In your VS Code terminal:

```bash
code --uninstall-extension validbeck.jn-toc
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
rm -rf validbeck.jn-toc-1.0.0/
```
</details>

## Settings

### Global settings

These are the expected ValidMind defaults; you should not need to adjust these if you are applying them to a ValidMind Jupyter Notebook.

Key|Expected Values|Default|Description
:---|:---:|:---:|:---
`jupyterNotebook.tableOfContents.tableHeader`|`string`|`## Contents`|Defines the heading for the table of contents cell.
`jupyterNotebook.tableOfContents.minHeaderLevel`|`1-6`|`2`|Defines the minimum level of notebook headers to be collected in the table of contents. `2` will leave the title of the notebook out as it is an `h1` header.
`jupyterNotebook.tableOfContents.maxHeaderLevel`|`1-6`|`4`|Defines the maximum level of notebook headers to be collected in the table of contents.
`jupyterNotebook.tableOfContents.showOnHtml`|`boolean`|`false`|Show the embedded table of contents when rendered as HTML with Quarto, defaults to `false` as Quarto has built-in ToC.

### Notebook level settings

Override the global settings for a specific notebook in the table of contents cell that gets generated within `jn-toc-notebook-config`. Defaults are set to ValidMind conventions.

Key|Expected Values|Default|Description
:---|:---:|:---:|:---
`numbering`|`boolean`|`false`|Enumerate the generated table of contents.
`anchor`|`boolean`|`true`|Table of contents is generated as a set of links to the page anchors.
`flat`|`boolean`|`false`|Flat table of contents without intendentions and list markers. Looks better when used with `numbering` enabled.
`minLevel`|`1-6`|`2`|Defines the minimum level of notebook headers to be collected in the table of contents. `2` will leave the title of the notebook out as it is an `h1` header.
`maxLevel`|`1-6`|`4`|Defines the maximum level of notebook headers to be collected in the table of contents.