# ValidMind Jupyter Notebooks — Table of Contents

This VS Code extension based off of [xelad0m/vscode-jupyter-toc](https://github.com/xelad0m/vscode-jupyter-toc) is customized for ValidMind's Jupyter Notebook conventions. It functions more or less the same with the following differences:

| Original ver. | ValidMind ver. | Notes
|---|---|---|
| | | Page anchors set above header instead of inset; original version was not parsed correctly by Quarto and broke the native ToC |
| | | No reverse anchors to top in page anchors |
| | | Top anchor in table of contents cell removed |
| | | Reduced global settings, defaults set to ValidMind conventions |

## Installation

Refer to the [Installation guide](installation/README.md).

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

## Updating the extension

### Key files

- **[`src/extension.ts`](src/extension.ts)** — This TypeScript file controls the core functionality of the extension.
- **[`package.json`](package.json)** — This JSON file includes the versioning and the setup for the VS Code global settings display under [`contributes.configuration`](https://code.visualstudio.com/api/references/contribution-points#contributes.configuration). 

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

Before you re-package the extension, make sure to bump the version so we can keep track of changes:

```bash
npm version patch
```

### Exporting the extension

Compile the code:

```bash
npm run compile
```

Install `@vscode/vsce` locally in your project directory:

```bash
npm install @vscode/vsce
```

Package the extension and move the completed file into the `installation` directory:

```bash
px vsce package && mv *.vsix installation
```

