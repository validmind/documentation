# Installation guide



## Uninstalling the extension

In your VS Code terminal:

```bash
code --uninstall-extension validbeck.validmind-toc
```

### Clear cached extension settings

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