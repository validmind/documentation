# Test Cases for Clone Target

Verified the following scenarios work as expected:

## 1. Clone Latest (HEAD)
```bash
make clone
# When prompted, enter: HEAD

# Expected and observed:
✓ Prompted for tag
✓ Cloned validmind-library from main when HEAD specified
✓ Showed warning about non-release files
✓ Installation repo cloned from main
```

## 2. Clone Specific Release
```bash
make clone
# When prompted, enter: v2.8.10

# Expected and observed:
✓ Prompted for tag
✓ Cloned validmind-library from tag v2.8.10
✓ No warning (since it's a release)
✓ Installation repo cloned from main
```

## 3. Clone Feature Branch
```bash
make clone BRANCH=beck/sc-9082/edit-validation-credit-risk-notebook

# Expected and observed:
✓ No prompt (used branch directly)
✓ Cloned validmind-library from specified branch
✓ Showed warning about non-release files
✓ Installation repo cloned from main
```

## 4. Clone Latest (main + HEAD)
```bash
make clone BRANCH=main
# When prompted, enter: HEAD

# Expected and observed:
✓ Prompted for tag
✓ Cloned validmind-library from main when HEAD specified
✓ Showed warning about non-release files
✓ Installation repo cloned from main
```

All test cases passed successfully, demonstrating that:
- Both `BRANCH` and `LIBRARY_BRANCH` parameters work
- Appropriate warnings are shown for non-release checkouts
- Installation repo consistently clones from main
- Tag prompting works as expected 