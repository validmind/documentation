#!/bin/bash
# Script to extract make docs site configurable for Docker image

# Define input and output paths
VARIABLES_PATH="_variables.yml"
CONFIG_PATH="config.json"

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
PRODUCT_NAME=$(awk '/vm:/{flag=1} flag && /product:/{gsub(/"/, "", $2); print $2; exit}' "$VARIABLES_PATH")

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
printf "VALIDMIND_URL → %s\n" "$VALIDMIND_PLACEHOLDER"
printf "JUPYTERHUB_URL → %s\n" "$JUPYTERHUB_PLACEHOLDER"
printf "PRODUCT_NAME → %s\n" "$PRODUCT_PLACEHOLDER"
printf "\nFound logo.svg:\n"
printf "%s ...\n" "$(echo "$LOGO_SVG" | head -n 5)"
printf "\nFound favicon.svg:\n"
printf "%s ...\n" "$(echo "$FAVICON_SVG" | head -n 5)"
printf "\n"

# Function to escape JSON string
escape_json() {
    echo "$1" | sed 's/\\/\\\\/g; s/"/\\"/g; s/\t/\\t/g; s/\r/\\r/g; s/\n/\\n/g'
}

# Generate the JSON file with extracted values for fallback
cat > "$CONFIG_PATH" << EOF
{
  "VALIDMIND_URL": "$VALIDMIND_URL",
  "JUPYTERHUB_URL": "$JUPYTERHUB_URL",
  "PRODUCT_NAME": "$PRODUCT_NAME",
  "LOGO_SVG": "$(escape_json "$LOGO_SVG")",
  "FAVICON_SVG": "$(escape_json "$FAVICON_SVG")"
}
EOF

# Check if JSON file was created successfully
if [ ! -f "$CONFIG_PATH" ]; then
    echo "Error: Failed to generate $CONFIG_PATH"
    exit 1
fi

printf "\nSuccessfully generated %s" "$CONFIG_PATH"

# Replace the actual URLs with placeholder URLs
sed -i'.tmp' -E "s|(us1:[ ]*\")([^\"]+)(\")|\1$VALIDMIND_PLACEHOLDER\3|g" "$VARIABLES_PATH"
sed -i'.tmp' -E "s|(jupyterhub:[ ]*\")([^\"]+)(\")|\1$JUPYTERHUB_PLACEHOLDER\3|g" "$VARIABLES_PATH"

# Replace the product name with placeholder in _variables.yml
sed -i'.tmp' -E "s|(product:[ ]*\")([^\"]+)(\")|\1$PRODUCT_PLACEHOLDER\3|g" "$VARIABLES_PATH"

# Remove temporary files created by sed
rm -f "${VARIABLES_PATH}.tmp"

printf "\nSuccessfully modified %s\n" "$VARIABLES_PATH"