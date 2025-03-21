#!/bin/bash
# Script to extract URL values and replace them with placeholders for Docker image

# Define input and output paths
VARIABLES_PATH="_variables.yml"
CONFIG_PATH="config.json"

# Define placeholder values, same as in docker_entrypoint.sh
VALIDMIND_PLACEHOLDER="https://app.prod.validmind-configurable-url.ai"
JUPYTERHUB_PLACEHOLDER="https://jupyterhub.validmind-configurable-url.ai"

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

# Check if values were found
if [ -z "$VALIDMIND_URL" ] || [ -z "$JUPYTERHUB_URL" ]; then
    echo "Error: Could not extract URLs from $VARIABLES_PATH"
    echo "Current content of $VARIABLES_PATH:"
    cat "$VARIABLES_PATH"
    exit 1
fi

echo "Found URLs in $VARIABLES_PATH:"
echo "VALIDMIND_URL: $VALIDMIND_URL"
echo "JUPYTERHUB_URL: $JUPYTERHUB_URL"

# Generate the JSON file with extracted values for fallback
cat > "$CONFIG_PATH" << EOF
{
  "VALIDMIND_URL": "$VALIDMIND_URL",
  "JUPYTERHUB_URL": "$JUPYTERHUB_URL"
}
EOF

# Check if JSON file was created successfully
if [ ! -f "$CONFIG_PATH" ]; then
    echo "Error: Failed to generate $CONFIG_PATH"
    exit 1
fi

echo "Successfully generated $CONFIG_PATH from $VARIABLES_PATH"

# Replace the actual URLs with placeholder URLs
sed -i'.tmp' -E "s|(us1:[ ]*\")([^\"]+)(\")|\1$VALIDMIND_PLACEHOLDER\3|g" "$VARIABLES_PATH"
sed -i'.tmp' -E "s|(jupyterhub:[ ]*\")([^\"]+)(\")|\1$JUPYTERHUB_PLACEHOLDER\3|g" "$VARIABLES_PATH"

# Remove temporary files created by sed
rm -f "${VARIABLES_PATH}.tmp"

echo "Modified $VARIABLES_PATH with placeholder values:"
echo "VALIDMIND_URL: $VALIDMIND_PLACEHOLDER"
echo "JUPYTERHUB_URL: $JUPYTERHUB_PLACEHOLDER"