#!/bin/bash
# Script to extract make docs site configurable for Docker image

# Define input and output paths
VARIABLES_PATH="_variables.yml"
MANIFEST_PATH="validmind-docs.yaml"

# Define placeholder values, same as in docker_entrypoint.sh
VALIDMIND_PLACEHOLDER="https://app.prod.validmind-configurable-url.ai"
JUPYTERHUB_PLACEHOLDER="https://jupyterhub.validmind-configurable-url.ai"
PRODUCT_PLACEHOLDER="CONFIGURABLE_PRODUCT_NAME"

# Check if variables file exists
if [ ! -f "$VARIABLES_PATH" ]; then
    echo "Error: $VARIABLES_PATH not found"
    exit 1
fi

# First, save the current state of the file in case we need to restore it
git diff "$VARIABLES_PATH" > /dev/null 2>&1 || git add "$VARIABLES_PATH" -N

# Use awk to directly extract URL values by looking for specific patterns
VALIDMIND_URL=$(awk '/url:/{flag=1} flag && /us1:/{gsub(/"/, "", $2); print $2; exit}' "$VARIABLES_PATH")
JUPYTERHUB_URL=$(awk '/url:/{flag=1} flag && /jupyterhub:/{gsub(/"/, "", $2); print $2; exit}' "$VARIABLES_PATH")

# Extract product name from _variables.yml
PRODUCT_NAME=$(awk '
/^validmind:/ { in_validmind=1; next }
/^[a-zA-Z]/ && in_validmind { in_validmind=0 }
in_validmind && /product:/ { 
    # Extract quoted string
    start = index($0, "\"")
    if (start > 0) {
        line = substr($0, start+1)
        end = index(line, "\"")
        if (end > 0) {
            print substr(line, 1, end-1)
            exit
        }
    }
}' "$VARIABLES_PATH")

# Extract SVG content from logo.svg and favicon.svg
if [ -f "logo.svg" ]; then
    LOGO_SVG=$(cat logo.svg)
else
    echo "Warning: logo.svg not found"
    LOGO_SVG=""
fi

if [ -f "favicon.svg" ]; then
    FAVICON_SVG=$(cat favicon.svg)
else
    echo "Warning: favicon.svg not found"
    FAVICON_SVG=""
fi

# Check if values were found
if [ -z "$VALIDMIND_URL" ] || [ -z "$JUPYTERHUB_URL" ]; then
    echo "Error: Could not extract URLs from $VARIABLES_PATH"
    echo "Current content of $VARIABLES_PATH:"
    cat "$VARIABLES_PATH"
    exit 1
fi

if [ -z "$PRODUCT_NAME" ]; then
    echo "Error: Could not extract PRODUCT_NAME from $VARIABLES_PATH"
    exit 1
fi

printf "\nFound values to configure in %s:\n" "$VARIABLES_PATH"
printf "VALIDMIND_URL: %s → %s\n" "$VALIDMIND_URL" "$VALIDMIND_PLACEHOLDER"
printf "JUPYTERHUB_URL: %s → %s\n" "$JUPYTERHUB_URL" "$JUPYTERHUB_PLACEHOLDER"
printf "PRODUCT_NAME: %s → %s\n" "$PRODUCT_NAME" "$PRODUCT_PLACEHOLDER"
printf "\nFound logo.svg:\n"
printf "%s ...\n" "$(echo "$LOGO_SVG" | head -n 5)"
printf "\nFound favicon.svg:\n"
printf "%s ...\n" "$(echo "$FAVICON_SVG" | head -n 5)"
printf "\n"

# Function to escape YAML multiline string
escape_yaml_multiline() {
    echo "$1" | sed 's/^/    /'
}

# Generate the Kubernetes ConfigMap manifest with extracted values
cat > "$MANIFEST_PATH" << EOF
apiVersion: v1
kind: ConfigMap
metadata:
  name: validmind-docs-config
  namespace: cmvm-test
data:
  VALIDMIND_URL: "$VALIDMIND_URL"
  JUPYTERHUB_URL: "$JUPYTERHUB_URL"
  PRODUCT_NAME: "$PRODUCT_NAME"
  LOGO_SVG: |
$(escape_yaml_multiline "$LOGO_SVG")
  FAVICON_SVG: |
$(escape_yaml_multiline "$FAVICON_SVG")
EOF

# Check if manifest file was created successfully
if [ ! -f "$MANIFEST_PATH" ]; then
    echo "Error: Failed to generate $MANIFEST_PATH"
    exit 1
fi

printf "\nSuccessfully generated %s" "$MANIFEST_PATH"

# Replacements in _variables.yml
sed -i'.tmp' -E "s|(us1:[ ]*\")([^\"]+)(\")|\1$VALIDMIND_PLACEHOLDER\3|g" "$VARIABLES_PATH"
sed -i'.tmp' -E "s|(jupyterhub:[ ]*\")([^\"]+)(\")|\1$JUPYTERHUB_PLACEHOLDER\3|g" "$VARIABLES_PATH"

# Replace only the first product: line after validmind: section
awk -v placeholder="$PRODUCT_PLACEHOLDER" '
/^validmind:/ { in_validmind=1; print; next }
/^[a-zA-Z]/ && in_validmind { in_validmind=0 }
in_validmind && /^[[:space:]]*product:/ && !replaced { 
    sub(/product:[[:space:]]*"[^"]*"/, "product: \"" placeholder "\"")
    replaced=1
}
{ print }
' "$VARIABLES_PATH" > "$VARIABLES_PATH.tmp" && mv "$VARIABLES_PATH.tmp" "$VARIABLES_PATH"

# Remove temporary files created by sed
rm -f "${VARIABLES_PATH}.tmp"

printf "\nSuccessfully modified %s\n" "$VARIABLES_PATH"